# -*- coding: utf-8 -*-
"""
Created on Wed May 13 21:23:22 2020

@author: Mustehssun
"""

from .impls.binary_relevance import transform_problem as binary_relevance


def cons_problem_transformer(problem_transformer_name):
    if problem_transformer_name == "binary_relevance":
        return binary_relevance
    else:
        raise Exception("Unexpected problem transformation method")


