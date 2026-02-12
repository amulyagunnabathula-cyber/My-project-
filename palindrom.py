
a = {"abba", "bbaa", "abbaba", "bbaabb"}
for word in a:
    if word == word[::-1]:
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")
