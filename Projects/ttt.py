import os
import time

# Vars

phases = {"d":"""   a     b     c
      |     |     
1  -  |  -  |  -  
 _____|_____|_____
      |     |     
2  -  |  -  |  -  
 _____|_____|_____
      |     |     
3  -  |  -  |  -  
      |     |     """,
      "a1": """   a     b     c
      |     |     
1  X  |  -  |  -  
 _____|_____|_____
      |     |     
2  -  |  -  |  -  
 _____|_____|_____
      |     |     
3  -  |  -  |  -  
      |     |     """}

print(phases["d"])

# Utilities
def update_scrn():
    os.system('cls' if os.name == 'nt' else 'clear')