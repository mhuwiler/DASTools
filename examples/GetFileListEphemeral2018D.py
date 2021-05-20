#!/usr/bin/env python


from __future__ import division, print_function

import MyTools.DASTools.DASTools as DASTools


folders = ['/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/323/775/00000/',
'/store/data/Run2018D/EphemeralHLTPhysics2/RAW/v1/000/323/775/00000/',
'/store/data/Run2018D/EphemeralHLTPhysics3/RAW/v1/000/323/775/00000/',
'/store/data/Run2018D/EphemeralHLTPhysics4/RAW/v1/000/323/775/00000/',
'/store/data/Run2018D/EphemeralHLTPhysics5/RAW/v1/000/323/775/00000/',
'/store/data/Run2018D/EphemeralHLTPhysics6/RAW/v1/000/323/775/00000/',
'/store/data/Run2018D/EphemeralHLTPhysics7/RAW/v1/000/323/775/00000/',
'/store/data/Run2018D/EphemeralHLTPhysics8/RAW/v1/000/323/775/00000/',
]

prefix = "/eos/cms"

files = []
for folder in folders: 
	filenamewithwildcards = prefix+folder+"*"
	files += DASTools.GetFileListFromFolder(filenamewithwildcards)
#files = DASTools.PrependPath(files, "file:") #only one trailing slash, as the path already has one
files = DASTools.RemovePrefix(files, prefix)
#DASTools.WriteComaSeparatedFileList("signalfiles.fls", files)
DASTools.WritePythonFileList("EphemeralHLTPhys2018DdatafilesComplete.py", files)


