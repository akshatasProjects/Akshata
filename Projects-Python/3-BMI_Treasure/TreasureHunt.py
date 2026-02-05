print("WELCOME TO THE TREASURE ISLAND")
print("YOUR MISSION IS TO FIND THE TREASURE")

direction = input("Where do you want to go? Type Left or Right: ").lower()
if direction == "left":
   swim_wait = input("Do you want to Swim or Wait? Type S or W: ").lower()
   if swim_wait == 'w':
        door = input("There are 3 doors to continue select any door, RED, YELLOW, BLUE: ").lower()
        if door == "red":
            print("GAME OVER: full of fire")
        elif door == "blue":
            print("GAME OVER: You entered room of beasts")
        elif door == "yellow":
            print("YOU WIN : You found the tresure")
        else:
            print("GAME OVER:Choose the door correctly ")
   else:
        print("GAME OVER: You are attacked by angry trout")
else:
    print("GAME OVER : You fell in the hole")