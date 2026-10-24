#Adventure game.
#You need to have at least 30 if statements.
#No direction can leave the user hanging without instructions.
print("You are facing two roads. The left road leads to a large house. The right leads to an underground dungeon.")
direction1 = input("Would you like to turn left or right? ")
if direction1.lower() == "left":
    print("You have entered a haunted house. The door closes itself behind you.")
    print("You hear sounds. You see a hallway infront of you. There are stairs to your right.")
    house_option1 = input("Which will you follow?\nA. Follow the sounds\nB. Go down the hallway\nC. Go up the stairs")
    if house_option1.lower() == "a":
        print("You followed the sounds.\nIt led you to a room with a ghost.\nYou were killed by the ghost!")
    elif house_option1.lower() == "b":
        print("You went down the hallway. There is a split in the hallway.")
        house_option2 = input("Will you turn left or right? ")
        if house_option2.lower() == "right":
            print("The floor falls from under you and you fall to your death.")
        else:
            print("A monster was hiding and it killed you.")
    else:
        print("You went upstairs into the attic. There is a chest and a closet.")
        house_option3 = input("Which one will you open? ")
        if house_option3.lower() == "chest":
            print("You opened the chest. A large spider jumped out and bit you, and you died fron the poison.")
        else:
            print("You opened the closet. You found a crowbar! Using the crowbar, you broke down the door and escaped the house.\nYOU SURVIVED! (Ending 1)")
else:
    print("You have entered a dungeon. Infront of you are two gates and a code panel. Entering 1 opens one gate while entering 2 opens the other.")
    dungeon_option1 = input("1 or 2?")
    if dungeon_option1 == "1":
        print("You enter a dark room. Its too dark to see anything clearly, but you can barely make out")
