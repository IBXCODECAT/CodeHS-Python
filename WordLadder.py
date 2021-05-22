BREAK = -1

def Init():
    return input("Enter an initial word for the word ladder\n")

def NextChar():
    
    returnValue = input("Enter a char: ")
    
    while(returnValue.isupper()):
        print "Character must be a lowercase letter!"
        
        returnValue = input("Enter a char: ")
    
    while(len(returnValue) > 1):
        print "Must be exactly one character!"
        
        returnValue = input("Enter a char: ")
        
    return returnValue
    
def NextIndex(word):

    invalid = True
    
    while(invalid):
        try:
            returnValue =  int(input("Enter an index to modify (-1 to quit): "))
            
            if(returnValue < -1 or returnValue > len(word)):
                print "Invalid index"
            else:
                invalid = False
                return returnValue
            
        except ValueError:
            print "ValueErr: Index must be of type 'int'."

#==============================================================================#

initState = Init()

_init = initState
_index = NextIndex(_init)

while(_index != BREAK):
    _init = _init[0 : _index] + NextChar() + _init[_index + 1 : len(_init)]
    print _init
    
    _index = NextIndex(_init)