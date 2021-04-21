#readFromTextFile.py
#A script that will read from text file and output to string

#Open the text file to a string variable

#Definition of variables to be checked

vowels = ['a','e','i','o','u']
try:
    s = open("example.txt").read()
    
    vowelCount = 0
    consonantCount = 0
    wordCount = len(s.split())

    print(s)

    for x in s:
        if x in vowels:
            vowelCount += 1
        elif x.isalpha():
            consonantCount += 1

    print("This file contains", wordCount, "words")
    print("This file contains", vowelCount, "vowels")
    print("This file contains", consonantCount, "consonants")

except:
    print("ERROR FILE NOT FOUND")
