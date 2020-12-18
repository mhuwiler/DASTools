#!/usr/bin/env python

from __future__ import division, print_function


QCD  = [
  "/QCD_Pt-15to3000_TuneCP5_Flat_14TeV_pythia8/Run3Winter20DRMiniAOD-DRFlatPU30to80_110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW",
]
Signal = [
  
]
HLTData = [
	"/EphemeralZeroBias2/Run2018D-v1/RAW", 
]

def getDataset(description):
	patterns = []
	
	if description == "QCD":  patterns = QCD  
	elif description == "bkg":    patterns = QCD    
	elif description == "sig":    patterns = Signal    
	elif description == "VV":    patterns = patternsVV    
	elif description == "WJets": patterns = patternsWJets 
	elif description == "QCD":   patterns = patternsQCD

	elif description == "mc":    patterns = QCD+Signal
	elif description == "all":   patterns = QCD+Signal
	elif description == "HLTData": 	patterns = HLTData

	else: 
		print("Dataset: No dataset was specified!\n Please specify which dataset to process (e.g. {QCD, sig, bkg})! ")

	return patterns
