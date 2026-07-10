#Day 10:python fundamental

# python shorthand if
#shorthand if
       #shorthand help to statement execute in dame line as the if statement

a=10
b=9
if a>b :print("a is greater")

#shorthand if..else

x='barun'
print('a is present') if 'a' in x else print("not")
       
#assign a value with if..else

is_valid=True
pancard='valid' if is_valid else 'invalid'
print(f'pancard is {pancard}') #same like ternary operator

#multiple condition on one line 

emp1=50000
emp2=40000
print("emp1 high salary") if emp1>emp2 else print("emp2 high salry") if a<b else print("equaal")

# notes for shorthand
#  +the condition and action are simple.
#  +it improves code readability.
#  +You want to make a quick assignment based on a condition


#python logical operators in if

temperature = 25
is_raining = False
is_weekend = True

if (temperature > 20 and not is_raining) or is_weekend:
  print("Great day for outdoor activities!")
else:
  print("stay home or go office ")


#Nested if statement
   #nested if used in inside if statement .
   #it slight concept of elif but not that much because if inner outer if execute true then inner is run
   #also inner if have its else chain
   
score =50
attendance=75
submitted=True

if attendance >= 75:
  print("will take exam")
  if score >=70 :
    print("Also a good scorer")
    if score >=30:
      print("average scorer")
      if submitted:
       print("Your year is clear")
      else:
       print("pass but project need to submit.")
    else:
      print("fail in exam")
  else:
    print("avg student")
else:
  ("year is back.")    


Score = 92
extra_credit = 5

if Score >= 90:
  if extra_credit > 0:
    print("A+ grade")
  else:
    print("A grade")
elif Score >= 80:
  print("B grade")
else:
  print("C grade or below")



#Pass statement

 #pass statement is null operation .when execute nothing happen.
 #uses: +when you are design your program str and want to implement taht logic later.
 #      +use when want to nothing can happen in specific condition.
 #      +Creating exception types or quick data structures that don't need custom methods.


a1=90
a2=80

if a1> a2 :
  pass
else:
  print("grade A")


#w3 school code challenge:
age=20
if age < 13:
  print("Child")
elif age < 18:
  print("Teenager")
else:
  print("Adult")




#Today practice question
"""
Problem Statement:
Google Cloud Platform (GCP) dynamically provisions high-performance 
computing clusters for AI workloads. Before spinning up expensive TPUs (Tensor
Processing Units), our orchestration module runs a strict gatekeeper script.
 
You need to write an evaluation engine that uses logical operators, 
shorthand notation, and nested checks to decide if a provisioning request passes
 security and budget constraints.
"""

user_role = "RESEARCHER"    # Roles can be: "ADMIN", "RESEARCHER", "GUEST"
requested_tpus = 8          # Number of TPU cores requested
budget_approved = True      # Budget allocation flag
is_billing_delinquent = False # If True, immediately lock out regardless of role

print("=============================================")
print("     GCP AI CLUSTER PROVISIONING ENGINE      ")
print("=============================================")

print("[REQUEST LOG]")
print(f"*Requester Role:{user_role}")
print(f"*Allocation Size: {requested_tpus} TPU Cores")
print("\n")

print("[PROVISIONNING DECISION]")

if is_billing_delinquent :
  print("Result Status    : REQUEST DENIED - ACCOUNT LOCKED (BILLING)")
  

elif user_role is 'ADMIN':
 pass
 print("Result Status    : REQUEST GRANTED - ADMIN AUTOMATIC BYPASS")
 

elif user_role is "RESEARCHER":
    if budget_approved is True and requested_tpus <= 8:
      print("Result Status: REQUEST GRANTED - PROVISIONING CORES")
    elif requested_tpus > 8 and budget_approved is not True:
      print("Access Denied")
else:
  print("Result Status    : REQUEST DENIED - POLICY OR BUDGET VIOLATION")

    
cluster_health= "HIGH_LOAD" if requested_tpus > 4 else "NORMAL"
print(f"Cluster Status:{cluster_health}")
print("\n")

print("=============================================")
print("Execution Status:NOMINAL | Token Commited")



