# File: homework1.py.

# --- Variable and Data Types --- 
a=10
print(a)
print(type(a))
# a is an integer, a whole number with no decimals

b=1.5 
print(b)
print(type(b))
# b is a float, a number with decimals

c=3j 
print(c)
print(type(c))
# c is a complex number, a number with a real and imaginary part

d="Hello"
print(d)
print(type(d))
# d is a string, a sequence of characters

e=[1, 2, 3]
print(e)
print(type(e))
# e is a list, an ordered collection of items

f={"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f))
# f is a dictionary, an unordered collection of key-value pairs

g=(1, 2)
print(g)
print(type(g))
# g is a tuple, an ordered collection of items that cannot be changed

h=["apple", "banana", "strawberry"]
print(h)
print(type(h))
# h is a list, an ordered collection of items

i = True 
print(i)
print(type(i))
# i is a boolean, a data type that can only be True or False

j = None
print(j)
print(type(j))
# j is a NoneType, a data type that represents the absence of a value

k=[True, "blue", 12]
print(k)
print(type(k))
# k is a list, an ordered collection of items

l=str(14)
print(l)
print(type(l))
# l is a string, a sequence of characters

m=1e4
print(m)
print(type(m))
# m is a float, a number with decimals

""" 
Q: 1 
I found 9 different data types in the code.

Q: 2
I found integers, floats, complex numbers, strings, lists, dictionaries, tuples, booleans, and NoneType in the code.

Q: 3
Floats: 1.5, 1e4
Lists: [1, 2, 3], ["apple", "banana", "strawberry"], [True, "blue", 12]
Strings: "Hello", str(14)

Q: 4
str() is a function that converts a value into a string data type. In the code, it is used to convert the integer 14 into a string.

Q: 5
I chose the data type of a range because that was not previously mentioned.
 """

r=range(32, 93, 238)
print(r)
print(type(r))
# r is a range, a data type that represents a sequence of numbers.


# --- Booleans --- 
print(10 > 9) 
# True, 10 is greater than 9

print(10 == 9)
# False, 10 is not equal to 9

print(10 <= 9)
# False, 10 is not less than or equal to 9

print(bool("abc"))
# True, a non-empty string is truthy

print(bool(123))
# True, a non-zero number is truthy

print(bool(["apple", "cherry", "banana"]))
# True, a non-empty list is truthy

print(bool(True))
# True, the boolean value True is truthy

print(bool(False))
# False, the boolean value False is falsy

print(bool(0))
# False, the integer 0 is falsy

print(bool(""))
# False, an empty string is falsy

print(bool(" "))
# True, a string with a space is truthy

print(bool(()))
# False, an empty tuple is falsy

print(bool([]))
# False, an empty list is falsy
 
print(bool({}))
# False, an empty dictionary is falsy

print(bool(True and False))
# False, True and False is False

print(bool(True and True))
# True, True and True is True

print(bool(False and False))
# False, False and False is False

print(bool(True or False))
# True, True or False is True

print(bool(True or True))
# True, True or True is True

print(bool(False or False))
# False, False or False is False

print(bool(not(False)))
# True, not False is True

print(bool(not(True)))
# False, not True is False

"""
Q: 1 The pattern I noticed is that any non-empty value is considered truthy, while empty values are considered falsy.
Q: 2 I was surprised to learn that the boolean value of a string with a space is True, while an empty string is False. 
Q: 3 print(bool("hello")) would return True, because a non-empty string is truthy.
Q: 4 print(bool(0.0)) would return False, because the float 0.0 is falsy.
"""

# --- Operators --- 
# Arithmetic Operators
print(10 + 5) 
# Output: 15, addition operator adds two numbers

print(10-5) 
# Output: 5, subtraction operator subtracts the second number from the first

print(2*4) 
#Output: 8, multiplication operator multiplies two numbers

print(6/3) 
# Output: 2.0, division operator divides the first number by the second

print(5/2) 
# Output: 2.5, division operator divides the first number by the second

print(3**2) 
# Output: 9, exponentiation operator raises the first number to the power of the second

print(15//2) 
# Output: 7, floor division operator divides the first number by the second and rounds down to the nearest whole number

#Operators: Comparison Operators
x=5
x += 5
x -= 4
x *= 3

#Operators: Logical Operators
"""
Q:1 The and operator returns True if both operands are True. 
5<10 and 2==2 would return True, because both conditions are True.
5<7 and 3==1 would return False, because the second condition is False.
Q:2 The or operator returns True if at least one operand is True
6=7 or 3==3 would return True, because the second condition is True.
6=7 or 3==1 would return False, because both conditions are False.
Q:3 The not operator returns the opposite boolean value of the operand.
not(True) would return False, because the operand is True.
not(False) would return True, because the operand is False.
"""

# more questions
"""
Q:1 the difference between / and // is that / performs regular division and returns a float, while // performs floor division and returns an integer.
Q:2 the difference between % and // is that % returns the remainder of a division operation, while // returns the quotient rounded down to the nearest whole number.
Q:3 the % operator is used to find the remainder of a division operation. 
10 % 3 would return 1, because 10 divided by 3 is 3 with a remainder of 1.
Q:4 Assignment operators are used to assign values to variables.
"""

# --- Strings --- 
my_string = "Hello"

print(my_string) 
# Prints: Hello

print(my_string[0]) 
# Prints: H, the first character of the string

print(my_string[1]) 
# Prints: e, the second character of the string

print(my_string[2]) 
# Prints: l, the third character of the string

print(my_string[3]) 
# Prints: l, the fourth character of the string

print(my_string[4]) 
# Prints: o, the fifth character of the string  

print(my_string[-1]) 
# Prints: o, the last character of the string

print(my_string[1:3]) 
# Prints: el, the characters from index 1 to 2 (3 is not included)

print(my_string[0:5:2]) 
# Prints: Hlo, the characters from index 0 to 4 with a step of 2

print(len(my_string)) 
# Prints: 5, the length of the string

print(my_string + "goodbye") 
# Prints: Hellogoodbye, concatenation of two strings

print(my_string * 7) 
# Prints: HelloHelloHelloHelloHelloHelloHello, repetition of the string 7 times

"""
Q:1 slicing is a way to extract a portion of a string by specifying the start and end indices.
Q:2 name=Oski 
print("Hello, my name is", name) would return "Hello, my name is Oski", because the variable name is concatenated with the string using a comma.
Q:3 name=Oski
print(f"Hello, my name is {name}") would return "Hello, my name is Oski", because the f-string allows for variable interpolation.
Q:4 the difference between using a comma and an f-string is that a comma separates the string and variable with a space, while an f-string allows for variable interpolation within the string.
"""

# --- Terminal Commands --- 
"""
cd 
changes the current directory to the specified directory. Use it to move from one folder to another
Example: cd Documents

ls
lists the files and directories in the current directory. Use it to see what files are in a folder
Example: ls 

ls -a 
lists all files and directories, including hidden ones, in the current directory. 
Example: ls -a

mkdir
creates a new directory with the specified name. Use it to create a new folder
Example: mkdir new_folder

cat
displays the contents of a file in the terminal. Use it to read the contents of a
Example: cat file.txt

pwd
prints the path of the current directory. Use it to see where you are in the file system.
Example: pwd

cd ..
moves up one directory level. Use it to go back to the previous folder or parent directory.
Example: cd ..

cd . 
stays in the current directory. Use it to remain in the same folder.
Example: cd .

cd ~ 
moves to the home directory. Use it to quickly navigate to your home folder.
Example: cd ~

cp 
copies a file or directory to a specified location. Use it to duplicate files or folders.
Example: cp file.txt /path/to/destination 

mv
moves a file or directory to a specified location. Use it to rename files or folders, or to move them to a different location.
Example: mv file.txt /path/to/destination

rm
removes a file or directory. Use it to delete files or folders.
Example: rm file.txt

clear
clears the terminal screen. Use it to remove all previous commands and outputs from view.
Example: clear

grep
searches for a specified pattern in a file or input. Use it to find specific text withinq files or outputs.
Example: grep "pattern" file.txt

Q:1 3 additional commands are touch, which creates a new empty file; echo, which prints text to the terminal; and history, which displays a list of previously executed commands.
Q:2 the difference between ls and ls -a is that ls lists only the visible files and directories in the current directory, while ls -a lists all files and directories, including hidden ones.
Q:3 a hidden file is a file that is not normally visible in the file system, and its name usually starts with a dot (.) to indicate that it is hidden. Hidden files are often used for configuration or system files that are not meant to be modified by the user.
Q: 4 -l display detailed information abou teach file, including permissions, ownership, size, and modification date. -h displays file sizes in a human-readable format (e.g., KB, MB, GB). -r lists files in reverse order. -t sorts files by modification time, with the most recently modified files listed first.

"""