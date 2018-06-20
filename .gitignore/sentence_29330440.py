# -*- coding: utf-8 -*-
"""
Created on Wed May  2 00:45:12 2018
Name: Kewen Deng
Student ID: 29330440
Last modified date: May 4 2018
Description:
    In this file, I have defined a class in this task for analysing the number of occurrences for each type of English sentences from the decoded sequences.
    This class have a instance variable which is a dictionary structure that is used for keeping track of the number of occurrences for each type of sentences,
    which is decoded by the Morse Code decoder in Task 1.
    
"""

class SentenceAnalyser:
    def __init__(self):
        # Build count of each character to by values in Dictionary
        self.count = [0]*3
        # Build '.', ',', '?' to be keys in Dictionary
        self.cha = ['.', ',', '?']
        self.dict = dict(zip(self.cha, self.count))
    
    def __str__(self):
        answer = 'The occurrences for each type of English sentences are: \n'
        # Readbale format print
        if any(self.dict.values()):
            for key in self.dict:
                answer = answer + key + ':' + str(self.dict[key]) + '\n'
            return answer
        else:
            return 'No sentences occurrence.'
    
    
    def analyse_sentences(self, decoded_sequence):
        comma_close = True # Judge the comma has been ended by '.'/'?' or not
        for i in decoded_sequence:
            if i == '.':
                self.dict['.'] += 1
                if comma_close == False: # If the comma has been ended by '.', count of ',' plus 1.
                    comma_close = True
                    self.dict[','] += 1
            if i == '?':
                self.dict['?'] += 1
                if comma_close == False: # If the comma has been ended by '?', count of ',' plus 1.
                    comma_close = True
                    self.dict[','] += 1
            if i == ',':
                self.dict[','] += 1
                comma_close = False
                
                