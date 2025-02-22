#python internship task 1:
# 1:create a python script that declares the variable in which print all information about yourself.
#variables:
#variable is the name of memory location in which we can stored different types of values. 
name= "Gulshan Mushataq"
gender= "female"
age= 25
Adress= "Bagh Azad kashmir"
degree= "BS Software Engineering"
dob= "2nd janurary 2000"
university= "virtual university of pakistan"
print(name, "\n", gender,"\n", age, "\n",Adress,"\n",degree,"\n",dob,"\n", university)

# 2: write a python script that declares type casting while swaping two variables and print before and afer swaping.
#Before swaping
x= 13
y=12

temp= x
print("The value of temp valriable is",temp)
x=y
print("The value of x is", x)
y= temp
print("The value of y is ", y)
#After swaping
# 3: declare a variable with different data types in python and display along variable with data types.
#variable has different data types like(integer, float, string, boolean, list, tuple, dictionary, set, nonetype)

integer_var = 10  # Integer
print(type(integer_var))
float_var = 10.5              # Float
print(type(float_var))
string_var = "Hello, World!"  # String
print(type(string_var))
boolean_var = True            # Boolean
print(type(boolean_var))
list_var = [1, 2, 3, 4]       # List
print(type(list_var))
tuple_var = (5, 6, 7)         # Tuple
print(type(tuple_var))
dict_var = {"name": "Alice", "age": 25}  # Dictionary
print(type(dict_var))
set_var = {1, 2, 3}           # Set
print(type(set_var))
none_var = None               # NoneType
print(type(None))

                    #task 2
# 1:write a python script using two variables and perform the following operations addition subtraction multiply division and Module.
a= 10
b= 5
print(a+b) #Addition
print(a-b) #subtract
print(a*b) #Multiply
print(a/b) # divide
print(a%b) #Module
# 2:using two numerical variables and write python scripts to compare them using comparision operations:
# Define two numerical variables
a = 15
b = 3

# Perform comparison operations
equal = a == b
not_equal = a != b
greater_than = a > b
less_than = a < b
greater_or_equal = a >= b
less_or_equal = a <= b

# Print results
print("Equal:", equal)
print("Not Equal:", not_equal)
print("Greater Than:", greater_than)
print("Less Than:", less_than)
print("Greater or Equal:", greater_or_equal)
print("Less or Equal:", less_or_equal)
# 3: Demonstrating Assignment Operators in Python

def assignment_operators_demo():
    # Simple assignment
    x = 10
    print("Initial value:", x)
    
    # Add and assign
    x += 5  # Equivalent to x = x + 5
    print("After x += 5:", x)
    
    # Subtract and assign
    x -= 3  # Equivalent to x = x - 3
    print("After x -= 3:", x)
    
    # Multiply and assign
    x *= 2  # Equivalent to x = x * 2
    print("After x *= 2:", x)
    
    # Divide and assign
    x /= 4  # Equivalent to x = x / 4
    print("After x /= 4:", x)
    
    # Floor divide and assign
    x //= 2  # Equivalent to x = x // 2
    print("After x //= 2:", x)
    
    # Modulus and assign
    x %= 3  # Equivalent to x = x % 3
    print("After x %= 3:", x)
    
    # Exponentiate and assign
    x **= 2  # Equivalent to x = x ** 2
    print("After x **= 2:", x)
    
    # 4: Define logic operators and define  boolean variables and logic operators. 
a = True
b = False
c = True

# Demonstrate logical AND
and_result = a and b
print(f"Logical AND: {a} and {b} = {and_result}")

# Demonstrate logical OR
or_result = a or b
print(f"Logical OR: {a} or {b} = {or_result}")

# Demonstrate logical NOT
not_a = not a
not_b = not b
print(f"Logical NOT: not {a} = {not_a}")
print(f"Logical NOT: not {b} = {not_b}")

# Evaluate complex logical expressions
complex_expression1 = (a and b) or not a
complex_expression2 = (not a or b) and (a or not b)
print(f"Complex Expression 1: (a and b) or not a = {complex_expression1}")
print(f"Complex Expression 2: (not a or b) and (a or not b) = {complex_expression2}")

# Additional examples
# Combining multiple logical operators
combined_expression = (a or b) and (b or c)
print(f"Combined Expression: (a or b) and (b or c) = {combined_expression}")

# Checking equality with logical operators
equality_check = (a == c) and (b != c)
print(f"Equality Check: (a == c) and (b != c) = {equality_check}")

# Using logical operators with numeric values
num1 = 5
num2 = 10
num3 = 0
numeric_logic = (num1 > num3) and (num2 > num1)
print(f"Numeric Logic: (num1 > num3) and (num2 > num1) = {numeric_logic}")

