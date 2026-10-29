# Fantasy Scout — League Intelligence
<!-- Roster Sync routine manages everything between AUTO markers -->

<!-- ============================================================ -->
<!-- MANUAL SECTION — edit freely, Roster Sync will not touch     -->
<!-- ============================================================ -->

## Automation Permissions
- Scope: this exception applies only within the Fantasy-scout
  repository. It does not extend to any other project or repo —
  the standard "develop on the assigned branch, never push
  elsewhere without explicit permission" guard rail stays in
  force everywhere else.
- The scheduled Roster Sync routine pushes to a dedicated branch
  (`automation/roster-sync`) and opens or updates a single pull
  request against `main`. It never commits directly to `main`.
- Before pushing, the routine must run
  `python3 scripts/validate_roster_sync.py --old-content "<CLAUDE.md at current main HEAD>" --new <path to the proposed new CLAUDE.md>`
  and may proceed only if it exits 0. If it exits non-zero, the
  routine must NOT push — leave `main` and any existing PR
  untouched, and report the validator's failure message instead of
  proceeding. The validator checks that: the content outside the
  AUTO markers is byte-identical to what's on `main` (so a broken
  run can never touch this MANUAL section), the markers each
  appear exactly once and in order, the Ownership Index has no
  duplicate player IDs and hasn't swung by more than 50% since the
  last sync, and every "POS (N): a, b, c" surplus/QB-room line has
  N distinct names. See `scripts/validate_roster_sync.py` for the
  full checks.
- The routine may auto-merge that pull request into `main` without
  waiting for a human, but only when all of the following hold:
  (a) the validator above exits 0, (b) any required CI checks
  pass, and (c) the diff touches only CLAUDE.md, only between the
  markers. Any diff outside that shape requires a human to review
  and merge — the routine must leave it as an open PR instead.
- This exception never covers edits to this MANUAL section, to any
  other file, or to any other automation in this repo — those
  still require a normal human-reviewed PR.
- Authorization history: granted by Scvazquez 2026-08-04; reaffirmed
  live 2026-08-09. Replaced 2026-09-11 by Scvazquez — the prior
  direct-to-main clause caused repeated corruption on `main` between
  2026-08-18 and 2026-09-11 (placeholder-content bugs and a stale
  roster dump wedged into this section), each requiring a manual fix
  commit. Direct-to-main pushes are retired in favor of the
  branch + PR + structural-validation flow above. Future
  re-affirmations or changes should be added as new dated lines
  here, not by editing this history in place.

## Identity
- Sleeper username: Scvazquez
- Sleeper user ID: 1257100239429435392
- League ID: 1336098153778155520
- Roster ID: 9

## Win Window & Strategy
Targeting a 2-year win window. Prioritize win-now production for
veterans. Never recommend moving players aged 24 or younger without
explicitly flagging the dynasty cost.

## Trade Intelligence
- Larz1111 (Roster 5): my father-in-law. Starts Dak Prescott;
  also owns Lamar Jackson and Anthony Richardson on the bench
  as surplus veteran QBs, plus Taylen Green and Ty Simpson on
  taxi. Warmest trade target in the league. (Corrected 2026-08-05:
  he does not own Stafford — that was a stale note. Stafford is
  on my own bench.)
- Darkkaze (Roster 7): 4 QBs — monitor for surplus deals
- DRoj (Roster 8): 7 QBs — will cut soon, watch for desperation
  value trades

## League Name
FOOTBALL JUNKIES — Season 2026

## League Format
12-team dynasty IDP
Roster: 31 players + 3 taxi slots (rookies only) + 2 IR slots

Lineup (exact slot order from API):
  QB   × 1
  RB   × 2
  WR   × 2
  TE   × 1
  FLEX × 3  ← RB/WR/TE eligible
  K    × 1
  DEF  × 1
  LB   × 2
  DB   × 2
  Total starters: 15

Note: 3 FLEX slots make RB and WR depth interchangeable.
Do not treat WR surplus and RB surplus as separate — they
compete for the same 3 flex spots. Evaluate positional
value accordingly.

## Scoring System

### Passing
| Category              | Points |
|-----------------------|--------|
| Passing yard          | 0.04   |
| Passing TD            | 6      |
| Interception thrown   | -1     |
| 2-point conversion    | 2      |
| First down (pass)     | 1      |
| TD 40+ yards bonus    | +1     |
| TD 50+ yards bonus    | +2     |
| Completion 40+ bonus  | +1     |

Note: 25 passing yards = 1 point. 6-point passing TDs —
premium QB value league.

### Rushing
| Category              | Points |
|-----------------------|--------|
| Rushing yard          | 0.1    |
| Rushing TD            | 6      |
| 2-point conversion    | 2      |
| First down (rush)     | 1      |
| Rush 40+ yards bonus  | +1     |
| Rush TD 40+ bonus     | +1     |
| Rush TD 50+ bonus     | +2     |

Note: 10 rushing yards = 1 point.

### Receiving
| Category              | Points |
|-----------------------|--------|
| Reception             | 1      |
| Receiving yard        | 0.1    |
| Receiving TD          | 6      |
| 2-point conversion    | 2      |
| First down (rec)      | 1      |
| Rec 40+ yards bonus   | +1     |
| Rec TD 40+ bonus      | +1     |
| Rec TD 50+ bonus      | +2     |

Note: Full PPR (1 point per reception). 10 receiving yards
= 1 point. Target hogs and high-volume slot receivers are
significantly boosted in this format.

### Fumbles
| Category              | Points |
|-----------------------|--------|
| Fumble lost           | -2     |
| Fumble recovered      | 2      |
| Fumble rec TD         | 6      |
| Fumble (no penalty)   | 0      |

### Kicking
| Category              | Points |
|-----------------------|--------|
| FG 0–29 yards         | 3      |
| FG 30–39 yards        | 3      |
| FG 40–49 yards        | 4      |
| FG 50+ yards          | 5      |
| FG miss               | -1     |
| Extra point made      | 1      |
| Extra point miss      | -3     |

### Team Defense
| Category              | Points |
|-----------------------|--------|
| Sack                  | 1      |
| Interception          | 2      |
| Fumble recovery       | 2      |
| Defensive TD          | 6      |
| Safety                | 2      |
| Blocked kick          | 2      |
| Points allowed 0      | 10     |
| Points allowed 1–6    | 7      |
| Points allowed 7–13   | 4      |
| Points allowed 14–20  | 1      |
| Points allowed 21–27  | 0      |
| Points allowed 28–34  | -1     |
| Points allowed 35+    | -4     |
| Forced fumble         | 1      |
| 3-and-out             | 1      |
| 4th down stop         | 1      |
| ST fumble recovery    | 1      |
| ST forced fumble      | 1      |
| ST TD                 | 6      |
| Tackle for loss       | 1      |
| Sack 2+ in game bonus | 1      |

### IDP Scoring
| Category              | Points |
|-----------------------|--------|
| Solo tackle           | 1      |
| Assist tackle         | 0.5    |
| Tackle for loss       | 1      |
| Sack                  | 2      |
| Interception          | 2      |
| Pass deflection       | 1      |
| Pass deflection 3+    | +1     |
| Forced fumble         | 2      |
| Fumble recovery       | 2      |
| Safety                | 2      |
| Blocked kick          | 2      |
| Defensive TD          | 6      |
| 10+ tackle game bonus | 2      |
| QB hit                | 0      |

Note: IDP sacks (2 pts) and INTs (2 pts) are high-value.
High-volume tacklers benefit from the 10+ tackle game
bonus (+2). QB hits score 0 — do not value players for
QB hit totals.

## League Rules & Settings
- Format: Dynasty (type 2), Season 2026
- Teams: 12
- Waiver type: FAAB ($500 budget)
- Waiver processing: Tuesday
- Trade deadline: Week 11
- Trade review period: 1 day
- Playoff teams: 6 (top 6 qualify)
- Playoff start: Week 15
- Draft rounds: 5 per year
- Pick trading: Enabled
- Taxi eligibility: Rookies only (vets cannot be taxied)
- Reserve/IR slots: 2
- League average matchup: No
- Best ball: No

## Waiver Wire Strategy
FAAB format with $500 budget. Blind bidding — opponent bids
are not visible. Budget management is a season-long asset.
Do not burn large FAAB on speculative adds. Reserve
significant budget (100+) for high-impact injury
replacements mid-season.

<!-- ============================================================ -->
<!-- AUTO SECTION — managed entirely by Roster Sync routine       -->
<!-- DO NOT EDIT BELOW THIS LINE                                  -->
<!-- ============================================================ -->
<!-- BEGIN_AUTO_GENERATED -->
## Roster State
Last synced: 2026-10-29 12:55 PM UTC (auto sync)

## Ownership Index
```
<!--
  Full set of all owned player IDs across all 12 rosters.
  Fantasy Scout uses this for verified free agent checks.
  Format: one ID per line inside a code block for easy parsing.
-->
96
421
650
1166
1373
1466
1479
2020
2133
2216
2306
2449
2505
2617
2747
3160
3163
3198
3214
3257
3271
3294
3451
3634
4017
4033
4034
4035
4037
4039
4046
4070
4081
4137
4147
4199
4217
4454
4663
4718
4866
4881
4892
4943
4960
4963
4971
4983
4984
4993
5001
5012
5017
5022
5041
5045
5332
5372
5843
5844
5846
5849
5850
5859
5870
5872
5876
5892
5927
5944
5947
5967
5995
6039
6083
6130
6183
6217
6485
6650
6768
6770
6783
6786
6788
6790
6794
6797
6801
6804
6806
6813
6815
6819
6860
6865
6904
6911
6949
7002
7016
7021
7042
7049
7069
7083
7090
7523
7525
7526
7527
7528
7543
7547
7553
7562
7564
7567
7569
7571
7588
7594
7600
7611
7640
7648
7672
7839
7841
8110
8111
8112
8116
8119
8121
8122
8126
8129
8130
8131
8132
8134
8135
8136
8137
8138
8142
8144
8146
8147
8148
8150
8151
8154
8155
8161
8167
8172
8180
8183
8188
8205
8207
8210
8228
8266
8267
8329
8330
8339
8408
8676
8698
8800
9221
9224
9225
9226
9228
9229
9230
9479
9480
9482
9484
9486
9487
9488
9493
9500
9501
9502
9504
9506
9508
9509
9511
9753
9754
9756
9757
9758
9997
10213
10219
10222
10229
10232
10235
10236
10857
10859
10880
10892
10949
10955
11034
11199
11237
11427
11435
11439
11533
11539
11557
11559
11560
11563
11564
11565
11566
11571
11575
11576
11581
11583
11584
11586
11589
11603
11604
11608
11610
11618
11620
11623
11624
11625
11627
11628
11630
11631
11632
11635
11637
11638
11643
11646
11647
11655
11678
11687
11705
11727
11729
11731
11739
11783
11786
11792
11834
12048
12185
12457
12469
12471
12474
12481
12482
12483
12484
12485
12487
12489
12490
12491
12492
12493
12495
12497
12498
12499
12501
12502
12504
12506
12507
12508
12509
12511
12512
12514
12517
12518
12519
12521
12522
12524
12526
12527
12529
12530
12531
12533
12534
12535
12536
12540
12541
12542
12543
12544
12545
12547
12567
12578
12591
12597
12617
12619
12718
13150
13264
13268
13269
13270
13272
13274
13275
13276
13277
13278
13279
13281
13285
13286
13287
13288
13289
13293
13294
13296
13297
13298
13299
13301
13302
13303
13305
13306
13311
13317
13319
13320
13324
13329
13330
13333
13335
13337
13338
13342
13345
13346
13347
13348
13349
13353
13363
13371
13375
13376
13377
13379
13380
13394
13401
13402
13404
13405
13411
13413
13414
13417
13420
13421
13423
13424
13453
13533
13545
13602
13726
BAL
CAR
CIN
CLE
DEN
DET
HOU
JAX
KC
LAR
MIN
NE
NYJ
PHI
PIT
SEA
SF
TB
WAS
```

## My Roster — Scvazquez (Roster 9)

### Starting Lineup

| Slot | Player | Pos | Team | Age |
|------|--------|-----|------|-----|
| QB | Matthew Stafford | QB | LAR | 38 |
| RB | Rico Dowdle | RB | PIT | 28 |
| RB | Saquon Barkley | RB | PHI | 29 |
| WR | CeeDee Lamb | WR | DAL | 27 |
| WR | Justin Jefferson | WR | MIN | 27 |
| TE | Kyle Pitts Sr. | TE | ATL | 26 |
| FLEX | Ladd McConkey | WR | LAC | 24 |
| FLEX | Jordan Addison | WR | MIN | 24 |
| FLEX | Mark Andrews | TE | BAL | 31 |
| K | Will Reichard | K | MIN | 25 |
| DEF | Detroit Lions | DEF | DET | ? |
| LB | Zack Baun | LB | PHI | 29 |
| LB | Quay Walker | LB | LV | 26 |
| DB | Kyle Hamilton | DB | BAL | 25 |
| DB | Xavier McKinney | DB | GB | 28 |

### Bench

- Alvin Kamara (RB, NO, Age 31, 9 yr exp)
- Christian Izien (DB, DET, Age 26, 3 yr exp)
- Darren Waller (TE, CAR, Age 34, 11 yr exp)
- David Montgomery (RB, HOU, Age 29, 7 yr exp)
- Derwin James Jr. (DB, LAC, Age 30, 8 yr exp)
- Edgerrin Cooper (LB, GB, Age 24, 2 yr exp)
- Elijah Arroyo (TE, SEA, Age 23, 1 yr exp)
- Jayden Daniels (QB, WAS, Age 25, 2 yr exp)
- Jaylin Noel (WR, HOU, Age 24, 1 yr exp)
- Kendrick Bourne (WR, ARI, Age 31, 9 yr exp)
- LeQuint Allen Jr. (RB, JAX, Age 22, 1 yr exp)
- Malik Davis (RB, DAL, Age 27, 4 yr exp)
- Tahj Brooks (RB, CIN, Age 24, 1 yr exp)
- Tampa Bay Buccaneers (DEF, TB, Age ?, ? yr exp)
- Terry McLaurin (WR, WAS, Age 31, 7 yr exp)
- Tre' Harris (WR, LAC, Age 24, 1 yr exp)
- Tyler Bass (K, BUF, Age 29, 6 yr exp)
- Will Anderson Jr. (DL, HOU, Age 25, 3 yr exp)

### Taxi Squad

- Cyrus Allen (WR, KC, Age 23) 🟡 ROOKIE
- Jack Strand (QB, ATL, Age 22) 🟡 ROOKIE

## All Opponent Rosters

### SmokeYall (Roster 1)

**Starters:**
- Joe Burrow (QB, CIN)
- Bucky Irving (RB, TB)
- Jahmyr Gibbs (RB, DET)
- Michael Wilson (WR, ARI)
- DeVonta Smith (WR, PHI)
- AJ Barner (TE, SEA)
- TreVeyon Henderson (RB, NE)
- Ollie Gordon II (RB, MIA)
- Puka Nacua (WR, LAR)
- Trey Smack (K, GB)
- Los Angeles Rams (DEF, LAR)
- Nakobe Dean (LB, LV)
- Devin Lloyd (LB, CAR)
- Alohi Gilman (DB, KC)
- Jessie Bates III (DB, ATL)

**QB Room (3 QBs):**
- Joe Burrow (CIN)
- Jordan Love (GB)
- Shedeur Sanders (CLE)

**Positional Surplus (3+ players at same position):**
- QB (3): Joe Burrow, Jordan Love, Shedeur Sanders
- RB (8): Bucky Irving, Emari Demercado, J'Mari Taylor, Jahmyr Gibbs, Jaleel McLaughlin, Jaydon Blue, Ollie Gordon II, TreVeyon Henderson
- TE (3): AJ Barner, George Kittle, Jake Tonges
- WR (16): Barion Brown, Chris Brazzell II, DJ Moore, DeVonta Smith, Isaac TeSlaa, Jalen Brooks, Jayden Reed, Malik Benson, Michael Wilson, Puka Nacua, Savion Williams, Skyler Bell, Ted Hurst III, Tory Horton, Tutu Atwell, Zavion Thomas

**Bench depth:**
- Barion Brown (WR, NO)
- Chris Brazzell II (WR, CAR)
- DJ Moore (WR, BUF)
- Emari Demercado (RB, HOU)
- George Kittle (TE, SF)
- Isaac TeSlaa (WR, DET)
- J'Mari Taylor (RB, JAX)
- Jake Tonges (TE, SF)
- Jaleel McLaughlin (RB, CLE)
- Jalen Brooks (WR, ARI)
- Jayden Reed (WR, GB)
- Jaydon Blue (RB, PHI)
- Jordan Love (QB, GB)
- Malik Benson (WR, LV)
- Savion Williams (WR, GB)
- Shedeur Sanders (QB, CLE)
- Skyler Bell (WR, BUF)
- Ted Hurst III (WR, TB)
- Tory Horton (WR, SEA)
- Tutu Atwell (WR, LAR)
- Zavion Thomas (WR, CHI)

### JQuinna10 (Roster 2)

**Starters:**
- Drake Maye (QB, NE)
- Kenneth Walker III (RB, KC)
- Rhamondre Stevenson (RB, NE)
- Tetairoa McMillan (WR, CAR)
- Denzel Boston (WR, CLE)
- Dallas Goedert (TE, PHI)
- Luther Burden III (WR, CHI)
- Jeremiyah Love (RB, ARI)
- Blake Corum (RB, LAR)
- Cam Little (K, JAX)
- New England Patriots (DEF, NE)
- Carson Schwesinger (LB, CLE)
- Blake Cashman (LB, MIN)
- Travis Hunter (DB, JAX)
- Nick Emmanwori (DB, SEA)

**QB Room (4 QBs):**
- Carson Beck (ARI)
- Drake Maye (NE)
- Jacoby Brissett (ARI)
- Jameis Winston (NYG)

**Positional Surplus (3+ players at same position):**
- QB (4): Carson Beck, Drake Maye, Jacoby Brissett, Jameis Winston
- RB (12): Blake Corum, Corey Kiner, Dylan Sampson, Emmett Johnson, Jeremiyah Love, Kenneth Walker III, Nicholas Singleton, Rhamondre Stevenson, Tank Bigsby, Trevor Etienne, Tyler Allgeier, Zach Charbonnet
- TE (4): Dallas Goedert, Eli Raridon, Eli Stowers, T.J. Hockenson
- WR (9): Denzel Boston, Efton Chism III, Konata Mumpfield, Kyle Williams, Luther Burden III, Marvin Harrison Jr., Pat Bryant, Romeo Doubs, Tetairoa McMillan

**Bench depth:**
- Carson Beck (QB, ARI)
- Corey Kiner (RB, NE)
- Dylan Sampson (RB, CLE)
- Efton Chism III (WR, NE)
- Eli Raridon (TE, NE)
- Eli Stowers (TE, PHI)
- Emmett Johnson (RB, KC)
- Houston Texans (DEF, HOU)
- Jacoby Brissett (QB, ARI)
- Jameis Winston (QB, NYG)
- Konata Mumpfield (WR, LAR)
- Kyle Williams (WR, NE)
- Marvin Harrison Jr. (WR, HOU)
- Nicholas Singleton (RB, TEN)
- Pat Bryant (WR, DEN)
- Romeo Doubs (WR, NE)
- T.J. Hockenson (TE, MIN)
- Tank Bigsby (RB, PHI)
- Trevor Etienne (RB, CAR)
- Tyler Allgeier (RB, ARI)
- Zach Charbonnet (RB, SEA)

### WOODYWOOD1978 (Roster 3)

**Starters:**
- Jared Goff (QB, DET)
- Woody Marks (RB, HOU)
- Dare Ogunbowale (RB, HOU)
- Devaughn Vele (WR, NO)
- Matthew Golden (WR, GB)
- Brock Bowers (TE, LV)
- Carnell Tate (WR, TEN)
- Travis Kelce (TE, KC)
- Rome Odunze (WR, CHI)
- Nick Folk (K, ATL)
- Washington Commanders (DEF, WAS)
- Andrew Van Ginkel (LB, MIN)
- Bobby Okereke (LB, CAR)
- D.J. Reed (CB, DET)
- Dillon Thieneman (DB, CHI)

**QB Room (3 QBs):**
- Jared Goff (DET)
- Jaxson Dart (NYG)
- Michael Penix Jr. (ATL)

**Positional Surplus (3+ players at same position):**
- LB (3): Andrew Van Ginkel, Bobby Okereke, Sonny Styles
- QB (3): Jared Goff, Jaxson Dart, Michael Penix Jr.
- RB (8): Bhayshul Tuten, Dare Ogunbowale, Jacob Saylors, Jadarian Price, James Cook III, Kyle Monangai, Tyjae Spears, Woody Marks
- WR (15): Antonio Williams, Brian Thomas Jr., Camden Brown, Carnell Tate, Darius Cooper, Devaughn Vele, Dohnte Meyers, Isaiah Williams, Ja'Kobi Lane, Kayshon Boutte, Matthew Golden, Quentin Johnston, Ricky Pearsall, Rome Odunze, Treylon Burks

**Bench depth:**
- Antonio Williams (WR, WAS)
- Bhayshul Tuten (RB, JAX)
- Brian Thomas Jr. (WR, JAX)
- Camden Brown (WR, DAL)
- Darius Cooper (WR, PHI)
- Dohnte Meyers (WR, CIN)
- Isaiah Williams (WR, NYJ)
- Ja'Kobi Lane (WR, BAL)
- Jacob Saylors (RB, DET)
- Jadarian Price (RB, SEA)
- James Cook III (RB, BUF)
- Jaxson Dart (QB, NYG)
- Kayshon Boutte (WR, HOU)
- Kyle Monangai (RB, CHI)
- Michael Penix Jr. (QB, ATL)
- Quentin Johnston (WR, LAC)
- Ricky Pearsall (WR, SF)
- Sonny Styles (LB, WAS)
- Treylon Burks (WR, WAS)
- Tyjae Spears (RB, TEN)

### Bombas (Roster 4)

**Starters:**
- Malik Willis (QB, MIA)
- RJ Harvey (RB, DEN)
- Kendre Miller (RB, NO)
- KC Concepcion Jr. (WR, CLE)
- Tre Tucker (WR, LV)
- Kenyon Sadiq (TE, NYJ)
- Braelon Allen (RB, NYJ)
- Germie Bernard (WR, PIT)
- Omar Cooper Jr. (WR, NYJ)
- Cairo Santos (K, CHI)
- Cleveland Browns (DEF, CLE)
- Devin Bush (LB, CHI)
- Jordyn Brooks (LB, MIA)
- Julian Love (DB, SEA)
- Malik Mustapha (DB, SF)

**QB Room (3 QBs):**
- Fernando Mendoza (LV)
- Malik Willis (MIA)
- Trevor Lawrence (JAX)

**Positional Surplus (3+ players at same position):**
- QB (3): Fernando Mendoza, Malik Willis, Trevor Lawrence
- RB (10): Braelon Allen, CJ Donaldson, Dameon Pierce, Demond Claiborne, Kaleb Johnson, Kaytron Allen, Kendre Miller, Pierre Strong Jr., RJ Harvey, Roschon Johnson
- TE (4): Darnell Washington, Kenyon Sadiq, Oronde Gadsden, Tyler Higbee
- WR (13): Adonai Mitchell, Dontayvion Wicks, Germie Bernard, Jack Bech, Jayden Higgins, Josh Cameron, KC Concepcion Jr., Keon Coleman, Malachi Fields, Omar Cooper Jr., Rashod Bateman, Tre Tucker, Troy Franklin

**Bench depth:**
- Adonai Mitchell (WR, NYJ)
- CJ Donaldson (RB, NO)
- Dameon Pierce (RB, PHI)
- Darnell Washington (TE, PIT)
- Demond Claiborne (RB, MIN)
- Dontayvion Wicks (WR, PHI)
- Fernando Mendoza (QB, LV)
- Jack Bech (WR, LV)
- Jayden Higgins (WR, HOU)
- Josh Cameron (WR, JAX)
- Kaleb Johnson (RB, GB)
- Kaytron Allen (RB, MIA)
- Keon Coleman (WR, BUF)
- Malachi Fields (WR, NYG)
- Oronde Gadsden (TE, LAC)
- Pierre Strong Jr. (RB, GB)
- Rashod Bateman (WR, BAL)
- Roschon Johnson (RB, CHI)
- Trevor Lawrence (QB, JAX)
- Troy Franklin (WR, DEN)
- Tyler Higbee (TE, LAR)

### Larz1111 (Roster 5)

**Starters:**
- Dak Prescott (QB, DAL)
- Chuba Hubbard (RB, CAR)
- Javonte Williams (RB, DAL)
- Jaxon Smith-Njigba (WR, SEA)
- Rashee Rice (WR, KC)
- Cade Otton (TE, TB)
- Jonah Coleman (RB, DEN)
- Jalen Coker (WR, CAR)
- Parker Washington (WR, JAX)
- Jake Bates (K, DET)
- Jacksonville Jaguars (DEF, JAX)
- Akeem Davis-Gaither (LB, IND)
- Alex Singleton (LB, DEN)
- Tykee Smith (DB, TB)
- Cooper DeJean (DB, PHI)

**QB Room (7 QBs):**
- Anthony Richardson Sr. (IND)
- Dak Prescott (DAL)
- Lamar Jackson (BAL)
- Tanner McKee (PHI)
- Taylen Green (CLE)
- Ty Simpson (LAR)
- Tyler Huntley (BAL)

**Positional Surplus (3+ players at same position):**
- QB (7): Anthony Richardson Sr., Dak Prescott, Lamar Jackson, Tanner McKee, Taylen Green, Ty Simpson, Tyler Huntley
- RB (8): Brian Robinson Jr., Chuba Hubbard, Javonte Williams, Jonah Coleman, Jonathon Brooks, Kaelon Black, Keaton Mitchell, Omarion Hampton
- TE (5): Cade Otton, Chig Okonkwo, Dalton Schultz, Michael Mayer, Terrance Ferguson
- WR (9): Alec Pierce, Elijah Sarratt, Jahan Dotson, Jalen Coker, Jaxon Smith-Njigba, Makai Lemon, Parker Washington, Rashee Rice, Wan'Dale Robinson

**Bench depth:**
- Alec Pierce (WR, IND)
- Anthony Richardson Sr. (QB, IND)
- Brian Robinson Jr. (RB, ATL)
- Carolina Panthers (DEF, CAR)
- Chig Okonkwo (TE, WAS)
- Dalton Schultz (TE, HOU)
- Elijah Sarratt (WR, BAL)
- Jahan Dotson (WR, ATL)
- Jonathon Brooks (RB, CAR)
- Kaelon Black (RB, SF)
- Keaton Mitchell (RB, LAC)
- Lamar Jackson (QB, BAL)
- Makai Lemon (WR, PHI)
- Michael Mayer (TE, LV)
- Omarion Hampton (RB, LAC)
- Tanner McKee (QB, PHI)
- Taylen Green (QB, CLE)
- Terrance Ferguson (TE, LAR)
- Ty Simpson (QB, LAR)
- Tyler Huntley (QB, BAL)
- Wan'Dale Robinson (WR, TEN)

### SnaggyNoDiploma (Roster 6)

**Starters:**
- Josh Allen (QB, BUF)
- Bijan Robinson (RB, ATL)
- Josh Jacobs (RB, GB)
- Tee Higgins (WR, CIN)
- Stefon Diggs (WR, WAS)
- Trey McBride (TE, ARI)
- DK Metcalf (WR, PIT)
- Josh Downs (WR, IND)
- Jaylen Waddle (WR, DEN)
- Evan McPherson (K, CIN)
- Seattle Seahawks (DEF, SEA)
- Foyesade Oluokun (LB, JAX)
- Ernest Jones IV (LB, SEA)
- Minkah Fitzpatrick (DB, NYJ)
- Jalen Ramsey (CB, PIT)

**QB Room (3 QBs):**
- Jalen Hurts (PHI)
- Josh Allen (BUF)
- Stetson Bennett IV (LAR)

**Positional Surplus (3+ players at same position):**
- LB (3): Ernest Jones IV, Foyesade Oluokun, Nick Bolton
- QB (3): Jalen Hurts, Josh Allen, Stetson Bennett IV
- RB (6): Bijan Robinson, Jacory Croskey-Merritt, Josh Jacobs, Sione Vaki, Ty Johnson, Tyler Goodson
- TE (4): Colby Parkinson, Greg Dulcich, Juwan Johnson, Trey McBride
- WR (12): Chris Godwin Jr., DK Metcalf, Dont'e Thornton Jr., Jaylen Waddle, John Metchie III, Jordan Whittington, Josh Downs, Kalif Raymond, Michael Pittman Jr., Stefon Diggs, Tee Higgins, Tez Johnson

**Bench depth:**
- Chase McLaughlin (K, TB)
- Chris Godwin Jr. (WR, TB)
- Colby Parkinson (TE, LAR)
- Dont'e Thornton Jr. (WR, LV)
- Greg Dulcich (TE, MIA)
- Jacory Croskey-Merritt (RB, WAS)
- Jalen Hurts (QB, PHI)
- John Metchie III (WR, CAR)
- Jordan Whittington (WR, LAR)
- Juwan Johnson (TE, NO)
- Kalif Raymond (WR, CHI)
- Michael Pittman Jr. (WR, PIT)
- Nick Bolton (LB, KC)
- Sione Vaki (RB, DET)
- Stetson Bennett IV (QB, LAR)
- Tez Johnson (WR, TB)
- Ty Johnson (RB, BUF)
- Tyler Goodson (RB, DAL)

### Darkkaze (Roster 7)

**Starters:**
- Caleb Williams (QB, CHI)
- Jaylen Warren (RB, PIT)
- Chase Brown (RB, CIN)
- Drake London (WR, ATL)
- Amon-Ra St. Brown (WR, DET)
- Tyler Warren (TE, IND)
- George Pickens (WR, DAL)
- Emanuel Wilson (RB, SEA)
- Jordan Mason (RB, MIN)
- Chad Ryland (K, ARI)
- Cincinnati Bengals (DEF, CIN)
- David Bailey (LB, NYJ)
- Payton Wilson (LB, PIT)
- Quentin Lake (DB, LAR)
- Evan Williams (DB, GB)

**QB Room (4 QBs):**
- Caleb Williams (CHI)
- Drew Allar (PIT)
- Sam Darnold (SEA)
- Tyler Shough (NO)

**Positional Surplus (3+ players at same position):**
- DEF (3): Cincinnati Bengals, Denver Broncos, Pittsburgh Steelers
- QB (4): Caleb Williams, Drew Allar, Sam Darnold, Tyler Shough
- RB (9): Chase Brown, De'Von Achane, Emanuel Wilson, J.K. Dobbins, Jaylen Warren, Jaylen Wright, Jordan Mason, Kenny Gainwell, Travis Etienne Jr.
- TE (5): Gunnar Helm, Mason Taylor, Matt Hibner, Max Klare, Tyler Warren
- WR (8): Amon-Ra St. Brown, Bryce Lance, Drake London, George Pickens, Keenan Allen, Khalil Shakir, Malik Washington, Rashid Shaheed

**Bench depth:**
- Bryce Lance (WR, NO)
- De'Von Achane (RB, MIA)
- Denver Broncos (DEF, DEN)
- Drew Allar (QB, PIT)
- Gunnar Helm (TE, TEN)
- J.K. Dobbins (RB, DEN)
- Jaylen Wright (RB, MIA)
- Ka'imi Fairbairn (K, HOU)
- Keenan Allen (WR, IND)
- Kenny Gainwell (RB, TB)
- Khalil Shakir (WR, BUF)
- Malik Washington (WR, MIA)
- Mason Taylor (TE, NYJ)
- Matt Hibner (TE, BAL)
- Max Klare (TE, LAR)
- Pittsburgh Steelers (DEF, PIT)
- Rashid Shaheed (WR, SEA)
- Sam Darnold (QB, SEA)
- Travis Etienne Jr. (RB, NO)
- Tyler Shough (QB, NO)

### DRoj (Roster 8)

**Starters:**
- Kirk Cousins (QB, LV)
- Quinshon Judkins (RB, CLE)
- Kyren Williams (RB, LAR)
- Xavier Worthy (WR, KC)
- Garrett Wilson (WR, NYJ)
- Sam LaPorta (TE, DET)
- Breece Hall (RB, NYJ)
- Harold Fannin Jr. (TE, CLE)
- Brenton Strange (TE, JAX)
- Matt Gay (K, LV)
- New York Jets (DEF, NYJ)
- Jamien Sherwood (LB, NYJ)
- Azeez Al-Shaair (LB, HOU)
- Malaki Starks (DB, BAL)
- Jeremy Chinn (DB, LV)

**QB Room (7 QBs):**
- Aaron Rodgers (PIT)
- Bo Nix (DEN)
- Bryce Young (CAR)
- C.J. Stroud (HOU)
- Daniel Jones (IND)
- Kirk Cousins (LV)
- Patrick Mahomes (KC)

**Positional Surplus (3+ players at same position):**
- QB (7): Aaron Rodgers, Bo Nix, Bryce Young, C.J. Stroud, Daniel Jones, Kirk Cousins, Patrick Mahomes
- RB (7): Aaron Jones Sr., Breece Hall, Isiah Pacheco, Kyren Williams, Mike Washington Jr., Quinshon Judkins, Zonovan Knight
- TE (5): Brenton Strange, Harold Fannin Jr., Jake Ferguson, Pat Freiermuth, Sam LaPorta
- WR (9): Chris Olave, Deebo Samuel Sr., Elic Ayomanor, Garrett Wilson, Jalen Nailor, Jerry Jeudy, Tank Dell, Xavier Worthy, Zachariah Branch

**Bench depth:**
- Aaron Jones Sr. (RB, MIN)
- Aaron Rodgers (QB, PIT)
- Bo Nix (QB, DEN)
- Bryce Young (QB, CAR)
- C.J. Stroud (QB, HOU)
- Chris Olave (WR, NO)
- Daniel Jones (QB, IND)
- Deebo Samuel Sr. (WR, SF)
- Elic Ayomanor (WR, TEN)
- Isiah Pacheco (RB, DET)
- Jake Ferguson (TE, DAL)
- Jalen Nailor (WR, LV)
- Jerry Jeudy (WR, CLE)
- Mike Washington Jr. (RB, LV)
- Pat Freiermuth (TE, PIT)
- Patrick Mahomes (QB, KC)
- Tank Dell (WR, HOU)
- Zachariah Branch (WR, ATL)
- Zonovan Knight (RB, ARI)

### Jdunn502 (Roster 10)

**Starters:**
- Kyler Murray (QB, MIN)
- Ashton Jeanty (RB, LV)
- Cam Skattebo (RB, NYG)
- Ja'Marr Chase (WR, CIN)
- Malik Nabers (WR, NYG)
- Tucker Kraft (TE, GB)
- Christian Watson (WR, GB)
- Tony Pollard (RB, TEN)
- Colston Loveland (TE, CHI)
- Spencer Shrader (K, IND)
- San Francisco 49ers (DEF, SF)
- Josiah Trotter (LB, TB)
- Jacob Rodriguez (LB, MIA)
- Jonas Sanker (DB, NO)
- Brandon Jones (DB, DEN)

**QB Room (8 QBs):**
- Cade Klubnik (NYJ)
- Cam Ward (TEN)
- Cole Payton (PHI)
- Deshaun Watson (CLE)
- Geno Smith (NYJ)
- Joe Milton (PHI)
- Kyler Murray (MIN)
- Will Howard (PIT)

**Positional Surplus (3+ players at same position):**
- LB (3): Jacob Rodriguez, Josiah Trotter, T.J. Watt
- QB (8): Cade Klubnik, Cam Ward, Cole Payton, Deshaun Watson, Geno Smith, Joe Milton, Kyler Murray, Will Howard
- RB (9): Ashton Jeanty, Cam Skattebo, Chris Rodriguez Jr., Devin Singletary, MarShawn Lloyd, Ray Davis, Seth McGowan, Tony Pollard, Tyrone Tracy Jr.
- TE (3): Colston Loveland, Oscar Delp, Tucker Kraft
- WR (8): Caleb Douglas, Chris Bell, Christian Watson, Ja'Marr Chase, Jalen McMillan, Jordyn Tyson, Malik Nabers, Reggie Virgil

**Bench depth:**
- Cade Klubnik (QB, NYJ)
- Caleb Douglas (WR, MIA)
- Cam Ward (QB, TEN)
- Chris Bell (WR, MIA)
- Chris Rodriguez Jr. (RB, JAX)
- Cole Payton (QB, PHI)
- Deshaun Watson (QB, CLE)
- Devin Singletary (RB, NYG)
- Geno Smith (QB, NYJ)
- Jalen McMillan (WR, TB)
- Joe Milton (QB, PHI)
- Jordyn Tyson (WR, NO)
- Kansas City Chiefs (DEF, KC)
- MarShawn Lloyd (RB, GB)
- Oscar Delp (TE, NO)
- Ray Davis (RB, BUF)
- Reggie Virgil (WR, ARI)
- Seth McGowan (RB, IND)
- T.J. Watt (LB, PIT)
- Tyrone Tracy Jr. (RB, NYG)
- Will Howard (QB, PIT)

### nicoyepes (Roster 11)

**Starters:**
- Justin Herbert (QB, LAC)
- Jonathan Taylor (RB, IND)
- Christian McCaffrey (RB, SF)
- Nico Collins (WR, HOU)
- DeMario Douglas (WR, NE)
- Hunter Henry (TE, NE)
- Davante Adams (WR, LAR)
- D'Andre Swift (RB, CHI)
- A.J. Brown (WR, NE)
- Jason Myers (K, SEA)
- Baltimore Ravens (DEF, BAL)
- Arvell Reese (LB, NYG)
- Roquan Smith (LB, BAL)
- Caleb Downs (DB, DAL)
- Chamarri Conner (DB, KC)

**QB Room (3 QBs):**
- Garrett Nussmeier (KC)
- Justin Herbert (LAC)
- Tua Tagovailoa (ATL)

**Positional Surplus (3+ players at same position):**
- LB (4): Arvell Reese, Jack Campbell, Micah Parsons, Roquan Smith
- QB (3): Garrett Nussmeier, Justin Herbert, Tua Tagovailoa
- RB (7): Christian McCaffrey, D'Andre Swift, DJ Giddens, James Conner, Jonathan Taylor, Sean Tucker, Trey Benson
- TE (5): David Njoku, Hunter Henry, John Michael Gyllenborg, Mike Gesicki, Nate Boerkircher
- WR (12): A.J. Brown, Brenen Thompson, CJ Daniels, Courtland Sutton, Davante Adams, DeMario Douglas, Deion Burks, Jameson Williams, Kevin Coleman Jr., Nico Collins, Ryan Flournoy, Tyquan Thornton

**Bench depth:**
- Brenen Thompson (WR, LAC)
- CJ Daniels (WR, LAR)
- Courtland Sutton (WR, DEN)
- DJ Giddens (RB, IND)
- David Njoku (TE, LAC)
- Deion Burks (WR, IND)
- Garrett Nussmeier (QB, KC)
- Jack Campbell (LB, DET)
- James Conner (RB, ARI)
- Jameson Williams (WR, DET)
- John Michael Gyllenborg (TE, KC)
- Kevin Coleman Jr. (WR, MIA)
- Micah Parsons (LB, GB)
- Mike Gesicki (TE, CIN)
- Nate Boerkircher (TE, JAX)
- Ryan Flournoy (WR, DAL)
- Sean Tucker (RB, TB)
- Trey Benson (RB, ARI)
- Tua Tagovailoa (QB, ATL)
- Tyquan Thornton (WR, KC)

### BedStuyBallers21 (Roster 12)

**Starters:**
- Baker Mayfield (QB, TB)
- Derrick Henry (RB, BAL)
- Rachaad White (RB, WAS)
- Jakobi Meyers (WR, JAX)
- Zay Flowers (WR, BAL)
- Dalton Kincaid (TE, BUF)
- Cooper Kupp (WR, SEA)
- Jauan Jennings (WR, MIN)
- Chimere Dike (WR, TEN)
- Brandon Aubrey (K, DAL)
- Philadelphia Eagles (DEF, PHI)
- Demetrius Knight Jr. (LB, CIN)
- Fred Warner (LB, SF)
- Budda Baker (DB, ARI)
- Xavier Watts (DB, ATL)

**QB Room (4 QBs):**
- Baker Mayfield (TB)
- Brock Purdy (SF)
- J.J. McCarthy (NYG)
- Mac Jones (SF)

**Positional Surplus (3+ players at same position):**
- QB (4): Baker Mayfield, Brock Purdy, J.J. McCarthy, Mac Jones
- RB (11): Adam Randall, Austin Ekeler, Derrick Henry, Eli Heidenreich, George Holani, Isaiah Davis, Justice Hill, Kimani Vidal, Najee Harris, Rachaad White, Samaje Perine
- TE (3): Dalton Kincaid, Isaiah Likely, Michael Trigg
- WR (10): Chimere Dike, Cooper Kupp, Darnell Mooney, De'Zhaun Stribling, Emeka Egbuka, Jakobi Meyers, Jauan Jennings, Mike Evans, Roman Wilson, Zay Flowers

**Bench depth:**
- Adam Randall (RB, BAL)
- Austin Ekeler (RB, WAS)
- Brock Purdy (QB, SF)
- Darnell Mooney (WR, NYG)
- De'Zhaun Stribling (WR, SF)
- Eli Heidenreich (RB, PIT)
- Emeka Egbuka (WR, TB)
- George Holani (RB, SEA)
- Isaiah Davis (RB, NYJ)
- Isaiah Likely (TE, NYG)
- J.J. McCarthy (QB, NYG)
- Justice Hill (RB, BAL)
- Kimani Vidal (RB, LAC)
- Mac Jones (QB, SF)
- Michael Trigg (TE, DAL)
- Mike Evans (WR, SF)
- Minnesota Vikings (DEF, MIN)
- Najee Harris (RB, FA)
- Roman Wilson (WR, PIT)
- Samaje Perine (RB, CIN)

<!-- END_AUTO_GENERATED -->
