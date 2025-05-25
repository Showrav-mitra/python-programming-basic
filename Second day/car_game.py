command = ''                # loop initial statement like i=0, here command as an empty string
while command != "quit":    # Condition then start the loop
    command = input(">").lower()
    if command == "start":
        print("Car Started")
    elif command=="stop":
        print("Car Stopped")
    elif command =="help":
        print("""
              Start - to start the car
              stop - to stop the car
              quit - to quit
              """)
    elif command == "quit":
        break
    else:
        print("sorry, i don't understand")