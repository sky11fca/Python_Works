def is_palindrome(a):
    copy_a = str(a)
    return copy_a == copy_a[::-1]


print(f"number 12321 is a palindrome: {is_palindrome(12321)}")
print(f"number 31215 is a palindrome: {is_palindrome(31215)}")
