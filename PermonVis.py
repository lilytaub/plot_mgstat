#!/usr/bin/env python
# coding: utf-8

import math
import pandas as pd
import argparse
from datetime import datetime
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange, IndexDateFormatter
from pButtons_ParsePerfmon import parse
from bokeh.plotting import *

## parse the timestamp associated with the perfmon data
def parse_datetime(x):
    dt=datetime.strptime(x, '%m/%d/%Y %H:%M:%S.%f')
    return dt

## retrieve pButtons input file
parser = argparse.ArgumentParser()
parser.add_argument('-f','--file',dest='file',help='pButtons file')
parser.add_argument('-o','--output',dest='output',help='directory for output files')
args = parser.parse_args()
pbuttons = args.file
output = args.output

## parse pButtons file, creates perfmon.txt file in cwd
parse(pbuttons,output)

## create dataframe from perfmon data text file
perfmon = pd.read_csv(output+"/perfmon.txt", header=0, index_col=0,low_memory=False,converters={0: parse_datetime})

## create output file for plots
output_file(output+"/perfmonvis.html")

##tools
TOOLS="pan,box_zoom,reset,save"

## list of perfmon plots
plots = []
index = 0

for name in perfmon:
	## put the first plot in a unique variable so it can
	## be used to link the x ranges of all subsequent plots
	if index == 0:
		firstplot = figure(tools=TOOLS,x_axis_type="datetime",
					title=name,width=600,height=350,x_axis_label="time")
		firstplot.line(perfmon.index,pd.to_numeric(perfmon[perfmon.columns[index]],errors='coerce'),
			line_width=1)
		plots.append(firstplot)
	else:
		myplot=figure(tools=TOOLS,x_axis_type="datetime",
					title=name,width=600,height=350,x_axis_label="time")
		myplot.line(perfmon.index,pd.to_numeric(perfmon[perfmon.columns[index]],errors='coerce'),
			line_width=1)
		## link x range of this plot to first plot
		myplot.x_range=firstplot.x_range
		## add plot to list of plots
		plots.append(myplot)
	index = index + 1

## show all plots in html file
show(gridplot(plots,ncols=2,merge_tools=False))