#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 23:00:18 2018

@author: rodrigo
"""

from sympy.abc import x, y, z
from sympy import Function, Array
from sympy import diff, derive_by_array, tensorcontraction, tensorproduct
from sympy import pprint


def flatten(l, ltypes=(list, tuple)):
    ltype = type(l)
    l = list(l)
    i = 0
    while i < len(l):
        while isinstance(l[i], ltypes):
            if not l[i]:
                l.pop(i)
                i -= 1
                break
            else:
                l[i:i + 1] = l[i]
        i += 1
    return ltype(l)


def grad(tensor, coordinates):
    return derive_by_array(tensor, coordinates)


def div(tensor, coordinates):
    if isinstance(tensor, sympy.tensor.array.dense_ndim_array.ImmutableDenseNDimArray):
        flatTensor = flatten(tensor.tolist())

        dimensions = len(coordinates)
        result = [None]*(dimensions**tensor.rank())
        repeat = len(result)//dimensions

        repeated_coordinates = [coord for coord in coordinates for _ in range(repeat)]
        result = [diff(flatTensor[i], coord) for i, coord in enumerate(repeated_coordinates)]

        while(len(result) is not dimensions):
            result = [result[i:i+dimensions] for i in range(0, len(result), dimensions)]

        result = Array(result)
        return tensorcontraction(result, (0,))
    else:
        raise ValueError('Object is a scalar or not a sympy NDimArray')


def laplacian(tensor, coordinates):
    return div(grad(tensor, coordinates), coordinates)

def dotProduct(tensor1, tensor2):
    if isinstance(tensor, sympy.tensor.array.dense_ndim_array.ImmutableDenseNDimArray):
        flat_tensor1 = flatten(tensor1.tolist())
        flat_tensor2 = flatten(tensor2.tolist())
        
        result_size = len(flat_tensor2)
        repeat = len(flat_tensor1)//result_size
        
        repeated_tensor2 = [element for element in flat_tensor2 for _ in range(repeat)]
        print(repeated_tensor2)
        result = [element1*element2  for element1, element2 in zip(flat_tensor1, repeated_tensor2)]
        print(result)
        
        while(len(result) is not result_size):
            result = [result[i:i+result_size] for i in range(0, len(result), result_size)]
        
        result = Array(result)
        return tensorcontraction(result, (0,))
        #result = [element1*element2 for element1, element2 in zip(flatTensor1, flatTensor2)]
        #print(result)
#        result = [None]*(dimensions**tensor.rank())
#        repeat = len(result)//dimensions
#
#        repeated_coordinates = [coord for coord in coordinates for _ in range(repeat)]
#        
#
#        while(len(result) is not dimensions):
#            result = [result[i:i+dimensions] for i in range(0, len(result), dimensions)]
#
#        result = Array(result)
#        return tensorcontraction(result, (0,))
#    else:
#        raise ValueError('Object is a scalar or not a sympy NDimArray')
#    return 
# def doubleDot(tensor1, tensor2):


def trace(tensor):
    return tensorcontraction(tensor, (0, 1))


coord = [x, y, z]

temp = Function("f")(x,y,z)
print(type(temp))

temp2 = 4
print(type(temp2))
print(isinstance(temp2, int))


scalar = Array([x])
vector = Array([Function("f_{0}".format(i))(x,y,z) for i in range(1,4)])
tensor = Array([[Function("f_{0}{1}".format(j,i))(x,y,z) for i in range(1,4)] for j in range(1,4)])

print(type(vector))
print(type(tensor))
print(isinstance(tensor, sympy.tensor.array.dense_ndim_array.ImmutableDenseNDimArray))

#print(isinstance())

print("TESTING SCALAR FUNCTIONS")
pprint(temp)
#print(temp.rank())
#print(temp.shape)
pprint(grad(temp, coord))
pprint(tensorcontraction(derive_by_array(temp, coord), (0,)))
pprint(div(grad(temp, coord), coord))

#print(scalar)
#print(scalar.rank())
#print(scalar.shape)


print("TESTING VECTOR FUNCTIONS")
pprint(vector)
pprint(vector.rank())
pprint(vector.shape)
for element in vector:
    pprint(element)
#pprint(tensorproduct(vector, vector))
print("TESTING VECTOR DIVERGENCE")
pprint(div(vector, coord))
print("TESTING VECTOR GRADIENT")
pprint(grad(vector, coord))
#pprint(tensorcontraction(derive_by_array(vector, coord), (0,)))
print("TESTING VECTOR LAPLACIAN")
pprint(div(grad(vector, coord), coord))
pprint(laplacian(vector, coord))
#pprint(tensorcontraction(derive_by_array(vector, coord), (1,)))


print("TESTING TENSOR FUNCTIONS")
pprint(tensor)
pprint(tensor.rank())
pprint(tensor.shape)
for element in tensor:
    pprint(element)
print("TESTING TENSOR DIVERGENCE")
pprint(div(tensor, coord))
#pprint(tensorcontraction(tensor, (0,)))
#pprint(tensorcontraction(tensor, (1,)))
#pprint(tensorcontraction(tensor, (0, 1)))

pprint(dotProduct(tensor, vector))





