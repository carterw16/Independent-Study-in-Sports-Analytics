import pandas as pd

def Data():
	pidf = pd.read_csv("nhl-game-data/player_info.csv")
	pidf["name"] = pidf["firstName"]+" "+pidf["lastName"]
	return pidf