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
Last synced: 2026-06-06 12:46 PM PT

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
4070
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
4968
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
5580
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
7600
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
8116
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
11834
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
13600
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
WAS
```

## My Roster — Scvazquez (Roster 9)

### Starting Lineup

| Slot | Player | Pos | Team | Age |
|------|--------|-----|------|-----|
| QB | Jayden Daniels | QB | WAS | 25 |
| RB | Saquon Barkley | RB | PHI | 29 |
| RB | David Montgomery | RB | HOU | 28 |
| WR | CeeDee Lamb | WR | DAL | 27 |
| WR | Justin Jefferson | WR | MIN | 26 |
| TE | Kyle Pitts | TE | ATL | 25 |
| FLEX | Ladd McConkey | WR | LAC | 24 |
| FLEX | Terry McLaurin | WR | WAS | 30 |
| FLEX | Rico Dowdle | RB | PIT | 27 |
| K | Ben Sauls | K | NYG | 24 |
| DEF | Detroit Lions | DEF | DET | ? |
| LB | Edgerrin Cooper | LB | GB | 24 |
| LB | Quay Walker | LB | LV | 26 |
| DB | Kyle Hamilton | DB | BAL | 25 |
| DB | Derwin James | DB | LAC | 29 |

### Bench

- Tre' Harris (WR, LAC, Age 24, 1 yr exp)
- Donovan Edwards (RB, MIA, Age 23, 1 yr exp)
- Elijah Arroyo (TE, SEA, Age 23, 1 yr exp)
- Jimmy Horn (WR, CAR, Age 23, 1 yr exp)
- Jaylin Noel (WR, HOU, Age 23, 1 yr exp)
- Arian Smith (WR, NYJ, Age 24, 1 yr exp)
- Tahj Brooks (RB, CIN, Age 24, 1 yr exp)
- LeQuint Allen (RB, JAX, Age 21, 1 yr exp)
- Alvin Kamara (RB, NO, Age 30, 9 yr exp)
- Mark Andrews (TE, BAL, Age 30, 8 yr exp)
- Zack Baun (LB, PHI, Age 29, 6 yr exp)
- Najee Harris (RB, FA, Age 27, 5 yr exp)
- Justin Fields (QB, KC, Age 27, 5 yr exp)
- Pierre Strong (RB, GB, Age 27, 4 yr exp)
- Greg Dulcich (TE, MIA, Age 26, 4 yr exp)
- Jordan Addison (WR, MIN, Age 24, 3 yr exp)

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
- 0 (UNK, FA)
- Atlanta Falcons (DEF, ATL)
- 0 (UNK, FA)
- 0 (UNK, FA)
- 0 (UNK, FA)
- 0 (UNK, FA)

**QB Room (3 QBs):**
- Joe Burrow (CIN)
- Shedeur Sanders (CLE)
- Jordan Love (GB)

**Positional Surplus (3+ players at same position):**
- QB (3): Joe Burrow, Shedeur Sanders, Jordan Love
- RB (8): Kalel Mullings, J'Mari Taylor, Jahmyr Gibbs, Jaydon Blue, Ollie Gordon, TreVeyon Henderson, Robert Henry, Bucky Irving
- TE (3): AJ Barner, George Kittle, Jake Tonges
- WR (19): Ted Hurst, Malik Benson, Ryan Flournoy, Skyler Bell, Keon Coleman, Zavion Thomas, Christian Kirk, Tory Horton, Darnell Mooney, DeVonta Smith, DJ Moore, Jaylin Lane, Chris Brazzell, Puka Nacua, Savion Williams, Tyreek Hill, Michael Wilson, Isaac TeSlaa, Jayden Reed

**Bench depth:**
- Malik Benson (WR, LV) 🟡 ROOKIE
- Ryan Flournoy (WR, DAL)
- Skyler Bell (WR, BUF) 🟡 ROOKIE
- Kalel Mullings (RB, TEN)
- Keon Coleman (WR, BUF)
- AJ Barner (TE, SEA)
- Zavion Thomas (WR, CHI) 🟡 ROOKIE
- Christian Kirk (WR, SF)
- Tory Horton (WR, SEA)
- Darnell Mooney (WR, NYG)
- Jaydon Blue (RB, DAL)
- Ollie Gordon (RB, MIA)
- Jaylin Lane (WR, WAS)
- Chris Brazzell (WR, CAR) 🟡 ROOKIE
- Savion Williams (WR, GB)
- Tyreek Hill (WR, FA)
- Shedeur Sanders (QB, CLE)
- Jordan Love (QB, GB)
- Isaac TeSlaa (WR, DET)
- Jayden Reed (WR, GB)
- Jake Tonges (TE, SF)

**Taxi Squad:**
- Ted Hurst (WR, TB) 🟡 ROOKIE
- J'Mari Taylor (RB, JAX) 🟡 ROOKIE
- Robert Henry (RB, WAS) 🟡 ROOKIE

### JQuinna10 (Roster 2)

**Starters:**
- Drake Maye (QB, NE)
- Kenneth Walker (RB, KC)
- Jeremiyah Love (RB, ARI)
- Tetairoa McMillan (WR, CAR)
- Luther Burden (WR, CHI)
- T.J. Hockenson (TE, MIN)
- Marvin Harrison (WR, ARI)
- Rhamondre Stevenson (RB, NE)
- Romeo Doubs (WR, NE)
- Cam Little (K, JAX)
- Houston Texans (DEF, HOU)
- Carson Schwesinger (LB, CLE)
- 0 (UNK, FA)
- Travis Hunter (WR, JAX)
- 0 (UNK, FA)

**QB Room (5 QBs):**
- Drake Maye (NE)
- Mac Jones (SF)
- Jacoby Brissett (ARI)
- Brock Purdy (SF)
- Carson Beck (ARI)

**Positional Surplus (3+ players at same position):**
- QB (5): Drake Maye, Mac Jones, Jacoby Brissett, Brock Purdy, Carson Beck
- RB (10): Zach Charbonnet, Jarquez Hunter, Nicholas Singleton, Rhamondre Stevenson, Emmett Johnson, Kenneth Walker, Jeremiyah Love, Jam Miller, Tyler Allgeier, Blake Corum
- TE (4): Pat Freiermuth, Dallas Goedert, T.J. Hockenson, Eli Raridon
- WR (11): Jalen Royals, Jayden Higgins, Xavier Legette, Romeo Doubs, Kyle Williams, Tetairoa McMillan, Pat Bryant, Marvin Harrison, Travis Hunter, Dontayvion Wicks, Luther Burden

**Bench depth:**
- Jalen Royals (WR, KC)
- Mac Jones (QB, SF)
- Zach Charbonnet (RB, SEA)
- Jacoby Brissett (QB, ARI)
- Jarquez Hunter (RB, LAR)
- Nicholas Singleton (RB, TEN) 🟡 ROOKIE
- Jayden Higgins (WR, HOU)
- Xavier Legette (WR, CAR)
- Pat Freiermuth (TE, PIT)
- Kyle Williams (WR, NE)
- Emmett Johnson (RB, KC) 🟡 ROOKIE
- Pat Bryant (WR, DEN)
- Brock Purdy (QB, SF)
- Dallas Goedert (TE, PHI)
- Tyler Allgeier (RB, ARI)
- Blake Corum (RB, LAR)
- Dontayvion Wicks (WR, PHI)
- New England Patriots (DEF, NE)

**Taxi Squad:**
- Carson Beck (QB, ARI) 🟡 ROOKIE
- Jam Miller (RB, NE) 🟡 ROOKIE
- Eli Raridon (TE, NE) 🟡 ROOKIE

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
- 0 (UNK, FA)
- New Orleans Saints (DEF, NO)
- Jordyn Brooks (LB, MIA)
- Sonny Styles (LB, WAS)
- Nick Cross (DB, WAS)
- Dillon Thieneman (DB, CHI)

**QB Room (2 QBs):**
- Jaxson Dart (NYG)
- Jared Goff (DET)

**Positional Surplus (3+ players at same position):**
- LB (4): Jihaad Campbell, Sonny Styles, Zaire Franklin, Jordyn Brooks
- RB (5): Woody Marks, Bhayshul Tuten, Kyle Monangai, James Cook, Tyjae Spears
- WR (9): Rome Odunze, Brian Thomas, Ricky Pearsall, Matthew Golden, Carnell Tate, Ja'Kobi Lane, Antonio Williams, Kayshon Boutte, Quentin Johnston

**Bench depth:**
- Woody Marks (RB, HOU)
- Matthew Golden (WR, GB)
- Jihaad Campbell (LB, PHI)
- Andy Borregales (K, NE)
- Ja'Kobi Lane (WR, BAL) 🟡 ROOKIE
- Antonio Williams (WR, WAS) 🟡 ROOKIE
- Travis Kelce (TE, KC)
- Jared Goff (QB, DET)
- Zaire Franklin (LB, GB)
- Kayvon Thibodeaux (DL, NYG)
- Kayshon Boutte (WR, NE)
- Tyjae Spears (RB, TEN)
- Quentin Johnston (WR, LAC)

### Bombas (Roster 4)

**Starters:**
- Trevor Lawrence (QB, JAX)
- RJ Harvey (RB, DEN)
- Jadarian Price (RB, SEA)
- KC Concepcion (WR, CLE)
- Omar Cooper (WR, NYJ)
- Kenyon Sadiq (TE, NYJ)
- Denzel Boston (WR, CLE)
- Eli Stowers (TE, PHI)
- Oronde Gadsden (TE, LAC)
- 0 (UNK, FA)
- 0 (UNK, FA)
- 0 (UNK, FA)
- 0 (UNK, FA)
- 0 (UNK, FA)
- 0 (UNK, FA)

**QB Room (4 QBs):**
- Malik Willis (MIA)
- Fernando Mendoza (LV)
- Michael Penix (ATL)
- Trevor Lawrence (JAX)

**Positional Surplus (3+ players at same position):**
- QB (4): Malik Willis, Fernando Mendoza, Michael Penix, Trevor Lawrence
- RB (10): Joe Mixon, Tank Bigsby, Dylan Sampson, Kaytron Allen, Jadarian Price, RJ Harvey, Kaleb Johnson, Braelon Allen, Brashard Smith, Demond Claiborne
- TE (6): Sam Roush, Will Kacmarek, Darnell Washington, Kenyon Sadiq, Eli Stowers, Oronde Gadsden
- WR (13): KC Concepcion, Denzel Boston, Germie Bernard, Adonai Mitchell, Colbie Young, Rashod Bateman, Omar Cooper, Jack Bech, Troy Franklin, Marvin Mims, Malachi Fields, Tre Tucker, Calvin Ridley

**Bench depth:**
- Sam Roush (TE, CHI) 🟡 ROOKIE
- Germie Bernard (WR, PIT) 🟡 ROOKIE
- Adonai Mitchell (WR, NYJ)
- Malik Willis (QB, MIA)
- Joe Mixon (RB, FA)
- Tank Bigsby (RB, PHI)
- Rashod Bateman (WR, BAL)
- Dylan Sampson (RB, CLE)
- Kaytron Allen (RB, WAS) 🟡 ROOKIE
- Fernando Mendoza (QB, LV) 🟡 ROOKIE
- Jack Bech (WR, LV)
- Troy Franklin (WR, DEN)
- Michael Penix (QB, ATL)
- Marvin Mims (WR, DEN)
- Malachi Fields (WR, NYG) 🟡 ROOKIE
- Tre Tucker (WR, LV)
- Darnell Washington (TE, PIT)
- Calvin Ridley (WR, TEN)
- Kaleb Johnson (RB, PIT)
- Braelon Allen (RB, NYJ)
- Brashard Smith (RB, KC)

**Taxi Squad:**
- Demond Claiborne (RB, MIN) 🟡 ROOKIE
- Will Kacmarek (TE, MIA) 🟡 ROOKIE
- Colbie Young (WR, CIN) 🟡 ROOKIE

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

**QB Room (6 QBs):**
- Taylen Green (CLE)
- Ty Simpson (LAR)
- Anthony Richardson (IND)
- Lamar Jackson (BAL)
- Matthew Stafford (LAR)
- Dak Prescott (DAL)

**Positional Surplus (3+ players at same position):**
- QB (6): Taylen Green, Ty Simpson, Anthony Richardson, Lamar Jackson, Matthew Stafford, Dak Prescott
- RB (8): Javonte Williams, Chuba Hubbard, Jonah Coleman, Jonathon Brooks, Kaelon Black, Keaton Mitchell, Brian Robinson, Omarion Hampton
- TE (4): Dalton Schultz, Chig Okonkwo, Michael Mayer, Terrance Ferguson
- WR (9): Makai Lemon, Wan'Dale Robinson, Jalen Coker, Rashee Rice, Jeff Caldwell, Alec Pierce, Elijah Sarratt, Jaxon Smith-Njigba, Parker Washington

**Bench depth:**
- Makai Lemon (WR, PHI) 🟡 ROOKIE
- Chig Okonkwo (TE, WAS)
- Michael Mayer (TE, LV)
- Jonah Coleman (RB, DEN) 🟡 ROOKIE
- Wan'Dale Robinson (WR, TEN)
- Jalen Coker (WR, CAR)
- Jonathon Brooks (RB, CAR)
- Anthony Richardson (QB, IND)
- Jacksonville Jaguars (DEF, JAX)
- Kaelon Black (RB, SF) 🟡 ROOKIE
- Keaton Mitchell (RB, LAC)
- Terrance Ferguson (TE, LAR)
- Lamar Jackson (QB, BAL)
- Brian Robinson (RB, ATL)
- Elijah Sarratt (WR, BAL) 🟡 ROOKIE
- Matthew Stafford (QB, LAR)

**Taxi Squad:**
- Ty Simpson (QB, LAR) 🟡 ROOKIE
- Taylen Green (QB, CLE) 🟡 ROOKIE
- Jeff Caldwell (WR, KC) 🟡 ROOKIE

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
- Josh Allen (BUF)
- Jalen Hurts (PHI)

**Positional Surplus (3+ players at same position):**
- DB (4): Jermod McCoy, Jaquan Brisker, Avieon Terrell, Genesis Smith
- LB (12): Nick Bolton, Terrel Bernard, Ernest Jones, Payton Wilson, Robert Spillane, Dee Winters, Foyesade Oluokun, Tyrel Dodson, Bobby Wagner, Bobby Okereke, David Bailey, Devin White
- RB (3): Josh Jacobs, Bijan Robinson, Jacory Croskey-Merritt
- WR (7): DK Metcalf, Michael Pittman, Josh Downs, Stefon Diggs, Tee Higgins, Chris Godwin, Jaylen Waddle

**Bench depth:**
- Juwan Johnson (TE, NO)
- Michael Pittman (WR, PIT)
- Nick Bolton (LB, KC)
- Terrel Bernard (LB, BUF)
- Ernest Jones (LB, SEA)
- Payton Wilson (LB, PIT)
- Josh Downs (WR, IND)
- Robert Spillane (LB, NE)
- Stefon Diggs (WR, FA)
- Dee Winters (LB, DAL)
- Jaquan Brisker (DB, PIT)
- Tyrel Dodson (LB, MIA)
- Bobby Wagner (LB, FA)
- Bobby Okereke (LB, FA)
- Genesis Smith (DB, LAC) 🟡 ROOKIE
- Yaya Diaby (DL, TB)
- David Bailey (LB, NYJ) 🟡 ROOKIE
- Jalen Hurts (QB, PHI)
- Devin White (LB, FA)

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
- 0 (UNK, FA)

**QB Room (4 QBs):**
- Drew Allar (PIT)
- Caleb Williams (CHI)
- Tyler Shough (NO)
- Sam Darnold (SEA)

**Positional Surplus (3+ players at same position):**
- QB (4): Drew Allar, Caleb Williams, Tyler Shough, Sam Darnold
- RB (10): J.K. Dobbins, Jaylen Wright, Emanuel Wilson, Jordan James, Chase Brown, Jaylen Warren, Travis Etienne, Kenneth Gainwell, De'Von Achane, Jordan Mason
- TE (6): Matt Hibner, Max Klare, Gunnar Helm, Tyler Warren, Justin Joly, Cade Otton
- WR (8): Amon-Ra St. Brown, Bryce Lance, Drake London, Rashid Shaheed, George Pickens, Malik Washington, Khalil Shakir, Tyren Montgomery

**Bench depth:**
- J.K. Dobbins (RB, DEN)
- Matt Hibner (TE, BAL) 🟡 ROOKIE
- Jaylen Wright (RB, MIA)
- Emanuel Wilson (RB, SEA)
- Jordan James (RB, SF)
- Gunnar Helm (TE, TEN)
- Kenneth Gainwell (RB, TB)
- Bryce Lance (WR, NO) 🟡 ROOKIE
- Rashid Shaheed (WR, SEA)
- Jordan Mason (RB, MIN)
- Tyler Shough (QB, NO)
- Pittsburgh Steelers (DEF, PIT)
- Cade Otton (TE, TB)
- Sam Darnold (QB, SEA)
- Malik Washington (WR, MIA)
- Khalil Shakir (WR, BUF)
- Tyren Montgomery (WR, TEN) 🟡 ROOKIE

**Taxi Squad:**
- Max Klare (TE, LAR) 🟡 ROOKIE
- Drew Allar (QB, PIT) 🟡 ROOKIE
- Justin Joly (TE, DEN) 🟡 ROOKIE

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
- Washington Commanders (DEF, WAS)
- Frankie Luvu (LB, WAS)
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
- LB (3): Devin Bush, Frankie Luvu, SirVocea Dennis
- QB (7): C.J. Stroud, Bo Nix, Bryce Young, Aaron Rodgers, Patrick Mahomes, Kirk Cousins, Daniel Jones
- RB (7): Breece Hall, Mike Washington, Kyren Williams, Aaron Jones, Quinshon Judkins, Devin Neal, Isiah Pacheco
- TE (5): Harold Fannin, Mason Taylor, Brenton Strange, Sam LaPorta, Jake Ferguson
- WR (9): Tank Dell, Chris Olave, Zachariah Branch, Elic Ayomanor, Xavier Worthy, Garrett Wilson, Deebo Samuel, Jalen Nailor, Jerry Jeudy

**Bench depth:**
- Devin Bush (LB, CHI)
- Tank Dell (WR, HOU)
- C.J. Stroud (QB, HOU)
- Mason Taylor (TE, NYJ)
- Aaron Jones (RB, MIN)
- Bo Nix (QB, DEN)
- Elic Ayomanor (WR, TEN)
- Xavier Worthy (WR, KC)
- Devin Neal (RB, NO)
- Bryce Young (QB, CAR)
- Deebo Samuel (WR, FA)
- Aaron Rodgers (QB, PIT)
- Jalen Nailor (WR, LV)
- Jake Ferguson (TE, DAL)
- Kirk Cousins (QB, LV)
- Isiah Pacheco (RB, DET)
- Daniel Jones (QB, IND)
- Jerry Jeudy (WR, CLE)

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
- 0 (UNK, FA)
- Los Angeles Chargers (DEF, LAC)
- 0 (UNK, FA)
- Nik Bonitto (LB, DEN)
- 0 (UNK, FA)
- 0 (UNK, FA)

**QB Room (7 QBs):**
- Kyler Murray (MIN)
- Deshaun Watson (CLE)
- Cade Klubnik (NYJ)
- Will Howard (PIT)
- Cam Ward (TEN)
- Cole Payton (PHI)
- Geno Smith (NYJ)

**Positional Surplus (3+ players at same position):**
- QB (7): Kyler Murray, Deshaun Watson, Cade Klubnik, Will Howard, Cam Ward, Cole Payton, Geno Smith
- RB (10): Ray Davis, Cam Skattebo, MarShawn Lloyd, Damien Martinez, Tyrone Tracy, Chris Rodriguez, Ashton Jeanty, Tony Pollard, Seth McGowan, Chris Brooks
- TE (5): Oscar Delp, Marlin Klein, Theo Johnson, Tucker Kraft, Colston Loveland
- WR (9): Brandon Aiyuk, Jordyn Tyson, Will Pauling, Malik Nabers, Chris Bell, Caleb Douglas, Christian Watson, Jalen McMillan, Ja'Marr Chase

**Bench depth:**
- Ray Davis (RB, BUF)
- Deshaun Watson (QB, CLE)
- Brandon Aiyuk (WR, SF)
- Talanoa Hufanga (DB, DEN)
- Cade Klubnik (QB, NYJ) 🟡 ROOKIE
- MarShawn Lloyd (RB, GB)
- Damien Martinez (RB, GB)
- Will Pauling (WR, SF) 🟡 ROOKIE
- Will Howard (QB, PIT)
- Tyrone Tracy (RB, NYG)
- Chris Rodriguez (RB, JAX)
- Tony Pollard (RB, TEN)
- Marlin Klein (TE, HOU) 🟡 ROOKIE
- Cleveland Browns (DEF, CLE)
- Cam Ward (QB, TEN)
- Chris Bell (WR, MIA) 🟡 ROOKIE
- Theo Johnson (TE, NYG)
- Caleb Douglas (WR, MIA) 🟡 ROOKIE
- Jalen McMillan (WR, TB)
- Geno Smith (QB, NYJ)
- Chris Brooks (RB, GB)

**Taxi Squad:**
- Oscar Delp (TE, NO) 🟡 ROOKIE
- Cole Payton (QB, PHI) 🟡 ROOKIE
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
- LB (4): Jack Campbell, Micah Parsons, Roquan Smith, Arvell Reese
- QB (3): Garrett Nussmeier, Justin Herbert, Tua Tagovailoa
- RB (8): Jonathan Taylor, DJ Giddens, Christian McCaffrey, Isaac Guerendo, Sean Tucker, James Conner, Trey Benson, D'Andre Swift
- TE (5): David Njoku, Mike Gesicki, Hunter Henry, Nate Boerkircher, John Michael Gyllenborg
- WR (11): Tyquan Thornton, Deion Burks, Kevin Coleman, Courtland Sutton, Jameson Williams, A.J. Brown, Nico Collins, Davante Adams, DeMario Douglas, Brenen Thompson, CJ Daniels

**Bench depth:**
- Tyquan Thornton (WR, KC)
- Deion Burks (WR, IND) 🟡 ROOKIE
- David Njoku (TE, LAC)
- Kevin Coleman (WR, MIA) 🟡 ROOKIE
- Courtland Sutton (WR, DEN)
- DJ Giddens (RB, IND)
- Garrett Nussmeier (QB, KC) 🟡 ROOKIE
- Micah Parsons (LB, GB)
- Arvell Reese (LB, NYG) 🟡 ROOKIE
- Mike Gesicki (TE, CIN)
- Isaac Guerendo (RB, SF)
- Sean Tucker (RB, TB)
- James Conner (RB, ARI)
- DeMario Douglas (WR, NE)
- Trey Benson (RB, ARI)
- John Michael Gyllenborg (TE, KC) 🟡 ROOKIE
- Tua Tagovailoa (QB, ATL)

**Taxi Squad:**
- CJ Daniels (WR, LAR) 🟡 ROOKIE
- Nate Boerkircher (TE, JAX) 🟡 ROOKIE
- Brenen Thompson (WR, LAC) 🟡 ROOKIE

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

**QB Room (2 QBs):**
- J.J. McCarthy (MIN)
- Baker Mayfield (TB)

**Positional Surplus (3+ players at same position):**
- DEF (3): Minnesota Vikings, New York Giants, Philadelphia Eagles
- LB (3): Tremaine Edmunds, Fred Warner, T.J. Watt
- RB (7): Ty Johnson, Derrick Henry, Eli Heidenreich, Kimani Vidal, Rachaad White, Justice Hill, Adam Randall
- TE (4): Colby Parkinson, Dalton Kincaid, Michael Trigg, Isaiah Likely
- WR (11): Darius Slayton, Devaughn Vele, Zay Flowers, Odell Beckham, Cooper Kupp, Chimere Dike, De'Zhaun Stribling, Mike Evans, Emeka Egbuka, Jakobi Meyers, Jauan Jennings

**Bench depth:**
- Colby Parkinson (TE, LAR)
- Minnesota Vikings (DEF, MIN)
- Darius Slayton (WR, NYG)
- Devaughn Vele (WR, NO)
- Tremaine Edmunds (LB, NYG)
- Ty Johnson (RB, BUF)
- New York Giants (DEF, NYG)
- Odell Beckham (WR, NYG)
- J.J. McCarthy (QB, MIN)
- Chimere Dike (WR, TEN)
- De'Zhaun Stribling (WR, SF) 🟡 ROOKIE
- T.J. Watt (LB, PIT)
- Jakobi Meyers (WR, JAX)
- Kimani Vidal (RB, LAC)
- Jauan Jennings (WR, MIN)
- Justice Hill (RB, BAL)

**Taxi Squad:**
- Adam Randall (RB, BAL) 🟡 ROOKIE
- Michael Trigg (TE, DAL) 🟡 ROOKIE
- Eli Heidenreich (RB, PIT) 🟡 ROOKIE

<!-- END_AUTO_GENERATED -->