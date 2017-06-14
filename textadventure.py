start = '''
It's nearly the end of summer and school is just around the corner.
You wake up one morning and you go downstairs to check the mail
You go open the door and see an envolope fall at your feet
You pick it and notice that it is for you, but the address in which it came from seems to be unfamiliar.
What do you do with it? Do you decide to throw it away or open it to further investigate?

'''


print(start)


print("Type '1' for the first option or '2' for the secon option.")
user_input = input()
if user_input == "1":
    print("You decide to throw it away. Congragulations! You've decided to continue with your boring unfufilled life.") # finished the story by writing what happens

elif user_input == "2":
    print("Congragulations you've been accepted into Hogwarts School of Witchcraft and Wizardry. You're really excited. Do you want to share this information with freinds through social media or do you plan to keep this as a secret?")
    user_input=input()
    if user_input == "1":
        print("Uh-oh! As soon as you press send you hear a loud knock at your door. A Ministry of Magic official barges in and pins you against the wall, shouting, 'Did you just share knowledge of the wizarding world with Muggles?' You're trembling in fear. Do you lie and claim your innocence or do you confess to sharing the message?")
        user_input = input()
        if user_input == "1":
            print("You fool! The Ministry official sees right through your lie and throws you in jail for it. Now you have to live out the rest of your life in prison.")
        elif user_input == "2":
            print("The official thanks you for telling the truth and deletes the message with a wave of his wand. As an act of mercy, he erases your memory and sends you on your way. You live blissfully unaware of magic and Hogwarts.")
        else:
            print("Incorrect input. Next time type 1 or 2.")

    elif user_input == "2":
        print ("Good choice. You don't want to tell the Muggle world about magic. But now you need to figure out how to get to the train station to go to school. Do you ask your mom for a ride or use all your savings to buy a bus ticket?")
        user_input = input()
        if user_input == "1":
            print ("Mom thinks your whole story is crazy, and after consulting your dad, they decide to send you off to a school for mentally disturbed children. No hope of going to Hogwarts now!")
        elif user_input == "2":
            print ("The bus takes you to King's Cross Station and you hope on the train to Hogwarts. Congratulations! You made it!")
        else:
            print ("Incorrect input. Next time type 1 or 2.")
    else:
        print ("Incorrect input. Next time type 1 or 2.")
