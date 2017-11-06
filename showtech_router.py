from netmiko import ConnectHandler
import re
import sys
import time

#Create netmiko compatible parameters to ssh to router
router = {'device_type':'cisco_xr','ip':'1.99.104.1','username':'root','password':'lab'}

#Create router console handle using netmiko ConnectHandler class
try:
    router_console = ConnectHandler(**router)
except:
    time.sleep(20)
    try:
       router_console = ConnectHandler(**router)
    except:
       print "Connect Handler failed. Exiting Gracefully"
       sys.exit()
print "SUCCESS: Connected to Router Console"
#Execute Show version
try:
    output = router_console.send_command("show version")
    print output
except:
    print "Could not execute show version on router. Exiting Gracefully"
    sys.exit()

#Execute show tech install using send_command_expect with delay_factor as
#send_command_expect has default timeout which is not sufficient to collect
#show tech output
try:
    output = router_console.send_command_expect("show tech-support install",delay_factor=10)
except:
    print "Unable to collect show tech output. Exiting Gracefully"
    sys.exit()
print "Show tech collection started"
#Creating an Empty List to store show tech file names
showtech_files = []

#Greping exact file name from the show tech output and storing in a list
if (re.search(r'Show tech output available at (.*) : /harddisk:/showtech/(.*)',str(output))):
    showtech_files.append(re.search(r'Show tech output available at (.*) : /harddisk:/showtech/(.*)',str(output)).group(2))
print "Checking content of showtech_files"
print showtech_files
#check for TFTP server reachability from router
try:
    output = router_console.send_command_expect("ping 1.99.0.7",delay_factor=10)
except:
    print "TFTP server is not Reachable.Exiting Gracefully"
    sys.exit()

ping_percentage = int(re.search(r'Success rate is (\d{1,3}) percent',str(output)).group(1))
if ping_percentage == 100:
    print "TFTP server is Reachable. Ready to copy Show tech files to TFTP server"
    for files in showtech_files:
        try:
            print "TFTP Server Copy Started"
            router_console.send_command_expect("copy harddisk:/showtech/{} tftp://1.99.0.7/auto/tftp-blr-users3/gponnusa/{}".format(files,files),expect_string='')
            time.sleep(10)
            output1 = router_console.send_command_expect("\n",expect_string='')
        except:
            print "TFTP Copy Failed. Exiting Gracefully"
            sys.exit()
print output1
if (re.search(r'Writing tftp://.*',str(output1))):
    print "TFTP COPY Success"
