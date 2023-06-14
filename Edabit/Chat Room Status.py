def chatroom_status(list1):
    if len(list1) == 0:
        print("no one online")
    elif len(list1) == 1:
        print(f"{list1[0]} online")
    elif len(list1) == 2:
        print(f"{list1[0]} and {list1[1]} online")

    else:
        print(f"{list1[0]}, {list1[1]} and {len(list1)-2} more online")

chatroom_status(["pap_ier44", "townieBOY",
 "panda321", "motor_bike5", "sandwichmaker833", "violinist91"])
