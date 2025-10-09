def is_palindrome(n):
    return str(n) == str(n)[::-1]


print(is_palindrome(12321))
print(is_palindrome(31215))