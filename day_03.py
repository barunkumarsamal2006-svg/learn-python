#day 03:python fundamental

#operators
#assignment operator

saving=100
saving+=50
saving*=3
saving-=5
print(saving)

#ternary operator

is_logged_in = False
status='welcome!' if is_logged_in  else 'please log in '
print(status)

#comparison operator

def is_valid_target(num, lower,upper):
    if num > lower and num < upper :
        return True
    else :
        return False
print(is_valid_target(7,1,5))

# logical operator

def can_enterclub(age, has_ticket, is_banned):
    if age >= 18 and has_ticket :
       return 'you are allowed to enter the club'
    elif is_banned:
        return'you are banned from entering the club'
    else:
        return 'you are not allowed to enter the club'
print(can_enterclub(20, True, False))    
    
#identity operator

def verify_identity(list1,list2):
    if list1 is list2:
        return 'same object'
    elif list1 == list2:
        return 'same values but different objects'
    else:
        return 'different values'
    
my_list = ['apple', 'banana']    
print(verify_identity(['apple', 'banana'], ['apple', 'banana'] ))


