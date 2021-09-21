"""Dictionary
            by Harshit Sharma """
import json

data = json.load(open("dictionary.json"))
#
#
# def SearchWorch():
#    word = print(input("enter the word you want to search: "))
#    word = str(word)
#    word = word.lower()
#    if word in data:
#        print(data[word])
#    else:
#        print("try again")
#
#
# SearchWorch()
word = print(input("enter the word you want to search: "))
word = str(word)
word = word.lower()
if word in data:
    print(data[word])
else:
    print("try again")
