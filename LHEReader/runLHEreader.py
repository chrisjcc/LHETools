#! /bin/env python                                                                                                             
import os
import sys
import string

if(len(sys.argv) < 2):
    print "Usage: python runLHEreader.py output.root inputfolder"
else:
    OutName = str (sys.argv[1])
    InputFolder = str (sys.argv[2])
    FileList = os.popen('ls -1 '+str(InputFolder)+'/*lhe').readlines()
    inputfiles = ""
    for File in FileList:
        inputfiles += "-i " + File   
    inputfiles = inputfiles.replace("\n", " ")     
    cmd = "lheReader " + inputfiles + "-o " + str(OutName)
    print cmd
    os.system(cmd)
