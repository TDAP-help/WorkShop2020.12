#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2020-12-02 @IOP
@Author  : cndaqiang
@Blog    : cndaqiang.github.io
@File    : 画图
"""
import sys
import os
import numpy as np
import matplotlib.pyplot as plt

#-----Input File
if len(sys.argv) > 1:
    inputfile = str(sys.argv[1])
else:
    inputfile = "./energy.dat"
if os.path.exists(inputfile):
    print("read from",inputfile)
else:
    print("EXIT: There are not "+inputfile)
    exit()

f=open(inputfile,'r')
ny=len(f.readline().split())
nx=int(os.popen('wc -l '+inputfile).read().split()[0])
ydata=np.zeros([nx,ny])
xdata=np.arange(nx)*0.01
#Read
ierror=f.seek(0,0)
alldat=f.readlines()
f.close()
for i in np.arange(nx):
    ydata[i]=[ np.float(x) for x in  alldat[i].split()[0:ny]]

#Plot
fig, ax = plt.subplots(1,1,sharex=True,sharey=False,figsize=(8,6))
for j in np.arange(ny):
    i=ny-1-j
    if(i<4): #occupation
        ax.plot(xdata,ydata[:,i],label=str(i-4))
    else:
        ax.plot(xdata,ydata[:,i],label=str(i-3))

ax.set_xlabel('Time')
ax.set_ylabel('Energy(eV)')
ax.set_title("TDKS Energy Level")
ax.legend() 
figfile=inputfile+".png"
plt.savefig(figfile,dpi=100)