

##############strings################
#you cannot use the add or append with strings.

my_string = "CBT NUGGETS"
print (my_string)

#you cannot add or append on a string hence they are imutable however you can update the the string but this will 
#replace the the above variable as we are UPDATING the Variable
my_string = ("CBT NUGGETS....is the best")
print (my_string) 

############tuple##################
#tuples are similar to lists but they are immutable unlike a list which is mutable

my_inventory = ("r1", "r2", "r3")
print (my_inventory)

#The only way we can update this tuple we would have to recreate the tuple as shown below adding sw1,sw2 and sw3. not the below
#has not been updated but a new tuple has been create with the same variable name of my_inventory
my_inventory = ("r1", "r2", "r3", "sw1", "sw2", "sw3")
print (my_inventory) 

