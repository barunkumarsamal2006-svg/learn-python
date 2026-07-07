#Day 07:python fundamental

#add list items
#append items

list1=['me','you','them']

list1.append('other') # add item  in the end of the listprint(list1)
                      # one important think is you only add one item use append method in one declaration
print(list1)

#insert items

list2=['me','you','them']
list2.insert(2,'our')

print(list2)

#extend items

list3=['me','you','them']
list4=['our','they','me']

list3.extend(list4) #add two list items in one list
print(list3)

tuple3=('our','they','me') #also use of extend can add a tuple,dict and set items in a list
list4.extend(tuple3)
print(list3)


#Remove items
#remove specified item --remove()

list5=['our','they','me']
list5.remove("they")#remove specified item in list 
                    #if specified item occure more than one in list then remove only first occurance
print(list5)

#remove specified index --pop()

list6=[1,4,5,6,5]
list6.pop(3) #remove specified index item 
             #if not specify methos remove last index item in list
print(list6)

#del keyword

list7=[7,16,18,45]
del list7[1] #delete specified index
print(list7)

list7=[7,16,18,45]
del list7  #delete list completely


#cleat the list

list8=['orange','mango','banana']
list8.clear()    #list still remain but no item
print(list8)

#Today problem
"""
The Problem: 
"The Google Network Buffer Cleaner"
You are building a system that manages network data packages arriving at a Google server. 
The network buffer starts with some initial packages, but it gets overloaded with a broken
 batch, which you must clean and update.
""" 

network_buffer = ["packet_A", "packet_B", "packet_C"]

network_buffer.insert(1,'urgent_packet')

new_stream = ["packet_D", "packet_E", "broken_sys.exe"]

network_buffer.extend(new_stream)

network_buffer.remove('broken_sys.exe')

network_buffer.pop(0)

del network_buffer[2]

print("==========GOOGLE NETWORK BUFFER=============")
print(f"Active Package: {network_buffer}")
print("============================================")