from netmiko import ConnectHandler
import re

#Create netmiko compatible parameters to ssh to router
router = {'device_type':'cisco_xr','ip':'1.99.104.1','username':'root','password':'lab'}

#Create router console handle using netmiko ConnectHandler class
try:
    router_console = ConnectHandler(**router)
except:
    print "Connect Handler failed. Exiting Gracefully"

#Execute Show version
try:
    output = router_console.send_command("show version")
    print output
except:
    print "Could not execute show version on router. Exiting Gracefully"

#Execute show tech install using send_command_expect with delay_factor as 
#send_command_expect has default timeout which is not sufficient to collect
#show tech output
try:
    output = router_console.send_command_expec("show tech-support install",delay_factor=10)
except:
    print "Unable to collect show tech output. Exiting Gracefully"

#Creating an Empty List to store show tech file names
showtech_files = []

#Greping exact file name from the show tech output and storing in a list
if (re.search(r'',output)):
    showtech_files.append(re.search(r'',output).group(2))

#check for TFT pserver reachability from router
try:
    output = router_console.send_command_expect("ping 223.255.254.254",delay_factor=10)
except:
    print "could not execute TFTP server ping. Exiting Grcefully"
   
