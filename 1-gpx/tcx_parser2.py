#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from pyworkout.parsers import tcxtools
# https://github.com/triskadecaepyon/pyworkout-toolkit

parser = argparse.ArgumentParser(description='Process tcx data')
parser.add_argument('--tcx', dest='tcxFile', required=True,
                   help='input tcx file')
parser.add_argument('--csv', dest='csvFile', required=True,
                   help='output csv file')


args = parser.parse_args()
tcxFile = args.tcxFile
csvFile = args.csvFile


workout_data = tcxtools.TCXPandas(tcxFile) # Create the Class Object
df = workout_data.parse() # Returns a dataframe

df.to_csv(csvFile, sep=",", index=False)

print(df)
