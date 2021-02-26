import pandas as pd

def data():
	pidf = pd.read_csv("nhl-game-data/player_info.csv")
	pidf["name"] = pidf["firstName"]+" "+pidf["lastName"]
	return pidf

sdf = pd.read_csv("nhl-game-data/game_skater_stats.csv")
sdf["season"] = sdf["game_id"].astype(str).str.slice(stop=4)

def goalsperseason(playerid): 
	''' takes playerid. returns dictionary. keys are seasons. values are goals.
	'''
	tmp = sdf.loc[sdf.player_id==playerid]
	ret = tmp[["goals","season"]].groupby(['season']).sum()
	return ret.to_dict()["goals"]

def pointsperseason(playerid):
	''' takes playerid. returns dictionary. keys are seasons. values are goals.
	'''
	tmp = sdf.loc[sdf.player_id==playerid]
	tmp["points"] = tmp["goals"]+tmp["assists"]
	ret = tmp[["points","season"]].groupby(['season']).sum()
	return ret.to_dict()["points"]