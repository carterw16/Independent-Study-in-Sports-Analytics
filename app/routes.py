from flask import render_template, request, redirect, session
from app import app
from .getdata import data, goalsperseason, pointsperseason
from .plot import plotdata
import json

@app.route('/', methods = ("GET","POST"))
@app.route('/home')
def home():
	pidf = data()
	# accounts = {'Peter Cembalest': 'rcuuyqtf','Alexi Judge':'jgnnq','Carter Weaver':'dcpcpc','Teacher':'vgcejgtrcuuyqtf'}
	if request.method == "GET":
		return render_template("home.html",title='Home')
	else:
		player = request.form.get("playername")
		if pidf.name.str.contains(player).any():
			playerdata = pidf[pidf.name==player].to_dict(orient="records")[0]
			
			goals = goalsperseason(playerdata["player_id"])
			points = pointsperseason(playerdata["player_id"])
			
			plots = []
			plotids = []
			print("Hello")

			for d, plot_id,title in [(goals, 'goalplot','Goals per Season'), (points, 'pointplot',"Points per Season")]: 
				x=[]
				y=[]
				for season,v in d.items():
					x.append(season)
					y.append(v)

				plots.append(plotdata(x,y,plot_id,title))
				plotids.append(plot_id)
			print(plots)

			nat = pidf[pidf.name==player].nationality.values[0]
			return render_template("home.html",title='Home',player=player,nat=nat,plots=json.dumps(plots),plotids=plotids)
		else:
			return render_template("home.html", message = "Input Invalid", title='Home')

