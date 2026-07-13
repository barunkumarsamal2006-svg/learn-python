#Day 11:python fundamental

#python match statement
    #matsh statement select one of many code blocks to be executed.

#syntax:
# match expression:
#     case x:
#         code block
#     case y:
#         code block
#     case z:
#         code block    
#     case _:           #(this is default value .this execute when there are not other matches.)
#          code block

#combine value
"""use  pipe character | as an or operator in the case evalution to check for more than 
    one value match in one case."""

day=6
match day:
    case  2|3|4|5|6:
        print("Today is workday.")
    case 1|7:
        print("weekends!")

            
#if statement as Guards
  #use in case evaluation asa an extra condition ckeck.

month=7
day=7
match day:
    case 1|2|3|4|5 if month ==4:
        print("a weekday in april")
    case 1|2|3|4|5 if month ==5:
        print("a weekday in may.")    
    case 1|2|3|4|5 if month ==6:
        print("a weekday in june")
    case 1|2|3|4|5 if month ==7:
        print("a weekday in july")
    case _:
        print("no match")            


"""
Problem Statement:
Google Cloud Platform (GCP) handles thousands of incoming infrastructure requests every second. 
We need a core routing engine that inspects a request tuple (containing an event type string, a
target value, and an operational region) and instantly routes it to the correct deployment path.

You must build a high-performance routing module using a single match-case block to parse these
incoming configurations cleanly.
"""
# Format: (EVENT_TYPE, TARGET_RESOURCE_OR_COUNT, DISPATCH_REGION)
incoming_request = ("PROVISION", 5, "us-east") 
print("="*60)
print("        GCP STRUCTURAL ROUTING TELEMETRY          ")
print("="*60)
print(f"[INGESTED PAYLOAD]:{incoming_request} ")
print("\n")

print("[ROUTING DECISION]")


match incoming_request:

    case   ("DECOMMISSION", "ALL", "global"):
        print("Orchestrator Path:High priority warning alerating that the entire global cluster is shutting down.")
        print("System Status    :UNSTABLE/ALERT")

    case ("PROVISION",count,"us-east"):
        print("Orchestrator Path:SUCCESS - Spinning up 5 servers in us-east.")
        print("System Status    : STABLE / BALANCED") 

    case  ("MAINTENANCE",_,_)  :
        print("Orchestrator Path:Standard cluster optimization log.")
        print("System Status    : STABLE/STANDARD")

    case _:
        print("REJECTED - INVALID API PAYLOAD")


print("\n")
print("="*60)
print("Execution Status: DEPLOYED | Day 11 Segment Logged")
    