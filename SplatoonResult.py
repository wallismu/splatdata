import json
import sys
import csv

class splatoonResult:
    def __init__(self, x):
        with open('weapons.json') as g:
            y = json.load(g)
        self.data = x['results']
        self.weaponData = y

    def __str__(self):
       return self.data

    def getAllBattleNumbers(self):
        battleNumbers = []
        for x in self.data:
            battleNumbers.append(x['battle_number'])

        return battleNumbers

    def getFirstBattleNumber(self):
        return int(self.getAllBattleNumbers()[0])

    def getLastBattleNumber(self):
        return int(self.getAllBattleNumbers()[-1])

    def getSingleMatchInfo(self, battle):
        row = []
        row.append(battle['battle_number']) # Unique battle #
        row.append(battle['start_time']) # Start time + date
        if "elapsed_time" in battle.keys():      # If turf war, 180 seconds. otherwise store
            row.append(battle['elapsed_time'])
        else:
            row.append(180)

        row.append(battle['my_team_result']['key']) # Win or lose (victory or defeat)
        row.append(battle['game_mode']['key']) # Game mode (regular, gachi, league) (specifies which kind of league)
        row.append(battle['type']) # Game type (regular, gachi, league)
        row.append(battle['rule']['key']) # game rule (splat zones, clam blitz, etc)
        row.append(battle['stage']['name'].lower() )# stage/map
        row.append(battle['player_result']['assist_count']) # assisted kills
        row.append(battle['player_result']['kill_count']) # total kills
        row.append(battle['player_result']['special_count']) # total specials
        row.append(battle['player_result']['death_count']) # death_count
        
        weapon = (battle['player_result']['player']['weapon']['name'].lower()) # weapon name
        row.append(weapon)

        row.append(self.weaponData[self.convertWeaponName(weapon)]['type_key']) # weapon type (pulled from JSON)
        
        row.append(battle['player_result']['player']['weapon']['sub']['name'].lower()) # sub 
        row.append(battle['player_result']['player']['weapon']['special']['name'].lower()) # special

        return row

    def generateCSV(self):
        filename = "master.csv"

        with open(filename, 'r') as f:
            lines = f.read().splitlines()
            lastLine = lines[-1]

        lastBattleCaptured = int(lastLine.split(',')[0])
        
        rows = []

        for x in range(len(self.data)-1, -1, -1):
            if int(self.data[x]['battle_number']) > lastBattleCaptured:
                rows.append(self.getSingleMatchInfo(self.data[x]))  
                #print(self.data)

        with open(filename, 'a+') as csvfile:    
            csvwriter = csv.writer(csvfile)  
            csvwriter.writerows(rows) 

        return len(rows)
        

    def convertWeaponName(self, name):
        name = name.replace("-","_")
        name = name.replace(" ","_")
        return name.lower()

# if __name__ == "__main__":
#     with open('results2.json') as g:
#         y = json.load(g)
#     sp = splatoonResult(y)
#     #print(sp.getMinMaxBattleNumbers())
#     sp.generateCSV()
