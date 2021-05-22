KEY = "owl"
itemCount = 0
itemIndecies = []

search = input("Please type a paragraph bellow:\n")

i_search = search.strip().lower()
i_content = i_search.split()

for index, item in enumerate(i_content):
    if(item.find(KEY) != -1):
        itemCount = itemCount + 1
        itemIndecies = itemIndecies + [index]
        
print "There were " + str(itemCount) + " words that contained \"" + KEY + "\".\nThey occurred at indices: " + str(itemIndecies)