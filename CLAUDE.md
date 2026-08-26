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
- The scheduled Roster Sync routine is explicitly authorized to
  commit directly to the `main` branch, without opening a PR or
  asking for confirmation first — push-then-review, not
  review-then-push. This applies ONLY to changes strictly inside
  the `<!-- BEGIN_AUTO_GENERATED -->` / `<!-- END_AUTO_GENERATED -->`
  markers in this file. It never covers edits to this MANUAL
  section, to any other file, or to any other automation in this
  repo — those still follow normal branch/PR conventions and still
  require confirmation.
- Authorization history: granted by Scvazquez 2026-08-04; reaffirmed
  live in an interactive chat session on 2026-08-09 (the session
  that produced the 2026-08-09 12:47 PM UTC roster sync commit),
  after the routine held off on a direct-to-main push pending
  exactly this kind of live confirmation. Future re-affirmations
  should be added as new dated lines here, not by editing this
  line in place, so the history stays auditable.

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
Last synced: 2026-08-26 01:10 PM UTC (auto sync)

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
1233
1373
1466
1479
1945
2078
2133
2216
2449
2505
2747
3163
3198
3214
3257
3294
3321
3451
4017
4018
4033
4034
4035
4037
4039
4046
4081
4137
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
5022
5041
5045
5332
5346
5726
5843
5844
5846
5849
5850
5859
5870
5872
5892
5912
5927
5944
5947
5967
5995
6119
6302
6315
6768
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
6807
6813
6815
6819
6865
6904
6949
7002
7016
7021
7049
7090
7136
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
7611
7640
7648
7659
7672
7715
7811
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
8311
8323
8329
8339
8392
8408
8659
8676
8698
8800
8932
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
9494
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
10905
10921
10949
10980
11017
11034
11199
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
11592
11597
11603
11604
11608
11610
11618
11620
11624
11625
11626
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
11742
11783
11786
11792
11834
12048
12455
12457
12467
12469
12471
12474
12476
12481
12482
12483
12484
12487
12489
12490
12492
12493
12495
12497
12498
12499
12501
12502
12504
12505
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
12567
12578
12597
12711
13150
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
13322
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
13368
13371
13375
13376
13377
13380
13389
13399
13400
13401
13402
13403
13404
13405
13408
13411
13413
13414
13417
13418
13420
13421
13423
13424
13434
13477
13533
13541
13602
13662
13726
BAL
CHI
CLE
DEN
DET
GB
HOU
JAX
KC
LAC
LAR
MIN
NE
PHI
PIT
SEA
```

## My Roster — Scvazquez (Roster 9)

### Starting Lineup

| Slot | Player | Pos | Team | Age |
|------|--------|-----|------|-----|
| QB | Jayden Daniels | QB | WAS | 25 |
| RB | Rico Dowdle | RB | PIT | 28 |
| RB | David Montgomery | RB | HOU | 29 |
| WR | Ladd McConkey | WR | LAC | 24 |
| WR | Justin Jefferson | WR | MIN | 27 |
| TE | Kyle Pitts | TE | ATL | 25 |
| FLEX | Saquon Barkley | RB | PHI | 29 |
| FLEX | Terry McLaurin | WR | WAS | 30 |
| FLEX | CeeDee Lamb | WR | DAL | 27 |
| K | Will Reichard | K | MIN | 25 |
| DEF | Detroit Lions | DEF | DET | None |
| LB | Zack Baun | LB | PHI | 29 |
| LB | Quay Walker | LB | LV | 26 |
| DB | Kyle Hamilton | DB | BAL | 25 |
| DB | Derwin James | DB | LAC | 30 |

### Bench

- Xavier McKinney (DB, GB, Age 28, 6 yr exp)
- Will Anderson (DL, HOU, Age 24, 3 yr exp)
- Edgerrin Cooper (LB, GB, Age 24, 2 yr exp)
- Justin Fields (QB, KC, Age 27, 5 yr exp)
- Matthew Stafford (QB, LAR, Age 38, 17 yr exp)
- Alvin Kamara (RB, NO, Age 31, 9 yr exp)
- Donovan Edwards (RB, MIA, Age 23, 1 yr exp)
- LeQuint Allen (RB, JAX, Age 22, 1 yr exp)
- Malik Davis (RB, DAL, Age 27, 4 yr exp)
- Tahj Brooks (RB, CIN, Age 24, 1 yr exp)
- Darren Waller (TE, CAR, Age 33, 11 yr exp)
- Elijah Arroyo (TE, SEA, Age 23, 1 yr exp)
- Mark Andrews (TE, BAL, Age 30, 8 yr exp)
- Jaylin Noel (WR, HOU, Age 23, 1 yr exp)
- Jordan Addison (WR, MIN, Age 24, 3 yr exp)
- Tre' Harris (WR, LAC, Age 24, 1 yr exp)

### Taxi Squad

- Cyrus Allen (WR, KC, Age 23) 🟡 ROOKIE
- Jack Strand (QB, ATL, Age 22) 🟡 ROOKIE

## All Opponent Rosters

### SmokeYall (Roster 1)

**Starters:**
- Joe Burrow (QB, CIN)
- Jahmyr Gibbs (RB, DET)
- TreVeyon Henderson (RB, NE)
- Puka Nacua (WR, LAR)
- DeVonta Smith (WR, PHI)
- Bucky Irving (RB, TB)
- DJ Moore (WR, BUF)
- Michael Wilson (WR, ARI)
- Jake Bates (K, DET)
- Los Angeles Rams (DEF, LAR)
- Nakobe Dean (LB, LV)
- Devin Lloyd (LB, CAR)
- Chamarri Conner (DB, KC)

**QB Room (3 QBs):**
- Joe Burrow (CIN)
- Jordan Love (GB)
- Shedeur Sanders (CLE)

**Positional Surplus (3+ players at same position):**
- QB (3): Joe Burrow, Jordan Love, Shedeur Sanders
- RB (8): Bucky Irving, Emari Demercado, J'Mari Taylor, Jahmyr Gibbs, Jaydon Blue, Ollie Gordon, Robert Henry, TreVeyon Henderson
- TE (3): AJ Barner, George Kittle, Jake Tonges
- WR (16): Barion Brown, Chris Brazzell, DJ Moore, DeVonta Smith, Isaac TeSlaa, Jalen Brooks, Jayden Reed, Malik Benson, Michael Wilson, Puka Nacua, Savion Williams, Skyler Bell, Ted Hurst, Tory Horton, Tyreek Hill, Zavion Thomas

**Bench depth:**
- Jordan Love (QB, GB)
- Shedeur Sanders (QB, CLE)
- Emari Demercado (RB, KC)
- Jaydon Blue (RB, DAL)
- Ollie Gordon (RB, MIA)
- Robert Henry (RB, WAS)
- AJ Barner (TE, SEA)
- George Kittle (TE, SF)
- Jake Tonges (TE, SF)
- Barion Brown (WR, NO)
- Chris Brazzell (WR, CAR)
- Isaac TeSlaa (WR, DET)
- Jalen Brooks (WR, ARI)
- Jayden Reed (WR, GB)
- Savion Williams (WR, GB)
- Skyler Bell (WR, BUF)
- Tory Horton (WR, SEA)
- Tyreek Hill (WR, FA)
- Zavion Thomas (WR, CHI)

**Taxi Squad:**
- Ted Hurst (WR, TB, Age 22) 🟡 ROOKIE
- Malik Benson (WR, LV, Age 23) 🟡 ROOKIE
- J'Mari Taylor (RB, JAX, Age 24) 🟡 ROOKIE

### JQuinna10 (Roster 2)

**Starters:**
- Drake Maye (QB, NE)
- Kenneth Walker (RB, KC)
- Jeremiyah Love (RB, ARI)
- Tetairoa McMillan (WR, CAR)
- Luther Burden (WR, CHI)
- Dallas Goedert (TE, PHI)
- Marvin Harrison (WR, ARI)
- Rhamondre Stevenson (RB, NE)
- Romeo Doubs (WR, NE)
- Cam Little (K, JAX)
- Houston Texans (DEF, HOU)
- Carson Schwesinger (LB, CLE)
- Travis Hunter (WR, JAX)
- Nick Emmanwori (DB, SEA)

**QB Room (3 QBs):**
- Carson Beck (ARI)
- Drake Maye (NE)
- Jacoby Brissett (ARI)

**Positional Surplus (3+ players at same position):**
- QB (3): Carson Beck, Drake Maye, Jacoby Brissett
- RB (10): Blake Corum, Emmett Johnson, Jam Miller, Jeremiyah Love, Kenneth Walker, Nicholas Singleton, Rhamondre Stevenson, Roschon Johnson, Tyler Allgeier, Zach Charbonnet
- TE (4): Dallas Goedert, Eli Raridon, Eli Stowers, T.J. Hockenson
- WR (13): Denzel Boston, Dontayvion Wicks, Jalen Royals, Jayden Higgins, Kyle Williams, Luther Burden, Marvin Harrison, Pat Bryant, Romeo Doubs, Tetairoa McMillan, Travis Hunter, Xavier Hutchinson, Xavier Legette

**Bench depth:**
- New England Patriots (DEF, NE)
- Jacoby Brissett (QB, ARI)
- Blake Corum (RB, LAR)
- Emmett Johnson (RB, KC)
- Jam Miller (RB, NE)
- Nicholas Singleton (RB, TEN)
- Roschon Johnson (RB, CHI)
- Tyler Allgeier (RB, ARI)
- Zach Charbonnet (RB, SEA)
- T.J. Hockenson (TE, MIN)
- Denzel Boston (WR, CLE)
- Dontayvion Wicks (WR, PHI)
- Jalen Royals (WR, KC)
- Jayden Higgins (WR, HOU)
- Kyle Williams (WR, NE)
- Pat Bryant (WR, DEN)
- Xavier Hutchinson (WR, HOU)
- Xavier Legette (WR, CAR)

**Taxi Squad:**
- Carson Beck (QB, ARI, Age 23) 🟡 ROOKIE
- Eli Stowers (TE, PHI, Age 23) 🟡 ROOKIE
- Eli Raridon (TE, NE, Age 22) 🟡 ROOKIE

### WOODYWOOD1978 (Roster 3)

**Starters:**
- Jaxson Dart (QB, NYG)
- James Cook (RB, BUF)
- Bhayshul Tuten (RB, JAX)
- Carnell Tate (WR, TEN)
- Rome Odunze (WR, CHI)
- Brock Bowers (TE, LV)
- Quentin Johnston (WR, LAC)
- Brian Thomas (WR, JAX)
- Travis Kelce (TE, KC)
- Tyler Loop (K, BAL)
- Green Bay Packers (DEF, GB)
- Zaire Franklin (LB, GB)
- Sonny Styles (LB, WAS)
- Nick Cross (DB, WAS)
- Dillon Thieneman (DB, CHI)

**QB Room (2 QBs):**
- Jared Goff (DET)
- Jaxson Dart (NYG)

**Positional Surplus (3+ players at same position):**
- LB (3): Jordyn Brooks, Sonny Styles, Zaire Franklin
- RB (5): Bhayshul Tuten, James Cook, Kyle Monangai, Tyjae Spears, Woody Marks
- TE (3): Brock Bowers, Charlie Kolar, Travis Kelce
- WR (14): Antonio Williams, Brian Thomas, Camden Brown, Carnell Tate, Darius Cooper, Devaughn Vele, Isaiah Williams, Ja'Kobi Lane, Kayshon Boutte, Lewis Bond, Matthew Golden, Quentin Johnston, Ricky Pearsall, Rome Odunze

**Bench depth:**
- Jordyn Brooks (LB, MIA)
- Jared Goff (QB, DET)
- Kyle Monangai (RB, CHI)
- Tyjae Spears (RB, TEN)
- Woody Marks (RB, HOU)
- Charlie Kolar (TE, LAC)
- Antonio Williams (WR, WAS)
- Camden Brown (WR, DAL)
- Darius Cooper (WR, PHI)
- Devaughn Vele (WR, NO)
- Isaiah Williams (WR, NYJ)
- Ja'Kobi Lane (WR, BAL)
- Kayshon Boutte (WR, HOU)
- Lewis Bond (WR, HOU)
- Matthew Golden (WR, GB)
- Ricky Pearsall (WR, SF)

### Bombas (Roster 4)

**Starters:**
- Trevor Lawrence (QB, JAX)
- RJ Harvey (RB, DEN)
- Jadarian Price (RB, SEA)
- KC Concepcion (WR, CLE)
- Omar Cooper (WR, NYJ)
- Kenyon Sadiq (TE, NYJ)
- Dylan Sampson (RB, CLE)
- Tre Tucker (WR, LV)
- Oronde Gadsden (TE, LAC)

**QB Room (4 QBs):**
- Fernando Mendoza (LV)
- Malik Willis (MIA)
- Michael Penix (ATL)
- Trevor Lawrence (JAX)

**Positional Surplus (3+ players at same position):**
- QB (4): Fernando Mendoza, Malik Willis, Michael Penix, Trevor Lawrence
- RB (10): Braelon Allen, Brashard Smith, Demond Claiborne, Dylan Sampson, Jadarian Price, Joe Mixon, Kaleb Johnson, Kaytron Allen, RJ Harvey, Tank Bigsby
- TE (5): Darnell Washington, Kenyon Sadiq, Oronde Gadsden, Sam Roush, Will Kacmarek
- WR (13): Adonai Mitchell, Calvin Ridley, Colbie Young, Germie Bernard, Jack Bech, KC Concepcion, Keon Coleman, Malachi Fields, Marvin Mims, Omar Cooper, Rashod Bateman, Tre Tucker, Troy Franklin

**Bench depth:**
- Fernando Mendoza (QB, LV)
- Malik Willis (QB, MIA)
- Michael Penix (QB, ATL)
- Braelon Allen (RB, NYJ)
- Brashard Smith (RB, KC)
- Joe Mixon (RB, FA)
- Kaleb Johnson (RB, PIT)
- Kaytron Allen (RB, WAS)
- Tank Bigsby (RB, PHI)
- Darnell Washington (TE, PIT)
- Sam Roush (TE, CHI)
- Adonai Mitchell (WR, NYJ)
- Calvin Ridley (WR, TEN)
- Germie Bernard (WR, PIT)
- Jack Bech (WR, LV)
- Keon Coleman (WR, BUF)
- Malachi Fields (WR, NYG)
- Marvin Mims (WR, DEN)
- Rashod Bateman (WR, BAL)
- Troy Franklin (WR, DEN)

**Taxi Squad:**
- Demond Claiborne (RB, MIN, Age 22) 🟡 ROOKIE
- Will Kacmarek (TE, MIA, Age 23) 🟡 ROOKIE
- Colbie Young (WR, CIN, Age 24) 🟡 ROOKIE

### Larz1111 (Roster 5)

**Starters:**
- Dak Prescott (QB, DAL)
- Omarion Hampton (RB, LAC)
- Javonte Williams (RB, DAL)
- Jaxon Smith-Njigba (WR, SEA)
- Rashee Rice (WR, KC)
- Chig Okonkwo (TE, WAS)
- Chuba Hubbard (RB, CAR)
- Jalen Coker (WR, CAR)
- Parker Washington (WR, JAX)
- Cameron Dicker (K, LAC)
- Jacksonville Jaguars (DEF, JAX)
- Jamien Sherwood (LB, NYJ)
- Cedric Gray (LB, TEN)
- Tykee Smith (DB, TB)
- Cooper DeJean (DB, PHI)

**QB Room (6 QBs):**
- Anthony Richardson (IND)
- Dak Prescott (DAL)
- Joe Milton (DAL)
- Lamar Jackson (BAL)
- Taylen Green (CLE)
- Ty Simpson (LAR)

**Positional Surplus (3+ players at same position):**
- QB (6): Anthony Richardson, Dak Prescott, Joe Milton, Lamar Jackson, Taylen Green, Ty Simpson
- RB (8): Brian Robinson, Chuba Hubbard, Javonte Williams, Jonah Coleman, Jonathon Brooks, Kaelon Black, Keaton Mitchell, Omarion Hampton
- TE (6): Cade Otton, Chig Okonkwo, Dalton Schultz, Michael Mayer, Tanner Koziol, Terrance Ferguson
- WR (9): Alec Pierce, Elijah Sarratt, Jahan Dotson, Jalen Coker, Jaxon Smith-Njigba, Makai Lemon, Parker Washington, Rashee Rice, Wan'Dale Robinson

**Bench depth:**
- Anthony Richardson (QB, IND)
- Joe Milton (QB, DAL)
- Lamar Jackson (QB, BAL)
- Brian Robinson (RB, ATL)
- Jonah Coleman (RB, DEN)
- Jonathon Brooks (RB, CAR)
- Keaton Mitchell (RB, LAC)
- Cade Otton (TE, TB)
- Dalton Schultz (TE, HOU)
- Michael Mayer (TE, LV)
- Tanner Koziol (TE, JAX)
- Terrance Ferguson (TE, LAR)
- Alec Pierce (WR, IND)
- Elijah Sarratt (WR, BAL)
- Jahan Dotson (WR, ATL)
- Makai Lemon (WR, PHI)
- Wan'Dale Robinson (WR, TEN)

**Taxi Squad:**
- Ty Simpson (QB, LAR, Age 23) 🟡 ROOKIE
- Taylen Green (QB, CLE, Age 23) 🟡 ROOKIE
- Kaelon Black (RB, SF, Age 24) 🟡 ROOKIE

### DopeOne83 (Roster 6)

**Starters:**
- Josh Allen (QB, BUF)
- Bijan Robinson (RB, ATL)
- Josh Jacobs (RB, GB)
- Tee Higgins (WR, CIN)
- Jaylen Waddle (WR, DEN)
- Trey McBride (TE, ARI)
- DK Metcalf (WR, PIT)
- Chris Godwin (WR, TB)
- Jacory Croskey-Merritt (RB, WAS)
- Lucas Havrisik (K, FA)
- Seattle Seahawks (DEF, SEA)
- Foyesade Oluokun (LB, JAX)
- Carl Granderson (DE, NO)
- Jermod McCoy (DB, LV)
- Avieon Terrell (DB, ATL)

**QB Room (2 QBs):**
- Jalen Hurts (PHI)
- Josh Allen (BUF)

**Positional Surplus (3+ players at same position):**
- DB (4): Avieon Terrell, Genesis Smith, Jaquan Brisker, Jermod McCoy
- LB (12): Bobby Okereke, Bobby Wagner, David Bailey, Dee Winters, Devin White, Ernest Jones, Foyesade Oluokun, Nick Bolton, Payton Wilson, Robert Spillane, Terrel Bernard, Tyrel Dodson
- RB (3): Bijan Robinson, Jacory Croskey-Merritt, Josh Jacobs
- WR (7): Chris Godwin, DK Metcalf, Jaylen Waddle, Josh Downs, Michael Pittman, Stefon Diggs, Tee Higgins

**Bench depth:**
- Genesis Smith (DB, LAC)
- Jaquan Brisker (DB, PIT)
- Yaya Diaby (DL, TB)
- Bobby Okereke (LB, FA)
- Bobby Wagner (LB, FA)
- David Bailey (LB, NYJ)
- Dee Winters (LB, DAL)
- Devin White (LB, DET)
- Ernest Jones (LB, SEA)
- Nick Bolton (LB, KC)
- Payton Wilson (LB, PIT)
- Robert Spillane (LB, NE)
- Terrel Bernard (LB, BUF)
- Tyrel Dodson (LB, MIA)
- Jalen Hurts (QB, PHI)
- Juwan Johnson (TE, NO)
- Josh Downs (WR, IND)
- Michael Pittman (WR, PIT)
- Stefon Diggs (WR, WAS)

### Darkkaze (Roster 7)

**Starters:**
- Caleb Williams (QB, CHI)
- De'Von Achane (RB, MIA)
- Chase Brown (RB, CIN)
- Amon-Ra St. Brown (WR, DET)
- Drake London (WR, ATL)
- Tyler Warren (TE, IND)
- George Pickens (WR, DAL)
- Travis Etienne (RB, NO)
- Jaylen Warren (RB, PIT)
- Ka'imi Fairbairn (K, HOU)
- Denver Broncos (DEF, DEN)
- Nate Landman (LB, LAR)
- Jeremy Chinn (DB, LV)
- Kam Curl (DB, LAR)
- Tre'von Moehrig (DB, CAR)

**QB Room (4 QBs):**
- Caleb Williams (CHI)
- Drew Allar (PIT)
- Sam Darnold (SEA)
- Tyler Shough (NO)

**Positional Surplus (3+ players at same position):**
- DB (3): Jeremy Chinn, Kam Curl, Tre'von Moehrig
- DEF (3): Chicago Bears, Denver Broncos, Pittsburgh Steelers
- QB (4): Caleb Williams, Drew Allar, Sam Darnold, Tyler Shough
- RB (9): Chase Brown, De'Von Achane, J.K. Dobbins, Jaylen Warren, Jaylen Wright, Jordan James, Jordan Mason, Kenny Gainwell, Travis Etienne
- TE (5): Gunnar Helm, Justin Joly, Matt Hibner, Max Klare, Tyler Warren
- WR (8): Amon-Ra St. Brown, Bryce Lance, Drake London, George Pickens, Keenan Allen, Khalil Shakir, Malik Washington, Rashid Shaheed

**Bench depth:**
- Chicago Bears (DEF, CHI)
- Pittsburgh Steelers (DEF, PIT)
- Sam Darnold (QB, SEA)
- Tyler Shough (QB, NO)
- J.K. Dobbins (RB, DEN)
- Jaylen Wright (RB, MIA)
- Jordan James (RB, SF)
- Jordan Mason (RB, MIN)
- Kenny Gainwell (RB, TB)
- Gunnar Helm (TE, TEN)
- Matt Hibner (TE, BAL)
- Bryce Lance (WR, NO)
- Keenan Allen (WR, IND)
- Khalil Shakir (WR, BUF)
- Malik Washington (WR, MIA)
- Rashid Shaheed (WR, SEA)

**Taxi Squad:**
- Max Klare (TE, LAR, Age 23) 🟡 ROOKIE
- Drew Allar (QB, PIT, Age 22) 🟡 ROOKIE
- Justin Joly (TE, DEN, Age 22) 🟡 ROOKIE

### DRoj (Roster 8)

**Starters:**
- Patrick Mahomes (QB, KC)
- Breece Hall (RB, NYJ)
- Kyren Williams (RB, LAR)
- Chris Olave (WR, NO)
- Garrett Wilson (WR, NYJ)
- Harold Fannin (TE, CLE)
- Brenton Strange (TE, JAX)
- Quinshon Judkins (RB, CLE)
- Sam LaPorta (TE, DET)
- Harrison Butker (K, KC)
- Kansas City Chiefs (DEF, KC)
- Devin Bush (LB, CHI)
- SirVocea Dennis (LB, TB)
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
- TE (5): Brenton Strange, Harold Fannin, Jake Ferguson, Mason Taylor, Sam LaPorta
- WR (9): Chris Olave, Deebo Samuel, Elic Ayomanor, Garrett Wilson, Jalen Nailor, Jerry Jeudy, Tank Dell, Xavier Worthy, Zachariah Branch

**Bench depth:**
- Aaron Rodgers (QB, PIT)
- Bo Nix (QB, DEN)
- Bryce Young (QB, CAR)
- C.J. Stroud (QB, HOU)
- Daniel Jones (QB, IND)
- Kirk Cousins (QB, LV)
- Aaron Jones (RB, MIN)
- Isiah Pacheco (RB, DET)
- Jake Ferguson (TE, DAL)
- Mason Taylor (TE, NYJ)
- Deebo Samuel (WR, SF)
- Elic Ayomanor (WR, TEN)
- Jalen Nailor (WR, LV)
- Jerry Jeudy (WR, CLE)
- Tank Dell (WR, HOU)
- Xavier Worthy (WR, KC)

**Taxi Squad:**
- Mike Washington (RB, LV, Age 23) 🟡 ROOKIE
- Zachariah Branch (WR, ATL, Age 22) 🟡 ROOKIE

### Jdunn502 (Roster 10)

**Starters:**
- Kyler Murray (QB, MIN)
- Ashton Jeanty (RB, LV)
- Cam Skattebo (RB, NYG)
- Ja'Marr Chase (WR, CIN)
- Malik Nabers (WR, NYG)
- Colston Loveland (TE, CHI)
- Jordyn Tyson (WR, NO)
- Christian Watson (WR, GB)
- Tony Pollard (RB, TEN)
- Chris Boswell (K, PIT)
- Los Angeles Chargers (DEF, LAC)
- Kaden Elliss (LB, NO)
- Patrick Queen (LB, PIT)
- Talanoa Hufanga (DB, DEN)

**QB Room (7 QBs):**
- Cade Klubnik (NYJ)
- Cam Ward (TEN)
- Cole Payton (PHI)
- Deshaun Watson (CLE)
- Geno Smith (NYJ)
- Kyler Murray (MIN)
- Will Howard (PIT)

**Positional Surplus (3+ players at same position):**
- QB (7): Cade Klubnik, Cam Ward, Cole Payton, Deshaun Watson, Geno Smith, Kyler Murray, Will Howard
- RB (8): Ashton Jeanty, Cam Skattebo, Chris Rodriguez, MarShawn Lloyd, Ray Davis, Seth McGowan, Tony Pollard, Tyrone Tracy
- TE (6): Colston Loveland, Erick All, Marlin Klein, Oscar Delp, Theo Johnson, Tucker Kraft
- WR (9): Brandon Aiyuk, Caleb Douglas, Chris Bell, Christian Watson, Ja'Marr Chase, Jalen McMillan, Jordyn Tyson, Malik Nabers, Will Pauling

**Bench depth:**
- Cleveland Browns (DEF, CLE)
- Cade Klubnik (QB, NYJ)
- Cam Ward (QB, TEN)
- Deshaun Watson (QB, CLE)
- Geno Smith (QB, NYJ)
- Will Howard (QB, PIT)
- Chris Rodriguez (RB, JAX)
- MarShawn Lloyd (RB, GB)
- Ray Davis (RB, BUF)
- Tyrone Tracy (RB, NYG)
- Erick All (TE, CIN)
- Marlin Klein (TE, HOU)
- Theo Johnson (TE, NYG)
- Tucker Kraft (TE, GB)
- Brandon Aiyuk (WR, SF)
- Caleb Douglas (WR, MIA)
- Chris Bell (WR, MIA)
- Jalen McMillan (WR, TB)
- Will Pauling (WR, SF)

**Taxi Squad:**
- Oscar Delp (TE, NO, Age 23) 🟡 ROOKIE
- Cole Payton (QB, PHI, Age 23) 🟡 ROOKIE
- Seth McGowan (RB, IND, Age 24) 🟡 ROOKIE

### nicoyepes (Roster 11)

**Starters:**
- Justin Herbert (QB, LAC)
- Jonathan Taylor (RB, IND)
- Christian McCaffrey (RB, SF)
- Nico Collins (WR, HOU)
- A.J. Brown (WR, NE)
- Hunter Henry (TE, NE)
- Davante Adams (WR, LAR)
- D'Andre Swift (RB, CHI)
- Jameson Williams (WR, DET)
- Jason Myers (K, SEA)
- Baltimore Ravens (DEF, BAL)
- Jack Campbell (LB, DET)
- Roquan Smith (LB, BAL)
- Brian Branch (DB, DET)
- Caleb Downs (DB, DAL)

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
- Arvell Reese (LB, NYG)
- Micah Parsons (LB, GB)
- Garrett Nussmeier (QB, KC)
- Tua Tagovailoa (QB, ATL)
- DJ Giddens (RB, IND)
- James Conner (RB, ARI)
- Sean Tucker (RB, TB)
- Trey Benson (RB, ARI)
- David Njoku (TE, LAC)
- John Michael Gyllenborg (TE, KC)
- Mike Gesicki (TE, CIN)
- Courtland Sutton (WR, DEN)
- DeMario Douglas (WR, NE)
- Deion Burks (WR, IND)
- Kevin Coleman (WR, MIA)
- Ryan Flournoy (WR, DAL)
- Tyquan Thornton (WR, KC)

**Taxi Squad:**
- CJ Daniels (WR, LAR, Age 24) 🟡 ROOKIE
- Nate Boerkircher (TE, JAX, Age 24) 🟡 ROOKIE
- Brenen Thompson (WR, LAC, Age 23) 🟡 ROOKIE

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
- Fred Warner (LB, SF)
- Budda Baker (DB, ARI)

**QB Room (4 QBs):**
- Baker Mayfield (TB)
- Brock Purdy (SF)
- J.J. McCarthy (MIN)
- Mac Jones (SF)

**Positional Surplus (3+ players at same position):**
- QB (4): Baker Mayfield, Brock Purdy, J.J. McCarthy, Mac Jones
- RB (10): Adam Randall, Derrick Henry, Devin Neal, Eli Heidenreich, George Holani, Isaiah Davis, Justice Hill, Kimani Vidal, Najee Harris, Rachaad White
- TE (4): Colby Parkinson, Dalton Kincaid, Isaiah Likely, Michael Trigg
- WR (11): Chimere Dike, Cooper Kupp, Darnell Mooney, De'Zhaun Stribling, Emeka Egbuka, Jakobi Meyers, Jauan Jennings, Mike Evans, Odell Beckham, Roman Wilson, Zay Flowers

**Bench depth:**
- Minnesota Vikings (DEF, MIN)
- Baker Mayfield (QB, TB)
- J.J. McCarthy (QB, MIN)
- Mac Jones (QB, SF)
- Devin Neal (RB, NO)
- George Holani (RB, SEA)
- Isaiah Davis (RB, NYJ)
- Justice Hill (RB, BAL)
- Kimani Vidal (RB, LAC)
- Najee Harris (RB, NYG)
- Colby Parkinson (TE, LAR)
- Chimere Dike (WR, TEN)
- Cooper Kupp (WR, SEA)
- Darnell Mooney (WR, NYG)
- De'Zhaun Stribling (WR, SF)
- Jauan Jennings (WR, MIN)
- Odell Beckham (WR, NYG)
- Roman Wilson (WR, PIT)

**Taxi Squad:**
- Adam Randall (RB, BAL, Age 22) 🟡 ROOKIE
- Michael Trigg (TE, DAL, Age 24) 🟡 ROOKIE
- Eli Heidenreich (RB, PIT, Age 23) 🟡 ROOKIE

<!-- END_AUTO_GENERATED -->
