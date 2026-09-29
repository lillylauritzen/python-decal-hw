#goodbye 
name = ("Lilly")
def say_goodbye(name):
    print("Goodbye,", name) 
say_goodbye(name)

#area of a circle
def area_of_circle(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    # The text must be enclosed in quotes after the 'f'
    print(f"with radius {radius}, the area of the circle is {area}") 

area_of_circle(3)

#subraction
def subtract(a, b):
    return a - b
print(subtract (5, 2))
 
#multiplication 
def multiply(a, b):
    return a * b 
print(multiply (50, 4))
# 50 x 4 = 200

#division 
def divide(a, b):
    return a / b
print(divide (81, 9))
# 81/9 = 9

# finding max and min of list of temperatures to determine what to wear
temperatures = [70, 66, 69, 72, 64, 76, 74, 61, 59, 65]

print(f"{min(temperatures)} , {max(temperatures)}")
print(f"the max temperature is {max(temperatures)}. Consider sunscreen!")
print(f"the min temperature is {min(temperatures)}. Make sure to budle up!")

#weekend with integers
Monday = 1
Tuesday = 2
Wednesday = 3
Thursday = 4
Friday = 5
Saturday = 6
Sunday = 7

def is_weekend(day):
    if day == 6 or day == 7:
        return True
    else: 
        return False

print(is_weekend(6))
print(is_weekend(3))

# divide miles/gallon to get fuel efficiency 
def divide(m, g):
   return m / g
print(divide (923, 39))

#encryption
def encrypt(int):
    last_digit = int % 10 
    remaining = int // 10 
    return last_digit * 10 ** len(str(remaining)) + remaining
print(encrypt(1234567))

#min & max with loops
def power(base, exponent):
    answer = 1;
    for _ in range(exponent):
        answer *= base
    return answer
print(power(3, 4))

#for loops
def min(numbers):
    minimum = numbers[0]
    for number in numbers: 
        if number < minimum: 
            minimum = number
    return minimum

def max(numbers):
    maximum = numbers[0]
    for number in numbers: 
        if number > maximum: 
            maximum = number
    return maximum

numbers = [3, 5, 7, 8, 4, 1]
print(min(numbers))
print(max(numbers))

#while loops
def minimum(numbers):
    minimum = numbers[0]
    index = 1
    while index < len(numbers):
        if numbers[index] < minimum:
            minimum = numbers[index]
        index += 1
    return minimum   

def maximum(numbers):
    maximum = numbers[0]
    index = 1
    while index < len(numbers):
        if numbers[index] > maximum:
            maximum = numbers[index]
        index += 1
    return maximum

numbers = [3, 5, 1, 6, 4, 10]
print(minimum(numbers))
print(maximum(numbers))

#calculate the sum
def sum_digits(number):
    total = 0
    while number > 0:
        total += number % 10
        number //=10
    return total
print(sum_digits(85902539))



print("my favorite function was the encryption function.")
#encryption

x = 1234567
result = encrypt(x)

print(f"The result of Secret Code (5.4) is {result}")