# NBA_Player_Clustering

NBA positions have been changing quite a bit over the past decade. Teams rarely start a traditional starting five of point guard, shooting guard, small forward, power forward, and center anymore. Often times we will see an additional guard/forward replace the power forward or center to sacrifice rebounding for an increased ability to switch on defense. With that in mind, I aimed to see if I could use a machine learning model to identify the new positions of the modern NBA. Below is a quick summary of the process I followed to perform this analysis (the full code can be found in repo’s Jupyter notebook): 
  •	Download data for NBA player per game stats and advanced stats for the 2022-2023 NBA season
  •	Combine the separate per game and advanced stats into one dataframe for Python
  •	Remove any extraneous columns and clean up data
  •	Reduce the dimensionality of the data from around 30 inputs to 3 using principal component analysis (PCA)
  •	Fit a K-Means Clustering machine learning algorithm on the dimensionally reduced data to obtain the groupings representing modern NBA     positions
  •	Manually analyze the groupings to come up with names for each position

The above analysis resulted in 8 positions that are found in the modern NBA:
  •	Volume combo guard
  •	Two-way big 
  •	3&D specialists
  •	Scoring playmaker
  •	3-point specialists
  •	Rebounding big 
  •	Volume scorer
  •	Two-way superstars

We’ll now dive into some trends observed and notable players for each position. Note that all statistics referenced below are an average for each position.

Position #1: Volume Combo Guard
The volume combo guard position consists of mainly point guards and shooting guards with the occasional forward mixed in. It is characterized by inefficient shooting (40.8 FG%, 31.9 3PT%) and near similar assist and turnover rates (18.4% assist rate, 14.3% turnover rate). They are also generally poor defenders (-0.66 defensive box plus-minus). When hot, the volume combo guard can be a useful contributor because of their ability to get shots up (8.2 FGA). However, given their overall inconsistencies offensively and poor defensive ability, NBA teams should not have more than 1-2 of these players on the roster. 
Notable Players:
  •	Dillon Brooks
  •	Lu Dort (was one of the stronger defensive players in this position)
  •	Jaden Ivey
  •	Dennis Schröder
  •	Gabe Vincent

Position #2: Two-way Big
The two-way big man position is a small group with only 18 players. They are characterized by generally combining solid offensive (14.7 PPG, 0.55 offensive box plus-minus) and defensive (1.9 steals + blocks, 0.77 defensive box plus-minus) abilities. While they may not be elite offensively or defensively, the ability to perform both at a high level is very valuable from the big man. From observing some of the names in this list play, they are also able to switch in the pick and roll which can really disrupt the opposing team’s offense. Finding a good two-way big man should be near the top of every NBA team’s shopping list.
Notable Players:
  •	Aaron Gordon
  •	Evan Mobley
  •	Jaren Jackson Jr.
  •	Myles Turner
  •	Ben Simmons (was a bit of an outlier in this position, despite his defense being outstanding his poor offensive game makes him            unplayable)

Position #3: 3&D Specialist
The 3&D specialist is characterized by players who, as the name suggests, are good at 3-point shooting (35.0 3PT%) and defense (0.42 defensive box plus-minus) but not much else (1.8 APG, 1.82 FTA). Even though they may be limited outside of three pointers and defense, those two skill sets are extremely valuable in the NBA. Additionally, these players do not require the ball in their hands to be successful which allows the star playmakers/scorers to control the ball on offense.
Notable Players:
  •	Alex Caruso
  •	Torrey Craig
  •	Caleb Martin
  •	Bruce Brown
  •	Al Horford (it is strange to see big men classified as 3&D but Horford was a 45% three-point shooter this season and recorded a 1.7       defensive box plus-minus)

Position #4: Scoring Playmaker
