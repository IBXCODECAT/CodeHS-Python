content = input("Enter a string bellow:\n")

content = content.split()

result = ""

for word in range(len(content)):
    
    i_word = content[word]
    
    for char in range(len(i_word)):
        
        if(i_word[char] == "i"):
            i_word = i_word[0 : char] + "!" + i_word[char + 1 : len(i_word)]
    
    result = result + i_word

print result