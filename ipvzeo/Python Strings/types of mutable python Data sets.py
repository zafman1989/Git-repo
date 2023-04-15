############varibales###########
router = "r1"
print (router) 

number_of_routes = 20
print (number_of_routes)

#do not start varibale with a digit hence the below will not be allowed
# 1router = "R1"




########### List Data type ###################

#for list data types we will be using [] square brackets for every item in the list we will be separating these with
# ,( a comma)


my_routes = [ "10.0.0.0/30", "192.168.10.0/24" , "172.16.0.0" ]

my_routes.append("8.8.8.8/32")

print (my_routes)


########### Dictionaries  ###############

#To create the dictionary we use curly braces {}
#this is a collection of key value pairs

my_credentials = { 
    "hostname" :"192.168.31.101",
    "port" : "22",
    "password" : "cisco"
}

print (my_credentials) 

# you can add add further key/value pairs with the below method
my_credentials["platform"] = "cisco_ios"

print (my_credentials)

####################set#######################
#when we are creating a list we are using the [] (Square brackets) but with curly brackets
# you will see that it looks similar to the dictionary however there are no key/value pairs within.
#the set will not allow any duplication 

set_of_vlans = { "vlan 5","vlan 10", "vlan 15", }
print (set_of_vlans)

# the below is how add a addtional value within a defined set i.E adding vlan 20 to the above set of values in the list
set_of_vlans.add("vlan 20")
print (set_of_vlans)

