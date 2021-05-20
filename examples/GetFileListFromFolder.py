#!/usr/bin/env python


from __future__ import division, print_function

import MyTools.DASTools.DASTools as DASTools


folders = ["store/group/phys_bphys/patatrack/bstautau/crab_BsToTauTau_PUFlat55To75_20201024_164758/201024_144812/0000/", 
"store/group/phys_bphys/patatrack/bstautau/crab_BsToTauTau_PUFlat55To75_20201024_164747/201024_144757/0000/", 
"store/group/phys_bphys/patatrack/bstautau/crab_BsToTauTau_PUFlat55To75_20201024_164732/201024_144746/0000/", 
"store/group/phys_bphys/patatrack/bstautau/crab_BsToTauTau_PUFlat55To75_20201024_164939/201024_144951/0000/", 
"store/group/phys_bphys/patatrack/bstautau/crab_BsToTauTau_PUFlat55To75_20201024_164813/201024_144826/0000/", 
"store/group/phys_bphys/patatrack/bstautau/crab_BsToTauTau_PUFlat55To75_20201024_164827/201024_144838/0000/", 
"store/group/phys_bphys/patatrack/bstautau/crab_BsToTauTau_PUFlat55To75_20201024_103345/201024_083355/0000/", 
"store/group/phys_bphys/patatrack/bstautau/crab_BsToTauTau_PUFlat55To75_20201024_103331/201024_083344/0000/", 
]

files = []
for folder in folders: 
	filenamewithwildcards = "/eos/cms/"+folder+"*"
	files += DASTools.GetFileListFromFolder(filenamewithwildcards)
files = DASTools.PrependPath(files, "file:") #only one trailing slash, as the path already has one
DASTools.WriteComaSeparatedFileList("signalfiles.fls", files)


