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
    inputfile = "./dipole.dat"
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
xyz=["x","y","z"]
for j in np.arange(ny):
    i=j
    ax.plot(xdata,ydata[:,i]-ydata[:,i].mean(),label=xyz[i])

plt.ylim([-0.05,0.05])
ax.set_xlabel('Time')
ax.set_ylabel('Dipole(au)')
ax.set_title("Dipole")
ax.legend() 
figfile=inputfile+".png"
plt.savefig(figfile,dpi=100)