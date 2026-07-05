#Day 05: python fundamental

#lists
# list are used to store multiple items in a single variable
#phase:1
fruits=['apple','orange','mango']
print(fruits)

#list items:ordered,changeable,allow duplicate
list1=['odisha','delhi','mumbai','odisha']
print(list1)  #duplicate
list1.append('chennai')
print(list1)  #ordered
list1[1]='kolkata'
print(list1)  #changeable
print(len(list1)) #how many items in list 
print(type(list1))

#use list() constructor when creating list it is possible 

list2=list(('1','2','3'))
print(list2)

#phase:2

#access items 
     
list3=['day','night']
print(list3[0])

list4=['morning','afternoon','evening','night']
#negative indexing
print(list4[-2])
#range of index
print(list4[1:3])
#range of negative indexing
print(list4[-3:-1])
#check if item exists
if 'evening' in list4:
    print('item exits')

#phase:3
#change item value

list6=['morning','afternoon','evening','night']
list6[2]='noon'
print(list6)    

#change the range of items values

list6[2:3]=['day','night','day']
print(list6)

#insert items
list6.insert(2,'night')
print(list6)

