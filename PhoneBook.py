names = {}

inputl = True
while(inputl):
    name = input('Enter a name to lookup or file>>>').strip()
    
    if(name == ''):
        inputl = False
    else:
        if name in names:
            print names[name]
        else:
            
            invalid = True
            while(invalid):
        
                num = input('Enter the phone number to file>>>')
                
                if(not num.isnumeric()):
                    print 'phone number must be numeric'
                else:
                    if(len(num) != 10):
                        print 'phone number must be ten chars long'
                    else:
                        invalid = False
                        names[name] = num
                        
print "buh bye"