def palindrom(word):
    if word == word[::-1]:
        print("palindrome")
    else:
        print("not a palindrome")
word = input()
palindrom(word)