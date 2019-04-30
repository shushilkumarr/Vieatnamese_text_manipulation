# Vieatnamese_text_manipulation

this is a simple text manipulation program that decodes the vietnamese text and finds the words using a key in the desending order of its frequency.

## Algorithmm

1) first step is to analyse the character mappings given in the text file.
2) replace the parts of words by matching the mappings.
    
    2.1) give a score to each mapping such that higher score mappings are given priority over lower ones.
    
    2.2) apply the rules in the desending order of score.
    
3) save the new list in a file.
4) create a dictionary with first letter of the words as the key to optimise the search.
5) get the key from the user and search the words whose start matches the key.
6) print the results in the decreasing order of their frequencies.
