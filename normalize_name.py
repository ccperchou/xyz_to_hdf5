# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 14:00:59 2021

@author: cleme
"""
import glob
import os
import shutil
import random
import re
import math
import statistics
import numpy as np





L_files=glob.glob("*.txt")
newfiles_name=''
completeName=''
i=1
# for each files
for files in L_files:
   
    name='MGV'+'-'+str(i)+'.txt'
    i=i+1
    os.rename(files, name)
    

f= open("ListMGV.txt","w+")
L_files=glob.glob("*.txt")
for files in L_files:
    f.write("\n" + files)
f.close()
    
    