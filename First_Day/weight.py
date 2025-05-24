w = input("Weight: ")
unit = input("Enter unit (lbs or kg): ").lower()  # make lowercase for easy comparison

if unit == 'lbs':
    convert = int(w) * 0.45
    print(f'Weight in kg = {convert}')

elif unit == 'kg':
    convert = int(w) / 0.45
    print(f'Weight in lbs = {convert}')

else:
    print('Invalid unit. Please enter "kg" or "lbs".')
