# -*- coding: utf-8 -*-
"""
Created on Wed May  2 22:57:27 2018
Name: Kewen Deng
Student ID: 29330440
Last modified date: May 4 2018
Description:
    In this file, I have defined a class for analysing the number of occurrences for each of the English words from the decoded sequences.
    This class have a instance variable which is a dictionary structure that is used for keeping track of the number of occurrences for each word,
    which is decoded by the Morse Code decoder in Task 1.
    
"""

class WordAnalyser:
    def __init__(self):
        # Build dictionary of words
        self.dict = {}
    
    def __str__(self):
        answer = 'The occurrences for each words are: \n'
        # Readbale format print
        if any(self.dict.values()):
            for key in self.dict:
                answer = answer + key + ':' + str(self.dict[key]) + '\n'
            return answer
        else:
            return 'No words occurrence.'

    def analyse_words(self, decoded_sequence):
        word = ''
        # Replace punctuations
        decoded_sequence = decoded_sequence.replace('?', '')
        decoded_sequence = decoded_sequence.replace('.', '')
        decoded_sequence = decoded_sequence.replace(',', '')
        decoded_sequence = decoded_sequence+ ' '
        
        for letter in decoded_sequence:
            exist = False # Judge the word exists or not
            if letter != ' ':
                word = word + letter
            else:
                for key in self.dict:
                    if key == word: # If the word is in Dictionary, add count.
                        self.dict[key] += 1
                        exist = True
                        break
                if exist == False and word !='': # If the word is not in Dictionary, add new word and new count.
                    self.dict[word] = 1
                word = ''
    
    
