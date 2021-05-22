def retrieve_positive_number():
    while(prompt):
        try:
            num = float(input("Enter a number: "))
            
            if(num >= 0):
                return num
            else:
                print("number can not be negated")
                
        except ValueError:
            print("number not valid try again")