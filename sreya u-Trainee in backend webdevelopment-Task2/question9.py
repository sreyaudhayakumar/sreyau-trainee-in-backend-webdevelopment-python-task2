# 9.Define a function that accepts roll number and returns whether the student is present or absent

def attendance(roll_number):
    present_roll_numbers = [27, 15, 10, 14, 28, 17, 16, 18, 1, 12]
    if roll_number in present_roll_numbers:
        print("student is present")
    else:
        print("student is absent")
        
roll_number = int(input("Enter the roll number: "))
attendance(roll_number)

        
    
    