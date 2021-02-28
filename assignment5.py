#Jacob Vesche
# 4/22/20
# assignment 5
# I have neither given nor received unauthorized aid in completing this work,
# nor have I presented someone else's work as my own."
# https://bytes.com/topic/python/answers/894970-how-do-you-read-up-specific-character-line-text
# https://stackoverflow.com/questions/20508689/write-string-and-date-to-text-file-in-python-3
import time


from datetime import datetime

f = open("Lic_usage.txt","r")
count = 0
lastUser = ""
# prints the unique users each on a new line
print("List of unique users:")
for line in f:
    newUser = line.split(",")[0]

    if(count != 0):
        if(newUser != lastUser):
        
            print(newUser)
    
    if(count != 0):
        lastUser = line.split(",")[0]

    count += 1

print("\n\nList of unique versions")
# prints the unique versions on each line. 
f.close()

f1 = open("Lic_usage.txt","r")
lastUser1 = ""
lastUser2 = ""
count = 0
test123 = []

for l in f1:
    vers = l.split(",")[0]
    if(vers == "user1"):
        version = l.split(",")[2]
    else:
        version = l.split(",")[3]

    print(version)
f1.close()


## user, machine, version
print("User, machine, and version")

f2 = open("Lic_usage.txt","r")

for i in f2:
    user123 = i.split(",")[0]
    if(user123 == "user1"):
        
        user4 = i.split(",")[1]
        user5 = i.split(",")[2]

    else:
        
        user4 = i.split(",")[1]
        user5 = i.split(",")[3]

    print(user123 + user4, user5)

f2.close()


## printing hello world to a file

startTime = datetime.now()
file = open("HelloWorld.txt","a")

file.write("Start time %s" %startTime)
file.write("\n")
for length in range(10):
    file.write(str(length + 1) + "- Hello World!\n")
    time.sleep(5)


endTime = datetime.now()
file.write("End time %s" %endTime) 
file.close()
