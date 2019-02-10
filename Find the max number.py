#!/usr/bin/env python3.7.2
#-*- coding: utf-8 -*-

L = []
i=0
while i <100:
    print('please input the', i+1 ,' number',"enter 'stop' to stop")
    a = input()
    L.append(a)
    if a=='stop':
        print('max number of all is', b)
        break


    elif i==1:
        if int(L[0]) > int(L[1]):
            print('max number so fa is',L[0])
            b = int(L[0])
        else:
            print('max number so far is',L[1])
            b = int(L[1])
    elif i>1:
        if int(L[i])>b:
            print('max number so fa is', L[i])
            b= int(L[i])
        else:
            print('max number so far is', b)


    i = i +1

    input()
