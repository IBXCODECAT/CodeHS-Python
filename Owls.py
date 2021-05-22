KEY = "owl"
itemCount = 0

search = input("Please type a paragraph bellow:\n")

i_search = search.strip().lower()
i_content = i_search.split()

for item in i_content:
    if(item.find(KEY) != -1):
        itemCount = itemCount + 1
        
print "There were " + str(itemCount) + " words that contained \"" + KEY + "\""