#!/usr/bin/env python3
"""Structural guardrail for the Roster Sync routine's direct-to-main commits.

Run this against the OLD (currently committed) and NEW (about to be committed)
CLAUDE.md content before pushing. Exit code 0 means the change is safe to
commit as-is; any non-zero exit means the routine must NOT push and should
surface the failure instead (see CLAUDE.md's Automation Permissions section).

This script has no dependencies beyond the standard library, so it can run
in any environment the sync routine has access to.

Usage:
    python3 scripts/validate_roster_sync.py --old old_claude_md.txt --new new_claude_md.txt
    python3 scripts/validate_roster_sync.py --old-content "$(git show HEAD:CLAUDE.md)" --new new_claude_md.txt
"""
import argparse
import re
import sys

BEGIN = "<!-- BEGIN_AUTO_GENERATED -->"
END = "<!-- END_AUTO_GENERATED -->"

# How much the ownership-index size may swing between syncs before it's
# treated as a sign of corruption (duplication, truncation) rather than
# normal roster churn.
MAX_OWNERSHIP_DELTA_RATIO = 0.5


class ValidationError(Exception):
    pass


def _standalone_marker_line_indices(lines, marker):
    """Line indices where `marker` appears alone on its own line (ignoring
    surrounding whitespace). A marker merely quoted inside other prose
    (e.g. backtick-fenced in the Automation Permissions bullet) does not
    count — only a line that IS the marker, structurally, counts."""
    return [i for i, l in enumerate(lines) if l.strip() == marker]


def split_sections(content, label):
    lines = content.split("\n")
    begin_lines = _standalone_marker_line_indices(lines, BEGIN)
    end_lines = _standalone_marker_line_indices(lines, END)
    if len(begin_lines) != 1:
        raise ValidationError(
            f"{label}: expected exactly 1 standalone '{BEGIN}' line, found {len(begin_lines)}"
        )
    if len(end_lines) != 1:
        raise ValidationError(
            f"{label}: expected exactly 1 standalone '{END}' line, found {len(end_lines)}"
        )
    begin_line, end_line = begin_lines[0], end_lines[0]
    if end_line < begin_line:
        raise ValidationError(f"{label}: END marker line appears before BEGIN marker line")
    before = "\n".join(lines[:begin_line])
    auto = "\n".join(lines[begin_line : end_line + 1])
    after = "\n".join(lines[end_line + 1 :])
    return before, auto, after


def extract_ownership_ids(auto_block):
    m = re.search(r"## Ownership Index\s*```(.*?)```", auto_block, re.S)
    if not m:
        raise ValidationError("could not find an ## Ownership Index code block")
    lines = [l.strip() for l in m.group(1).split("\n")]
    ids = [l for l in lines if l and not l.startswith("<!--") and not l.startswith("-->")]
    return ids


def check_no_duplicate_ownership_ids(ids):
    seen = set()
    dupes = set()
    for i in ids:
        if i in seen:
            dupes.add(i)
        seen.add(i)
    if dupes:
        raise ValidationError(
            f"Ownership Index contains {len(dupes)} duplicate ID(s): "
            f"{sorted(dupes)[:10]}{'...' if len(dupes) > 10 else ''}"
        )


def check_surplus_lines_consistent(auto_block):
    """Each '- POS (N): a, b, c' surplus/QB-room line must have N distinct names."""
    for line in auto_block.split("\n"):
        m = re.match(r"^-\s+([A-Za-z]+)\s+\((\d+)\)(?:\s+QBs)?:\s*(.+)$", line.strip())
        if not m:
            continue
        declared_count = int(m.group(2))
        names = [n.strip() for n in m.group(3).split(",") if n.strip()]
        if len(names) != len(set(names)):
            dupes = sorted({n for n in names if names.count(n) > 1})
            raise ValidationError(
                f"duplicate name(s) in line {line.strip()!r}: {dupes}"
            )
        if len(names) != declared_count:
            raise ValidationError(
                f"declared count {declared_count} doesn't match {len(names)} "
                f"listed name(s) in line {line.strip()!r}"
            )


def check_manual_section_untouched(old_before, old_after, new_before, new_after):
    if old_before != new_before:
        raise ValidationError(
            "content BEFORE the BEGIN_AUTO_GENERATED marker changed — the "
            "MANUAL section must never be touched by an automated sync"
        )
    if old_after != new_after:
        raise ValidationError(
            "content AFTER the END_AUTO_GENERATED marker changed — the "
            "MANUAL section must never be touched by an automated sync"
        )


def check_roster_count(auto_block):
    my_roster = auto_block.count("## My Roster")
    opponents = len(re.findall(r"^### .+\(Roster \d+\)", auto_block, re.M))
    if my_roster != 1:
        raise ValidationError(f"expected exactly one '## My Roster' heading, found {my_roster}")
    if opponents != 11:
        raise ValidationError(f"expected 11 opponent roster headings, found {opponents}")


def check_ownership_delta(old_auto, new_ids):
    try:
        old_ids = extract_ownership_ids(old_auto)
    except ValidationError:
        return  # old file was already broken; nothing to compare against
    old_n, new_n = len(old_ids), len(new_ids)
    if old_n == 0:
        return
    delta_ratio = abs(new_n - old_n) / old_n
    if delta_ratio > MAX_OWNERSHIP_DELTA_RATIO:
        raise ValidationError(
            f"Ownership Index size changed by {delta_ratio:.0%} "
            f"({old_n} -> {new_n} IDs), more than the {MAX_OWNERSHIP_DELTA_RATIO:.0%} "
            f"sanity threshold — looks like corruption, not normal roster churn"
        )


def validate(old_content, new_content):
    old_before, old_auto, old_after = split_sections(old_content, "OLD file")
    new_before, new_auto, new_after = split_sections(new_content, "NEW file")

    check_manual_section_untouched(old_before, old_after, new_before, new_after)

    if not new_auto.strip().startswith(BEGIN):
        raise ValidationError("auto block doesn't start cleanly with the BEGIN marker")
    if "## Roster State" not in new_auto:
        raise ValidationError("auto block is missing the '## Roster State' heading")

    new_ids = extract_ownership_ids(new_auto)
    check_no_duplicate_ownership_ids(new_ids)
    check_ownership_delta(old_auto, new_ids)
    check_surplus_lines_consistent(new_auto)
    check_roster_count(new_auto)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--old", help="path to the currently-committed CLAUDE.md")
    ap.add_argument("--new", help="path to the proposed new CLAUDE.md")
    ap.add_argument("--old-content", help="old CLAUDE.md content given inline instead of a path")
    ap.add_argument("--new-content", help="new CLAUDE.md content given inline instead of a path")
    args = ap.parse_args()

    old_content = args.old_content if args.old_content is not None else open(args.old).read()
    new_content = args.new_content if args.new_content is not None else open(args.new).read()

    try:
        validate(old_content, new_content)
    except ValidationError as e:
        print(f"VALIDATION FAILED: {e}", file=sys.stderr)
        sys.exit(1)

    print("OK: proposed CLAUDE.md passes all structural safety checks")
    sys.exit(0)


if __name__ == "__main__":
    main()
