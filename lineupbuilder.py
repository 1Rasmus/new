# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 18:24:29 2020

@author: Rasmus
"""

import pandas as pd
from random import randrange
from operator import itemgetter, attrgetter
import numpy as np



target = 500
maxbudget =75
minbudget= 74.6

# import Ecxelfile with players
df = pd.read_excel (r'Playerlist.xlsx')

# create additional columns
df['rand'] = ''
df['id'] = ''
#df['used'] = 0



# datframe to python list
playerlist = df.values.tolist()

# add id to playerlist
for i in range(len(playerlist)):
    playerlist[i][5] = (randrange(1000))


# create roster list
rosterlist = [['spieler1','spieler2','spieler3','spieler4','spieler5','spieler6','spieler7', 'Salary', 'Proj. Points'], ['','','','','','','','', '']]


######################
###################### LineupBuilder

lineupcount = 0
failcount = 0

# MainLoop
while lineupcount < target+1 and failcount <= 100000:
    
    picked_player =0
    
        # randomize playerlist
    for i in range(len(playerlist)):
        
        playerlist[i][6] = (randrange(100))
    
    playerlist = sorted (playerlist, key = itemgetter(3), reverse=True)
    playerlist[0][6] +=500
    playerlist = sorted (playerlist, key = itemgetter(6), reverse=True)
    
    
    
            #first player PG
        
    for i in range(len(playerlist)):
            
            if playerlist[i][2] == 'Point Guard' and playerlist[i][3] > 0:
                rosterlist[lineupcount][0] = playerlist[i][0]
                picked_player +=1
                temp1 =i
                team_cost = playerlist[i][1]
                team_proj = playerlist[i][4]
                break
        
        #second player SG
    
    for i in range(len(playerlist)):
            
            if playerlist[i][2] == 'Shooting Guard' and playerlist[i][3] > 0:
                rosterlist[lineupcount][1] = playerlist[i][0]
                picked_player +=1
                temp2=i
                team_cost = team_cost + playerlist[i][1]
                team_proj = team_proj + playerlist[i][4]
                break
            
        #third player SF
    
    for i in range(len(playerlist)):
            
            if playerlist[i][2] == 'Small Forward' and playerlist[i][3] > 0:
                rosterlist[lineupcount][2] = playerlist[i][0]
                picked_player +=1
                temp3=i
                team_cost = team_cost + playerlist[i][1]
                team_proj = team_proj + playerlist[i][4]
                break
    
        #fourth player PF
    
    for i in range(len(playerlist)):
            
            if playerlist[i][2] == 'Power Forward' and playerlist[i][3] > 0:
                rosterlist[lineupcount][3] = playerlist[i][0]
                picked_player +=1
                temp4=i
                team_cost = team_cost + playerlist[i][1]
                team_proj = team_proj + playerlist[i][4]
                break
            
        #fifth player Center
    
    for i in range(len(playerlist)):
            
            if playerlist[i][2] == 'Center' and playerlist[i][3] > 0:
                rosterlist[lineupcount][4] = playerlist[i][0]
                picked_player +=1
                temp5=i
                team_cost = team_cost + playerlist[i][1]
                team_proj = team_proj + playerlist[i][4]
                break
            
        #sixt player Utility
    
    for i in range(len(playerlist)):
            
            if playerlist[i][0] != rosterlist[lineupcount][0] and playerlist[i][0] != rosterlist[lineupcount][1] and playerlist[i][0] != rosterlist[lineupcount][2] and playerlist[i][0] != rosterlist[lineupcount][3] and playerlist[i][0] != rosterlist[lineupcount][4] and playerlist[i][3] > 0:
                rosterlist[lineupcount][5] = playerlist[i][0]
                picked_player +=1
                temp6=i
                team_cost = team_cost + playerlist[i][1]
                team_proj = team_proj + playerlist[i][4]
                break
    
        #seventh player Utility
    
    for i in range(len(playerlist)):
            
            if playerlist[i][0] != rosterlist[lineupcount][0] and playerlist[i][0] != rosterlist[lineupcount][1] and playerlist[i][0] != rosterlist[lineupcount][2] and playerlist[i][0] != rosterlist[lineupcount][3] and playerlist[i][0] != rosterlist[lineupcount][4] and playerlist[i][0] != rosterlist[lineupcount][5] and (team_cost + playerlist[i][1]) <= maxbudget and (team_cost + playerlist[i][1]) >= minbudget and playerlist[i][3] > 0:
                rosterlist[lineupcount][6] = playerlist[i][0]
                picked_player +=1
                temp7=i
                team_cost = team_cost + playerlist[i][1]
                rosterlist[lineupcount][7] = team_cost
                team_proj = team_proj + playerlist[i][4]
                rosterlist[lineupcount][8] = team_proj
                break
    
    # update Playerlist
    if picked_player ==7:

        
        playerlist[temp1][3] -=1
        playerlist[temp2][3] -=1
        playerlist[temp3][3] -=1
        playerlist[temp4][3] -=1
        playerlist[temp5][3] -=1
        playerlist[temp6][3] -=1
        playerlist[temp7][3] -=1
        
        lineupcount +=1
        rosterlist.append (['','','','','','','','',''])
    else:
        failcount +=1
        

  #### Print Playerlist
playerlist = sorted (playerlist, key = itemgetter(1), reverse=True)
playerlist = pd.DataFrame(playerlist)
playerlist.columns=['Player', 'Cost', 'Position', 'NotUsed', 'Projected', 'PlayerID', 'Rnd']
print (playerlist.to_string())


 #### Print completed Lineups 
rosterlist = pd.DataFrame(rosterlist)
rosterlist[8] = pd.to_numeric(rosterlist[8], errors='coerce')
rosterlist = rosterlist[np.isfinite(rosterlist[8])]
rosterlist = rosterlist.sort_values(by=[8], ascending=False)
rosterlist.columns=['Player1', 'Player2', 'Player3', 'Player4', 'Player5', 'Player6', 'Player7', 'TeamCost', 'Proj.Points']
print(rosterlist.head(25).to_string())

   
print ("Lineups erstellt: ", lineupcount-1)





