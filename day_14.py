#Day 14:python fundamental

# 'function'
"""
1.A function is a block of code which only runs when it is called.
2.A function can return data as a result.
3.A functin helps avoiding code repetition.
4.A function is defined using the "def" keyword.
"""
def my_function ():
    print("Hello from a function")
my_function()     #calling the function 

#calling a function multiple time
def my_function ():
    print("Hello from a function")
my_function()     
my_function()
my_function()

#without function same calculation need reatedly.
#convert fahrenheit to celsius with function

def temperature(fahrenheit):
    return (fahrenheit-32)*5/9
print(temperature(77))
print(temperature(52))
print(temperature(89))

#Return values
"""
Function can send data back to the code that called using return statement.
When a function reaches a return statement ,it stops executing and sends the result back.

"""
def gretting():
    return "Hello function"
msg=gretting()
print(msg)

#return value directly
def gretting():
    return "Hello function"
print(gretting())

#Pass statement
def my_function():
    pass
     #pass statement used when define structure first and implement detail later.










