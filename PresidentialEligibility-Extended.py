#Prompt for user's input and store it inside of variables

age = int(input("Enter your age: "))
nationality = input("Enter if you from the US 'Yes' or 'No': ")
resident = int(input("Enter how many years have you lived in the US: "))

#Check that requirements to run for presient have been met

if (age >= 18 and nationality == "Yes" and resident >= 14):
    
    print("\nYou are eligible to run for president. Reasons for eligibility:")
    print("\b\tAge > 18\n\b\tUS naturally born citizen\n\b\tUs resident more than 14 years")

else: #requirements were not met
    
    #Check to see which requirements were not met and report to the user
    
    if(age < 18 and nationality != "Yes" and resident < 14): #All three requirements have not been met?
        
        print("\nYou are not eligible to run for president Reasons for ineligibility:")
        print("\b\tYou are too young to run for president\n\b\tYou were not born in the United States\n\b\tYou have not been a United States resident for more than 14 years")
        
    else: #Only 1 or 2 requirement(s) have not been met
    
        #Check if two requirements were missed
        
        if(age < 18 and nationality != "Yes"): #First two requirements have not been met?
            
            print("\nYou are not eligible to run for president Reasons for ineligibility:")
            print("\b\tYou are too young to run for president\n\b\tYou were not born in the United States")
            
        elif(nationality != "Yes" and resident < 14): #Last two requirements have not been met?
            
            print("\nYou are not eligible to run for president Reasons for ineligibility:")
            print("\b\tYou were not born in the United States\n\b\tYou have not been a United States resident for more than 14 years")
            
        elif(resident < 14 and age < 18): #First and last requirement have not been met?
            
            print("\nYou are not eligible to run for president Reasons for ineligibility:")
            print("\b\tYou are too young to run for president\n\b\tYou have not been a United States resident for more than 14 years")
        
        else: #Only one requirement has been missed
            
            if(age < 18):
                
                print("\nYou are not eligible to run for president Reasons for ineligibility:")
                print("\b\tYou are too young to run for president")
        
            elif(nationality != "Yes"):
                
                print("\nYou are not eligible to run for president Reasons for ineligibility:")
                print("\b\tYou were not born in the United States")
                
            else: #There are no other alternitaves, the requirement missed must be residency
                
                print("\nYou are not eligible to run for president Reasons for ineligibility:")
                print("\b\tYou have not been a United States resident for more than 14 years")