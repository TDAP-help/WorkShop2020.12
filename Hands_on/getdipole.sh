#!/usr/bin/env bash
##################################
# Author : cndaqiang             #
# Update : 2020-12-02            #
# Build  : 2020-12-02            #
# What   : getdipole from TDAP2.0  #
#################################
grep dipole result |  grep TDAP | grep -v Debye | awk -F\= '{ print $2 }' > dipole.dat
