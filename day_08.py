#Day 08:python fundamental

#loop list
#loop through a list

list1=['apple','banana','orange']

for fruits in list1: #use for loop for looping the list
    print(fruits)    #the use variable fruits that use your suitable words and letter

#loop through  the index number 

list2=['cherry','kiwi','papaya']

for fruits in range(len(list2)):
    print(list2[fruits])

#while loop

list3=['cherry','kiwi','papaya']

i=0
while i < len(list3): #len() usee to determine the length of the list then start at 0 
                    # and loop your way through the list items by referring to their indexs.
    print(list3[i]) #looping through while 
    i=i+1

#looping using list comprehension

list4=['cherry','kiwi','papaya']
[print(fruits) for fruits in list4] #list comprehension offers the shortest syntax for looping through lists


#today practice question


# ==============================================================================
# GOOGLE ENGINEERING TICKET: #2026-D8-A
# Component: infrastructure-load-balancer
# ==============================================================================

# Input Data Stream (Ping latencies in milliseconds)
ping_latencies = [120, 80, 195, 75, 110, 220, 95, 130, 185, 60]

print("==================================================")
print("        NETWORK LOAD BALANCER TELEMETRY          ")
print("==================================================")
print("[TELEMETRY SCAN ACTIVATED]")

# Initialize our explicit index pointer at the first node
i = 0

# Process the stream using a manual while loop for pointer control
while i < len(ping_latencies):
    current_latency = ping_latencies[i]
    
    # Check for critical latency threshold
    if current_latency > 150:
        # Calculate reduction value needed to hit the target baseline of 50ms
        reduction = current_latency - 50
        
        # Modify the original list in-place (O(1) auxiliary space optimization)
        ping_latencies[i] = 50
        
        # Log the incident metrics to the terminal dashboard
        print(f"* CRITICAL: Node Index {i} ({current_latency}ms) -> Reducing by {reduction}ms.")
        print("* INFO    : Neighbor Node skipped due to traffic migration.")
        
        # CRUCIAL NOOGLER ARCHITECTURE: Advance by 2 to completely jump 
        # past the immediate neighbor node
        i += 2
    else:
        # Normal node: Leave value untouched and advance pointer by 1
        i += 1

print("\n[POST-OPTIMIZATION MATRIX]")
print(f"Updated Buffer State: {ping_latencies}")
print("==================================================")
