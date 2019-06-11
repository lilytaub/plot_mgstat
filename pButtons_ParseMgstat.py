#!/usr/bin/env python
# coding: utf-8

import os
import argparse

## parses pButtons mgstat section
def parse(pButtons):
	f = open(pButtons)
	inmgstat = 0
	output = open(os.getcwd()+"/mgstat.txt","w+")
	for line in f:
	    if "beg_mgstat" in line:
	        inmgstat = 1
	        continue
	    if "end_mgstat" in line:
	        inmgstat = 0
	        continue
	    if inmgstat == 1:
	        output.write(line)
	output.close()
	f.close()