print("This Program will prompt the user to enter a students first and last name, then their three test scores."
      + " Then the program will display the name of the student and their test average.")

first_name = input("Enter Student First Name:")
last_name = input("Enter Student Last Name:")
test_1 = input("Enter Test 1 Score:")
test_2 = input("Enter Test 2 Score:")
test_3 = input("Enter Test 3 Score:")

print("\nStudent: " + first_name +" "+ last_name)

test_avg = ((float)(test_1)+(float)(test_2+test_3)/3.0

print("Test Average: " + (str)(test_avg))
