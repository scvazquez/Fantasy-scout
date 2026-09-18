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
Last synced: 2026-09-18 12:48 PM UTC (auto sync)

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
2020
2078
2133
2216
2449
2505
2617
2747
3163
3198
3214
3257
3294
3321
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
4177
4199
4217
4227
4866
4881
4892
4943
4960
4971
4981
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
5346
5726
5840
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
5947
5967
5995
6083
6130
6650
6711
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
6904
6949
7002
7021
7049
7069
7090
7523
7525
7526
7527
7528
7543
7547
7553
7564
7567
7569
7571
7588
7591
7594
7600
7611
7640
7648
7659
7672
7715
7811
7839
7841
8110
8111
8112
8119
8121
8126
8127
8130
8131
8132
8134
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
8162
8167
8180
8183
8188
8205
8210
8228
8259
8266
8267
8323
8329
8330
8339
8392
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
10859
10880
10892
10914
10947
10949
11034
11199
11237
11370
11533
11539
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
11597
11603
11604
11608
11610
11618
11620
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
11685
11687
11705
11742
11783
11786
11792
11834
12048
12457
12469
12471
12472
12474
12481
12482
12483
12484
12486
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
12515
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
12543
12544
12545
12547
12566
12567
12578
12591
12597
12617
12711
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
13298
13299
13301
13302
13303
13305
13306
13307
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
13365
13371
13375
13376
13377
13379
13380
13389
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
13541
13545
13602
13726
BAL
CAR
CIN
DAL
DEN
DET
GB
HOU
JAX
KC
LAR
MIN
NE
PHI
PIT
SEA
SF
TB
```

## My Roster — Scvazquez (Roster 9)

### Starting Lineup

| Slot | Player | Pos | Team | Age |
|------|--------|-----|------|-----|
| QB | Jayden Daniels | QB | WAS | 25 |
| RB | Saquon Barkley | RB | PHI | 29 |
| RB | David Montgomery | RB | HOU | 29 |
| WR | Justin Jefferson | WR | MIN | 27 |
| WR | Ladd McConkey | WR | LAC | 24 |
| TE | Mark Andrews | TE | BAL | 31 |
| FLEX | Terry McLaurin | WR | WAS | 31 |
| FLEX | CeeDee Lamb | WR | DAL | 27 |
| FLEX | Rico Dowdle | RB | PIT | 28 |
| K | Will Reichard | K | MIN | 25 |
| DEF | Detroit Lions | DEF | DET | ? |
| LB | Zack Baun | LB | PHI | 29 |
| LB | Edgerrin Cooper | LB | GB | 24 |
| DB | Derwin James | DB | LAC | 30 |
| DB | Kyle Hamilton | DB | BAL | 25 |

### Bench

- Donovan Edwards (RB, FA, Age 23, 1 yr exp)
- Xavier McKinney (DB, GB, Age 28, 6 yr exp)
- Jordan Addison (WR, MIN, Age 24, 3 yr exp)
- Darren Waller (TE, CAR, Age 34, 11 yr exp)
- Alvin Kamara (RB, NO, Age 31, 9 yr exp)
- Malik Davis (RB, DAL, Age 27, 4 yr exp)
- LeQuint Allen (RB, JAX, Age 22, 1 yr exp)
- Elijah Arroyo (TE, SEA, Age 23, 1 yr exp)
- Jaylin Noel (WR, HOU, Age 24, 1 yr exp)
- Will Anderson (DL, HOU, Age 25, 3 yr exp)
- Justin Fields (QB, KC, Age 27, 5 yr exp)
- Quay Walker (LB, LV, Age 26, 4 yr exp)
- Tahj Brooks (RB, CIN, Age 24, 1 yr exp)
- Tre' Harris (WR, LAC, Age 24, 1 yr exp)
- Matthew Stafford (QB, LAR, Age 38, 17 yr exp)
- Kyle Pitts (TE, ATL, Age 25, 5 yr exp)

### Taxi Squad

- Cyrus Allen (WR, KC, Age 23) 🟡 ROOKIE
- Jack Strand (QB, ATL, Age 22) 🟡 ROOKIE

## All Opponent Rosters

### SmokeYall (Roster 1)

**Starters:**
- Joe Burrow (QB, CIN)
- Jahmyr Gibbs (RB, DET)
- Bucky Irving (RB, TB)
- Puka Nacua (WR, LAR)
- DeVonta Smith (WR, PHI)
- George Kittle (TE, SF)
- TreVeyon Henderson (RB, NE)
- DJ Moore (WR, BUF)
- Michael Wilson (WR, ARI)
- Jake Bates (K, DET)
- Los Angeles Rams (DEF, LAR)
- Nakobe Dean (LB, LV)
- Devin Lloyd (LB, CAR)
- Alohi Gilman (DB, KC)
- Jessie Bates (DB, ATL)

**QB Room (3 QBs):**
- Joe Burrow (CIN)
- Jordan Love (GB)
- Shedeur Sanders (CLE)

**Positional Surplus (3+ players at same position):**
- QB (3): Joe Burrow, Jordan Love, Shedeur Sanders
- RB (8): Bucky Irving, Devin Singletary, Emari Demercado, J'Mari Taylor, Jahmyr Gibbs, Jaydon Blue, Ollie Gordon, TreVeyon Henderson
- TE (3): AJ Barner, George Kittle, Jake Tonges
- WR (16): Barion Brown, Chris Brazzell, DJ Moore, DeVonta Smith, Isaac TeSlaa, Jalen Brooks, Jayden Reed, Malik Benson, Michael Wilson, Puka Nacua, Savion Williams, Skyler Bell, Ted Hurst, Tory Horton, Tyreek Hill, Zavion Thomas

**Bench depth:**
- AJ Barner (TE, SEA)
- Barion Brown (WR, NO)
- Chris Brazzell (WR, CAR)
- Devin Singletary (RB, NYG)
- Emari Demercado (RB, DAL)
- Isaac TeSlaa (WR, DET)
- J'Mari Taylor (RB, JAX) [TAXI]
- Jake Tonges (TE, SF)
- Jalen Brooks (WR, ARI)
- Jayden Reed (WR, GB)
- Jaydon Blue (RB, PHI)
- Jordan Love (QB, GB)
- Malik Benson (WR, LV) [TAXI]
- Ollie Gordon (RB, MIA)
- Savion Williams (WR, GB)
- Shedeur Sanders (QB, CLE)
- Skyler Bell (WR, BUF)
- Ted Hurst (WR, TB) [TAXI]
- Tory Horton (WR, SEA)
- Tyreek Hill (WR, FA)
- Zavion Thomas (WR, CHI)

### JQuinna10 (Roster 2)

**Starters:**
- Drake Maye (QB, NE)
- Kenneth Walker (RB, KC)
- Rhamondre Stevenson (RB, NE)
- Tetairoa McMillan (WR, CAR)
- Luther Burden (WR, CHI)
- Dallas Goedert (TE, PHI)
- Marvin Harrison (WR, ARI)
- Jeremiyah Love (RB, ARI)
- Romeo Doubs (WR, NE)
- Cam Little (K, JAX)
- New England Patriots (DEF, NE)
- Carson Schwesinger (LB, CLE)
- Jihaad Campbell (LB, PHI)
- Travis Hunter (DB, JAX)
- Nick Emmanwori (DB, SEA)

**QB Room (3 QBs):**
- Carson Beck (ARI)
- Drake Maye (NE)
- Jacoby Brissett (ARI)

**Positional Surplus (3+ players at same position):**
- DEF (3): Cincinnati Bengals, Houston Texans, New England Patriots
- QB (3): Carson Beck, Drake Maye, Jacoby Brissett
- RB (11): Blake Corum, Chris Brooks, Corey Kiner, Emmett Johnson, Jeremiyah Love, Kenneth Walker, Nicholas Singleton, Raheim Sanders, Rhamondre Stevenson, Tyler Allgeier, Zach Charbonnet
- TE (4): Dallas Goedert, Eli Raridon, Eli Stowers, T.J. Hockenson
- WR (10): Denzel Boston, Dontayvion Wicks, Jayden Higgins, Kyle Williams, Luther Burden, Marvin Harrison, Pat Bryant, Romeo Doubs, Tetairoa McMillan, Xavier Hutchinson

**Bench depth:**
- Blake Corum (RB, LAR)
- Carson Beck (QB, ARI) [TAXI]
- Chris Brooks (RB, GB)
- Cincinnati Bengals (DEF, CIN)
- Corey Kiner (RB, NE)
- Denzel Boston (WR, CLE)
- Dontayvion Wicks (WR, PHI)
- Eli Raridon (TE, NE) [TAXI]
- Eli Stowers (TE, PHI) [TAXI]
- Emmett Johnson (RB, KC)
- Houston Texans (DEF, HOU)
- Jacoby Brissett (QB, ARI)
- Jayden Higgins (WR, HOU)
- Kyle Williams (WR, NE)
- Nicholas Singleton (RB, TEN)
- Pat Bryant (WR, DEN)
- Raheim Sanders (RB, CLE)
- T.J. Hockenson (TE, MIN)
- Tyler Allgeier (RB, ARI)
- Xavier Hutchinson (WR, HOU)
- Zach Charbonnet (RB, SEA)

### WOODYWOOD1978 (Roster 3)

**Starters:**
- Jared Goff (QB, DET)
- James Cook (RB, BUF)
- Bhayshul Tuten (RB, JAX)
- Devaughn Vele (WR, NO)
- Rome Odunze (WR, CHI)
- Travis Kelce (TE, KC)
- Quentin Johnston (WR, LAC)
- Brock Bowers (TE, LV)
- Matthew Golden (WR, GB)
- Tyler Loop (K, BAL)
- Green Bay Packers (DEF, GB)
- Zaire Franklin (LB, GB)
- Sonny Styles (LB, WAS)
- Nick Cross (DB, WAS)
- Dillon Thieneman (DB, CHI)

**QB Room (3 QBs):**
- Dillon Gabriel (CLE)
- Jared Goff (DET)
- Jaxson Dart (NYG)

**Positional Surplus (3+ players at same position):**
- LB (3): Jordyn Brooks, Sonny Styles, Zaire Franklin
- QB (3): Dillon Gabriel, Jared Goff, Jaxson Dart
- RB (6): Bhayshul Tuten, Jacob Saylors, James Cook, Kyle Monangai, Tyjae Spears, Woody Marks
- TE (3): Brock Bowers, Charlie Kolar, Travis Kelce
- WR (15): Antonio Williams, Brian Thomas, Camden Brown, Carnell Tate, Darius Cooper, Devaughn Vele, Dohnte Meyers, Isaiah Williams, Ja'Kobi Lane, Kayshon Boutte, Lewis Bond, Matthew Golden, Quentin Johnston, Ricky Pearsall, Rome Odunze

**Bench depth:**
- Antonio Williams (WR, WAS)
- Brian Thomas (WR, JAX)
- Camden Brown (WR, DAL) [TAXI]
- Carnell Tate (WR, TEN)
- Charlie Kolar (TE, LAC)
- Darius Cooper (WR, PHI)
- Dillon Gabriel (QB, CLE)
- Dohnte Meyers (WR, CIN)
- Isaiah Williams (WR, NYJ)
- Ja'Kobi Lane (WR, BAL) [TAXI]
- Jacob Saylors (RB, DET)
- Jaxson Dart (QB, NYG)
- Jordyn Brooks (LB, MIA)
- Kayshon Boutte (WR, HOU)
- Kyle Monangai (RB, CHI)
- Lewis Bond (WR, HOU)
- Ricky Pearsall (WR, SF)
- Tyjae Spears (RB, TEN)
- Woody Marks (RB, HOU)

### Bombas (Roster 4)

**Starters:**
- Trevor Lawrence (QB, JAX)
- RJ Harvey (RB, DEN)
- Demond Claiborne (RB, MIN)
- KC Concepcion (WR, CLE)
- Adonai Mitchell (WR, NYJ)
- Kenyon Sadiq (TE, NYJ)
- Jack Bech (WR, LV)
- Tre Tucker (WR, LV)
- Omar Cooper (WR, NYJ)
- Cairo Santos (K, CHI)
- Dallas Cowboys (DEF, DAL)
- Ventrell Miller (LB, JAX)
- Daiyan Henley (LB, LAC)
- Jalen Thompson (DB, DAL)
- Julian Love (DB, SEA)

**QB Room (4 QBs):**
- Fernando Mendoza (LV)
- Malik Willis (MIA)
- Michael Penix (ATL)
- Trevor Lawrence (JAX)

**Positional Surplus (3+ players at same position):**
- QB (4): Fernando Mendoza, Malik Willis, Michael Penix, Trevor Lawrence
- RB (10): Braelon Allen, Demond Claiborne, Dylan Sampson, Jadarian Price, Kaleb Johnson, Kaytron Allen, Kendre Miller, RJ Harvey, Roschon Johnson, Tank Bigsby
- TE (3): Darnell Washington, Kenyon Sadiq, Oronde Gadsden
- WR (12): Adonai Mitchell, Calvin Ridley, Germie Bernard, Jack Bech, Josh Cameron, KC Concepcion, Keon Coleman, Malachi Fields, Omar Cooper, Rashod Bateman, Tre Tucker, Troy Franklin

**Bench depth:**
- Braelon Allen (RB, NYJ)
- Calvin Ridley (WR, TEN)
- Darnell Washington (TE, PIT)
- Dylan Sampson (RB, CLE)
- Fernando Mendoza (QB, LV)
- Germie Bernard (WR, PIT) [TAXI]
- Jadarian Price (RB, SEA)
- Josh Cameron (WR, JAX) [TAXI]
- Kaleb Johnson (RB, GB)
- Kaytron Allen (RB, WAS)
- Kendre Miller (RB, NO)
- Keon Coleman (WR, BUF)
- Malachi Fields (WR, NYG) [TAXI]
- Malik Willis (QB, MIA)
- Michael Penix (QB, ATL)
- Oronde Gadsden (TE, LAC)
- Rashod Bateman (WR, BAL)
- Roschon Johnson (RB, CHI)
- Tank Bigsby (RB, PHI)
- Troy Franklin (WR, DEN)

### Larz1111 (Roster 5)

**Starters:**
- Lamar Jackson (QB, BAL)
- Omarion Hampton (RB, LAC)
- Javonte Williams (RB, DAL)
- Jaxon Smith-Njigba (WR, SEA)
- Rashee Rice (WR, KC)
- Michael Mayer (TE, LV)
- Chuba Hubbard (RB, CAR)
- Jalen Coker (WR, CAR)
- Parker Washington (WR, JAX)
- Cameron Dicker (K, LAC)
- Jacksonville Jaguars (DEF, JAX)
- Jamien Sherwood (LB, NYJ)
- Alex Singleton (LB, DEN)
- Tykee Smith (DB, TB)
- Cooper DeJean (DB, PHI)

**QB Room (6 QBs):**
- Anthony Richardson (IND)
- Dak Prescott (DAL)
- Lamar Jackson (BAL)
- Sam Howell (DAL)
- Taylen Green (CLE)
- Ty Simpson (LAR)

**Positional Surplus (3+ players at same position):**
- QB (6): Anthony Richardson, Dak Prescott, Lamar Jackson, Sam Howell, Taylen Green, Ty Simpson
- RB (8): Brian Robinson, Chuba Hubbard, Javonte Williams, Jonah Coleman, Jonathon Brooks, Kaelon Black, Keaton Mitchell, Omarion Hampton
- TE (5): Cade Otton, Chig Okonkwo, Dalton Schultz, Michael Mayer, Terrance Ferguson
- WR (9): Alec Pierce, Elijah Sarratt, Jahan Dotson, Jalen Coker, Jaxon Smith-Njigba, Makai Lemon, Parker Washington, Rashee Rice, Wan'Dale Robinson

**Bench depth:**
- Alec Pierce (WR, IND)
- Anthony Richardson (QB, IND)
- Brian Robinson (RB, ATL)
- Cade Otton (TE, TB)
- Chig Okonkwo (TE, WAS)
- Dak Prescott (QB, DAL)
- Dalton Schultz (TE, HOU)
- Elijah Sarratt (WR, BAL) [TAXI]
- Jahan Dotson (WR, ATL)
- Jonah Coleman (RB, DEN)
- Jonathon Brooks (RB, CAR)
- Kaelon Black (RB, SF)
- Keaton Mitchell (RB, LAC)
- Makai Lemon (WR, PHI)
- Sam Howell (QB, DAL)
- Taylen Green (QB, CLE) [TAXI]
- Terrance Ferguson (TE, LAR)
- Ty Simpson (QB, LAR) [TAXI]
- Wan'Dale Robinson (WR, TEN)

### DopeOne83 (Roster 6)

**Starters:**
- Josh Allen (QB, BUF)
- Bijan Robinson (RB, ATL)
- Jacory Croskey-Merritt (RB, WAS)
- Tee Higgins (WR, CIN)
- Jaylen Waddle (WR, DEN)
- Trey McBride (TE, ARI)
- Michael Pittman (WR, PIT)
- DK Metcalf (WR, PIT)
- Stefon Diggs (WR, WAS)
- Evan McPherson (K, CIN)
- Seattle Seahawks (DEF, SEA)
- Foyesade Oluokun (LB, JAX)
- Ernest Jones (LB, SEA)
- Jaquan Brisker (DB, PIT)
- Avieon Terrell (DB, ATL)

**QB Room (2 QBs):**
- Jalen Hurts (PHI)
- Josh Allen (BUF)

**Positional Surplus (3+ players at same position):**
- LB (4): Ernest Jones, Foyesade Oluokun, Nick Bolton, Robert Spillane
- RB (3): Bijan Robinson, Jacory Croskey-Merritt, Josh Jacobs
- WR (8): Chris Godwin, DK Metcalf, Jaylen Waddle, Josh Downs, Kalif Raymond, Michael Pittman, Stefon Diggs, Tee Higgins

**Bench depth:**
- Chase McLaughlin (K, TB)
- Chris Godwin (WR, TB)
- Jalen Hurts (QB, PHI)
- Josh Downs (WR, IND)
- Josh Jacobs (RB, GB)
- Juwan Johnson (TE, NO)
- Kalif Raymond (WR, CHI)
- Nick Bolton (LB, KC)
- Robert Spillane (LB, NE)

### Darkkaze (Roster 7)

**Starters:**
- Caleb Williams (QB, CHI)
- De'Von Achane (RB, MIA)
- Chase Brown (RB, CIN)
- Amon-Ra St. Brown (WR, DET)
- George Pickens (WR, DAL)
- Tyler Warren (TE, IND)
- Drake London (WR, ATL)
- Travis Etienne (RB, NO)
- Jaylen Warren (RB, PIT)
- Ka'imi Fairbairn (K, HOU)
- Tampa Bay Buccaneers (DEF, TB)
- Jacob Rodriguez (LB, MIA)
- Josh Hines-Allen (DE, JAX)
- Quentin Lake (DB, LAR)
- Tre'von Moehrig (DB, CAR)

**QB Room (4 QBs):**
- Caleb Williams (CHI)
- Drew Allar (PIT)
- Sam Darnold (SEA)
- Tyler Shough (NO)

**Positional Surplus (3+ players at same position):**
- DEF (3): Denver Broncos, Pittsburgh Steelers, Tampa Bay Buccaneers
- QB (4): Caleb Williams, Drew Allar, Sam Darnold, Tyler Shough
- RB (8): Chase Brown, De'Von Achane, J.K. Dobbins, Jaylen Warren, Jaylen Wright, Jordan Mason, Kenny Gainwell, Travis Etienne
- TE (5): Gunnar Helm, Marlin Klein, Matt Hibner, Max Klare, Tyler Warren
- WR (9): Amon-Ra St. Brown, Bryce Lance, Drake London, George Pickens, Keenan Allen, Khalil Shakir, Mack Hollins, Malik Washington, Rashid Shaheed

**Bench depth:**
- Bryce Lance (WR, NO)
- Denver Broncos (DEF, DEN)
- Drew Allar (QB, PIT) [TAXI]
- Gunnar Helm (TE, TEN)
- J.K. Dobbins (RB, DEN)
- Jaylen Wright (RB, MIA)
- Jordan Mason (RB, MIN)
- Keenan Allen (WR, IND)
- Kenny Gainwell (RB, TB)
- Khalil Shakir (WR, BUF)
- Mack Hollins (WR, NE)
- Malik Washington (WR, MIA)
- Marlin Klein (TE, HOU)
- Matt Hibner (TE, BAL) [TAXI]
- Max Klare (TE, LAR) [TAXI]
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
- Harold Fannin (TE, CLE)
- Deebo Samuel (WR, SF)
- Quinshon Judkins (RB, CLE)
- Sam LaPorta (TE, DET)
- Matt Gay (K, LV)
- Carolina Panthers (DEF, CAR)
- Devin Bush (LB, CHI)
- Cedric Gray (LB, TEN)
- Malaki Starks (DB, BAL)
- Cam Bynum (DB, IND)

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
- RB (6): Aaron Jones, Breece Hall, Isiah Pacheco, Kyren Williams, Mike Washington, Quinshon Judkins
- TE (6): Brenton Strange, Harold Fannin, Jake Ferguson, Mason Taylor, Pat Freiermuth, Sam LaPorta
- WR (9): Chris Olave, Deebo Samuel, Elic Ayomanor, Garrett Wilson, Jalen Nailor, Jerry Jeudy, Tank Dell, Xavier Worthy, Zachariah Branch

**Bench depth:**
- Aaron Jones (RB, MIN)
- Aaron Rodgers (QB, PIT)
- Bo Nix (QB, DEN)
- Brenton Strange (TE, JAX)
- Bryce Young (QB, CAR)
- C.J. Stroud (QB, HOU)
- Daniel Jones (QB, IND)
- Elic Ayomanor (WR, TEN)
- Harrison Butker (K, KC)
- Isiah Pacheco (RB, DET)
- Jake Ferguson (TE, DAL)
- Jalen Nailor (WR, LV)
- Jerry Jeudy (WR, CLE)
- Kirk Cousins (QB, LV)
- Mason Taylor (TE, NYJ)
- Mike Washington (RB, LV) [TAXI]
- Pat Freiermuth (TE, PIT)
- Tank Dell (WR, HOU)
- Xavier Worthy (WR, KC)
- Zachariah Branch (WR, ATL) [TAXI]

### Jdunn502 (Roster 10)

**Starters:**
- Geno Smith (QB, NYJ)
- Ashton Jeanty (RB, LV)
- Cam Skattebo (RB, NYG)
- Ja'Marr Chase (WR, CIN)
- Malik Nabers (WR, NYG)
- Colston Loveland (TE, CHI)
- Tucker Kraft (TE, GB)
- Christian Watson (WR, GB)
- Caleb Douglas (WR, MIA)
- Trey Smack (K, GB)
- San Francisco 49ers (DEF, SF)
- T.J. Watt (LB, PIT)
- Josiah Trotter (LB, TB)
- Talanoa Hufanga (DB, DEN)
- Kamari Lassiter (DB, HOU)

**QB Room (8 QBs):**
- Cade Klubnik (NYJ)
- Cam Ward (TEN)
- Cole Payton (PHI)
- Deshaun Watson (CLE)
- Geno Smith (NYJ)
- Jalon Daniels (TB)
- Kyler Murray (MIN)
- Will Howard (PIT)

**Positional Surplus (3+ players at same position):**
- LB (3): Anthony Hill, Josiah Trotter, T.J. Watt
- QB (8): Cade Klubnik, Cam Ward, Cole Payton, Deshaun Watson, Geno Smith, Jalon Daniels, Kyler Murray, Will Howard
- RB (8): Ashton Jeanty, Cam Skattebo, Chris Rodriguez, MarShawn Lloyd, Ray Davis, Seth McGowan, Tony Pollard, Tyrone Tracy
- TE (4): Colston Loveland, Oscar Delp, Theo Johnson, Tucker Kraft
- WR (7): Caleb Douglas, Chris Bell, Christian Watson, Ja'Marr Chase, Jalen McMillan, Jordyn Tyson, Malik Nabers

**Bench depth:**
- Anthony Hill (LB, TEN)
- Cade Klubnik (QB, NYJ)
- Cam Ward (QB, TEN)
- Chris Bell (WR, MIA)
- Chris Rodriguez (RB, JAX)
- Cole Payton (QB, PHI) [TAXI]
- Deshaun Watson (QB, CLE)
- Jalen McMillan (WR, TB)
- Jalon Daniels (QB, TB)
- Jordyn Tyson (WR, NO)
- Kansas City Chiefs (DEF, KC)
- Kyler Murray (QB, MIN)
- MarShawn Lloyd (RB, GB)
- Oscar Delp (TE, NO) [TAXI]
- Ray Davis (RB, BUF)
- Seth McGowan (RB, IND) [TAXI]
- Theo Johnson (TE, NYG)
- Tony Pollard (RB, TEN)
- Tyrone Tracy (RB, NYG)
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
- Jameson Williams (WR, DET)
- Jason Myers (K, SEA)
- Baltimore Ravens (DEF, BAL)
- Jack Campbell (LB, DET)
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
- WR (12): A.J. Brown, Brenen Thompson, CJ Daniels, Courtland Sutton, Davante Adams, DeMario Douglas, Deion Burks, Jameson Williams, Kevin Coleman, Nico Collins, Ryan Flournoy, Tyquan Thornton

**Bench depth:**
- A.J. Brown (WR, NE)
- Arvell Reese (LB, NYG)
- Brenen Thompson (WR, LAC) [TAXI]
- CJ Daniels (WR, LAR) [TAXI]
- Courtland Sutton (WR, DEN)
- DJ Giddens (RB, IND)
- David Njoku (TE, LAC)
- Deion Burks (WR, IND)
- Garrett Nussmeier (QB, KC)
- James Conner (RB, ARI)
- John Michael Gyllenborg (TE, KC)
- Kevin Coleman (WR, MIA)
- Micah Parsons (LB, GB)
- Mike Gesicki (TE, CIN)
- Nate Boerkircher (TE, JAX) [TAXI]
- Ryan Flournoy (WR, DAL)
- Sean Tucker (RB, TB)
- Trey Benson (RB, ARI)
- Tua Tagovailoa (QB, ATL)
- Tyquan Thornton (WR, KC)

### BedStuyBallers21 (Roster 12)

**Starters:**
- Brock Purdy (QB, SF)
- Derrick Henry (RB, BAL)
- Rachaad White (RB, WAS)
- Zay Flowers (WR, BAL)
- Emeka Egbuka (WR, TB)
- Isaiah Likely (TE, NYG)
- Mike Evans (WR, SF)
- Dalton Kincaid (TE, BUF)
- Jakobi Meyers (WR, JAX)
- Brandon Aubrey (K, DAL)
- Philadelphia Eagles (DEF, PHI)
- Demetrius Knight (LB, CIN)
- Fred Warner (LB, SF)
- Budda Baker (DB, ARI)
- Xavier Watts (DB, ATL)

**QB Room (4 QBs):**
- Baker Mayfield (TB)
- Brock Purdy (SF)
- J.J. McCarthy (MIN)
- Mac Jones (SF)

**Positional Surplus (3+ players at same position):**
- QB (4): Baker Mayfield, Brock Purdy, J.J. McCarthy, Mac Jones
- RB (10): Adam Randall, Derrick Henry, Eli Heidenreich, George Holani, Isaiah Davis, Justice Hill, Kimani Vidal, Najee Harris, Rachaad White, Samaje Perine
- TE (3): Dalton Kincaid, Isaiah Likely, Michael Trigg
- WR (11): Chimere Dike, Cooper Kupp, Darnell Mooney, De'Zhaun Stribling, Emeka Egbuka, Jakobi Meyers, Jauan Jennings, Mike Evans, Odell Beckham, Roman Wilson, Zay Flowers

**Bench depth:**
- Adam Randall (RB, BAL)
- Baker Mayfield (QB, TB)
- Chimere Dike (WR, TEN)
- Cooper Kupp (WR, SEA)
- Darnell Mooney (WR, NYG)
- De'Zhaun Stribling (WR, SF) [TAXI]
- Eli Heidenreich (RB, PIT) [TAXI]
- George Holani (RB, SEA)
- Isaiah Davis (RB, NYJ)
- J.J. McCarthy (QB, MIN)
- Jauan Jennings (WR, MIN)
- Justice Hill (RB, BAL)
- Kimani Vidal (RB, LAC)
- Mac Jones (QB, SF)
- Michael Trigg (TE, DAL) [TAXI]
- Minnesota Vikings (DEF, MIN)
- Najee Harris (RB, NYG)
- Odell Beckham (WR, NYG)
- Roman Wilson (WR, PIT)
- Samaje Perine (RB, CIN)

<!-- END_AUTO_GENERATED -->
