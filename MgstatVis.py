#!/usr/bin/env python
# coding: utf-8


import math
import pandas as pd
import sys
import argparse
import os
from datetime import datetime
from bokeh.plotting import *

##retrieve mgstat file input
parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()
mgstatfile = args.file

##put mgstat data into a dataframe, index on date
data = pd.read_csv(mgstatfile,header=1,parse_dates=[[0,1]])
data.columns = data.columns.str.strip()
data=data.rename(columns={'Date_       Time':'DateTime'})
data.index = data.DateTime

##output file for bokeh plots
output_file(os.getcwd()+"/mgstatvis.html")

##tools
TOOLS="pan,box_zoom,reset,save"

## list of plots of each mgstat metric
plots = []

for name in data:
	if name == "DateTime":
		continue
	## Glorefs is the first metric graphed. Putting this plot in a unique variable so
	## it can be used to link the x ranges of all plots
	elif name == "Glorefs":
		firstplot = figure(tools=TOOLS,x_axis_type="datetime",title=name,
							width=600,height=350,x_axis_label="time")
		firstplot.line(data.index,data[name],legend=name,line_width=1)
		plots.append(firstplot)

	else:
		myplot = figure(tools=TOOLS,x_axis_type="datetime",title=name,
					width=600,height=350,x_axis_label="time")
		myplot.line(data.index,data[name],legend=name,line_width=1)
		##links x ranges of all plots
		myplot.x_range=firstplot.x_range
		##add plot to list
		plots.append(myplot)

##show all plots
show(gridplot(plots,ncols=2,merge_tools=False))





