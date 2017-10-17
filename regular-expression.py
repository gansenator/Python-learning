
#Program for Regular expression to check the entered ROMMON Variable to correct
While(1):
 import re
 rommon_number = input_raw("Enter the Rommon Number you want to check")

#Pattern for Rommon varaible check

 patter = '''^                    # Starting with
           M{0,3}                # Checking for thousands
           (D?C{0,3}|CD|CM)      # Checking For 100 to 900
           (L?X{0,3}|XL|XC)      # Checking for 10 to 90
           (V?I{0,3}|IV|IX)      # Checking for 1 to 9
           $                     # End of pattern 
           '''
 if re.match(pattern,rommon_number,re.VERBOSE):
           print "Correct Rommon Number Entered'
 else:
           print "please enter Correct Rommon Number"

