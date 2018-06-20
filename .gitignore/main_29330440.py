# -*- coding: utf-8 -*-
"""
Created on Thu May  3 01:06:07 2018
Name: Kewen Deng
Student ID: 29330440
Last modified date: May 4 2018
Description:
    This file tests all the classes defined before.
    I have defined a function called main() that will drive the flow of execution of the program.
    Below are the import part of other classes and the sequence of tasks that execute within the main() function. 

"""

from decoder_29330440 import Decoder as Decoder
from character_29330440 import CharacterAnalyser as CharacterAnalyser
from word_29330440 import WordAnalyser as WordAnalyser
from sentence_29330440 import SentenceAnalyser as SentenceAnalyser



def main():
    # Create instances for 4 classes
    my_decoder = Decoder()
    my_character = CharacterAnalyser()
    my_word = WordAnalyser()
    my_sentence = SentenceAnalyser()
    
    print(my_decoder) # Print the readble format of Morse Code table.

    # A menu with options allowing the user to select which level of analysis is intended.
    character_option = input("Count character or not? Enter T or F : ")
    word_option = input("Count word or not? Enter T or F : ")
    sentence_option = input("Count sentence or not? Enter T or F : ")
    
    total_sequence = ''
    # Prompt the user to input any random sequences of Morse Code.
    user_input = input("Please enter a Morse Code sequence. Press Enter to quit. \n")
    while user_input != '':
        decoded_sequence =  my_decoder.decode(user_input) # Perform the decoding on each sequence.
        print(decoded_sequence) # Display the decoded sequence.
        total_sequence = total_sequence + decoded_sequence + ' '
        user_input = input("Please enter a Morse Code sequence. Press Enter to quit. \n")
    
    # Options of execution    
    if character_option == 'T':
        my_character.analyse_characters(total_sequence) # Determine the total number of occurrences for each of the letters and numerals.
        print(my_character) # Print the total occurrences of characters.
    if word_option == 'T':
        my_word.analyse_words(total_sequence) # Determine the total number of occurrences for each word.
        print(my_word) # Print the total occurrences of words.
    if sentence_option == 'T':
        my_sentence.analyse_sentences(total_sequence) # Determine the total number of occurrences for each sentence.
        print(my_sentence) # Print the total occurrences of sentences.
    
if __name__ == '__main__':
    main()
        


