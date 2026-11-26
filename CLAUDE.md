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
Last synced: 2026-11-26 12:46 PM UTC (auto sync)

## Ownership Index
```
<!--
  Full set of all owned player IDs across all 12 rosters.
  Fantasy Scout uses this for verified free agent checks.
  Format: one ID per line inside a code block for easy parsing.
-->
96
421
1166
1373
1466
1479
1945
2020
2133
2216
2449
2505
2617
2747
3155
3160
3163
3198
3214
3257
3271
3286
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
4066
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
4972
4983
4984
4993
5001
5012
5017
5022
5041
5045
5119
5332
5844
5846
5848
5849
5850
5854
5859
5870
5872
5892
5908
5927
5947
5967
5995
6039
6083
6141
6183
6217
6650
6770
6783
6786
6788
6790
6794
6797
6801
6803
6804
6806
6813
6815
6819
6865
6901
6904
6911
6949
7002
7016
7021
7042
7049
7090
7523
7525
7526
7527
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
8121
8122
8126
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
8148
8150
8151
8154
8155
8161
8167
8172
8183
8188
8205
8207
8210
8228
8266
8267
8311
8323
8329
8330
8339
8392
8395
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
10218
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
10927
10949
11034
11199
11237
11292
11427
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
11579
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
11624
11625
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
11682
11685
11687
11705
11710
11727
11729
11739
11783
11786
11792
11834
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
12494
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
12533
12534
12535
12536
12540
12541
12543
12544
12545
12547
12578
12591
12605
12617
12634
12646
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
13335
13337
13338
13345
13346
13347
13348
13349
13350
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
13425
13453
13533
13602
13726
13833
BAL
BUF
CHI
CIN
CLE
DAL
DEN
DET
GB
HOU
JAX
KC
LAR
LV
MIN
NE
NYG
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
| QB | Jayden Daniels | QB | WAS | 25 |
| RB | Saquon Barkley | RB | PHI | 29 |
| RB | Rico Dowdle | RB | PIT | 28 |
| WR | Ladd McConkey | WR | LAC | 25 |
| WR | Tre' Harris | WR | LAC | 24 |
| TE | Kyle Pitts Sr. | TE | ATL | 26 |
| FLEX | David Montgomery | RB | HOU | 29 |
| FLEX | Alvin Kamara | RB | NO | 31 |
| FLEX | Mark Andrews | TE | BAL | 31 |
| K | Will Reichard | K | MIN | 25 |
| DEF | Detroit Lions | DEF | DET | ? |
| LB | Quay Walker | LB | LV | 26 |
| LB | Will Anderson Jr. | DL | HOU | 25 |
| DB | Kyle Hamilton | DB | BAL | 25 |
| DB | Xavier McKinney | DB | GB | 28 |

### Bench

- Christian Izien (DB, DET, Age 26, 3 yr exp)
- Darren Waller (TE, CAR, Age 34, 11 yr exp)
- Derwin James Jr. (DB, LAC, Age 30, 8 yr exp)
- Edgerrin Cooper (LB, GB, Age 25, 2 yr exp)
- Elijah Arroyo (TE, SEA, Age 23, 1 yr exp)
- Jaylin Noel (WR, HOU, Age 24, 1 yr exp)
- Jordan Addison (WR, MIN, Age 24, 3 yr exp)
- Kendrick Bourne (WR, ARI, Age 31, 9 yr exp)
- Kyle McCord (QB, MIA, Age 24, 1 yr exp)
- LeQuint Allen Jr. (RB, JAX, Age 22, 1 yr exp)
- Malik Davis (RB, DAL, Age 28, 4 yr exp)
- Marvin Harrison Jr. (WR, HOU, Age 24, 2 yr exp)
- Matthew Stafford (QB, LAR, Age 38, 17 yr exp)
- Tahj Brooks (RB, CIN, Age 24, 1 yr exp)
- Terry McLaurin (WR, WAS, Age 31, 7 yr exp)
- Tyler Bass (K, BUF, Age 29, 6 yr exp)
- Zack Baun (LB, PHI, Age 29, 6 yr exp)

### Taxi Squad

- Cyrus Allen (WR, KC, Age 23) 🟡 ROOKIE
- Jack Strand (QB, ATL, Age 22) 🟡 ROOKIE

## All Opponent Rosters

### SmokeYall (Roster 1)

**Starters:**
- Joe Burrow (QB, CIN)
- Jahmyr Gibbs (RB, DET)
- Ollie Gordon II (RB, MIA)
- DJ Moore (WR, BUF)
- DeVonta Smith (WR, PHI)
- George Kittle (TE, SF)
- Ted Hurst III (WR, TB)
- Bucky Irving (RB, TB)
- Tutu Atwell (WR, LAR)
- Cairo Santos (K, CHI)
- New York Jets (DEF, NYJ)
- Nakobe Dean (LB, LV)
- Devin Lloyd (LB, CAR)
- Calen Bullock (DB, HOU)
- Dillon Thieneman (DB, CHI)

**QB Room (3 QBs):**
- Joe Burrow (CIN)
- Jordan Love (GB)
- Shedeur Sanders (CLE)

**Positional Surplus (3+ players at same position):**
- QB (3): Joe Burrow, Jordan Love, Shedeur Sanders
- RB (7): Bucky Irving, Emari Demercado, J'Mari Taylor, Jahmyr Gibbs, Jaydon Blue, Ollie Gordon II, TreVeyon Henderson
- TE (3): AJ Barner, George Kittle, Jake Tonges
- WR (16): Barion Brown, Chris Brazzell II, DJ Moore, DeVonta Smith, Isaac TeSlaa, Jalen Brooks, Jayden Reed, Malik Benson, Michael Wilson, Puka Nacua, Savion Williams, Skyler Bell, Ted Hurst III, Tory Horton, Tutu Atwell, Zavion Thomas

**Bench depth:**
- AJ Barner (TE, SEA)
- Barion Brown (WR, NO)
- Chris Brazzell II (WR, CAR)
- Emari Demercado (RB, HOU)
- Isaac TeSlaa (WR, DET)
- J'Mari Taylor (RB, JAX)
- Jake Tonges (TE, SF)
- Jalen Brooks (WR, ARI)
- Jayden Reed (WR, GB)
- Jaydon Blue (RB, PHI)
- Jordan Love (QB, GB)
- Los Angeles Rams (DEF, LAR)
- Malik Benson (WR, LV)
- Michael Wilson (WR, ARI)
- Puka Nacua (WR, LAR)
- Savion Williams (WR, GB)
- Shedeur Sanders (QB, CLE)
- Skyler Bell (WR, BUF)
- Tory Horton (WR, SEA)
- TreVeyon Henderson (RB, NE)
- Zavion Thomas (WR, CHI)

### JQuinna10 (Roster 2)

**Starters:**
- Trevor Lawrence (QB, JAX)
- Emmett Johnson (RB, KC)
- Blake Corum (RB, LAR)
- Justin Jefferson (WR, MIN)
- Luther Burden III (WR, CHI)
- T.J. Hockenson (TE, MIN)
- Rhamondre Stevenson (RB, NE)
- Mike Evans (WR, SF)
- Tetairoa McMillan (WR, CAR)
- Cam Little (K, JAX)
- Washington Commanders (DEF, WAS)
- Blake Cashman (LB, MIN)
- Carson Schwesinger (LB, CLE)
- Travis Hunter (DB, JAX)
- Amani Hooker (DB, BUF)

**QB Room (4 QBs):**
- Baker Mayfield (TB)
- Drake Maye (NE)
- Tommy DeVito (NE)
- Trevor Lawrence (JAX)

**Positional Surplus (3+ players at same position):**
- DEF (4): Houston Texans, New England Patriots, New York Giants, Washington Commanders
- QB (4): Baker Mayfield, Drake Maye, Tommy DeVito, Trevor Lawrence
- RB (11): Blake Corum, Corey Kiner, Emmett Johnson, Jeremiyah Love, Kenneth Walker III, Nicholas Singleton, Rhamondre Stevenson, Tank Bigsby, Travis Etienne Jr., Tyler Allgeier, Zach Charbonnet
- TE (4): Dallas Goedert, Eli Raridon, Eli Stowers, T.J. Hockenson
- WR (8): Denzel Boston, Justin Jefferson, Kyle Williams, Luther Burden III, Mike Evans, Pat Bryant, Romeo Doubs, Tetairoa McMillan

**Bench depth:**
- Baker Mayfield (QB, TB)
- Corey Kiner (RB, NE)
- Dallas Goedert (TE, PHI)
- Denzel Boston (WR, CLE)
- Drake Maye (QB, NE)
- Eli Raridon (TE, NE)
- Eli Stowers (TE, PHI)
- Houston Texans (DEF, HOU)
- Jeremiyah Love (RB, ARI)
- Kenneth Walker III (RB, KC)
- Kyle Williams (WR, NE)
- New England Patriots (DEF, NE)
- New York Giants (DEF, NYG)
- Nicholas Singleton (RB, TEN)
- Pat Bryant (WR, DEN)
- Romeo Doubs (WR, NE)
- Tank Bigsby (RB, PHI)
- Tommy DeVito (QB, NE)
- Travis Etienne Jr. (RB, NO)
- Tyler Allgeier (RB, ARI)
- Zach Charbonnet (RB, SEA)

### WOODYWOOD1978 (Roster 3)

**Starters:**
- Jared Goff (QB, DET)
- Bhayshul Tuten (RB, JAX)
- James Cook III (RB, BUF)
- Matthew Golden (WR, GB)
- Carnell Tate (WR, TEN)
- Brock Bowers (TE, LV)
- Rome Odunze (WR, CHI)
- Travis Kelce (TE, KC)
- Antonio Williams (WR, WAS)
- Dominic Zvada (K, NYG)
- Las Vegas Raiders (DEF, LV)
- Sonny Styles (LB, WAS)
- Andrew Van Ginkel (LB, MIN)
- Jaquan Brisker (DB, PIT)
- Cole Bishop (DB, BUF)

**QB Room (3 QBs):**
- Jared Goff (DET)
- Jaxson Dart (NYG)
- Michael Penix Jr. (ATL)

**Positional Surplus (3+ players at same position):**
- QB (3): Jared Goff, Jaxson Dart, Michael Penix Jr.
- RB (8): Bhayshul Tuten, Dare Ogunbowale, Jacob Saylors, Jadarian Price, James Cook III, Kyle Monangai, Tyjae Spears, Woody Marks
- TE (3): Brock Bowers, Evan Engram, Travis Kelce
- WR (15): Antonio Williams, Brian Thomas Jr., Camden Brown, Carnell Tate, Darius Cooper, Devaughn Vele, Dohnte Meyers, Isaiah Williams, Ja'Kobi Lane, Kayshon Boutte, Matthew Golden, Quentin Johnston, Ricky Pearsall, Rome Odunze, Treylon Burks

**Bench depth:**
- Brian Thomas Jr. (WR, JAX)
- Camden Brown (WR, DAL)
- Dare Ogunbowale (RB, HOU)
- Darius Cooper (WR, PHI)
- Devaughn Vele (WR, NO)
- Dohnte Meyers (WR, CIN)
- Evan Engram (TE, DEN)
- Isaiah Williams (WR, NYJ)
- Ja'Kobi Lane (WR, BAL)
- Jacob Saylors (RB, DET)
- Jadarian Price (RB, SEA)
- Jaxson Dart (QB, NYG)
- Kayshon Boutte (WR, HOU)
- Kyle Monangai (RB, CHI)
- Michael Penix Jr. (QB, ATL)
- Quentin Johnston (WR, LAC)
- Ricky Pearsall (WR, SF)
- Treylon Burks (WR, WAS)
- Tyjae Spears (RB, TEN)
- Woody Marks (RB, HOU)

### Bombas (Roster 4)

**Starters:**
- Fernando Mendoza (QB, LV)
- Kaleb Johnson (RB, GB)
- Braelon Allen (RB, NYJ)
- Adonai Mitchell (WR, NYJ)
- KC Concepcion Jr. (WR, CLE)
- Kenyon Sadiq (TE, NYJ)
- Germie Bernard (WR, PIT)
- Omar Cooper Jr. (WR, NYJ)
- Jack Bech (WR, LV)
- Chris Boswell (K, PIT)
- Dallas Cowboys (DEF, DAL)
- Alex Singleton (LB, DEN)
- Jordyn Brooks (LB, MIA)
- Jordan Battle (DB, CIN)
- Nick Cross (DB, WAS)

**QB Room (3 QBs):**
- Carson Beck (ARI)
- Fernando Mendoza (LV)
- Malik Willis (MIA)

**Positional Surplus (3+ players at same position):**
- QB (3): Carson Beck, Fernando Mendoza, Malik Willis
- RB (7): Braelon Allen, Demond Claiborne, J.K. Dobbins, Kaleb Johnson, Kaytron Allen, Kendre Miller, RJ Harvey
- TE (4): Darnell Washington, Kenyon Sadiq, Oronde Gadsden, Tyler Higbee
- WR (15): Adonai Mitchell, Brandon Aiyuk, Dontayvion Wicks, Germie Bernard, Jack Bech, Jayden Higgins, Jordan Watkins, Josh Cameron, KC Concepcion Jr., Keon Coleman, Malachi Fields, Omar Cooper Jr., Rashod Bateman, Reggie Virgil, Tre Tucker

**Bench depth:**
- Brandon Aiyuk (WR, WAS)
- Carson Beck (QB, ARI)
- Cleveland Browns (DEF, CLE)
- Darnell Washington (TE, PIT)
- Demond Claiborne (RB, MIN)
- Dontayvion Wicks (WR, PHI)
- J.K. Dobbins (RB, DEN)
- Jayden Higgins (WR, HOU)
- Jordan Watkins (WR, SF)
- Josh Cameron (WR, JAX)
- Kaytron Allen (RB, MIA)
- Kendre Miller (RB, DAL)
- Keon Coleman (WR, BUF)
- Malachi Fields (WR, NYG)
- Malik Willis (QB, MIA)
- Oronde Gadsden (TE, LAC)
- RJ Harvey (RB, DEN)
- Rashod Bateman (WR, BAL)
- Reggie Virgil (WR, ARI)
- Tre Tucker (WR, LV)
- Tyler Higbee (TE, LAR)

### Larz1111 (Roster 5)

**Starters:**
- Dak Prescott (QB, DAL)
- Chuba Hubbard (RB, CAR)
- Javonte Williams (RB, DAL)
- Parker Washington (WR, JAX)
- Rashee Rice (WR, KC)
- Chig Okonkwo (TE, WAS)
- Jonah Coleman (RB, DEN)
- Jalen Coker (WR, CAR)
- Omarion Hampton (RB, LAC)
- Jake Bates (K, DET)
- Kansas City Chiefs (DEF, KC)
- Drue Tranquill (LB, KC)
- Terrel Bernard (LB, BUF)
- Tykee Smith (DB, TB)
- Joshua Metellus (DB, MIN)

**QB Room (8 QBs):**
- Anthony Richardson Sr. (IND)
- Dak Prescott (DAL)
- Drew Lock (SEA)
- Jacoby Brissett (BAL)
- Jalon Daniels (TB)
- Lamar Jackson (BAL)
- Taylen Green (CLE)
- Ty Simpson (LAR)

**Positional Surplus (3+ players at same position):**
- QB (8): Anthony Richardson Sr., Dak Prescott, Drew Lock, Jacoby Brissett, Jalon Daniels, Lamar Jackson, Taylen Green, Ty Simpson
- RB (9): Brian Robinson Jr., Chuba Hubbard, Derrick Henry, Javonte Williams, Jonah Coleman, Jonathon Brooks, Kaelon Black, Keaton Mitchell, Omarion Hampton
- TE (5): Cade Otton, Chig Okonkwo, Dalton Schultz, Michael Mayer, Terrance Ferguson
- WR (8): Alec Pierce, Elijah Sarratt, Jalen Coker, Jaxon Smith-Njigba, Makai Lemon, Parker Washington, Rashee Rice, Wan'Dale Robinson

**Bench depth:**
- Alec Pierce (WR, IND)
- Anthony Richardson Sr. (QB, IND)
- Brian Robinson Jr. (RB, ATL)
- Cade Otton (TE, TB)
- Dalton Schultz (TE, HOU)
- Derrick Henry (RB, BAL)
- Drew Lock (QB, SEA)
- Elijah Sarratt (WR, BAL)
- Jacksonville Jaguars (DEF, JAX)
- Jacoby Brissett (QB, BAL)
- Jalon Daniels (QB, TB)
- Jaxon Smith-Njigba (WR, SEA)
- Jonathon Brooks (RB, CAR)
- Kaelon Black (RB, SF)
- Keaton Mitchell (RB, LAC)
- Lamar Jackson (QB, BAL)
- Makai Lemon (WR, PHI)
- Michael Mayer (TE, LV)
- Taylen Green (QB, CLE)
- Terrance Ferguson (TE, LAR)
- Ty Simpson (QB, LAR)
- Wan'Dale Robinson (WR, TEN)

### SnaggyNoDiploma (Roster 6)

**Starters:**
- Josh Allen (QB, BUF)
- Sione Vaki (RB, DET)
- Ty Johnson (RB, BUF)
- Tee Higgins (WR, CIN)
- Stefon Diggs (WR, WAS)
- Trey McBride (TE, ARI)
- Jaylen Waddle (WR, DEN)
- Josh Downs (WR, KC)
- DK Metcalf (WR, PIT)
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
- RB (7): Bijan Robinson, Jacory Croskey-Merritt, Josh Jacobs, Roschon Johnson, Sione Vaki, Ty Johnson, Tyler Goodson
- TE (4): Colby Parkinson, Greg Dulcich, Juwan Johnson, Trey McBride
- WR (11): Chris Godwin Jr., DK Metcalf, Dont'e Thornton Jr., Jaylen Waddle, Josh Downs, Kalif Raymond, Laquon Treadwell, Michael Pittman Jr., Stefon Diggs, Tee Higgins, Tez Johnson

**Bench depth:**
- Bijan Robinson (RB, ATL)
- Chase McLaughlin (K, TB)
- Chris Godwin Jr. (WR, TB)
- Colby Parkinson (TE, LAR)
- Dont'e Thornton Jr. (WR, LV)
- Greg Dulcich (TE, MIA)
- Jacory Croskey-Merritt (RB, WAS)
- Jalen Hurts (QB, PHI)
- Josh Jacobs (RB, GB)
- Juwan Johnson (TE, NO)
- Kalif Raymond (WR, CHI)
- Laquon Treadwell (WR, IND)
- Michael Pittman Jr. (WR, PIT)
- Nick Bolton (LB, KC)
- Roschon Johnson (RB, CHI)
- Stetson Bennett IV (QB, LAR)
- Tez Johnson (WR, TB)
- Tyler Goodson (RB, DAL)

### Darkkaze (Roster 7)

**Starters:**
- Caleb Williams (QB, CHI)
- Chase Brown (RB, CIN)
- Jaylen Warren (RB, PIT)
- George Pickens (WR, DAL)
- Amon-Ra St. Brown (WR, DET)
- Tyler Warren (TE, IND)
- Malik Washington (WR, MIA)
- CeeDee Lamb (WR, DAL)
- Drake London (WR, ATL)
- Ka'imi Fairbairn (K, HOU)
- Cincinnati Bengals (DEF, CIN)
- David Bailey (LB, NYJ)
- Payton Wilson (LB, PIT)
- Evan Williams (DB, GB)
- Quentin Lake (DB, LAR)

**QB Room (4 QBs):**
- Caleb Williams (CHI)
- Drew Allar (PIT)
- Sam Darnold (SEA)
- Tyler Shough (NO)

**Positional Surplus (3+ players at same position):**
- DB (3): Evan Williams, Jessie Bates III, Quentin Lake
- DEF (4): Cincinnati Bengals, Denver Broncos, Green Bay Packers, Pittsburgh Steelers
- QB (4): Caleb Williams, Drew Allar, Sam Darnold, Tyler Shough
- RB (6): Chase Brown, De'Von Achane, Jaylen Warren, Jaylen Wright, Jordan Mason, Kenny Gainwell
- TE (5): Gunnar Helm, Mason Taylor, Matt Hibner, Max Klare, Tyler Warren
- WR (10): Amon-Ra St. Brown, Bryce Lance, CeeDee Lamb, Drake London, George Pickens, Keenan Allen, Khalil Shakir, Konata Mumpfield, Malik Washington, Rashid Shaheed

**Bench depth:**
- Bryce Lance (WR, NO)
- De'Von Achane (RB, MIA)
- Denver Broncos (DEF, DEN)
- Drew Allar (QB, PIT)
- Green Bay Packers (DEF, GB)
- Gunnar Helm (TE, TEN)
- Jaylen Wright (RB, MIA)
- Jessie Bates III (DB, JAX)
- Jordan Mason (RB, MIN)
- Keenan Allen (WR, SF)
- Kenny Gainwell (RB, TB)
- Khalil Shakir (WR, BUF)
- Konata Mumpfield (WR, LAR)
- Mason Taylor (TE, NYJ)
- Matt Hibner (TE, BAL)
- Max Klare (TE, LAR)
- Pittsburgh Steelers (DEF, PIT)
- Rashid Shaheed (WR, SEA)
- Sam Darnold (QB, SEA)
- Tyler Shough (QB, NO)

### DRoj (Roster 8)

**Starters:**
- Patrick Mahomes (QB, KC)
- Breece Hall (RB, NYJ)
- Kyren Williams (RB, LAR)
- Chris Olave (WR, NO)
- Garrett Wilson (WR, NYJ)
- Sam LaPorta (TE, DET)
- Brenton Strange (TE, JAX)
- Quinshon Judkins (RB, CLE)
- Tony Pollard (RB, TEN)
- Matt Gay (K, LV)
- Chicago Bears (DEF, CHI)
- Jamien Sherwood (LB, NYJ)
- Barrett Carter (LB, CIN)
- Brandon Jones (DB, DEN)
- Jeremy Chinn (DB, LV)

**QB Room (6 QBs):**
- Aaron Rodgers (PIT)
- Bo Nix (DEN)
- C.J. Stroud (HOU)
- Daniel Jones (FA)
- Kirk Cousins (MIN)
- Patrick Mahomes (KC)

**Positional Surplus (3+ players at same position):**
- QB (6): Aaron Rodgers, Bo Nix, C.J. Stroud, Daniel Jones, Kirk Cousins, Patrick Mahomes
- RB (8): Aaron Jones Sr., Breece Hall, Isiah Pacheco, Kyren Williams, Mike Washington Jr., Quinshon Judkins, Tony Pollard, Zonovan Knight
- TE (5): Brenton Strange, Harold Fannin Jr., Jake Ferguson, Pat Freiermuth, Sam LaPorta
- WR (8): Chris Olave, Deebo Samuel Sr., Elic Ayomanor, Garrett Wilson, Jerry Jeudy, Tank Dell, Xavier Worthy, Zachariah Branch

**Bench depth:**
- Aaron Jones Sr. (RB, MIN)
- Aaron Rodgers (QB, PIT)
- Bo Nix (QB, DEN)
- C.J. Stroud (QB, HOU)
- Daniel Jones (QB, FA)
- Deebo Samuel Sr. (WR, SF)
- Elic Ayomanor (WR, TEN)
- Harold Fannin Jr. (TE, CLE)
- Isiah Pacheco (RB, DET)
- Jake Ferguson (TE, DAL)
- Jerry Jeudy (WR, CLE)
- Kirk Cousins (QB, MIN)
- Mike Washington Jr. (RB, LV)
- Pat Freiermuth (TE, PIT)
- Tank Dell (WR, HOU)
- Xavier Worthy (WR, KC)
- Zachariah Branch (WR, ATL)
- Zonovan Knight (RB, ARI)

### Jdunn502 (Roster 10)

**Starters:**
- Deshaun Watson (QB, CLE)
- Ashton Jeanty (RB, LV)
- Cam Skattebo (RB, NYG)
- Ja'Marr Chase (WR, CIN)
- Malik Nabers (WR, NYG)
- Tucker Kraft (TE, GB)
- Christian Watson (WR, GB)
- Caleb Douglas (WR, MIA)
- Jordyn Tyson (WR, NO)
- Jason Sanders (K, NYJ)
- Tampa Bay Buccaneers (DEF, TB)
- Josiah Trotter (LB, TB)
- Jacob Rodriguez (LB, MIA)
- Jacob Parrish (DB, TB)
- Dane Belton (DB, NYJ)

**QB Room (8 QBs):**
- Bryce Young (CAR)
- Cade Klubnik (NYJ)
- Cam Ward (TEN)
- Cole Payton (PHI)
- Deshaun Watson (CLE)
- Geno Smith (NYJ)
- Kyler Murray (MIN)
- Mason Rudolph (PIT)

**Positional Surplus (3+ players at same position):**
- DB (3): Dane Belton, Jacob Parrish, Kamari Lassiter
- LB (3): Jacob Rodriguez, Josiah Trotter, T.J. Watt
- QB (8): Bryce Young, Cade Klubnik, Cam Ward, Cole Payton, Deshaun Watson, Geno Smith, Kyler Murray, Mason Rudolph
- RB (8): Ashton Jeanty, Audric Estime, Cam Skattebo, Chris Rodriguez Jr., MarShawn Lloyd, Ray Davis, Seth McGowan, Tyrone Tracy Jr.
- TE (3): Colston Loveland, Oscar Delp, Tucker Kraft
- WR (7): Caleb Douglas, Chris Bell, Christian Watson, Ja'Marr Chase, Jalen McMillan, Jordyn Tyson, Malik Nabers

**Bench depth:**
- Audric Estime (RB, NO)
- Bryce Young (QB, CAR)
- Cade Klubnik (QB, NYJ)
- Cam Ward (QB, TEN)
- Chris Bell (WR, MIA)
- Chris Rodriguez Jr. (RB, JAX)
- Cole Payton (QB, PHI)
- Colston Loveland (TE, CHI)
- Geno Smith (QB, NYJ)
- Jalen McMillan (WR, TB)
- Kamari Lassiter (DB, HOU)
- Kyler Murray (QB, MIN)
- MarShawn Lloyd (RB, GB)
- Mason Rudolph (QB, PIT)
- Oscar Delp (TE, NO)
- Ray Davis (RB, BUF)
- San Francisco 49ers (DEF, SF)
- Seth McGowan (RB, IND)
- Spencer Shrader (K, IND)
- T.J. Watt (LB, PIT)
- Tyrone Tracy Jr. (RB, NYG)

### nicoyepes (Roster 11)

**Starters:**
- Justin Herbert (QB, LAC)
- Jonathan Taylor (RB, IND)
- Christian McCaffrey (RB, SF)
- Jameson Williams (WR, DET)
- DeMario Douglas (WR, NE)
- Mike Gesicki (TE, CIN)
- Ryan Flournoy (WR, DAL)
- Nico Collins (WR, HOU)
- A.J. Brown (WR, NE)
- Jason Myers (K, SEA)
- Buffalo Bills (DEF, BUF)
- Arvell Reese (LB, NYG)
- Roquan Smith (LB, BAL)
- Caleb Downs (DB, DAL)
- Chamarri Conner (DB, KC)

**QB Room (3 QBs):**
- Garrett Nussmeier (KC)
- Joe Fagnano (BAL)
- Justin Herbert (LAC)

**Positional Surplus (3+ players at same position):**
- LB (4): Arvell Reese, Jack Campbell, Micah Parsons, Roquan Smith
- QB (3): Garrett Nussmeier, Joe Fagnano, Justin Herbert
- RB (7): Christian McCaffrey, D'Andre Swift, DJ Giddens, James Conner, Jonathan Taylor, Sean Tucker, Trey Benson
- TE (4): David Njoku, Hunter Henry, Mike Gesicki, Nate Boerkircher
- WR (13): A.J. Brown, Brenen Thompson, CJ Daniels, Courtland Sutton, Davante Adams, DeMario Douglas, Demarcus Robinson, Jameson Williams, Kevin Coleman Jr., Marquise Brown, Nico Collins, Ryan Flournoy, Tyquan Thornton

**Bench depth:**
- Baltimore Ravens (DEF, BAL)
- Brenen Thompson (WR, LAC)
- CJ Daniels (WR, LAR)
- Courtland Sutton (WR, DEN)
- D'Andre Swift (RB, CHI)
- DJ Giddens (RB, IND)
- Davante Adams (WR, LAR)
- David Njoku (TE, LAC)
- Demarcus Robinson (WR, SF)
- Garrett Nussmeier (QB, KC)
- Hunter Henry (TE, NE)
- Jack Campbell (LB, DET)
- James Conner (RB, ARI)
- Joe Fagnano (QB, BAL)
- Kevin Coleman Jr. (WR, MIA)
- Marquise Brown (WR, FA)
- Micah Parsons (LB, GB)
- Nate Boerkircher (TE, JAX)
- Sean Tucker (RB, TB)
- Trey Benson (RB, ARI)
- Tyquan Thornton (WR, KC)

### BedStuyBallers21 (Roster 12)

**Starters:**
- Brock Purdy (QB, SF)
- Rachaad White (RB, WAS)
- Zay Flowers (WR, BAL)
- Jakobi Meyers (WR, JAX)
- Isaiah Likely (TE, NYG)
- Chimere Dike (WR, TEN)
- Emeka Egbuka (WR, TB)
- Brandon Aubrey (K, DAL)
- Philadelphia Eagles (DEF, PHI)
- Demetrius Knight Jr. (LB, CIN)
- Fred Warner (LB, SF)
- Budda Baker (DB, ARI)
- Xavier Watts (DB, ATL)

**QB Room (4 QBs):**
- Brock Purdy (SF)
- J.J. McCarthy (NYG)
- Joe Milton (PHI)
- Mac Jones (SF)

**Positional Surplus (3+ players at same position):**
- QB (4): Brock Purdy, J.J. McCarthy, Joe Milton, Mac Jones
- RB (9): Adam Randall, Austin Ekeler, Dylan Sampson, Eli Heidenreich, Isaiah Davis, Justice Hill, Kimani Vidal, Rachaad White, Samaje Perine
- TE (3): Dalton Kincaid, Isaiah Likely, Michael Trigg
- WR (10): Chimere Dike, Cooper Kupp, Darnell Mooney, De'Zhaun Stribling, Emeka Egbuka, Jakobi Meyers, Jauan Jennings, Roman Wilson, Xavier Hutchinson, Zay Flowers

**Bench depth:**
- Adam Randall (RB, BAL)
- Austin Ekeler (RB, WAS)
- Cooper Kupp (WR, SEA)
- Dalton Kincaid (TE, BUF)
- Darnell Mooney (WR, NYG)
- De'Zhaun Stribling (WR, SF)
- Dylan Sampson (RB, CLE)
- Eli Heidenreich (RB, PIT)
- Isaiah Davis (RB, NYJ)
- J.J. McCarthy (QB, NYG)
- Jauan Jennings (WR, MIN)
- Joe Milton (QB, PHI)
- Justice Hill (RB, BAL)
- Kimani Vidal (RB, LAC)
- Mac Jones (QB, SF)
- Michael Trigg (TE, DAL)
- Minnesota Vikings (DEF, MIN)
- Roman Wilson (WR, PIT)
- Samaje Perine (RB, CIN)
- Xavier Hutchinson (WR, HOU)

<!-- END_AUTO_GENERATED -->
