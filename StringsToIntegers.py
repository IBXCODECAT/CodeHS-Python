def safe_int(char):
    try:
        return int(char)
    except:
        return 0

list_of_strings = ["a", "2", "7", "zebra"]
final_list = []

for char in [x for x in list_of_strings]: final_list.append(safe_int(char))

print final_list