import random
import time

# Your personal data stored in a dictionary
sharan = {
    "Name": "Sharan",
    "College": "BMSCE",
    "Age": 19,
    "Favourite Food": "Noodles 🍜",
    "Favourite Colour": "Orange 🟠",
    "Favourite Marvel Character": "Iron Man 🤖",
    "Favourite Drink": "Orange Juice 🧃",
    "Hobby": "Riding a Bike 🏍️"
}

# Fun ASCII banner
banner = r"""
   _____ _                                 
  / ____| |                                
 | (___ | |__   __ _ _ __ __ _ _ __ 
  \___ \| '_ \ / _` | '__/ _` | '_ \ 
  ____) | | | | (_| | | | (_| | | | |
 |_____/|_| |_|\__,_|_|  \__,_|_| |_|                                 
"""

print(banner)
print("🚀 Welcome to Sharan's Auto-Intro Program 🚀\n")

# Dramatic reveal effect
for key, value in sharan.items():
    print(f"{key}: {value}")
    time.sleep(0.6)  # suspense effect

# Add a fun twist: random fact generator
fun_facts = [
    "Did you know? Sharan believes noodles are happiness in a bowl!",
    "Iron Man is Sharan's role model 🦾.",
    "When you see an orange 🟠, think of Sharan's vibe!",
    "Sharan loves the thrill of the open road on his bike 🏍️."
]

print("\n✨ Random Fun Fact ✨")
print(random.choice(fun_facts))
