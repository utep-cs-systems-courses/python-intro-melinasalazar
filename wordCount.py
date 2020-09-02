import sys
import string 

filename = sys.argv[1] #First input file argument
output_file = sys.argv[2] #Second output file argument

in_file = open(filename, "r")  
file_read = in_file.read()

words = file_read.strip().lower() #Remove newlines and spaces/ Make all words lowercase

def wordCount (words):
    list_words = [] #Store list of words here

    words = words.translate(words.maketrans("", "", string.punctuation)) # Remove any punctuation marks from list i.e. . , ; : '' "" -
    
    final_words = words.split() #Split list into words

    set_words = set(final_words) #Create a set of words

    sort_words = sorted(set_words) #Sort words in alphabetical order

    output = open(output_file, "w")
    for word in sort_words: 
    	output.write(word + " %s\n"%final_words.count(word))
    	#print(word+ " %s"%final_words.count(word))
    output.close()

wordCount(words)
