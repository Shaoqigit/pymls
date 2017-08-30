#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# Transfert_Interfaces.py
#
# This file is part of pypw, a software distributed under the MIT license.
# For any question, please contact one of the authors cited below.
#
# Copyright (c) 2017
# 	Olivier Dazel <olivier.dazel@univ-lemans.fr>
# 	Mathieu Gaborit <gaborit@kth.se>
# 	Peter Göransson <pege@kth.se>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#

import numpy as np

def Interface_Fluid_Pem(O):
       
    a=-np.array([O[1,1],O[1,2]],[O[5,1],O[5,2]]);
    Tau=np.dot(np.linalg.inv(a),np.array([[O[1,0]],[O[5,0]]]));
    Omega_moins=np.array([[O[2,0]],[O[4,0]]])+np.dot(np.array([[O[2,1],O[2,2]],[O[4,1],O[4,2]]]),Tau);
    return (Omega_moins,Tau)

def Interface_Solid_Fluid(O):
    
    Omega_moins=np.zeros((4,2),dtype=np.complex)
    Omega_moins[1,0]=O[0,0]
    Omega_moins[2,0]=-O[1,0]
    Omega_moins[3,1]=1
    Tau=np.zeros((4,2),dtype=np.complex);

    return (Omega_moins,Tau)

def Interface_Fluid_Solid(O):

    Tau=-O[0,0]/O[0,1]
    Omega_moins=np.array([[O[1,1]],[-O[2,1]]])*Tau+np.array([[O[1,0]],[-O[2,0]]]);

    return (Omega_moins,Tau)