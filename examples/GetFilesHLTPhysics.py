#!/usr/bin/env python


from __future__ import division, print_function

import DASTools

import Dataset


datasetnames = ["/HLTPhysics/Run2018D-v1/RAW"]

files = []
for datasetname in datasetnames: 
	query = DASTools.queryGOClient(datasetname).splitlines()
	files+=query
#files = DASTools.PrependPath(files, "root://cms-xrd-global.cern.ch/") #only one trailing slash, as the path already has one
#DASTools.WriteComaSeparatedFileList("ZeroBias2018Ddata.py", files)
DASTools.WritePythonFileList("HLTPhysics2018local.py", files)


