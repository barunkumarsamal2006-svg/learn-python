#Day 02 :python fundamental

#strings


print('nice day "today"')

x='me'
print(x)

a="""
   today is wenesday day
   i continue my journey 
   of python"""
print(a) #multiline string

b='today '
print(len(b)) #length of string

name='barun'
print('a' in name) #check if 'a' is in name

#check with if statement
txt='github is a platform '
if 'github' in txt:
    print('yes')
else:
    print('no')

#check if not in string only use not before the in

# slicing
a='ramayan'
b='hanuman'
print(a[:3]) 
print(b[-3:])

#modify
#   upper
#   lower
#   strip
#   replace
#   split
  
#concatenation
x='barun'
y='samal'
#in cancatination of string
z=a+b
print(z )

#format string
'''
in fstring we can add number and string in the same string
also variable can be added in the string through fstring {}
also perform operation
'''
x='barun'
age=20
print(f'my name is {x} and age {age:.2f}')

print(min(55,16,7))
print(max(55,16,7))

'''
🛒 The Problem: 
"The Smart Bill Generator"You are building a basic checkout system for an online store. 
Write a Python script that calculates the final bill for a customer, applies a discount 
code if they are eligible, and prints a clean invoice.
'''

product_price=1250.50
quantity_purchased=3

subtotal=product_price*quantity_purchased
is_premium_member=True
if is_premium_member is True:
    discount=200
else:
    discount=0

final_total=subtotal-discount
print(final_total)
print('Thank you for shopping with us!')






