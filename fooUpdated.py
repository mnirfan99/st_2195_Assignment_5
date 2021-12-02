# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 14:11:13 2021

@author: ZeRoyale
"""

def is_divisible_by_k(x, k):
    '''
    checks whether x is divisible by k
    
    '''
    return x%k == 0
    
    
'''
Store all integers that are multiples of 2 or 5 or 7 that are lower or
equal to 1000(excluding doubles)
'''
x = []
for i in range(1001):
    if(is_divisible_by_k(i, 2) or is_divisible_by_k(i, 3)) or is_divisible_by_k(i, 7):
        x.append(i)
    
'''
Sum all the integers that are multiples of 2 or 5 or 7 that are lower or equal
 to 1000(excluding doubles)
 '''
 
print(sum(x))

'''
First bug found is the indentation error in line 23. Adding a tab space will
fix it
'''
'''
Next bug is the unsupported operand type for & which is in line 22-23. We fix
the bug by chnaging x to i
'''
'''
Next bug is the unsupported operand type for &: none type and none type. This 
means the def function does not return any values. Hence, we change assert
to return. 
'''
'''
Next bug is that the tuple object has no attribute append. we have to change
x = () into something that can be appended. So to fix it, we do x=[]
'''
'''
the code runs fine then but looking at the codes, it does not do as intended. 
firstly, the range does not include 1000, so we fix it by changing to 1001.& 
is also a wrong function to use, it should be or and the | should be or as well
That should be good enough :D
'''

