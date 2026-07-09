#Day 9:python fundamental

#skip list for few days after loop and function is finished i start list

#python if statement

# python condition and if statement
  #python supports usual logical condition:
          #a==b,a!=b,a<b,a>b,a<=b,a>=b

x=15
y=12
if x >= y :
    print("x is greater")

#multiple statement in if block

age=19
if age >=18:
    print("you are a adult")
    print("you are eligible for vote.")
    print("you eligible for go to jail. ")
    

#using variable in condition
is_vip_member=True
if is_vip_member:
    print('access the pro version')


#python elif statement
    #this use for multiple condition for true 


a=33
b=33
if a < b:
    print('a is greater')
elif a==b:
    print("a is equal to b")
    
#multiple elif statement

score=float(input("enter your score"))
if score >=90:
    grade="A"
elif score >=80:  #use elif more efficient than separate if because python stop checking once it find true.
    grade="B" 
elif score >=70:
    grade="C"
elif score >=70:
    grade="D"     #in elif that evaluate top to buttom and print first true condition even after that condition is also true.

print(f"your grade is:{grade}")    


#Else keyword
     #else is prinyt when if and elif condition is false.
     #Also when none of the upper condition is true.
     #we use else in with elif and also without elif but if is constant.
     #this useful for error handling,validation and provide default value.

#with elif
number = 7

if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")    

#without elif
temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")


#today practice question

"""
Problem Statement:
Google Cloud Identity and Access Management (IAM) systems evaluate incoming security tokens to grant or deny server room access.
You need to write an automated evaluation block that checks an employee's clearance tier, their security keys, and system override
flags to determine system access.
"""
employee_name = "Barun"
clearance_level = 3        # Scale of 1 to 5 (Level 5 is highest)
has_valid_mfa = True       # Multi-Factor Authentication token status
is_emergency_override = False # Global datacenter safety override flag


print("=============================================")
print("      GOOGLE IAM AUTOMATED ACCESS LOG        ")
print(f"Target Engineer: {employee_name}")
print(f"Clearance Metric: Level{clearance_level}")
print("Security Protocol : Evaluating Criteria...")

print("\n")
if is_emergency_override is True:
   print("\n[ACCESS DECISION]:Granted ")
   print("[SECURITY ALERT]  : CRITICAL OVERRIDE ACTIVATED")

elif clearance_level > 3 and has_valid_mfa:
   print("[ACCESS DECISION]:Granted - Admin Access")
   print("[SECURITY ALERT]  : SECURITY VIOLATION LOGGED")


elif clearance_level <= 3 and has_valid_mfa:
   print("[ACCESS DECISION]:Granted - Engineer Access")
   print("[SECURITY ALERT]  : SYSTEM SECURE / NOMINAL")

elif has_valid_mfa is False:
   print("[ACCESS DECISION]:Denied-'MFA BREACH'")
   print("[SECURITY ALERT]  : SYSTEM SECURE / NOMINAL")


else:
   print(" INSUFFICIENT PRIVILEGES")
   print("[SECURITY ALERT]  : ACCESS BLOCKED")

print("==============================================")
print("Execution Status: SUCCESS | Canary Safe")