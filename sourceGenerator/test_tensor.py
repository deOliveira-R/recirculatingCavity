#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 05:38:06 2018

@author: rodrigo
"""

from TensorModule import *
import unittest


class TensorUnitTest(unittest.TestCase):

    def setUp(self):
        if not HAVE_SYMPY:
            return
        self.U = Tensor(NP.array(([X**3, sympy.sin(X), sympy.exp(X)],
                                  [Y**3, sympy.sin(Y), sympy.exp(Y)],
                                  [Z**3, sympy.sin(Z), sympy.exp(Z)])))

    def test_type(self):
        if not HAVE_SYMPY:
            return
        self.assertEqual(isTensor(self.U), 1)

    def test_rank(self):
        if not HAVE_SYMPY:
            return
        self.assertEqual(self.U.rank, 2)
        self.assertEqual(grad(self.U).rank, 3)

    def test_gradient(self):
        if not HAVE_SYMPY:
            return
        self.assertEqual(grad(self.U), Tensor(NP.array([[[3*X**2, 0, 0 ], [0, 3*Y**2, 0 ], [0, 0, 3*Z**2 ]], [[sympy.cos(X), 0, 0 ], [0, sympy.cos(Y), 0 ], [0, 0, sympy.cos(Z) ]], [[sympy.exp(X), 0, 0 ], [0, sympy.exp(Y), 0 ], [0, 0, sympy.exp(Z) ]]])))

    def test_symmetric_gradient(self):
        if not HAVE_SYMPY:
            return
        # attention: sensible 3.0*X**2 != 3*X**2
        self.assertEqual(gradsym(self.U), Tensor(NP.array(
            [[[3.0*X**2, 0.5*sympy.cos(X), 0.5*sympy.exp(X)], [0, 1.5*Y**2, 0], [0, 0, 1.5*Z**2]],
             [[0.5*sympy.cos(X), 0, 0], [1.5*Y**2, 1.*sympy.cos(Y), 0.5*sympy.exp(Y)], [0, 0, 0.5*sympy.cos(Z)]],
             [[0.5*sympy.exp(X), 0, 0], [0, 0.5*sympy.exp(Y), 0], [1.5*Z**2, 0.5*sympy.cos(Z), 1.*sympy.exp(Z)]]])))

    def test_divergence(self):
        if not HAVE_SYMPY:
            return
        self.assertEqual(div(grad(self.U)), Tensor(NP.array([[6*X, 6*Y, 6*Z ], [-sympy.sin(X), -sympy.sin(Y), -sympy.sin(Z) ], [sympy.exp(X), sympy.exp(Y), sympy.exp(Z)]]) ))
    
    def test_laplacian(self):
        if not HAVE_SYMPY:
            return
        self.assertEqual(laplacian(self.U), Tensor(NP.array([[6*X, 6*Y, 6*Z ], [-sympy.sin(X), -sympy.sin(Y), -sympy.sin(Z) ], [sympy.exp(X), sympy.exp(Y), sympy.exp(Z)]]) ))

    
    def testProduitDoubleContracte(self):
        if not HAVE_SYMPY:
            return
        TensO4Sym = Tensor(NP.array([[[[ 400.,           0.,           0.,       ],
                                       [   0.,         200.,           0.,       ],
                                       [   0.,           0.,         200.,       ]],
                                      [[   0.,          66.66666667,   0.,       ],
                                       [  66.66666667,   0.,           0.,       ],
                                       [   0.,           0.,           0.,       ]],
                                      [[   0.,           0.,         133.33333333],
                                       [   0.,           0.,           0.,       ],
                                       [ 133.33333333,   0.,           0.,       ]]],
                                     [[[   0.,          66.66666667,   0.,       ],
                                       [  66.66666667,   0.,           0.,       ],
                                       [   0.,           0.,           0.,       ]],
                                      [[ 200.,           0.,           0.,       ],
                                       [   0.,         233.33333333,   0.,       ],
                                       [   0.,           0.,         166.66666667]],
                                      [[   0.,           0.,           0.,       ],
                                       [   0.,           0.,          66.66666667],
                                       [   0.,          66.66666667,   0.,       ]]],
                                     [[[   0.,           0.,         133.33333333],
                                       [   0.,           0.,           0.,       ],
                                       [ 133.33333333,   0.,           0.,       ]],
                                      [[   0.,           0.,           0.,       ],
                                       [   0.,           0.,          66.66666667],
                                       [   0.,          66.66666667,   0.,       ]],
                                      [[ 200.,           0.,           0.,       ],
                                       [   0.,         166.66666667,   0.,       ],
                                       [   0.,           0.,         233.33333333]]]]) )

        self.assertEqual(TensO4Sym.produitDoubleContracte(self.U),
                         Tensor(NP.array([[200.000000000000*sympy.sin(Y) + 400.000000000000*X**3 + 200.000000000000*sympy.exp(Z), 66.6666666700000*sympy.sin(X) + 66.6666666700000*Y**3, 133.333333330000*Z**3 + 133.333333330000*sympy.exp(X) ],
                                          [66.6666666700000*sympy.sin(X) + 66.6666666700000*Y**3, 233.333333330000*sympy.sin(Y) + 200.000000000000*X**3 + 166.666666670000*sympy.exp(Z),       66.6666666700000*sympy.sin(Z) + 66.6666666700000*sympy.exp(Y) ],
                                          [133.333333330000*Z**3 + 133.333333330000*sympy.exp(X),       66.6666666700000*sympy.sin(Z) + 66.6666666700000*sympy.exp(Y),       166.666666670000*sympy.sin(Y) + 200.000000000000*X**3 + 233.333333330000*sympy.exp(Z) ]])))

    def testproduitSimpleContracte(self):
        if not HAVE_SYMPY:
            return
        self.assertEqual(self.U.produitSimpleContracte(Tensor(NP.array([-1, 0, 0]))), Tensor(NP.array([-X**3, -Y**3, -Z**3])))


if __name__ == '__main__':
    unittest.main()
