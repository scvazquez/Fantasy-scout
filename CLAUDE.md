# Fantasy Scout — League Intelligence
<!-- Roster Sync routine manages everything between AUTO markers -->

<!-- ============================================================ -->
<!-- MANUAL SECTION — edit freely, Roster Sync will not touch     -->
<!-- ============================================================ -->

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
- Larz1111 (Roster 5): my father-in-law. Owns Lamar Jackson plus
  3 surplus QBs (Richardson, Stafford, Prescott). Warmest trade
  target in the league.
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
Last synced: 2026-06-29 12:47 PM PT

## Ownership Index
```
96
421
1166
1233
1373
1466
2078
2133
2216
2449
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
4066
4081
4137
4199
4217
4227
4866
4881
4892
4943
4950
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
6039
6119
6149
6315
6768
6770
6783
6786
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
8172
8180
8183
8188
8205
8210
8228
8259
8266
8280
8311
8323
8339
8355
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
10219
10222
10229
10232
10236
10859
10880
10905
10921
10980
11017
11292
11370
11435
11533
11559
11560
11563
11564
11565
11566
11569
11571
11575
11576
11581
11583
11584
11586
11589
11597
11600
11603
11604
11610
11618
11620
11624
11625
11626
11627
11628
11631
11632
11635
11637
11638
11643
11646
11647
11651
11655
11678
11687
11705
11727
11742
11783
11786
12048
12455
12457
12462
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
12503
12504
12505
12506
12507
12508
12509
12510
12511
12512
12514
12515
12516
12517
12518
12519
12521
12522
12523
12524
12526
12527
12529
12530
12533
12534
12535
12536
12539
12540
12543
12544
12545
12547
12566
12567
12574
12578
12641
12713
13066
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
13392
13399
13400
13401
13402
13403
13404
13405
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
13662
ATL
BAL
CLE
DEN
DET
HOU
JAX
LAC
LAR
MIN
NE
NO
NYG
PHI
PIT
SEA
```

## My Roster — Scvazquez (Roster 9)

### Starting Lineup

| Slot | Player | Pos | Team | Age |
|------|--------|-----|------|-----|
| QB | Jayden Daniels | QB | WAS | 25 |
| RB | Saquon Barkley | RB | PHI | 29 |
| RB | David Montgomery | RB | HOU | 29 |
| WR | CeeDee Lamb | WR | DAL | 27 |
| WR | Justin Jefferson | WR | MIN | 27 |
| TE | Kyle Pitts | TE | ATL | 25 |
| FLEX | Ladd McConkey | WR | LAC | 24 |
| FLEX | Terry McLaurin | WR | WAS | 30 |
| FLEX | Rico Dowdle | RB | PIT | 28 |
| K | Ben Sauls | K | NYG | 24 |
| DEF | Detroit Lions | DEF | DET | ? |
| LB | Edgerrin Cooper | LB | GB | 24 |
| LB | Quay Walker | LB | LV | 26 |
| DB | Kyle Hamilton | DB | BAL | 25 |
| DB | Derwin James | DB | LAC | 29 |

### Bench

- Zack Baun (LB, PHI, Age 29, 6 yr exp)
- Justin Fields (QB, KC, Age 27, 5 yr exp)
- Matthew Stafford (QB, LAR, Age 38, 17 yr exp)
- Alvin Kamara (RB, NO, Age 30, 9 yr exp)
- Donovan Edwards (RB, MIA, Age 23, 1 yr exp)
- LeQuint Allen (RB, JAX, Age 21, 1 yr exp)
- Malik Davis (RB, DAL, Age 27, 4 yr exp)
- Najee Harris (RB, FA, Age 27, 5 yr exp)
- Tahj Brooks (RB, CIN, Age 24, 1 yr exp)
- Elijah Arroyo (TE, SEA, Age 23, 1 yr exp)
- Greg Dulcich (TE, MIA, Age 26, 4 yr exp)
- Mark Andrews (TE, BAL, Age 30, 8 yr exp)
- Arian Smith (WR, NYJ, Age 24, 1 yr exp)
- Jaylin Noel (WR, HOU, Age 23, 1 yr exp)
- Jimmy Horn (WR, CAR, Age 23, 1 yr exp)
- Jordan Addison (WR, MIN, Age 24, 3 yr exp)
- Tre' Harris (WR, LAC, Age 24, 1 yr exp)

### Taxi Squad

- Cyrus Allen (WR, KC, Age 23)

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
- Unknown(0) (UNK, FA)
- Atlanta Falcons (DEF, ATL)
- Unknown(0) (UNK, FA)
- Unknown(0) (UNK, FA)
- Unknown(0) (UNK, FA)
- Unknown(0) (UNK, FA)

**QB Room (3 QBs):**
- Joe Burrow (CIN)
- Jordan Love (GB)
- Shedeur Sanders (CLE)

**Positional Surplus (3+ players at same position):**
- QB (3): Joe Burrow, Jordan Love, Shedeur Sanders
- RB (8): Bucky Irving, J'Mari Taylor, Jahmyr Gibbs, Jaydon Blue, Kalel Mullings, Ollie Gordon, Robert Henry, TreVeyon Henderson
- TE (3): AJ Barner, George Kittle, Jake Tonges
- WR (19): Chris Brazzell, Christian Kirk, DJ Moore, Darnell Mooney, DeVonta Smith, Isaac TeSlaa, Jayden Reed, Jaylin Lane, Keon Coleman, Malik Benson, Michael Wilson, Puka Nacua, Ryan Flournoy, Savion Williams, Skyler Bell, Ted Hurst, Tory Horton, Tyreek Hill, Zavion Thomas

**Bench depth:**
- AJ Barner (TE, SEA)
- Chris Brazzell (WR, CAR) 🟡 ROOKIE
- Christian Kirk (WR, SF)
- Darnell Mooney (WR, NYG)
- Isaac TeSlaa (WR, DET)
- Jake Tonges (TE, SF)
- Jayden Reed (WR, GB)
- Jaydon Blue (RB, DAL)
- Jaylin Lane (WR, WAS)
- Jordan Love (QB, GB)
- Kalel Mullings (RB, TEN)
- Keon Coleman (WR, BUF)
- Malik Benson (WR, LV) 🟡 ROOKIE
- Ollie Gordon (RB, MIA)
- Ryan Flournoy (WR, DAL)
- Savion Williams (WR, GB)
- Shedeur Sanders (QB, CLE)
- Skyler Bell (WR, BUF) 🟡 ROOKIE
- Tory Horton (WR, SEA)
- Tyreek Hill (WR, FA)
- Zavion Thomas (WR, CHI) 🟡 ROOKIE

**Taxi Squad:**
- J'Mari Taylor (RB, JAX) 🟡 ROOKIE
- Robert Henry (RB, WAS) 🟡 ROOKIE
- Ted Hurst (WR, TB) 🟡 ROOKIE

### JQuinna10 (Roster 2)

**Starters:**
- Drake Maye (QB, NE)
- Kenneth Walker (RB, KC)
- Jeremiyah Love (RB, ARI)
- Tetairoa McMillan (WR, CAR)
- Marvin Harrison (WR, ARI)
- T.J. Hockenson (TE, MIN)
- Luther Burden (WR, CHI)
- Rhamondre Stevenson (RB, NE)
- Jayden Higgins (WR, HOU)
- Cam Little (K, JAX)
- Houston Texans (DEF, HOU)
- Carson Schwesinger (LB, CLE)
- Unknown(0) (UNK, FA)
- Travis Hunter (WR, JAX)
- Unknown(0) (UNK, FA)

**QB Room (4 QBs):**
- Carson Beck (ARI)
- Drake Maye (NE)
- Jacoby Brissett (ARI)
- Tommy DeVito (NE)

**Positional Surplus (3+ players at same position):**
- QB (4): Carson Beck, Drake Maye, Jacoby Brissett, Tommy DeVito
- RB (10): Blake Corum, Emmett Johnson, George Holani, Jam Miller, Jarquez Hunter, Jeremiyah Love, Kenneth Walker, Nicholas Singleton, Rhamondre Stevenson, Tyler Allgeier
- TE (4): Dallas Goedert, Eli Raridon, Eli Stowers, T.J. Hockenson
- WR (12): Dontayvion Wicks, Isaiah Bond, Jalen Royals, Jayden Higgins, Kyle Williams, Luther Burden, Marvin Harrison, Pat Bryant, Romeo Doubs, Tetairoa McMillan, Travis Hunter, Xavier Legette

**Bench depth:**
- Blake Corum (RB, LAR)
- Dallas Goedert (TE, PHI)
- Dontayvion Wicks (WR, PHI)
- Emmett Johnson (RB, KC) 🟡 ROOKIE
- George Holani (RB, SEA)
- Isaiah Bond (WR, CLE)
- Jacoby Brissett (QB, ARI)
- Jalen Royals (WR, KC)
- Jam Miller (RB, NE) 🟡 ROOKIE
- Jarquez Hunter (RB, LAR)
- Kyle Williams (WR, NE)
- New England Patriots (DEF, NE)
- Nicholas Singleton (RB, TEN) 🟡 ROOKIE
- Pat Bryant (WR, DEN)
- Romeo Doubs (WR, NE)
- Tommy DeVito (QB, NE)
- Tyler Allgeier (RB, ARI)
- Xavier Legette (WR, CAR)

**Taxi Squad:**
- Carson Beck (QB, ARI) 🟡 ROOKIE
- Eli Raridon (TE, NE) 🟡 ROOKIE
- Eli Stowers (TE, PHI) 🟡 ROOKIE

### WOODYWOOD1978 (Roster 3)

**Starters:**
- Jaxson Dart (QB, NYG)
- James Cook (RB, BUF)
- Bhayshul Tuten (RB, JAX)
- Carnell Tate (WR, TEN)
- Rome Odunze (WR, CHI)
- Brock Bowers (TE, LV)
- Kyle Monangai (RB, CHI)
- Brian Thomas (WR, JAX)
- Ricky Pearsall (WR, SF)
- Andy Borregales (K, NE)
- New Orleans Saints (DEF, NO)
- Jordyn Brooks (LB, MIA)
- Sonny Styles (LB, WAS)
- Nick Cross (DB, WAS)
- Dillon Thieneman (DB, CHI)

**QB Room (2 QBs):**
- Jared Goff (DET)
- Jaxson Dart (NYG)

**Positional Surplus (3+ players at same position):**
- LB (4): Jihaad Campbell, Jordyn Brooks, Sonny Styles, Zaire Franklin
- RB (5): Bhayshul Tuten, James Cook, Kyle Monangai, Tyjae Spears, Woody Marks
- WR (9): Antonio Williams, Brian Thomas, Carnell Tate, Ja'Kobi Lane, Kayshon Boutte, Matthew Golden, Quentin Johnston, Ricky Pearsall, Rome Odunze

**Bench depth:**
- Antonio Williams (WR, WAS) 🟡 ROOKIE
- Ja'Kobi Lane (WR, BAL) 🟡 ROOKIE
- Jared Goff (QB, DET)
- Jihaad Campbell (LB, PHI)
- Kayshon Boutte (WR, NE)
- Kayvon Thibodeaux (DL, NYG)
- Matthew Golden (WR, GB)
- Quentin Johnston (WR, LAC)
- Travis Kelce (TE, KC)
- Tyjae Spears (RB, TEN)
- Woody Marks (RB, HOU)
- Zaire Franklin (LB, GB)

### Bombas (Roster 4)

**Starters:**
- Trevor Lawrence (QB, JAX)
- RJ Harvey (RB, DEN)
- Jadarian Price (RB, SEA)
- KC Concepcion (WR, CLE)
- Omar Cooper (WR, NYJ)
- Kenyon Sadiq (TE, NYJ)
- Denzel Boston (WR, CLE)
- Tre Tucker (WR, LV)
- Oronde Gadsden (TE, LAC)
- Unknown(0) (UNK, FA)
- Unknown(0) (UNK, FA)
- Unknown(0) (UNK, FA)
- Unknown(0) (UNK, FA)
- Unknown(0) (UNK, FA)
- Unknown(0) (UNK, FA)

**QB Room (4 QBs):**
- Fernando Mendoza (LV)
- Malik Willis (MIA)
- Michael Penix (ATL)
- Trevor Lawrence (JAX)

**Positional Surplus (3+ players at same position):**
- QB (4): Fernando Mendoza, Malik Willis, Michael Penix, Trevor Lawrence
- RB (10): Braelon Allen, Brashard Smith, Demond Claiborne, Dylan Sampson, Jadarian Price, Joe Mixon, Kaleb Johnson, Kaytron Allen, RJ Harvey, Tank Bigsby
- TE (5): Darnell Washington, Kenyon Sadiq, Oronde Gadsden, Sam Roush, Will Kacmarek
- WR (13): Adonai Mitchell, Calvin Ridley, Colbie Young, Denzel Boston, Germie Bernard, Jack Bech, KC Concepcion, Malachi Fields, Marvin Mims, Omar Cooper, Rashod Bateman, Tre Tucker, Troy Franklin

**Bench depth:**
- Adonai Mitchell (WR, NYJ)
- Braelon Allen (RB, NYJ)
- Brashard Smith (RB, KC)
- Calvin Ridley (WR, TEN)
- Darnell Washington (TE, PIT)
- Dylan Sampson (RB, CLE)
- Fernando Mendoza (QB, LV) 🟡 ROOKIE
- Germie Bernard (WR, PIT) 🟡 ROOKIE
- Jack Bech (WR, LV)
- Joe Mixon (RB, FA)
- Kaleb Johnson (RB, PIT)
- Kaytron Allen (RB, WAS) 🟡 ROOKIE
- Malachi Fields (WR, NYG) 🟡 ROOKIE
- Malik Willis (QB, MIA)
- Marvin Mims (WR, DEN)
- Michael Penix (QB, ATL)
- Rashod Bateman (WR, BAL)
- Sam Roush (TE, CHI) 🟡 ROOKIE
- Tank Bigsby (RB, PHI)
- Troy Franklin (WR, DEN)

**Taxi Squad:**
- Colbie Young (WR, CIN) 🟡 ROOKIE
- Demond Claiborne (RB, MIN) 🟡 ROOKIE
- Will Kacmarek (TE, MIA) 🟡 ROOKIE

### Larz1111 (Roster 5)

**Starters:**
- Dak Prescott (QB, DAL)
- Omarion Hampton (RB, LAC)
- Javonte Williams (RB, DAL)
- Jaxon Smith-Njigba (WR, SEA)
- Rashee Rice (WR, KC)
- Dalton Schultz (TE, HOU)
- Chuba Hubbard (RB, CAR)
- Alec Pierce (WR, IND)
- Parker Washington (WR, JAX)
- Cameron Dicker (K, LAC)
- Los Angeles Rams (DEF, LAR)
- Jamien Sherwood (LB, NYJ)
- Cedric Gray (LB, TEN)
- Tykee Smith (DB, TB)
- Cooper DeJean (DB, PHI)

**QB Room (5 QBs):**
- Anthony Richardson (IND)
- Dak Prescott (DAL)
- Lamar Jackson (BAL)
- Taylen Green (CLE)
- Ty Simpson (LAR)

**Positional Surplus (3+ players at same position):**
- QB (5): Anthony Richardson, Dak Prescott, Lamar Jackson, Taylen Green, Ty Simpson
- RB (8): Brian Robinson, Chuba Hubbard, Javonte Williams, Jonah Coleman, Jonathon Brooks, Kaelon Black, Keaton Mitchell, Omarion Hampton
- TE (4): Chig Okonkwo, Dalton Schultz, Ja'Tavion Sanders, Terrance Ferguson
- WR (9): Alec Pierce, Elijah Sarratt, Jalen Coker, Jaxon Smith-Njigba, Jeff Caldwell, Makai Lemon, Parker Washington, Rashee Rice, Wan'Dale Robinson

**Bench depth:**
- Anthony Richardson (QB, IND)
- Brian Robinson (RB, ATL)
- Chig Okonkwo (TE, WAS)
- Elijah Sarratt (WR, BAL) 🟡 ROOKIE
- Ja'Tavion Sanders (TE, CAR)
- Jacksonville Jaguars (DEF, JAX)
- Jalen Coker (WR, CAR)
- Jonah Coleman (RB, DEN) 🟡 ROOKIE
- Jonathon Brooks (RB, CAR)
- Kaelon Black (RB, SF) 🟡 ROOKIE
- Keaton Mitchell (RB, LAC)
- Lamar Jackson (QB, BAL)
- Makai Lemon (WR, PHI) 🟡 ROOKIE
- Terrance Ferguson (TE, LAR)
- Wan'Dale Robinson (WR, TEN)

**Taxi Squad:**
- Jeff Caldwell (WR, KC) 🟡 ROOKIE
- Taylen Green (QB, CLE) 🟡 ROOKIE
- Ty Simpson (QB, LAR) 🟡 ROOKIE

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
- Lucas Havrisik (K, GB)
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
- Bobby Okereke (LB, FA)
- Bobby Wagner (LB, FA)
- David Bailey (LB, NYJ) 🟡 ROOKIE
- Dee Winters (LB, DAL)
- Devin White (LB, FA)
- Ernest Jones (LB, SEA)
- Genesis Smith (DB, LAC) 🟡 ROOKIE
- Jalen Hurts (QB, PHI)
- Jaquan Brisker (DB, PIT)
- Josh Downs (WR, IND)
- Juwan Johnson (TE, NO)
- Michael Pittman (WR, PIT)
- Nick Bolton (LB, KC)
- Payton Wilson (LB, PIT)
- Robert Spillane (LB, NE)
- Stefon Diggs (WR, FA)
- Terrel Bernard (LB, BUF)
- Tyrel Dodson (LB, MIA)
- Yaya Diaby (DL, TB)

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
- Unknown(0) (UNK, FA)

**QB Room (4 QBs):**
- Caleb Williams (CHI)
- Drew Allar (PIT)
- Sam Darnold (SEA)
- Tyler Shough (NO)

**Positional Surplus (3+ players at same position):**
- QB (4): Caleb Williams, Drew Allar, Sam Darnold, Tyler Shough
- RB (10): Chase Brown, De'Von Achane, Emanuel Wilson, J.K. Dobbins, Jaylen Warren, Jaylen Wright, Jordan James, Jordan Mason, Kenny Gainwell, Travis Etienne
- TE (7): Cade Otton, Evan Engram, Gunnar Helm, Justin Joly, Matt Hibner, Max Klare, Tyler Warren
- WR (7): Amon-Ra St. Brown, Bryce Lance, Drake London, George Pickens, Khalil Shakir, Malik Washington, Rashid Shaheed

**Bench depth:**
- Bryce Lance (WR, NO) 🟡 ROOKIE
- Cade Otton (TE, TB)
- Emanuel Wilson (RB, SEA)
- Evan Engram (TE, DEN)
- Gunnar Helm (TE, TEN)
- J.K. Dobbins (RB, DEN)
- Jaylen Wright (RB, MIA)
- Jordan James (RB, SF)
- Jordan Mason (RB, MIN)
- Kenny Gainwell (RB, TB)
- Khalil Shakir (WR, BUF)
- Malik Washington (WR, MIA)
- Matt Hibner (TE, BAL) 🟡 ROOKIE
- Pittsburgh Steelers (DEF, PIT)
- Rashid Shaheed (WR, SEA)
- Sam Darnold (QB, SEA)
- Tyler Shough (QB, NO)

**Taxi Squad:**
- Drew Allar (QB, PIT) 🟡 ROOKIE
- Justin Joly (TE, DEN) 🟡 ROOKIE
- Max Klare (TE, LAR) 🟡 ROOKIE

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
- Unknown(0) (UNK, FA)
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
- RB (7): Aaron Jones, Breece Hall, Devin Neal, Isiah Pacheco, Kyren Williams, Mike Washington, Quinshon Judkins
- TE (5): Brenton Strange, Harold Fannin, Jake Ferguson, Mason Taylor, Sam LaPorta
- WR (9): Chris Olave, Deebo Samuel, Elic Ayomanor, Garrett Wilson, Jalen Nailor, Jerry Jeudy, Tank Dell, Xavier Worthy, Zachariah Branch

**Bench depth:**
- Aaron Jones (RB, MIN)
- Aaron Rodgers (QB, PIT)
- Bo Nix (QB, DEN)
- Bryce Young (QB, CAR)
- C.J. Stroud (QB, HOU)
- Daniel Jones (QB, IND)
- Deebo Samuel (WR, FA)
- Devin Neal (RB, NO)
- Elic Ayomanor (WR, TEN)
- Isiah Pacheco (RB, DET)
- Jake Ferguson (TE, DAL)
- Jalen Nailor (WR, LV)
- Jerry Jeudy (WR, CLE)
- Kirk Cousins (QB, LV)
- Mason Taylor (TE, NYJ)
- Tank Dell (WR, HOU)
- Xavier Worthy (WR, KC)

**Taxi Squad:**
- Mike Washington (RB, LV) 🟡 ROOKIE
- Zachariah Branch (WR, ATL) 🟡 ROOKIE

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
- Tucker Kraft (TE, GB)
- Unknown(0) (UNK, FA)
- Los Angeles Chargers (DEF, LAC)
- Unknown(0) (UNK, FA)
- Nik Bonitto (LB, DEN)
- Unknown(0) (UNK, FA)
- Unknown(0) (UNK, FA)

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
- RB (10): Ashton Jeanty, Cam Skattebo, Chris Brooks, Chris Rodriguez, Damien Martinez, MarShawn Lloyd, Ray Davis, Seth McGowan, Tony Pollard, Tyrone Tracy
- TE (5): Colston Loveland, Marlin Klein, Oscar Delp, Theo Johnson, Tucker Kraft
- WR (9): Brandon Aiyuk, Caleb Douglas, Chris Bell, Christian Watson, Ja'Marr Chase, Jalen McMillan, Jordyn Tyson, Malik Nabers, Will Pauling

**Bench depth:**
- Brandon Aiyuk (WR, SF)
- Cade Klubnik (QB, NYJ) 🟡 ROOKIE
- Caleb Douglas (WR, MIA) 🟡 ROOKIE
- Cam Ward (QB, TEN)
- Chris Bell (WR, MIA) 🟡 ROOKIE
- Chris Brooks (RB, GB)
- Chris Rodriguez (RB, JAX)
- Cleveland Browns (DEF, CLE)
- Damien Martinez (RB, GB)
- Deshaun Watson (QB, CLE)
- Geno Smith (QB, NYJ)
- Jalen McMillan (WR, TB)
- MarShawn Lloyd (RB, GB)
- Marlin Klein (TE, HOU) 🟡 ROOKIE
- Ray Davis (RB, BUF)
- Talanoa Hufanga (DB, DEN)
- Theo Johnson (TE, NYG)
- Tony Pollard (RB, TEN)
- Tyrone Tracy (RB, NYG)
- Will Howard (QB, PIT)
- Will Pauling (WR, SF) 🟡 ROOKIE

**Taxi Squad:**
- Cole Payton (QB, PHI) 🟡 ROOKIE
- Oscar Delp (TE, NO) 🟡 ROOKIE
- Seth McGowan (RB, IND) 🟡 ROOKIE

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
- RB (8): Christian McCaffrey, D'Andre Swift, DJ Giddens, Isaac Guerendo, James Conner, Jonathan Taylor, Sean Tucker, Trey Benson
- TE (5): David Njoku, Hunter Henry, John Michael Gyllenborg, Mike Gesicki, Nate Boerkircher
- WR (11): A.J. Brown, Brenen Thompson, CJ Daniels, Courtland Sutton, Davante Adams, DeMario Douglas, Deion Burks, Jameson Williams, Kevin Coleman, Nico Collins, Tyquan Thornton

**Bench depth:**
- Arvell Reese (LB, NYG) 🟡 ROOKIE
- Courtland Sutton (WR, DEN)
- DJ Giddens (RB, IND)
- David Njoku (TE, LAC)
- DeMario Douglas (WR, NE)
- Deion Burks (WR, IND) 🟡 ROOKIE
- Garrett Nussmeier (QB, KC) 🟡 ROOKIE
- Isaac Guerendo (RB, SF)
- James Conner (RB, ARI)
- John Michael Gyllenborg (TE, KC) 🟡 ROOKIE
- Kevin Coleman (WR, MIA) 🟡 ROOKIE
- Micah Parsons (LB, GB)
- Mike Gesicki (TE, CIN)
- Sean Tucker (RB, TB)
- Trey Benson (RB, ARI)
- Tua Tagovailoa (QB, ATL)
- Tyquan Thornton (WR, KC)

**Taxi Squad:**
- Brenen Thompson (WR, LAC) 🟡 ROOKIE
- CJ Daniels (WR, LAR) 🟡 ROOKIE
- Nate Boerkircher (TE, JAX) 🟡 ROOKIE

### BedStuyBallers21 (Roster 12)

**Starters:**
- Baker Mayfield (QB, TB)
- Derrick Henry (RB, BAL)
- Rachaad White (RB, WAS)
- Zay Flowers (WR, BAL)
- Emeka Egbuka (WR, TB)
- Dalton Kincaid (TE, BUF)
- Mike Evans (WR, SF)
- Isaiah Likely (TE, NYG)
- Cooper Kupp (WR, SEA)
- Brandon Aubrey (K, DAL)
- Philadelphia Eagles (DEF, PHI)
- Abdul Carter (DL, NYG)
- Fred Warner (LB, SF)
- Budda Baker (DB, ARI)
- Jessie Bates (DB, ATL)

**QB Room (5 QBs):**
- Baker Mayfield (TB)
- Brock Purdy (SF)
- J.J. McCarthy (MIN)
- Jalen Milroe (SEA)
- Mac Jones (SF)

**Positional Surplus (3+ players at same position):**
- DEF (3): Minnesota Vikings, New York Giants, Philadelphia Eagles
- QB (5): Baker Mayfield, Brock Purdy, J.J. McCarthy, Jalen Milroe, Mac Jones
- RB (9): Adam Randall, Derrick Henry, Eli Heidenreich, Isaiah Davis, Justice Hill, Kimani Vidal, Rachaad White, Ty Johnson, Zach Charbonnet
- TE (4): Colby Parkinson, Dalton Kincaid, Isaiah Likely, Michael Trigg
- WR (11): Chimere Dike, Cooper Kupp, Darius Slayton, De'Zhaun Stribling, Emeka Egbuka, Jahan Dotson, Jakobi Meyers, Jauan Jennings, Mike Evans, Odell Beckham, Zay Flowers

**Bench depth:**
- Brock Purdy (QB, SF)
- Chimere Dike (WR, TEN)
- Colby Parkinson (TE, LAR)
- Darius Slayton (WR, NYG)
- De'Zhaun Stribling (WR, SF) 🟡 ROOKIE
- Isaiah Davis (RB, NYJ)
- J.J. McCarthy (QB, MIN)
- Jahan Dotson (WR, ATL)
- Jakobi Meyers (WR, JAX)
- Jalen Milroe (QB, SEA)
- Jauan Jennings (WR, MIN)
- Justice Hill (RB, BAL)
- Kimani Vidal (RB, LAC)
- Mac Jones (QB, SF)
- Minnesota Vikings (DEF, MIN)
- New York Giants (DEF, NYG)
- Odell Beckham (WR, NYG)
- Ty Johnson (RB, BUF)
- Zach Charbonnet (RB, SEA)

**Taxi Squad:**
- Adam Randall (RB, BAL) 🟡 ROOKIE
- Eli Heidenreich (RB, PIT) 🟡 ROOKIE
- Michael Trigg (TE, DAL) 🟡 ROOKIE

<!-- END_AUTO_GENERATED -->