#!/usr/bin/env python3.7.2
#-*- coding: utf-8 -*-

H = input('输入您的身高')
W = input('输入您的体重')
Height = int(H)
Weight = int(W)

BMI = Weight/(Height*Height/10000)

print(BMI)

if BMI < 18.5:
    print('过轻')
elif BMI <=25:
    print('正常')
elif BMI <=28:
    print('过重')