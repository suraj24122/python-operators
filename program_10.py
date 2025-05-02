'''
Check if a person can apply for a driving license:

Conditions: age ≥ 18 and they must pass an eye test (yes/no)
'''

age = int(input("Enter your age: "))
eye_test = input("Did you pass the eye test? (yes/no): ").strip().lower()

if age >= 18 and eye_test == "yes":
    print("You are eligible to apply for a driving license.")
else:
    print("You are not eligible to apply for a driving license.")


