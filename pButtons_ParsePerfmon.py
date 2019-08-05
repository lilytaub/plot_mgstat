#!/usr/bin/env python
# coding: utf-8
def parse(pButtons,output):
	f = open(pButtons)
	inperf = 0
	output = open(output+"/perfmon.txt","w+")
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