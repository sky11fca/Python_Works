def is_palindrome(a):
    copy_a = a
    palindrome=0
    while copy_a:
        palindrome, copy_a = palindrome*10+copy_a%10, copy_a//10

    return a==palindrome


print(f"number 12321 is a palindrome: {is_palindrome(12321)}")
print(f"number 31215 is a palindrome: {is_palindrome(31215)}")
