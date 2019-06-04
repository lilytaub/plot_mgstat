#!/usr/bin/env python
# coding: utf-8


import math
import pandas as pd
import sys
import argparse
import os
from datetime import datetime
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange, IndexDateFormatter
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
	myplot = figure(tools=TOOLS,x_axis_type="datetime",title=name,
					width=600,height=350,x_axis_label="time")
	myplot.line(data.index,data[name],legend=name,line_width=1)
	##add plot to list
	plots.append(myplot)

##show all plots
show(gridplot(plots,ncols=2,merge_tools=True))





