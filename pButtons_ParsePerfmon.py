#!/usr/bin/env python
# coding: utf-8

import os
import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("pButtonsFile")
# args = parser.parse_args()

def parse(pButtons):
	f = open(pButtons)
	inperf = 0
	output = open(os.getcwd()+"/perfmon.txt","w+")
	for line in f:
		if "beg_win_perfmon" in line:
			inperf = 1
			continue
		elif "end_win_perfmon" in line:
			inperf = 0
			continue

		if inperf == 1:
			output.write(line)
	output.close()
	f.close()