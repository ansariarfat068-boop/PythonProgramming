def check_prime(num):
    if num<=1:
        return "NOT PRIME"
    for i in range(2,num):
        if num % i == 0:
            return "NOT PRIME"

        return "PRIME"


print(check_prime(7))
print(check_prime(29))
print(check_prime(6))
print(check_prime(18))
print(check_prime(1))    