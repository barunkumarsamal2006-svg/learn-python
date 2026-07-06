"""
Part 1: 
The Google "SRE" Logic QuestionScenario: 
Google Site Reliability Engineers (SREs) monitor Google’s servers to make 
sure YouTube and Gmail never go offline.

"""

active_connection_string="8500"
connections=int(active_connection_string)
is_overloaded =connections > 10000

maintenance_mode=False
send_alert= is_overloaded and maintenance_mode is False

print("=========]GOOGLE SERVER STATUS==========")
print(f"Current connection: {active_connection_string}")
print(f"Cluster overloaded:{is_overloaded}")
print(f"Alert dispatched:{send_alert}")
print("=========================================")



"""
Part 2:
 The Google Photos Data ChallengeScenario: 
 Google Photos stores user image metadata in sequences. Sometimes, data gets corrupted during upload, and engineers have to manually inspect and fix the collection.
 Instructions:
 1. tracking 4 uploaded items:
 2.Access and print the very last asset in the list using a negative index.
 3.Fix the corrupted file: Change the value at index 2 from "ERROR_CORRUPT.txt" to a valid image named "IMG_003.png".
 4.Create a slice named only_images that grabs the first three items from your updated list.
"""

uploaded_assets = ["IMG_001.png", "IMG_002.png", "ERROR_CORRUPT.txt", "VID_001.mp4"]
uploaded_assets[2]="IMG_003.png"
only_images=uploaded_assets[:3]
print("+++++++++++++ GOOGLE PHOTOS DATA++++++++++++++")
print(f"Last asset:{uploaded_assets[-1]}")
print(f"Update batches:{uploaded_assets}")
print(f"Filtered images:{only_images}")
print("++++++++++++++++++++++++++++++++++++++++++++++++")

"""
The Problem Statement: 
"Google Drive Storage Alert"
Google Drive gives users free storage, but warning flags must trigger when they run out of space.
You are given a raw data feed containing a user's account status:
The account owner's name is "Barun".
Their current used space is stored as a string: "14.8" (in Gigabytes).
The maximum free space allowed is 15.0 Gigabytes.
They have a backup system active, stored as a boolean: True.Your system needs to process this data.
 A storage warning flag (True) should only trigger if the user's current space is greater than or equal to 14.5 Gigabytes AND their backup system is active (True).
"""
#concept:1
user_account="Barun"
used_storage="14.8"
current_storage=float(used_storage)
max_storage=15.0
is_back_active=True

warning_triggered = current_storage >= 14.5 and is_back_active

print(f"_________________GOOGLE DRIVE STORAGE________________")
print(f"user:{user_account}")
print(f"current storage:{current_storage}GB")
print(f"storage limit:{max_storage}GB")
print(f"warning triggered:{warning_triggered}")
print("______________________________________________________")


#concept:2
owner_account="Barun"
Used_storage="14.8"

maximum_storage=15.0
Is_backup_active=True
curr_storage=float(Used_storage)
print(f"_________________GOOGLE DRIVE STORAGE________________")
print(f"user:{owner_account}")
print(f"current storage:{curr_storage}GB")
print(f"storage limit:{maximum_storage}GB")
if curr_storage >= 14.5 and Is_backup_active:
    print("warning triggered " \
          " Get more storage for store your memories ")
else:
    print("storage in comfort stage.")

print("_____________________________________________________")

    