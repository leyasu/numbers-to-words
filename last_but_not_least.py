# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 20:20:44 2017

@author: leyasu
"""

def last_not_least():
    n=int(input('please enter an integer between 1 and 9999: '))
    first=["","one", "two", "three", "four", "five", "six", "seven", "eight","nine", "ten"]
    second = ["","eleven", "twelve", "thirteen", "fourteen", "fifteen","sixteen","seventeen","eighteen", "nineteen"]
    third =["","", "twenty","thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    a= int(n / 1000)
    b=int( (n-a*1000)/100)
    c=int((n%100)/10)
    d=n%10
    if a > 0:
        print(first[a], "thousand ", end="")
    else: 
        print("", end="")
    if b>0:
        print(first[b], "hundred ", end="")
    else:
        print("", end="")
    if c ==0:
        print(first[d], end="")
    elif c >= 2:
        print(third[c], first[d], end="")
    elif 0<c<2:
        print(second[d], end="")
last_not_least()