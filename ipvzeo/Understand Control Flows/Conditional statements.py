#contorl flow the order in which your program flow executes. the control flow is regulated by conditional statments and you
#will also see thing such as loops.

# we will see the contrstion of if, elif and else statments as part of loops.
# loops allow us to do repetititve tasks consistently and rapidly.
#we will also be putting conditional statments in loops i.e if,elif or else 

###########################conditional statements###########################################

"""the if is mandatory when doing conditional statments and the other two are optional"""

# we are going to create a if statement below and evalute if something is true and also add a else statement as a catachall statement

age = 17

if age > 20:
    print ("you are old enough to buy beer") # you will see no print from this as the age is not greater then 20
else:
    print("you are not old enough to a buy a beer kiddo")
# the scrip will skip the if state as the age is not greater and will move onto the else statement    
#else in the above statement is a catachall statement
    
"""in the below you will see the same statement as the above but we will be adding a elif (else if) """

age = 19 
if age > 20:
    print ("you are old enough to buy beer and vote")
elif age > 17:
    print ("you cant buy beer but you can vote")
else:
    print ("you are too young to vote or buy beer")

""" for the above statement we will firstly test the age against the if statement to see if this is true however if this is false the next 
check is a elif statement, if this is true it will print "you cant buy beer but you can vote" and if this is false then it will then move onto 
the else statement and print "you are too young to vote or buy beer" """

"""you will see witht the below statement the age is 25 and the if ststament will be true and it will not move on to the elif or else statements"""
age = 25 
if age > 20:
    print ("you are old enough to buy beer and vote")
elif age > 17:
    print ("you cant buy beer but you can vote")
else:
    print ("you are too young to vote or buy beer")
    
"""if you wanted to test agains multiple criteria you can do multiple elif statement as shown below as show below, if the value of the input
doe not match the the if (Firstly) or the multiple elif statements (In the order) then the else will act as a catch all and print
'This is not possible'"""

vendor = input("enter the vendor you wish to automate: ")

if vendor =="cisco":    
    print ("you have selected cisco and this is possible")      
elif vendor == "Juniper":
    print ("you have selcted juniper and this is possible")
elif vendor == "HPE":
    print ("you have selected HPE and this is possible")
elif vendor == "Fortigate":
    print ("you have selected fortigate and this is possible")
elif vendor == "Sophos":
    print ("you have selected Sophos and this is possible")
else:
    print ("unregonised vendor and This is not possible") 
    
"""note the indentation of the print statement for the if, elif and else statements
Note the condtional statement denoted by the : (Colon) symbol"""