# ASCII art for "Merry X-Mas Noble Friend"
from traceback import print_tb


ascii_art = r"""
$$\      $$\                                               $$\   $$\                                         $$$$$$$$\ $$\       $$\ 
$$$\    $$$ |                                              $$ |  $$ |                                        $$  _____|\__|      $$ |
$$$$\  $$$$ | $$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\       \$$\ $$  |$$$$$$\$$$$\   $$$$$$\   $$$$$$$\       $$ |      $$\  $$$$$$$ |
$$\$$\$$ $$ |$$  __$$\ $$  __$$\ $$  __$$\ $$ |  $$ |       \$$$$  / $$  _$$  _$$\  \____$$\ $$  _____|      $$$$$\    $$ |$$  __$$ |
$$ \$$$  $$ |$$$$$$$$ |$$ |  \__|$$ |  \__|$$ |  $$ |       $$  $$<  $$ / $$ / $$ | $$$$$$$ |\$$$$$$\        $$  __|   $$ |$$ /  $$ |
$$ |\$  /$$ |$$   ____|$$ |      $$ |      $$ |  $$ |      $$  /\$$\ $$ | $$ | $$ |$$  __$$ | \____$$\       $$ |      $$ |$$ |  $$ |
$$ | \_/ $$ |\$$$$$$$\ $$ |      $$ |      \$$$$$$$ |      $$ /  $$ |$$ | $$ | $$ |\$$$$$$$ |$$$$$$$  |      $$ |      $$ |\$$$$$$$ |
\__|     \__| \_______|\__|      \__|       \____$$ |      \__|  \__|\__| \__| \__| \_______|\_______/       \__|      \__| \_______|
                                           $$\   $$ |                                                                                
                                           \$$$$$$  |                                                                                
                                            \______/                                                                                
"""

# Additional regular text message
regular_text = """
My noble friend,
I commend you for this honorable journey and wish to convene soon.
Do spare me some of Jane's delicious eggnog.
Love to the children.
"""

# Password protection
valid_passwords = ["CLEVELAND", "cleveland", "Cleveland"]

import time

# Welcome message
print("You have entered the final stage")

time.sleep(2)

print("""
A shadow replace—this name, character, and place.
Hunting in trinity, bereft of dignity.
Marking its end in the shape of a prawn,
The fifth cross is drawn.
       """)

time.sleep(6)

print("insert the name and proceed to the next step")

# Get password input
user_input = input("password: ")

# Check the password
if user_input in valid_passwords:
    time.sleep (1)
    print("...")
    time.sleep (1)
    print("..")
    time.sleep (1)
    print(".")
    time.sleep(2)
    print("\nAccess granted:\n")
    print(ascii_art)
    print(regular_text)
    input("\nPress Enter to exit...")
else:
    time.sleep (1)
    print("...")
    time.sleep (1)
    print("..")
    time.sleep (1)
    print(".")
    time.sleep(2)
    print("\nAccess denied. Try Again")
