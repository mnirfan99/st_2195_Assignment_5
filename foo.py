# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 23:02:02 2021

@author: ZeRoyale
"""

def is_divisible_by_k(x, k):
    '''
    checks whether x is divisible by k
    
    '''
    assert x%k == 0
    
    
'''
Store all integers that are multiples of 2 or 5 or 7 that are lower or
equal to 1000(excluding doubles)
'''
x = ()
for i in range(1000):
    if(is_divisible_by_k(x, 2) & is_divisible_by_k(x, 3)) | is_divisible_by_k(x, 7):
    x.append(i)
    
'''
Sum all the integers that are multiples of 2 or 5 or 7 that are lower or equal
 to 1000(excluding doubles)
 '''
 
sum(x)
 


