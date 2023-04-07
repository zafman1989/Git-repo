########################string method############################

#as a high level overview you can imagine methods as somthing which adds functionality to your code

platform = "cisco ios"

#upper_platform = platform.upper()
# print (upper_platform)


platform = input("what is the platfrom of the network device ")
show_commands = input("what show commands do you want to send: ")
platform_to_test = platform.lower()

#if platform =="cisco":
if platform_to_test == "Cisco" :
    commands_to_send = f"enable\n {show_commands}\n"
    print (commands_to_send)

interface = "Gigabitethernet0/2"
interface.lower
print ("interface")
    
