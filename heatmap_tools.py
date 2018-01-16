import datetime
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go

programmers = ['Alex','Nicole','Sara','Etienne','Chelsea','Jody','Marianne']

base = datetime.datetime.today()
date_list = [base - datetime.timedelta(days=x) for x in range(0, 180)]

z = []

for prgmr in programmers:
    new_row = []
    for date in date_list:
        new_row.append( np.random.poisson() )
    z.append(list(new_row))

def get_hm_data():
	return [
		go.Heatmap(
			z=z,
			x=date_list,
			y=programmers,
			colorscale='Viridis',
		)
	]

def get_hm_layout():
	return go.Layout(
		title='GitHub commits per day',
		xaxis = dict(ticks='', nticks=36),
		yaxis = dict(ticks='')
	)