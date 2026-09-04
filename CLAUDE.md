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
Last synced: 2026-09-04 12:47 PM UTC (auto sync)

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
5017
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
11685
11687
11705
11727
11729
11742
11783
11786
11792
11834
12015
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
13434
13477
13533
13541
13602
13726
13946
BAL
CHI
DAL
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
| DEF | Detroit Lions | DEF | DET | ? |
| LB | Zack Baun | LB | PHI | 29 |
| LB | Quay Walker | LB | LV | 26 |
| DB | Kyle Hamilton | DB | BAL | 25 |
| DB | Derwin James | DB | LAC | 30 |

### Bench

- Donovan Edwards (RB, FA, Age 23, 1 yr exp)
- Xavier McKinney (DB, GB, Age 28, 6 yr exp)
- Jordan Addison (WR, MIN, Age 24, 3 yr exp)
- Darren Waller (TE, CAR, Age 33, 11 yr exp)
- Edgerrin Cooper (LB, GB, Age 24, 2 yr exp)
- Alvin Kamara (RB, NO, Age 31, 9 yr exp)
- Malik Davis (RB, DAL, Age 27, 4 yr exp)
- LeQuint Allen (RB, JAX, Age 22, 1 yr exp)
- Mark Andrews (TE, BAL, Age 30, 8 yr exp)
- Elijah Arroyo (TE, SEA, Age 23, 1 yr exp)
- Jaylin Noel (WR, HOU, Age 24, 1 yr exp)
- Will Anderson (DL, HOU, Age 25, 3 yr exp)
- Justin Fields (QB, KC, Age 27, 5 yr exp)
- Tahj Brooks (RB, CIN, Age 24, 1 yr exp)
- Tre' Harris (WR, LAC, Age 24, 1 yr exp)
- Matthew Stafford (QB, LAR, Age 38, 17 yr exp)

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
- Chamarri Conner (DB, KC)
- Jessie Bates (DB, ATL)

**QB Room (3 QBs):**
- Joe Burrow (CIN)
- Shedeur Sanders (CLE)
- Jordan Love (GB)

**Positional Surplus (3+ players at same position):**
- QB (3): Joe Burrow, Jordan Love, Shedeur Sanders
- RB (8): Bucky Irving, Emari Demercado, J'Mari Taylor, Jahmyr Gibbs, Jaydon Blue, Ollie Gordon, Sione Vaki, TreVeyon Henderson
- TE (3): AJ Barner, George Kittle, Jake Tonges
- WR (16): Barion Brown, Chris Brazzell, DJ Moore, DeVonta Smith, Isaac TeSlaa, Jalen Brooks, Jayden Reed, Malik Benson, Michael Wilson, Puka Nacua, Savion Williams, Skyler Bell, Ted Hurst, Tory Horton, Tyreek Hill, Zavion Thomas

**Bench depth:**
- Jalen Brooks (WR, ARI)
- Skyler Bell (WR, BUF)
- Sione Vaki (RB, DET)
- Emari Demercado (RB, DAL)
- AJ Barner (TE, SEA)
- Zavion Thomas (WR, CHI)
- Tory Horton (WR, SEA)
- Barion Brown (WR, NO)
- Jaydon Blue (RB, PHI)
- Ollie Gordon (RB, MIA)
- Chris Brazzell (WR, CAR)
- Savion Williams (WR, GB)
- Tyreek Hill (WR, FA)
- Shedeur Sanders (QB, CLE)
- Jordan Love (QB, GB)
- Isaac TeSlaa (WR, DET)
- Jayden Reed (WR, GB)
- Jake Tonges (TE, SF)

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
- Drake Maye (NE)
- Jacoby Brissett (ARI)
- Carson Beck (ARI)

**Positional Surplus (3+ players at same position):**
- QB (3): Carson Beck, Drake Maye, Jacoby Brissett
- RB (11): Blake Corum, Chris Brooks, Corey Kiner, Emmett Johnson, Jeremiyah Love, Kenneth Walker, Nicholas Singleton, Rhamondre Stevenson, Roschon Johnson, Tyler Allgeier, Zach Charbonnet
- TE (4): Dallas Goedert, Eli Raridon, Eli Stowers, T.J. Hockenson
- WR (13): Denzel Boston, Dontayvion Wicks, Jalen Royals, Jayden Higgins, Kyle Williams, Luther Burden, Marvin Harrison, Pat Bryant, Romeo Doubs, Tetairoa McMillan, Travis Hunter, Xavier Hutchinson, Xavier Legette

**Bench depth:**
- Jalen Royals (WR, KC)
- Zach Charbonnet (RB, SEA)
- Jacoby Brissett (QB, ARI)
- Roschon Johnson (RB, CHI)
- Denzel Boston (WR, CLE)
- Nicholas Singleton (RB, TEN)
- Jayden Higgins (WR, HOU)
- Xavier Legette (WR, CAR)
- Kyle Williams (WR, NE)
- Xavier Hutchinson (WR, HOU)
- Emmett Johnson (RB, KC)
- Pat Bryant (WR, DEN)
- Tyler Allgeier (RB, ARI)
- Blake Corum (RB, LAR)
- Dontayvion Wicks (WR, PHI)
- Corey Kiner (RB, NE)
- T.J. Hockenson (TE, MIN)
- Chris Brooks (RB, GB)
- New England Patriots (DEF, NE)

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
- Matthew Golden (WR, GB)
- Lewis Bond (WR, HOU)
- Charlie Kolar (TE, LAC)
- Devaughn Vele (WR, NO)
- Ja'Kobi Lane (WR, BAL)
- Dillon Gabriel (QB, CLE)
- Darius Cooper (WR, PHI)
- Kyle Monangai (RB, CHI)
- Tyjae Spears (RB, TEN)
- Jordyn Brooks (LB, MIA)
- Jared Goff (QB, DET)
- Woody Marks (RB, HOU)
- Ricky Pearsall (WR, SF)
- Dohnte Meyers (WR, CIN)
- Jacob Saylors (RB, DET)
- Isaiah Williams (WR, NYJ)
- Antonio Williams (WR, WAS)
- Kayshon Boutte (WR, HOU)

### Bombas (Roster 4)

**Starters:**
- Trevor Lawrence (QB, JAX)
- RJ Harvey (RB, DEN)
- Jadarian Price (RB, SEA)
- KC Concepcion (WR, CLE)
- Omar Cooper (WR, NYJ)
- Oronde Gadsden (TE, LAC)
- Dylan Sampson (RB, CLE)
- Tre Tucker (WR, LV)
- Calvin Ridley (WR, TEN)
- Harrison Mevis (K, LAR)
- Dallas Cowboys (DEF, DAL)

**QB Room (4 QBs):**
- Malik Willis (MIA)
- Fernando Mendoza (LV)
- Michael Penix (ATL)
- Trevor Lawrence (JAX)

**Positional Surplus (3+ players at same position):**
- QB (4): Fernando Mendoza, Malik Willis, Michael Penix, Trevor Lawrence
- RB (10): Braelon Allen, Brashard Smith, Demond Claiborne, Dylan Sampson, Jadarian Price, Joe Mixon, Kaleb Johnson, Kaytron Allen, RJ Harvey, Tank Bigsby
- TE (5): Darnell Washington, Kenyon Sadiq, Oronde Gadsden, Sam Roush, Will Kacmarek
- WR (13): Adonai Mitchell, Calvin Ridley, Colbie Young, Germie Bernard, Jack Bech, KC Concepcion, Keon Coleman, Malachi Fields, Marvin Mims, Omar Cooper, Rashod Bateman, Tre Tucker, Troy Franklin

**Bench depth:**
- Sam Roush (TE, CHI)
- Germie Bernard (WR, PIT)
- Adonai Mitchell (WR, NYJ)
- Keon Coleman (WR, BUF)
- Malik Willis (QB, MIA)
- Joe Mixon (RB, FA)
- Tank Bigsby (RB, PHI)
- Rashod Bateman (WR, BAL)
- Kaytron Allen (RB, WAS)
- Fernando Mendoza (QB, LV)
- Jack Bech (WR, LV)
- Troy Franklin (WR, DEN)
- Michael Penix (QB, ATL)
- Marvin Mims (WR, DEN)
- Malachi Fields (WR, NYG)
- Darnell Washington (TE, PIT)
- Kaleb Johnson (RB, GB)
- Braelon Allen (RB, NYJ)
- Kenyon Sadiq (TE, NYJ)
- Brashard Smith (RB, KC)

### Larz1111 (Roster 5)

**Starters:**
- Lamar Jackson (QB, BAL)
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
- Taylen Green (CLE)
- Sam Howell (DAL)
- Ty Simpson (LAR)
- Anthony Richardson (IND)
- Lamar Jackson (BAL)
- Dak Prescott (DAL)

**Positional Surplus (3+ players at same position):**
- QB (6): Anthony Richardson, Dak Prescott, Lamar Jackson, Sam Howell, Taylen Green, Ty Simpson
- RB (8): Brian Robinson, Chuba Hubbard, Javonte Williams, Jonah Coleman, Jonathon Brooks, Kaelon Black, Keaton Mitchell, Omarion Hampton
- TE (5): Cade Otton, Chig Okonkwo, Dalton Schultz, Michael Mayer, Terrance Ferguson
- WR (9): Alec Pierce, Elijah Sarratt, Jahan Dotson, Jalen Coker, Jaxon Smith-Njigba, Makai Lemon, Parker Washington, Rashee Rice, Wan'Dale Robinson

**Bench depth:**
- Makai Lemon (WR, PHI)
- Dalton Schultz (TE, HOU)
- Sam Howell (QB, DAL)
- Michael Mayer (TE, LV)
- Jonah Coleman (RB, DEN)
- Wan'Dale Robinson (WR, TEN)
- Jonathon Brooks (RB, CAR)
- Anthony Richardson (QB, IND)
- Alec Pierce (WR, IND)
- Keaton Mitchell (RB, LAC)
- Terrance Ferguson (TE, LAR)
- Brian Robinson (RB, ATL)
- Elijah Sarratt (WR, BAL)
- Cade Otton (TE, TB)
- Jahan Dotson (WR, ATL)
- Dak Prescott (QB, DAL)

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
- Josh Allen (BUF)
- Jalen Hurts (PHI)

**Positional Surplus (3+ players at same position):**
- DB (4): Avieon Terrell, Genesis Smith, Jaquan Brisker, Jermod McCoy
- LB (12): Bobby Okereke, Bobby Wagner, David Bailey, Dee Winters, Devin White, Ernest Jones, Foyesade Oluokun, Nick Bolton, Payton Wilson, Robert Spillane, Terrel Bernard, Tyrel Dodson
- RB (3): Bijan Robinson, Jacory Croskey-Merritt, Josh Jacobs
- WR (7): Chris Godwin, DK Metcalf, Jaylen Waddle, Josh Downs, Michael Pittman, Stefon Diggs, Tee Higgins

**Bench depth:**
- Juwan Johnson (TE, NO)
- Michael Pittman (WR, PIT)
- Nick Bolton (LB, KC)
- Terrel Bernard (LB, BUF)
- Ernest Jones (LB, SEA)
- Payton Wilson (LB, PIT)
- Josh Downs (WR, IND)
- Robert Spillane (LB, NE)
- Stefon Diggs (WR, WAS)
- Dee Winters (LB, DAL)
- Jaquan Brisker (DB, PIT)
- Tyrel Dodson (LB, CAR)
- Bobby Wagner (LB, FA)
- Bobby Okereke (LB, CAR)
- Genesis Smith (DB, LAC)
- Yaya Diaby (DL, TB)
- David Bailey (LB, NYJ)
- Jalen Hurts (QB, PHI)
- Devin White (LB, DET)

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
- Drew Allar (PIT)
- Caleb Williams (CHI)
- Tyler Shough (NO)
- Sam Darnold (SEA)

**Positional Surplus (3+ players at same position):**
- DB (3): Jeremy Chinn, Kam Curl, Tre'von Moehrig
- DEF (3): Chicago Bears, Denver Broncos, Pittsburgh Steelers
- QB (4): Caleb Williams, Drew Allar, Sam Darnold, Tyler Shough
- RB (9): Chase Brown, De'Von Achane, J.K. Dobbins, Jaylen Warren, Jaylen Wright, Jordan James, Jordan Mason, Kenny Gainwell, Travis Etienne
- TE (5): Gunnar Helm, Marlin Klein, Matt Hibner, Max Klare, Tyler Warren
- WR (8): Amon-Ra St. Brown, Bryce Lance, Drake London, George Pickens, Keenan Allen, Khalil Shakir, Malik Washington, Rashid Shaheed

**Bench depth:**
- J.K. Dobbins (RB, DEN)
- Jaylen Wright (RB, MIA)
- Chicago Bears (DEF, CHI)
- Jordan James (RB, SF)
- Gunnar Helm (TE, TEN)
- Kenny Gainwell (RB, TB)
- Bryce Lance (WR, NO)
- Keenan Allen (WR, IND)
- Rashid Shaheed (WR, SEA)
- Marlin Klein (TE, HOU)
- Jordan Mason (RB, MIN)
- Tyler Shough (QB, NO)
- Pittsburgh Steelers (DEF, PIT)
- Sam Darnold (QB, SEA)
- Malik Washington (WR, MIA)
- Khalil Shakir (WR, BUF)

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
- C.J. Stroud (HOU)
- Bo Nix (DEN)
- Bryce Young (CAR)
- Aaron Rodgers (PIT)
- Patrick Mahomes (KC)
- Kirk Cousins (LV)
- Daniel Jones (IND)

**Positional Surplus (3+ players at same position):**
- QB (7): Aaron Rodgers, Bo Nix, Bryce Young, C.J. Stroud, Daniel Jones, Kirk Cousins, Patrick Mahomes
- RB (6): Aaron Jones, Breece Hall, Isiah Pacheco, Kyren Williams, Mike Washington, Quinshon Judkins
- TE (5): Brenton Strange, Harold Fannin, Jake Ferguson, Mason Taylor, Sam LaPorta
- WR (9): Chris Olave, Deebo Samuel, Elic Ayomanor, Garrett Wilson, Jalen Nailor, Jerry Jeudy, Tank Dell, Xavier Worthy, Zachariah Branch

**Bench depth:**
- Tank Dell (WR, HOU)
- C.J. Stroud (QB, HOU)
- Mason Taylor (TE, NYJ)
- Aaron Jones (RB, MIN)
- Bo Nix (QB, DEN)
- Elic Ayomanor (WR, TEN)
- Xavier Worthy (WR, KC)
- Bryce Young (QB, CAR)
- Deebo Samuel (WR, SF)
- Aaron Rodgers (QB, PIT)
- Jalen Nailor (WR, LV)
- Jake Ferguson (TE, DAL)
- Kirk Cousins (QB, LV)
- Isiah Pacheco (RB, DET)
- Daniel Jones (QB, IND)
- Jerry Jeudy (WR, CLE)

### Jdunn502 (Roster 10)

**Starters:**
- Kyler Murray (QB, MIN)
- Ashton Jeanty (RB, LV)
- Cam Skattebo (RB, NYG)
- Ja'Marr Chase (WR, CIN)
- Malik Nabers (WR, NYG)
- Colston Loveland (TE, CHI)
- Tucker Kraft (TE, GB)
- Christian Watson (WR, GB)
- Tony Pollard (RB, TEN)
- Chris Boswell (K, PIT)
- Los Angeles Chargers (DEF, LAC)
- Kaden Elliss (LB, NO)
- Patrick Queen (LB, PIT)
- Talanoa Hufanga (DB, DEN)
- Kamari Lassiter (DB, HOU)

**QB Room (8 QBs):**
- Kyler Murray (MIN)
- Deshaun Watson (CLE)
- Jalon Daniels (TB)
- Cade Klubnik (NYJ)
- Will Howard (PIT)
- Cam Ward (TEN)
- Cole Payton (PHI)
- Geno Smith (NYJ)

**Positional Surplus (3+ players at same position):**
- QB (8): Cade Klubnik, Cam Ward, Cole Payton, Deshaun Watson, Geno Smith, Jalon Daniels, Kyler Murray, Will Howard
- RB (9): Ashton Jeanty, Cam Skattebo, Chris Rodriguez, Jamal Haynes, MarShawn Lloyd, Ray Davis, Seth McGowan, Tony Pollard, Tyrone Tracy
- TE (4): Colston Loveland, Oscar Delp, Theo Johnson, Tucker Kraft
- WR (8): Brandon Aiyuk, Caleb Douglas, Chris Bell, Christian Watson, Ja'Marr Chase, Jalen McMillan, Jordyn Tyson, Malik Nabers

**Bench depth:**
- Ray Davis (RB, BUF)
- Deshaun Watson (QB, CLE)
- Brandon Aiyuk (WR, SF)
- Jalon Daniels (QB, TB)
- Cade Klubnik (QB, NYJ)
- MarShawn Lloyd (RB, GB)
- Jordyn Tyson (WR, NO)
- Will Howard (QB, PIT)
- Jamal Haynes (RB, FA)
- Tyrone Tracy (RB, NYG)
- Chris Rodriguez (RB, JAX)
- Cam Ward (QB, TEN)
- Chris Bell (WR, MIA)
- Theo Johnson (TE, NYG)
- Caleb Douglas (WR, MIA)
- Jalen McMillan (WR, TB)
- Geno Smith (QB, NYJ)

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
- Tyquan Thornton (WR, KC)
- Deion Burks (WR, IND)
- David Njoku (TE, LAC)
- Kevin Coleman (WR, MIA)
- Ryan Flournoy (WR, DAL)
- Courtland Sutton (WR, DEN)
- DJ Giddens (RB, IND)
- Garrett Nussmeier (QB, KC)
- Micah Parsons (LB, GB)
- Arvell Reese (LB, NYG)
- Mike Gesicki (TE, CIN)
- Sean Tucker (RB, TB)
- James Conner (RB, ARI)
- DeMario Douglas (WR, NE)
- Trey Benson (RB, ARI)
- John Michael Gyllenborg (TE, KC)
- Tua Tagovailoa (QB, ATL)

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
- Mac Jones (SF)
- Brock Purdy (SF)
- J.J. McCarthy (MIN)
- Baker Mayfield (TB)

**Positional Surplus (3+ players at same position):**
- QB (4): Baker Mayfield, Brock Purdy, J.J. McCarthy, Mac Jones
- RB (10): Adam Randall, Derrick Henry, Devin Neal, Eli Heidenreich, George Holani, Isaiah Davis, Justice Hill, Kimani Vidal, Najee Harris, Rachaad White
- TE (4): Colby Parkinson, Dalton Kincaid, Isaiah Likely, Michael Trigg
- WR (11): Chimere Dike, Cooper Kupp, Darnell Mooney, De'Zhaun Stribling, Emeka Egbuka, Jakobi Meyers, Jauan Jennings, Mike Evans, Odell Beckham, Roman Wilson, Zay Flowers

**Bench depth:**
- Colby Parkinson (TE, LAR)
- Minnesota Vikings (DEF, MIN)
- Mac Jones (QB, SF)
- Najee Harris (RB, NYG)
- Odell Beckham (WR, NYG)
- Darnell Mooney (WR, NYG)
- Cooper Kupp (WR, SEA)
- Devin Neal (RB, NO)
- J.J. McCarthy (QB, MIN)
- George Holani (RB, SEA)
- Chimere Dike (WR, TEN)
- Roman Wilson (WR, PIT)
- Baker Mayfield (QB, TB)
- Isaiah Davis (RB, NYJ)
- Kimani Vidal (RB, LAC)
- Jauan Jennings (WR, MIN)
- Justice Hill (RB, BAL)
- Adam Randall (RB, BAL)

<!-- END_AUTO_GENERATED -->
