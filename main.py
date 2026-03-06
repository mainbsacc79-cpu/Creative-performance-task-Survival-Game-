import random


health = 100
energy = 100
day = 1

inventory = {
    "wood":0,
    "stone":0,
    "berries":0,
    "arrows":0,
    "meat":0,
    "cooked_meat":0,
    "hide":0
    }
    
tools = {
    "sword":False,
    "bow":False
}

def show_stats():
    print("\n---------------------")
    print("Day:", day)
    print("Health: ", health)
    print("Energy: ", energy)
    print("Inventory:")
    for item, amount in inventory.items():
        print("  ",item, ": " ,amount)
    print("Tools:")
    for tool, has_tool in tools.items():
        print(f"  {tool}: {'Yes' if has_tool else 'No'}")
    print("---------------------\n")
    
def show_actions():

    print("\nChoose action:")
    print("1 - Gather wood")
    print("2 - Gather stone")
    print("3 - Gather berries")
    print("4 - Craft")
    print("5 - Hunt")
    print("6 - Eat")
    #print("7 - Build campfire")
    #print("8 - Cook meat")
    #print("9 - Stats/Inventory")
    
def gather_wood():
    global energy
    
    if energy < 20:
        print ("Not enough energy")
        return

    amount = random.randint(1, 4)
    inventory["wood"] += amount
    energy-= 20
    print ("You gathered ", amount ," wood!")

def gather_stone():
    global energy
    
    if energy < 20:
        print ("Not enough energy")
        return

    amount = random.randint(1, 4)
    inventory["stone"] += amount
    energy-= 20
    print ("You gathered ", amount ," stones!")

def gather_berries():
    amount = random.randint(1, 3)
    inventory["berries"] += amount * 2
    print ("You gathered ", amount * 2 ," berries!")
    
def craft():

    print("Craft:")
    print("1 - Arrows (1 feathers, 1 wood, 1 stone)")
    print("2 - Sword (1 wood, 2 stone)")
    print("3 - Bow (1 wood, 1 hide)")

    choice = input("Choose: ")

    if choice == "1":
        if inventory["feather"] >= 1 and inventory["wood"] >= 1 and inventory["stone"] >= 1:
            inventory["arrows"] += 5
            inventory["feather"] -= 1
            inventory["wood"] -= 1
            inventory["stone"] -= 1
            print("You crafted arrows!")

    elif choice == "2":
        if inventory["wood"] >= 1 and inventory["stone"] >= 2:
            tools["sword"] = True
            inventory["wood"] -= 1
            inventory["stone"] -= 2
            print("You crafted a sword!")

    elif choice == "3":
        if inventory["wood"] >= 1 and inventory["hide"] >= 1:
            tools["bow"] = True
            inventory["wood"] -= 1
            inventory["hide"] -= 1
            print("You crafted a bow!")

def hunt():

    global energy
    global health
    
    energy -= 25

    weapon = "nothing"

    if tools["sword"]:
        weapon = "sword"
    elif tools["bow"]:
        weapon = "bow"

    success = random.random()

    if weapon == "bow":
        chance = 0.8
    elif weapon == "sword":
        chance = 0.6
    else:
        chance = 0.4

    if success < chance:

        animal = random.choice(["deer","chicken","rabbit"])

        print("You hunted a", animal)

        if animal == "deer":
            inventory["hide"] += 1
            inventory["meat"] += 2

        elif animal == "chicken":
            inventory["feather"] += 3
            inventory["meat"] += 1

        elif animal == "rabbit":
            inventory["meat"] += 1
            print("Health +20!")
            health += 20

    else:
        print("Hunt failed")

def eat():
    global health
    global energy

    choose = input("Choose food:\n1 - berries\n2 - raw meat\n3 - cooked meat\n")
    amount = int(input("How much: "))

    if choose == "1":
        health += 10 * amount
        energy += 10 * amount
        print("Restored:", 10*amount, "health and energy")
        inventory["berries"] -= amount

    elif choose == "2":
        health += 15 * amount
        energy += 20 * amount
        print("Restored:", 15*amount, "health and", 20*amount, "energy")
        inventory["meat"] -= amount

    elif choose == "3":
        health += 30 * amount
        energy += 50 * amount
        print("Restored:", 30*amount, "health and", 50*amount, "energy")
        inventory["cooked_meat"] -= amount

    
print("Welcome to island survival!")

while day <= 5:

    show_stats()  
    
    actions_left = 5  
    while actions_left > 0:
        show_actions()
        choice = input("Enter action: ")

        if choice == "1":
            gather_wood()
        elif choice == "2":
            gather_stone()
        elif choice == "3":
            gather_berries()
        elif choice == "4":
            craft()
        elif choice == "5":
            hunt()
        elif choice == "6":
            eat()

        actions_left -= 1


    print("Night falls...")
    day += 1
