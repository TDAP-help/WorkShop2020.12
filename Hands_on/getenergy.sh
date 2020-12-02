#!/usr/bin/env bash
##################################
# Author : cndaqiang             #
# Update : 2020-12-02            #
# Build  : 2020-12-02            #
# What   : getenergy from TDAP2.0  #
#################################
grep TDAP result | grep Energy | awk -F: '{ print $3 }'>> energy.dat
