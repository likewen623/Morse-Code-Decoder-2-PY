# -*- coding: utf-8 -*-
"""
Created on Tue May  1 19:15:30 2018
Name: Kewen Deng
Student ID: 29330440
Last modified date: May 4 2018
Description:
    In this file, I have defined a class that serves as the Morse Code decoder.
    This class have a instance variable which is a dictionary structure that represents each of the Morse Code characters as a string sequences of binary digits.
    This decoder class is used for decoding any Morse Code sequences.
    
"""

class Decoder:
    def __init__(self):
        # Build A-Z, 0-9 and punctuations to be values in Dictionary
        self.cha = []
        for cha in range(65,91):
            self.cha.append(chr(cha))
        for cha in range(0,10):
            self.cha.append(str(cha))
        self.cha.append('.')
        self.cha.append(',')
        self.cha.append('?')          
        # Build Morse Code to be keys in Dictionary
        self.mc = [ '01', '1000',  '1010',   '100',     '0',  '0010',   '110',  '0000',    '00',  '0111',   '101',  '0100',
                    '11',   '10',   '111',  '0110',  '1101',   '010',   '000',     '1',   '001',  '0001',   '011',  '1001',
                  '1011', '1100', '11111', '01111', '00111', '00011', '00001', '00000', '10000', '11000', '11100', '11110',
                  '010101', '110011', '001100']
        # Zip Morse Code(keys) and character(values) to Dictionary
        self.dict = dict(list(zip(self.mc, self.cha)))
    
    def __str__(self):
        format_output = ''
        # Readbale format print
        for key in range(0,13) :        
            format_output = format_output \
                     + self.dict[list(self.dict.keys())[key]] + ':' + list(self.dict.keys())[key] + '\t' \
                     + self.dict[list(self.dict.keys())[key+13]] + ':' + list(self.dict.kAeys())[key+13] + '\t' \
                     + self.dict[list(self.dict.keys())[key+26]] + ':' + list(self.dict.keys())[key+26] + '\n'
        return format_output
    
    def decode(self, morse_code_sequence):
        output = '' # output is the answer to print
        morse = '' # morse is the subsequence to decode
        count_star = 0
        
        # if the input is short than 6, which means it can not contain any punctuation, show error message.
        if len(morse_code_sequence) < 6:
            print("This input is invalid!")
        
        # if the decoded sequence end without punctuation, show error message.
        elif morse_code_sequence[-6:] not in ('010101', '110011', '001100'):
            print("End without punctuation. This input is invalid!")
        
        # if the decoded sequence start with punctuation, show error message.
        elif morse_code_sequence[:6] in ('010101', '110011', '001100'):
            print("Start with punctuation. This input is invalid!")
        
        # if the decoded sequence start with *, show error message.
        elif morse_code_sequence[0] == '*':
            print("Start with *. This input is invalid!")
        
        else:    
           user_input = morse_code_sequence + '*' # put an * to indicate the end of a sequence      
           
           # Loop for cut down long subsequence to single word
           for letter in user_input: # letter is every single character in inputAAA
                if letter != '*': # extract subsequence from a whole sequence
                    morse = morse + letter
                elif morse != '' : # judge the subsequence is valid or not
                    if count_star == 1 or count_star > 2 : # judge the total number of chain of *
                        print("Chain of 2 * or more than 3 *. This input is invalid!")
                        output = ''
                        break 
                    if count_star == 2:
                        output = output + ' '
                        
                    if morse in self.dict.keys() : # if the subsequence is valid, add it to output
                        output = output + self.dict[morse]
                    else: # if the subsequence is invalid, send an error message
                        print("Contains of undecodable message. This input is invalid!")
                        output = ''
                        break
                    morse = '' # clear morse for next subsequence 
                    count_star = 0
                else:
                    count_star += 1
   
        if output != '': # judge the output is vacant or not
            if ' ' not in output: # judge the output contains at least one space or not
                print("No space exists. This input is invalid!")
                output = ''
            else: # judge the output contains chains of punctuations or not
                output_check = output.replace(' ', '')
                for i in range(len(output_check)-1):
                    if output_check[i] in ('?', '.', ',') and output_check[i+1] in ('?', '.', ','):
                        print("Chain of more than 1 punctuation. This input is invalid!")
                        output = ''
                        break 
        
        return output
