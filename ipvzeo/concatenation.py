
###################concatenation#########################

""" the below is an example of con concatenation. you will see the command_string is asking for a input and the 
command_to_send is sending this but witht he enable command and then the input in the command_string """

command_string = input ("enter the command you wish to send to the device: ")

commands_to_Send = "enable\n" + command_string + "\n"

print (commands_to_Send)



greeting = "hello my name is zaf and my age is "
age = 18 
string_age = str(age)

print (greeting + string_age)