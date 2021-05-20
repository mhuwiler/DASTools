#!/usr/bin/env python


from __future__ import division, print_function

import MyTools.DASTools.DASTools as DASTools

import Dataset


files = []
for datasetname in Dataset.getDataset("HLTData"): 
	query = DASTools.queryGOClient(datasetname).splitlines()
	files+=DASTools.queryGOClient(datasetname).splitlines()
#files = DASTools.PrependPath(files, "root://cms-xrd-global.cern.ch/") #only one trailing slash, as the path already has one
#DASTools.WriteComaSeparatedFileList("ZeroBias2018Ddata.py", files)
DASTools.WritePythonFileList("ZeroBias2018Ddata.py", files)


