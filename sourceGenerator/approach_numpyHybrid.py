#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 23:25:34 2018

@author: rodrigo
"""

import numpy as np
from sympy.abc import x, y, z
from sympy import Function
from sympy import diff
from sympy import pprint

coord = [x, y, z]

scalar = np.array(Function("f")(x, y, z))
scalar2 = np.array(x)
pprint(scalar)
#print(type(scalar), scalar.ndim)
pprint(diff(scalar2, x))
