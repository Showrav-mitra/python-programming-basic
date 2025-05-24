age = int(input("what is the age? "))
if age < 13:
    print("You are a child.")
elif age >=13 and age < 19:  # elif 13 <= age <= 19:

    print("You are a teenager.")
else:
    print("You are an adult.")