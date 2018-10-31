import tkinter, random, time


def user_checker(username):
    searchfile = open("Users.txt", "r")
    for line in searchfile:
        if username in line:
            print("Welcome back " + username + "! Come back to your colony")
            start_game()
        else:
            new_file = input("This user is not in the save file, do you wish to restart >> ")
            if new_file == "yes":
                print("Your new username is " + username)
                print("IMPORTANT! YOU ARE REQUIRED TO RE RUN PROGRAM AND INPUT USERNAME AGAIN TO PLAY")
                user_file = open("Users.txt", "w")
                user_file.write(username)

                wood_file = open("wood.txt", "w")
                wood_file.write("0000000000")

                iron_file = open("iron.txt", "w")
                iron_file.write("0000000000")

                gather_file = open("gatherers.txt", "w")
                gather_file.write("0000000000")

                wood_coll_file = open("wood_collection.txt", "w")
                wood_coll_file.write("15")

                hunter_file = open("Hunters.txt", "w")
                hunter_file.write("0000000000")

                bone_file = open("bones.txt", "w")
                bone_file.write("0000000000")

                hides_file = open("hides.txt", "w")
                hides_file.write("0")

                feathers_file = open("feathers.txt", "w")
                feathers_file.write("0000000000")

                huts_file = open("Huts.txt", "w")
                huts_file.write("0000000000")

                butch_file = open("Butchers.txt", "w")
                butch_file.write("0000000000")

                meat_file = open("meat_count.txt", "w")
                meat_file.write("0000000000")

                people_file = open("People_Relations.txt", "w")
                people_file.write("Willing workers")

                absentees_file = open("people_count.txt", "w")
                absentees_file.write("0000000000")

                armour_file = open("people_count.txt", "w")
                armour_file.write("10")

                gather_file.close()
                people_file.close()
                bones_file.close()
                hides_file.close()
                feathers_file.close()
                meat_file.close()
                butch_file.close()
                user_file.close()
                hunter_file.close()
                huts_file.close()
                iron_file.close()
                armour_file.close()
                start_game()
            else:
                username = input("Username: ")
                user_checker(username)


def start_game():
    cha = open("wood.txt", "r")
    wood_count_main = int(cha.readline(10))

    meat_read = open("meat_count.txt", "r")
    meat_count = int(meat_read.read(10))

    char1 = open("Hunters.txt", "r")
    hunters = int(char1.readline(10))

    char3 = open("Tanners.txt", "r")
    tanners = int(char3.readline(10))

    char4 = open("Huts.txt", "r")
    huts = int(char4.readline(10))

    char5 = open("bones.txt", "r")
    bones_count = int(char5.readline(10))

    char6 = open("hides.txt", "r")
    hide_count = int(char6.readline(10))

    char7 = open("feathers.txt", "r")
    feather_count = int(char7.readline(10))

    char8 = open("gatherers.txt", "r")
    gatherers = int(char8.readline(10))

    char9 = open("people_count.txt", "r")
    people_count = int(char9.readline(10))

    char10 = open("iron.txt", "r")
    iron_count = int(char10.readline(10))

    armour = open("armour.txt", "r")
    heal = int(armour.readline(10))
    armour.close()

    health_change = open("health.txt", "w")
    health_change.write(str(heal))
    health_change.close()

    root = tkinter.Tk()

    photo = tkinter.PhotoImage(file="camp.png")

    frame1 = tkinter.Frame(root)
    frame2 = tkinter.Frame(root)

    root.configure(background="orange")
    frame2.configure(background="orange")

    picture = tkinter.Label(frame1, image=photo)

    hunter = tkinter.Button(frame2, text=" Hunters: " + str(hunters), command= lambda : hunter_adder())
    tanner = tkinter.Button(frame2, text="Tanners: " + str(tanners), command= lambda : tanner_adder())
    gatherer = tkinter.Button(frame2, text="Gatherers: " + str(gatherers), command= lambda : gatherer_adder())

    Actions = tkinter.Button(frame2, text="Collection Depot", command= lambda: actions_passover())
    Build = tkinter.Button(frame2, text="Builders Workshop", command=lambda: build_win())
    quit = tkinter.Button(frame2, text="  Quit    ", command = lambda: quit())
    forest = tkinter.Button(frame2, text="Dark Forest", command=lambda: dark_forest_passover())

    wood = tkinter.Label(frame2, text="Wood: " + str(wood_count_main))
    meat = tkinter.Label(frame2, text="Meat: " + str(meat_count))
    hides = tkinter.Label(frame2, text="Hides: " + str(hide_count))
    bones = tkinter.Label(frame2, text="Bones: " + str(bones_count))
    feathers = tkinter.Label(frame2, text="Feathers: " + str(feather_count))
    people = tkinter.Label(frame2, text="People Count: " + str(people_count))
    iron = tkinter.Label(frame2, text="Iron: " + str(iron_count))

    wood.grid(row=8, pady=10)
    iron.grid(row=12, pady=10)
    meat.grid(row=7, pady=10)
    feathers.grid(row=9, pady=10)
    bones.grid(row=10, pady=10)
    hides.grid(row=11, pady=10)

    quit.grid(row=13, pady=15)
    Actions.grid(row = 4, pady=10)
    Build.grid(row=5, pady=10)
    forest.grid(row=6, pady=10)

    gatherer.grid(row=1, pady=10)
    hunter.grid(row=0, pady=10)
    tanner.grid(row=2, pady=10)
    people.grid(row=3, pady=10)

    frame1.grid(row=0, column=0, rowspan=8, columnspan=8)
    frame2.grid(row=0, column=9, rowspan=2, columnspan=2)

    picture.grid(row=0, column=0)

    def hunter_adder():
        root.destroy()
        read = open("Hunters.txt")
        hunter_count = int(read.readline(10))
        read.close()

        read = open("Tanners.txt")
        tanner_count = int(read.readline(10))
        read.close()

        read = open("gatherers.txt")
        gatherer_count = int(read.readline(10))
        read.close()

        read = open("people_count.txt")
        people_count = int(read.readline(10))
        read.close()

        task_count = hunter_count + gatherer_count + tanner_count

        if people_count > task_count:
            hunter_count += 1
            read = open("Hunters.txt", "w")
            read.write(str(hunter_count))
            read.close()
            start_game()
        else:
            hunter_win = tkinter.Tk()
            tkinter.Label(hunter_win, text="You do not have the necessary amount of people", fg="red").pack()
            tkinter.Label(hunter_win, text="Press X to return to camp.").pack()
            hunter_win.mainloop()
            time.sleep(1)
            start_game()

    def tanner_adder():
        root.destroy()
        read = open("Hunters.txt")
        hunter_count = int(read.readline(10))
        read.close()

        read = open("Tanners.txt")
        tanner_count = int(read.readline(10))
        read.close()

        read = open("gatherers.txt")
        gatherer_count = int(read.readline(10))
        read.close()

        read = open("people_count.txt")
        people_count = int(read.readline(10))
        read.close()

        task_count = hunter_count + gatherer_count + tanner_count

        if people_count > task_count:
            tanner_count += 1
            read = open("Tanners.txt", "w")
            read.write(str(tanner_count))
            read.close()
            start_game()
        else:
            hunter_win = tkinter.Tk()
            tkinter.Label(hunter_win, text="You do not have the necessary amount of people", fg="red").pack()
            tkinter.Label(hunter_win, text="Press X to return to camp.").pack()
            hunter_win.mainloop()
            time.sleep(1)
            start_game()

    def gatherer_adder():
        root.destroy()
        read = open("Hunters.txt")
        hunter_count = int(read.readline(10))
        read.close()

        read = open("Tanners.txt")
        tanner_count = int(read.readline(10))
        read.close()

        read = open("gatherers.txt")
        gatherer_count = int(read.readline(10))
        read.close()

        read = open("people_count.txt")
        people_count = int(read.readline(10))
        read.close()

        task_count = hunter_count + gatherer_count + tanner_count

        if people_count > task_count:
            gatherer_count += 1
            read = open("gatherers.txt", "w")
            read.write(str(gatherer_count))
            read.close()
            start_game()
        else:
            hunter_win = tkinter.Tk()
            tkinter.Label(hunter_win, text="You do not have the necessary amount of people", fg="red").pack()
            tkinter.Label(hunter_win, text="Press X to return to camp.").pack()
            hunter_win.mainloop()
            time.sleep(1)
            start_game()

    def actions_passover():
        root.destroy()
        actions()

    def build_win():
        root.destroy()

        buildings = tkinter.Tk()

        buildings.configure(background="orange")

        photo = tkinter.PhotoImage(file="Workshop.png")

        frame1 = tkinter.Frame(buildings)
        frame2 = tkinter.Frame(buildings)

        frame2.configure(background="grey")

        picture = tkinter.Label(frame1, image=photo)

        cart = tkinter.Button(frame2, text="Cart: 200 Wood", command=lambda : build_cart())
        convoy = tkinter.Button(frame2, text="Convoy: 800 Wood, 400 Hides, 50 Iron", command=lambda: build_convoy())
        cart_info = tkinter.Label(frame2, text="Cart lets you get 50 wood instead of 15")
        convoy_info = tkinter.Label(frame2, text="Convoy lets you gather 200 wood at a time")

        spacer_1 = tkinter.Label(frame2, text="====================================")
        spacer_1.configure(background="grey")
        spacer_2 = tkinter.Label(frame2, text="====================================")
        spacer_2.configure(background="grey")
        spacer_3 = tkinter.Label(frame2, text="====================================")
        spacer_3.configure(background="grey")

        leather_armour = tkinter.Button(frame2, text="Leather armour: 500 Hides", command=lambda: build_armour())

        hut = tkinter.Button(frame2, text="Huts: 500 Wood, 50 Hides", command=lambda: build_hut())

        quit = tkinter.Button(frame2, text="Return to Camp", command=lambda: quit_build())

        frame1.grid(row=0, column=0, rowspan=8, columnspan=8)
        frame2.grid(row=0, column=9, rowspan=2, columnspan=2)

        cart.grid(row= 1, pady=20)
        cart_info.grid(row=2, pady=20)
        convoy.grid(row=3, pady=20)
        convoy_info.grid(row=4, pady=20)

        hut.grid(row=8,pady=20)

        spacer_1.grid(row=5, pady=5)
        spacer_2.grid(row=7, pady=5)
        spacer_3.grid(row=9, pady=5)

        quit.grid(row=10, pady=20)

        leather_armour.grid(row=6, pady=20)

        picture.grid(row=0, column=0)

        def quit_build():
            buildings.destroy()
            start_game()

        def build_armour():
            read = open("hides.txt", "r")
            hide = int(read.readline(10))
            read.close()

            read = open("armour.txt", "r")
            health = int(read.readline(10))
            read.close()

            if hide >= 500 and health == 10:
                hide -= 500
                read = open("hides.txt", "w")
                read.write(str(hide))
                read.close()

                read = open("armour.txt", "w")
                read.write("20")
                read.close()
            else:
                print("invalid")
                buildings.destroy()
                start_game()

        def build_convoy():
            cart_status = ""
            wood_collection_read = open("wood_collection.txt", "r")
            wood_collection = int(wood_collection_read.readline(10))
            wood_collection_read.close()
            if wood_collection == 200:
                print("invalid operation")
                cart_status = "built"
            else:
                wood_collection = 200

            if cart_status == "built":
                print("You have been sent back to the home page")
                buildings.destroy()
                start_game()
            else:
                hide_read = open('hides.txt', "r")
                hides = int(hide_read.readline(10))
                hide_read.close()

                iron_read = open('iron.txt', "r")
                iron = int(iron_read.readline(10))
                iron_read.close()

                wood_read = open("wood.txt", "r")
                wood = int(wood_read.readline(10))
                if wood >= 800 and hides >= 500 and iron >= 50:
                    wood -= 800
                    hides -= 500
                    iron -= 50
                    wood_read.close()

                    wood_collection_write = open("wood_collection.txt", "w")
                    wood_collection_write.write(str(wood_collection))

                    wood_change = open("wood.txt", "w")
                    wood_change.write(str(wood))
                    wood_change.close()

                    iron_change = open("iron.txt", "w")
                    iron_change.write(str(iron))
                    iron_change.close()

                    hide_change = open("hides.txt", "w")
                    hide_change.write(str(hides))
                    hide_change.close()

        def build_hut():
            read = open("wood.txt", "r")
            wood_count = int(read.readline(10))
            read.close()
            read = open("hides.txt", "r")
            hides_count = int(read.readline(10))
            read.close()
            if wood_count >= 500 and hides_count >= 50:
                read = open("Huts.txt", "r")
                hut_count = int(read.readline(10))
                read.close()

                new_hut_count = hut_count + 1

                read = open("Huts.txt", "w")
                read.write(str(new_hut_count))
                read.close()

                read = open("wood.txt", "r")
                wood_count = int(read.readline(10))
                read.close()

                new_wood_count = wood_count - 500

                read = open("wood.txt", "w")
                read.write(str(new_wood_count))
                read.close()

                read = open("hides.txt", "r")
                hide_count = int(read.readline(10))
                read.close()

                new_hide_count = hide_count - 50

                read = open("hides.txt", "w")
                read.write(str(new_hide_count))
                read.close()

        def build_cart():
            cart_status = ""
            wood_collection_read = open("wood_collection.txt", "r")
            wood_collection = int(wood_collection_read.readline(10))
            wood_collection_read.close()
            if wood_collection > 50:
                print("invalid operation")
                cart_status = "built"
            else:
                wood_collection = 50

            if cart_status == "built":
                print("You have been sent back to the home page")
                buildings.destroy()
                start_game()
            else:
                wood_read = open("wood.txt", "r")
                wood = int(wood_read.readline(10))
                if wood >= 200:
                    wood -= 200
                    wood_read.close()

                    wood_collection_write = open("wood_collection.txt", "w")
                    wood_collection_write.write(str(wood_collection))
                    wood_collection_write.close()

                    wood_change = open("wood.txt", "w")
                    wood_change.write(str(wood))
                    wood_change.close()

        buildings.mainloop()

    def dark_forest_passover():
        root.destroy()
        dark_forest()

    def dark_forest():
        read = open("health.txt", "r")
        health = int(read.readline(10))
        read.close()

        if health > 0:
            pic = ""

            Forest = tkinter.Tk()

            Forest.configure(background="green")

            frame_forest = tkinter.Frame(Forest)
            frame_forest.grid(rowspan=10, columnspan=10)

            movement = tkinter.Frame(Forest)
            movement.grid(column = 0, row= 10, rowspan=4, columnspan=4)

            movement.configure(background="gray")

            exit = tkinter.Button(movement, text="Return to base", command=lambda: quit2())
            exit.grid(column=4, row=13)

            left = tkinter.Button(movement, text="Left", command=lambda: quit_main())
            left.grid(column=3, row=11)

            right = tkinter.Button(movement, text="Right", command=lambda: quit_main())
            right.grid(column=5, row=11)

            down = tkinter.Button(movement, text="Down", command=lambda: quit_main())
            down.grid(column=4, row=12)

            up = tkinter.Button(movement, text="Up", command = lambda : quit_main())
            up.grid(column=4, row=10)

            health_lbl = tkinter.Label(movement, text="Health: " + str(health))
            health_lbl.grid(column=4, row=17, pady = 1)

            picture_decider = random.randint(0, 2)

            if picture_decider == 0:
                pic = "marsh.png"
                event_decider_first = random.randint(0, 4)
                if event_decider_first == 1:
                    event = tkinter.Label(movement, text="Crocodile attack, -4 to hp")

                    read = open("health.txt", "r")
                    health = int(read.readline(10))
                    read.close()

                    health -= 4

                    read = open("health.txt", "w")
                    read.write(str(health))
                    read.close()

                    event.grid(column = 0, row = 14, columnspan=7)

                elif event_decider_first == 0:
                    event = tkinter.Label(movement, text="Dead animal, +5 food, +2 bones, +3 hides")
                    event.grid(column = 0, row = 14, columnspan=7)

                    read = open("meat_count.txt", "r")
                    meat = int(read.readline(10))
                    meat += 5
                    read.close()

                    read = open("bones.txt", "r")
                    bones = int(read.readline(10))
                    bones += 2
                    read.close()

                    read = open("hides.txt", "r")
                    hides = int(read.readline(10))
                    hides += 3
                    read.close()

                    read = open("meat_count.txt", "w")
                    read.write(str(meat))
                    read.close()

                    read = open("bones.txt", "w")
                    read.write(str(bones))
                    read.close()

                    read = open("hides.txt", "w")
                    read.write(str(hides))
                    read.close()

                elif event_decider_first == 2:
                    read = open("People_Relations.txt", "r")
                    people_relations = read.readline(20)
                    read.close()

                    read = open("people_count.txt", "r")
                    people_original = int(read.readline(10))
                    read.close()

                    read = open("Huts.txt", "r")
                    hut_count = int(read.readline(10))
                    read.close()

                    max_people = hut_count * 3

                    if max_people <= people_original:
                        event = tkinter.Label(movement, text="Person found, no room to hold them.")

                    else:
                        event = tkinter.Label(movement, text="Person found, +1 to " + people_relations)

                        people_count = people_original + 1

                        read = open("people_count.txt", "w")
                        read.write(str(people_count))
                        read.close()

                    event.grid(column = 0, row = 14, columnspan=7)

                elif event_decider_first == 3:
                    event = tkinter.Label(movement, text="Snake attack, -2 to hp")
                    event.grid(column = 0, row = 14, columnspan=7)
                    read = open("health.txt", "r")
                    health = int(read.readline(10))
                    read.close()

                    health -= 2

                    read = open("health.txt", "w")
                    read.write(str(health))
                    read.close()

                elif event_decider_first == 4:
                    event = tkinter.Label(movement, text="Quicksand, you die, -50 wood")
                    event.grid(column = 0, row = 14, columnspan=7)
                    read = open("health.txt", "r")
                    health = int(read.readline(10))
                    read.close()

                    health -= health

                    read = open("health.txt", "w")
                    read.write(str(health))
                    read.close()

            elif picture_decider == 1:
                pic = "tree.png"
                event_decider_first = random.randint(0, 4)
                if event_decider_first == 1:
                    event = tkinter.Label(movement, text="Monkey attack, -4 to hp")
                    event.grid(column=0, row=14, columnspan=7)
                    read = open("health.txt", "r")
                    health = int(read.readline(10))
                    read.close()

                    health -= 4

                    read = open("health.txt", "w")
                    read.write(str(health))
                    read.close()

                elif event_decider_first == 0:
                    event = tkinter.Label(movement, text="Dead monkey, +5 food, +2 bones, +3 hides")
                    event.grid(column=0, row=14, columnspan=7)

                    read = open("meat_count.txt", "r")
                    meat = int(read.readline(10))
                    meat += 5
                    read.close()

                    read = open("bones.txt", "r")
                    bones = int(read.readline(10))
                    bones += 2
                    read.close()

                    read = open("hides.txt", "r")
                    hides = int(read.readline(10))
                    hides += 3
                    read.close()

                    read = open("meat_count.txt", "w")
                    read.write(str(meat))
                    read.close()

                    read = open("bones.txt", "w")
                    read.write(str(bones))
                    read.close()

                    read = open("hides.txt", "w")
                    read.write(str(hides))
                    read.close()

                elif event_decider_first == 2:
                    read = open("People_Relations.txt", "r")
                    people_relations = read.readline(20)
                    read.close()

                    read = open("people_count.txt", "r")
                    people_original = int(read.readline(10))
                    read.close()

                    read = open("Huts.txt", "r")
                    hut_count = int(read.readline(10))
                    read.close()

                    max_people = hut_count * 3

                    if max_people <= people_original:
                        event = tkinter.Label(movement, text="Person found, no room to hold them.")

                    else:
                        event = tkinter.Label(movement, text="Person found, +1 to " + people_relations)

                        people_count = people_original + 1

                        read = open("people_count.txt", "w")
                        read.write(str(people_count))
                        read.close()

                    event.grid(column=0, row=14, columnspan=7)

                elif event_decider_first == 3:
                    event = tkinter.Label(movement, text="Dead birds, +4 feathers, +6 meat, +3 bones")
                    event.grid(column=0, row=14, columnspan=7)

                    read = open("meat_count.txt", "r")
                    meat = int(read.readline(10))
                    meat += 6
                    read.close()

                    read = open("bones.txt", "r")
                    bones = int(read.readline(10))
                    bones += 3
                    read.close()

                    read = open("feathers.txt", "r")
                    feather = int(read.readline(10))
                    feather += 4
                    read.close()

                    read = open("meat_count.txt", "w")
                    read.write(str(meat))
                    read.close()

                    read = open("bones.txt", "w")
                    read.write(str(bones))
                    read.close()

                    read = open("feathers.txt", "w")
                    read.write(str(feather))
                    read.close()

                elif event_decider_first == 4:
                    event = tkinter.Label(movement, text="You stepped in a rival colony trap, you die, -50 wood")
                    event.grid(column=0, row=14, columnspan=7)
                    read = open("health.txt", "r")
                    health = int(read.readline(10))
                    read.close()

                    health -= health

                    read = open("health.txt", "w")
                    read.write(str(health))
                    read.close()
            elif picture_decider == 2:
                pic = "plains.png"
                event_decider_first = random.randint(0, 4)
                if event_decider_first == 1:
                    event = tkinter.Label(movement, text="Lion attack, -4 to hp")
                    event.grid(column=0, row=14, columnspan=7)
                    read = open("health.txt", "r")
                    health = int(read.readline(10))
                    read.close()

                    health -= 4

                    read = open("health.txt", "w")
                    read.write(str(health))
                    read.close()

                elif event_decider_first == 0:
                    event = tkinter.Label(movement, text="Dead elephant, +5 food, +2 bones, +3 hides")
                    event.grid(column=0, row=14, columnspan=7)

                    read = open("meat_count.txt", "r")
                    meat = int(read.readline(10))
                    meat += 5
                    read.close()

                    read = open("bones.txt", "r")
                    bones = int(read.readline(10))
                    bones += 2
                    read.close()

                    read = open("hides.txt", "r")
                    hides = int(read.readline(10))
                    hides += 3
                    read.close()

                    read = open("meat_count.txt", "w")
                    read.write(str(meat))
                    read.close()

                    read = open("bones.txt", "w")
                    read.write(str(bones))
                    read.close()

                    read = open("hides.txt", "w")
                    read.write(str(hides))
                    read.close()

                elif event_decider_first == 2:
                    read = open("People_Relations.txt", "r")
                    people_relations = read.readline(20)
                    read.close()

                    read = open("people_count.txt", "r")
                    people_original = int(read.readline(10))
                    read.close()

                    read = open("Huts.txt", "r")
                    hut_count = int(read.readline(10))
                    read.close()

                    max_people = hut_count * 3

                    if max_people <= people_original:
                        event = tkinter.Label(movement, text="Person found, no room to hold them.")

                    else:
                        event = tkinter.Label(movement, text="Person found, +1 to " + people_relations)

                        people_count = people_original + 1

                        read = open("people_count.txt", "w")
                        read.write(str(people_count))
                        read.close()

                    event.grid(column=0, row=14, columnspan=7)

                elif event_decider_first == 3:
                    event = tkinter.Label(movement, text="Bison stampede, -1 to hp, +10 to meat, + 5 to bones + 4 to hides")
                    event.grid(column=0, row=14, columnspan=7)
                    read = open("health.txt", "r")
                    health = int(read.readline(10))
                    read.close()

                    health -= 1

                    read = open("health.txt", "w")
                    read.write(str(health))
                    read.close()

                    read = open("meat_count.txt", "r")
                    meat = int(read.readline(10))
                    meat += 10
                    read.close()

                    read = open("bones.txt", "r")
                    bones = int(read.readline(10))
                    bones += 5
                    read.close()

                    read = open("hides.txt", "r")
                    hides = int(read.readline(10))
                    hides += 4
                    read.close()

                    read = open("meat_count.txt", "w")
                    read.write(str(meat))
                    read.close()

                    read = open("bones.txt", "w")
                    read.write(str(bones))
                    read.close()

                    read = open("hides.txt", "w")
                    read.write(str(hides))
                    read.close()

                elif event_decider_first == 4:
                    event = tkinter.Label(movement, text="You loose yourself in the grass, you die of starvation, -50 wood")
                    event.grid(column=0, row=14, columnspan=7)
                    read = open("health.txt", "r")
                    health = int(read.readline(10))
                    read.close()

                    health -= health

                    read = open("health.txt", "w")
                    read.write(str(health))
                    read.close()

            tree = tkinter.PhotoImage(file=pic)

            back_ground = tkinter.Label(frame_forest, image=tree)
            back_ground.grid(row=0, column=0, rowspan=10, columnspan=10)

            iron_decider = random.randint(0, 100)
            if iron_decider == 1:
                a = random.randint(0, 5)
                event2 = tkinter.Label(movement, text="You found iron! +" + str(a))

                read = open("iron.txt", "r")
                iron = int(read.readline(10))
                read.close()

                iron += a

                read = open("iron.txt", "w")
                read.write(str(iron))
                read.close()

                event2.grid(column=0, row=15, columnspan=7)

            def quit2():
                Forest.destroy()
                start_game()

            def quit_main():
                Forest.destroy()
                dark_forest()

            Forest.mainloop()
        else:
            read = open("wood.txt", "r")
            wood_count = int(read.readline(10))
            read.close()

            wood_count = wood_count - 50

            read = open("wood.txt", "w")
            read.write(str(wood_count))
            read.close()

            read = open("health.txt", "r")
            health_count = int(read.readline(10))
            read.close()

            read = open("armour.txt", "r")
            armour_count = int(read.readline(10))
            read.close()

            health_count = armour_count

            read = open("health.txt", "w")
            read.write(str(health_count))
            read.close()

            Forest = tkinter.Tk()
            death = tkinter.PhotoImage(file="Skull.png")

            back_ground = tkinter.Label(Forest, image=death)
            back_ground.grid()

            tkinter.Label(Forest, text="You died. Press x to go back to camp", fg="red").grid()

            Forest.mainloop()

            start_game()

    def actions():
        depot = tkinter.Tk()

        photo = tkinter.PhotoImage(file="Cart.png")

        frame1 = tkinter.Frame(depot)
        frame2 = tkinter.Frame(depot)

        depot.configure(background="orange")
        frame2.configure(background="orange")

        picture = tkinter.Label(frame1, image=photo)

        quit = tkinter.Button(frame2, text="Return to camp", command=lambda: close_win())

        make_wood = tkinter.Button(frame2, text="Collect wood", command=lambda : wood_adder())
        get_meat = tkinter.Button(frame2, text="Set traps", command=lambda : meat_adder())
        get_hides = tkinter.Button(frame2, text="Procure hides", command=lambda: hide_adder())
        get_items = tkinter.Button(frame2, text="Scavenge the ground", command=lambda: item_adder())

        get_meat.grid(row=5, pady=20)
        make_wood.grid(row=6, pady=20)
        get_hides.grid(row=7, pady=20)
        get_items.grid(row=8, pady=20)
        quit.grid(row=9, pady=20)

        frame1.grid(row=0, column=0, rowspan=8, columnspan=8)
        frame2.grid(row=0, column=9, rowspan=2, columnspan=2)

        picture.grid(row=0, column=0)

        def close_win():
            depot.destroy()
            start_game()

        def wood_adder():
            read = open("wood.txt", "r")
            wood = int(read.readline(10))
            read.close()

            read = open("wood_collection.txt", "r")
            wood_adding_sum = int(read.readline(10))
            read.close()

            wood_count = wood_adding_sum + wood

            read = open("wood.txt", "w")
            read.write(str(wood_count))
            read.close()

        def hide_adder():
            read = open("hides.txt", "r")
            hide = int(read.readline(10))
            read.close()

            read = open("Tanners.txt", "r")
            hide_adding_sum = int(read.readline(10))
            read.close()

            hide_count = hide_adding_sum + hide

            read = open("hides.txt", "w")
            read.write(str(hide_count))
            read.close()

        def item_adder():
            read = open("feathers.txt", "r")
            feather = int(read.readline(10))
            read.close()

            feather_count = feather + random.randint(0,3)

            read = open("wood.txt", "r")
            wood = int(read.readline(10))
            read.close()

            wood_count = wood + random.randint(0,10)

            read = open("bones.txt", "r")
            bones = int(read.readline(10))
            read.close()

            bone_count = bones + random.randint(0, 10)

            read = open("wood.txt", "w")
            read.write(str(wood_count))
            read.close()
            read = open("feathers.txt", "w")
            read.write(str(feather_count))
            read.close()
            read = open("bones.txt", "w")
            read.write(str(bone_count))
            read.close()

        def meat_adder():
            read = open("meat_count.txt", "r")
            meat = int(read.readline(10))
            read.close()

            read = open("Hunters.txt", "r")
            meat_adding_sum = int(read.readline(10)) * 3
            read.close()

            meat_count = meat_adding_sum + meat

            read = open("meat_count.txt", "w")
            read.write(str(meat_count))
            read.close()
        depot.mainloop()

    def quit():
        root.destroy()
    root.mainloop()


username = input("Username: ")
if username != "":
    user_checker(username)
else:
    print("That is not a legible user name, please re run this program")