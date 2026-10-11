
def prime_numbers(start, end):
    primes = []

    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)

    return primes


if __name__ == "__main__":
    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))
    print(prime_numbers(start, end))
