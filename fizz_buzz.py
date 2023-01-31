def fizzBuzz(start, stop):
    for x in range(start, stop+1):
        if x %3 == 0 and x %5 == 0:
            print("FizzBuzz!")
        elif x %3 == 0:
            print("Fizz")
        elif x %5 == 0:
            print("Buzz")
        else:
            print(x)

print(fizzBuzz(1, 30))

# prints:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz!
# 16
# 17
# Fizz
# 19
# Buzz
# Fizz
# 22
# 23
# Fizz
# Buzz
# 26
# Fizz
# 28
# 29
# FizzBuzz!