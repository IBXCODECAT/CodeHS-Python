age = int(input("Please enter your age: "))
nationality = input("Are you from the US 'Yes' or 'No': ")


if (age >= 18 and nationality == "Yes"):
    print("You are eligible to run for president.")
else:
    print("You are not eligible to run for president.")