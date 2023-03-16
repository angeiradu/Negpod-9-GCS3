#Write a program that given a string.
#Print all consonant letters except vowels.
#Letter Y should be considered a vowel.
# The user converts all words entered to lowercase.

w=input("please enter a word:").lower()

v=['i','u','o','a','e','y']

#loop through each letter in the word
i=0
while i<len(w):
    if w[i] not in v:
        print(w[i])
    i+=1    
