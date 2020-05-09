from flask import render_template, request, redirect, session
from app import app
from .getdata import Data

@app.route('/', methods = ("GET","POST"))
@app.route('/home')
def home():
	pidf = Data()
	print(pidf)
	# accounts = {'Peter Cembalest': 'rcuuyqtf','Alexi Judge':'jgnnq','Carter Weaver':'dcpcpc','Teacher':'vgcejgtrcuuyqtf'}
	if request.method == "GET":
		return render_template("home.html",title='Home')
	else:
		player = request.form.get("playername")
		if pidf.name.str.contains(player).any():
			nat = pidf[pidf.name==player].nationality.values[0]
			return render_template("home.html",title='Home',player=player,nat=nat)
		else:
			return render_template("home.html", message = "Input Invalid", title='Home')

