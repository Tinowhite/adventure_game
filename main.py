name = input("Type your name: ")
print("welcome", name, "to this adventure! ")

answer = input(
    "you are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? "
).lower()

if answer == "left":
    answer = input(
        "You come to a river, you can come walk around it or swim across? Type walk to walk around and swim to swim around: "
    )

    if answer == "swim":
        print("You swim across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for any miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input(
        "You come to a bridge, it looks wobbly, do you want to cross or head back (cross/back)? "
    )

    if answer == "back":
        print("you go back and lose.")

    elif answer == "cross":
        answer = input(
            "you cross the bridge meet a stranger. Do you talk to them (yes/no)? "
        )

        if answer == "yes":
            print("You talk to the stranger and they give you gold. YOU WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")

print("Thank you for trying")
