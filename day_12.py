#Day 12 :python fundamental

#python while loop
    #while loop we can execute a set of statements as long as a condition is true.

i=0
while i< 6:
    print(i)
    i+=1

#break statement
   #break stop the loop even if the while condition is true.

j=1
while j < 6:
    print(j)
    if j==3:
        break
    j+=1   

#continue statement
   #continue stop the current iteration and continue with next.

k=0
while k<6:
    k+=1
    if k==3:
        continue
    print(k)

#else statement
   #use else we can run a block of code once when the condition no longer is true.

l=1
while l < 7:
    print(l)
    l+=1
else:    #it not work if loop stopped by break statement
    print("l is no longer less than 7")    


"""
Problem Statement:
Google Cloud Pub/Sub ingests data packets streaming from IoT devices. When data traffic
spikes, the server's memory buffer fills up. We need a throttling engine that
continuously processes data batches from the buffer queue until the load drops to a safe 
threshold.

You must write a structural simulation using a while loop that drains a simulated system 
buffer based on changing network conditions.


"""


current_buffer_size = 4500  # Total data units currently in memory (MB)
drain_rate_per_cycle = 800  # How much data the server processes each loop (MB)
safe_threshold = 1000       # Target buffer size before throttling stops (MB)
cycle_count = 0             # Loop counter tracking execution ticks

print("="*60)
print("       GCP MEMORY BUFFER THROTTLING SYSTEM        ")
print("="*60)

print("[INITIAL MONITORING CAPTURED]")
print(f"Starting Buffer Load:{current_buffer_size}MB")
print(f"Target Safe Ceiling:{safe_threshold}MB")
print("\n")
print("[THROTTLING CYCLES ACTIVATED]")

while current_buffer_size > safe_threshold:
    cycle_count+=1 
    current_buffer_size -= drain_rate_per_cycle
  
    if cycle_count==3:
        current_buffer_size+=1200
        print(f"* CYCLE {cycle_count:02d} | NETWORK SPIKE! | Buffer Increased to: {current_buffer_size} MB")
    else:
        if current_buffer_size <0:    
            current_buffer_size=0
        print(f"* CYCLE {cycle_count:02d} | Buffer Drained to: {current_buffer_size} MB")

print("\n[SYSTEM REGULATION COMPLETE]")
print(f"Final Stable Buffer Size: {current_buffer_size} MB")
print(f"Total Iteration Cycles  : {cycle_count} cycles")
print("="*60)
print("Execution Status: SUCCESS | Drain Metrics Logged")
















