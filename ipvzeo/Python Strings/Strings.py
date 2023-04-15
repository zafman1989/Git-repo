#################strings#######################

#strings are a ordered sequence of characters and string are immutable
#you will see that i can 

name = "zaf"
surname = "hus"
print (name[0])
print (name[1])
print (name[2])
print (name, surname) 

#you can define string with a single quotation mark'' or a double quotation "" 

#you can use triple quotes to create a doc String this is effectively like comments using the hash
"""this line is a example of a doc string and will not execute any command"""


#When using the \n this create a break and moved the ongoing text to a new line as shown below
networks = (" Name: home network\n network : 192.168.1.0\n default gateway:192.168.1.1\n subnetmask: 255.255.255.0\n broadcast address: 192.168.1.255 ")
print (networks)

#debug output from the terminal

 #network : 192.168.1.0
 #default gateway:192.168.1.1
 #subnetmask: 255.255.255.0
 #broadcast address: 192.168.1.255

# NOTE that intergers that are wrapped in quotation mark are strings and not intergers


""" the below will not work as the vaule for the version is a string and we are doing a conditonal check on a 
value which is"""

version =  "15"
if version > 12:
    print ("version check passed")
else:
    print  ("Version check Failed")


""" the below will work as we are are changing the version value to a interger"""

version = "15"
interger_version = int(version) #####this line is changing the string value of version to a interger (int)
if interger_version >12:
    print ("version check passed")
else:
    print ("Version check has not passed")


""" the below is changing the integer value number to a string value which is the opposite of the above paragraph and also changing the 
to a float"""

number_test = 4

string_number_test = str(number_test) ##this line is changing the interger to a string NOTE the str
print (string_number_test)

float_number_test = float(number_test) ####this line is changing the interger to a float    
print (float_number_test) 

