from difflib import get_close_matches
lst1 = ["apple", "mango", "banana", "orange"]
yn = input("Did you mean % s instead? Enter Y if yes, or N if no: " %
           get_close_matches)
