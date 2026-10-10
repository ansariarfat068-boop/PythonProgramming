
def check_palindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    if original == reverse:
        return "PALINDROME"
    else:
        return "NOT PALINDROME"


print(check_palindrome(121))
print(check_palindrome(123))
print(check_palindrome(1221))
print(check_palindrome(7))
print(check_palindrome(10))

