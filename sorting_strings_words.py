# Task: Sorting the words alphabetically without caring for their capitalization
# Input: A string of words separated by commas
# Output: A string of words sorted alphabetically
# Method: Using a function to perform this task

string = input("Enter your string : ")


def sorting_words(user_string):
    word = user_string.split()
    sorted_words = sorted(word, key=str.lower)
    str1: str = " "
    return str1.join(sorted_words)


print(sorting_words(string))

