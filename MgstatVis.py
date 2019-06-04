#!/usr/bin/env python
# coding: utf-8

# In[1]:


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

data = pd.read_csv(mgstatfile,header=1,parse_dates=[[0,1]])
data.columns = data.columns.str.strip()
data=data.rename(columns={'Date_       Time':'DateTime'})
data.index = data.DateTime

#for debugging:
#list(data)

output_file(os.getcwd()+"/mgstatvis.html")
TOOLS="pan,box_zoom,reset,save"

left = figure(tools=TOOLS,x_axis_type="datetime",title="Jrn Writes", width=600,height=350,
             x_axis_label="time")
right = figure(tools=TOOLS,x_axis_type="datetime", title="Phys Writes", width=600,height=350,
              x_axis_label="time",x_range=left.x_range)
left.line(data.index,data.Jrnwrts,legend="JrnWrts",line_width=1)
right.line(data.index,data.PhyWrs,legend="PhyWrs",line_width=1)
p=gridplot([[left,right]])
show(p)





