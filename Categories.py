items = "";
cat = "";

for i in range(3):
    items = ""
    cat = input("Please enter a catagroy: ")
    
    for i in range(3):
        temp_item = input("Please enter a list item: ")
        items = items + temp_item + " "
    
    print cat + ": " + items