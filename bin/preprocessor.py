# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 12:55:39 2020

@author: HP
"""
import re
class PreprocessDoc:
    """
    Module for preprocessin articles
    """
    def removeSpclChar(self,text):
        """
        Remove special Characters
        
        Input:
            text: string
        Output:
            modifiedText: string
        """
        filteredText = re.sub(',|;|#|$','',text)
        return filteredText

    def convertToLower(self,text):
        return text.lower()
    
    