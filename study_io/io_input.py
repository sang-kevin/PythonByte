# coding=utf-8

test = "上海自来水来自海上"
print(test)
print(test[::-1])

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)


something = input("Enter text: ")
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")

