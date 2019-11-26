# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 04:01:26 2019

@author: rijul karmakar
"""
import re 
class Password:
    def passwordValidate(password):
        flag = 0
        while True:   
            if (len(password)<8): 
                flag = -1
                break
            elif not re.search("[a-z]", password): 
                flag = -1
                break
            elif not re.search("[A-Z]", password): 
                flag = -1
                break
            elif not re.search("[0-9]", password): 
                flag = -1
                break
            elif not re.search("[_@$]", password): 
                flag = -1
                break
            elif re.search("\s", password): 
                flag = -1
                break
            else: 
                flag = 0
                return True 
                break
          
        if flag ==-1: 
            return False