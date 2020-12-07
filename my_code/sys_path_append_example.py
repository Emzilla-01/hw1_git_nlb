# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 10:47:45 2020

@author: emmam
"""
import os

import sys

print(f"current directory is {os.getcwd()}")
# sys.path.append(r"C:\Users\emmam\Documents\nlb\loans_module\home_loans\nested")
sys.path.append(r"C:\Users\emmam\Documents\nlb\loans_module")
import example
example.nest()

import home_loans.rules as hr_rules
hr_rules.rule1()
