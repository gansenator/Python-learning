
#Program for Regular expression to check the entered ROMMON Variable to correct

import re
rommon_number = input_raw("Enter the Rommon Number you want to check")

#Pattern for Rommon varaible check

patter = '''^                    # Starting with
           M{0,3}
           (D?C{0,3}|CD|DC)      # Checking For 100 tp 900
