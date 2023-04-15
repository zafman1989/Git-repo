###########string formatting########################

"""old way which is called the format method"""

name = input ("what is your name :")
age = input ("what is your age :")

"""as you can see from the below int the string withiin curly braces {} is the above keys and note
the .format (name=name. age-age) this maps the values in the string to the value of the key above """
message1 = "hello there {name}, your age is {age}".format (name=name, age=age)
print (message1)

"""the number with the curly braces below refernce the keys which are in the normal brackets which come after .format"""
message2 = "hello {0}, you age is {1}".format (name, age)
print (message2)

""" with the below you will see in the string within the curly braces there are no number as these are place holders and 
in the first curly braces it will look for the first key name (Which is known as 0) and in the second which is age """
message3 = "hello {}, your age is {}".format(name, age)
print (message3)

##################new way - known as f-string##############################
"""the below is the new way to format strings"""
device_name = "R1"
version_number = "15.8"
"""note the f which comes just after the the first bracket, this stands for format and note the key's that are found in the 
curly braces"""
print(f"the device name is {device_name}, and the version is {version_number}")

""" the new way i.E f-string is more easily readable then the old way of format method"""
#note that when using either the format method or the the f-string the method  intergers are automatically converted to
#strings.
