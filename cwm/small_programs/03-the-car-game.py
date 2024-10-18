command = ""
start_status = False
#stop_status = True
while True:
    command = input("> ").lower()
    if command == "start":
        if start_status: # <--- Boolean vale initialised as False
            print("The car is already started.")
        else:
            start_status = True
            print("The car started ... let's go.")
    elif command == "stop":
        if not start_status: # <--- 'if not' looking to act on False value for boolean
            print("The car is already stopped.")
        else:
            start_status = False
            print("The car has stopped.")
    elif command == "help":
        print("""
    start - start the car
    stop  - stop the car
    quit  - quit the game
              """)
    elif command == "quit":
        print("Thanks for playing.")
        break
    else:
        print("Invalid command, try again.")