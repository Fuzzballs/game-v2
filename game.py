def gaming():
    usable_words = print("Usable words: speak, walk forward, turn left, turn right, stop, grab item, enter, quit")
    the_begining = str.lower(input("Welcome to the house, would you like to enter?: "))
    while the_begining != str.lower("quit"):
        if the_begining == "enter":
            print("You have entered the house, and there is an eary feelng, you see something to your right, out of the corner of your eye")
            break
        else:
            print("Option not avalable, but you can enter the house")
    if the_begining == str.lower("quit"):
        return("0")

    feeling = str.lower(input("What shall you do?: "))
    while feeling != str.lower("quit"):
        if feeling == "turn left":
            print("There is a hutch, and nothing to be seen")
        elif feeling == "turn right":
            print("You have turned right, and see the whisps of a dress walking down the hall")
            break
        elif feeling == "stop":
            print("You have already stopped")
        else:
            print("Option unavailable")
    if feeling == str.lower("quit"):
        return("0")

    hall = str.lower(input("Will you fallow or will you let fear take you over?: "))
    while hall != str.lower("quit"):
        usable_words
        if hall == "walk forward":
            print("""
You look to the right down the hall and see a woman facing out the window, 
her back to you.  She sways back and forth humming lightely a tune you cannot make out, nor want to make out""")
            break
        else:
            print("Option Unavailable")
    if hall == str.lower("quit"):
        return("0")


    ghost = str.lower(input("should you walk up to her, look around you?  Or will you stay where you are paralyzed with fear?: "))
    while ghost != str.lower("quit"):
        if ghost == "turn left":
            print("You see a table and on the table is a knife")
            grab = str.lower(input(""))
            if grab == "grab item":
                print("You have grabbed the knife.  now what?")
            break
        elif ghost == "turn right":
            print("There is a table with what appears to be holy water")
            grab1 = str.lower(input(""))
            if grab1 == "grab item":
                print("You have grabbed the bottle, now what?")
            break
        elif ghost == "speak":
            print('You call out, "Who are you? she stays where she is and continues her humming"')
            break
        else:
            print("Option unavailable")
    if ghost == str.lower("quit"):
        return("0")

    the_point = str.lower(input(""))
    while the_point != str.lower("quit"):
        usable_words
        if the_point == "walk forward":
            print("The figure turns around and you see a black void as the white pale hands reach out to you")
            break
        elif the_point == "turn left":
            print("There is nothing there anymore")
            break
        elif the_point == "turn right":
            print("There is nothing to your right")
            break
        else:
            print("Option unavailable")

    if the_point == str.lower("quit"):
        return("0")

    print("""
The figure grabs your shoulders, and you feel nothing but cold.  You look at your hands, any item you may have had looks useless at this point.
You look into the void once more and......
""")


gaming()

