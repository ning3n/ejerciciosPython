for n in range(1, 101):
    divisibleByThree = n % 3 == 0
    divisibleByFive = n % 5 == 0
    if divisibleByThree and divisibleByFive:
        print("FizzBuzz")
    elif divisibleByThree:
        print("Fizz")
    elif divisibleByFive:
        print("Buzz")
    else:
        print(n)
