# -*- coding: utf-8 -*-
"""
Created on Tue May  1 20:40:59 2018
Name: Kewen Deng
Student ID: 29330440
Last modified date: May 4 2018
Description:
    In this file, I have defined a class for analysing the number of occurrences for each of the letters and numerals from the decoded sequences.
    This class have a instance variable which is a dictionary structure that is used for keeping track of the number of occurrences for each of the letters and numerals,
    which are decoded by the Morse Code decoder in Task 1.
    
"""

class CharacterAnalyser:
    def __init__(self):
        # Build count of each character to by values in Dictionary
        self.count = [0]*36
        # Build A-Z and 0-9 to be keys in Dictionary
        self.cha = []
        for cha in range(65,91):
            self.cha.append(chr(cha))
        for cha in range(0,10):
            self.cha.append(str(cha))
        # Zip A-Z and 0-9 (keys) and counts(values) to Dictionary
        self.dict = dict(zip(self.cha, self.count))
    
    def __str__(self):
        output = 'The occurrences for each characters are: \n'
        answer = ''
        # Readbale format print
        for key in self.dict:
            if self.dict[key] > 0:
                answer = answer + key + ':' + str(self.dict[key]) + '\n'
        # If no occurrence, show error message.
        if answer != '':
            return output + answer
        else:
            return 'No letters occurrence.'
        
    def analyse_characters(self, decoded_sequence):
        for i in decoded_sequence:
            # Find the charater in dictionary and add count
            for key in self.dict:
                if i == key:
                    self.dict[key] += 1
                    break
            
            


