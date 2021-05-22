role = input("Are you adminastrator, student or teacher: ")

if role != "adminastrator" and role != "student" and role != "teacher":
    print("You can only be an administrator, teacher, or student!")
elif (role == "adminastrator" or role == "teacher"):
    print("Administrators and teachers get keys!")
else:
    print("Students do not get keys")