#Day 13:python fundamental

#For loop
    #for loop is used iterating over a sequence i.e. list,tuple,dict,string
    #in for loop we can execute a set of statements,once for each item in a list,tuple,set etc.

#print each fruit
fruits=['apple','banana','cherry']
for x in fruits:
    print(x)


#looping through string

for x in 'banana':
    print(x)


#break statement
   #with break statement we can stop the loop before it has looped through all the items.
#exist loop when x in 'banana'
fruits=['apple','orange','banana','cherry']
for x in fruits:
    print(x) 
    if x=='banana':      
       break   

#exist loop when x is 'banana' ,but this time break comes before the print.
for x in fruits:   
    if x=='banana':
       break
    print(x)

#continue statement
fruit=['apple','orange','banana','cherry']
for x in fruit:
    
    if x =='banana':
           continue
    print(x)  
  
#range() function
   #to loop through a set of code a specified no. of times,we can use range()
   # the range() returns a sequence of numbers,starting from o by default,and
   # increment by 1 by default,and ends at a specified number.

for x in range(7):   #values from 0-6 not including 7
    print(x)    

#using start parameter
for x in range (3,8):  #value from 3-7
    print(x)

#set increment 3 by adding third parameter
for x in range(2,40,4):
    print(x)


#else in for loop
   #else keytword in a for loop specified a block of code to be executed when the loop is finished.

#print all numbers from 0 to 5 and print a msg when loop has ended.

for x in range(6):
    print(x)
    if x==5:              #if is possible just i known by testing
        print("last element of loop")
else:
    print("loop finished")

#nested loop
  #nested loop is a loop inside a loop.
  #The inner loop will execute one time for each iteration of the outer loop.

#print each adjective for every fruit:
adj=['red','big','tasty']
fruits=['apple','banana','cherry']
for x in adj:
    for y in fruits:
        print(x,y)   #this print like'red apple','red banana' for each iteration

 #if we print below print method that print 
 # red                                    
 #apple
 #red
 #banana    like iteration
        print(x)
        print(y)


#pass statement

for x in [0, 1, 2]:
  pass

# having an empty for loop like this, would raise an error without the pass statement

"""
 Problem Statement:
 A Google cloud instance is emitting a continuous stream of system event codes. We need 
 a scanner that processes these codes in order. The scanner must tally healthy events, 
completely ignore minor warning codes to save processing power, and immediately shut down
the scan if a critical system failure code is detected.
"""

# System event codes: 100-199 (Healthy), 200-299 (Warnings), 999 (Critical Failure)
event_log_stream = [101, 204, 102, 105, 201, 103, 999, 104, 202]

print("="*60)
print("     GOOGLE INFRASTRUCTER LOG SCANNER      ")
print("="*60)

print("[SCANNER INITIALIZED]")
print("processing event stream logs...")

print("\n")
print("[PARSING TELEMETRY]")
healty_count=0
for x in event_log_stream:
    if x in range(100,200):
        print(f"[+] SUCCESS: Event {x} registered.")
        healty_count+=1
    elif x in range(200,999):
        continue
    elif x==999:
        print(f"[!] CRITICAL FAILURE: Code {x} detected! Halting loop.")
        break
else:
    print("[STREAM ANALYSIS COMPLETE]")

print(f"Total healty event logged:{healty_count}")
print("="*60)
    





