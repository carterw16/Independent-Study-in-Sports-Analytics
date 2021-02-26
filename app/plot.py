import json
import plotly

def plotdata(x,y,id,title):
	graph = dict(
        data=[
        	dict(
            	x=x,
                y=y,
                type='bar'
            ),
        ],
        layout=dict(
	        title=title
        ),
        id = id
    )
	graphJSON = json.dumps(graph, cls=plotly.utils.PlotlyJSONEncoder)
	return graph
