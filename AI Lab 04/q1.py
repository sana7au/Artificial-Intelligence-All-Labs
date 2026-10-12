correct_pin = 4521

while(True):
    print("\n======ATM PIN CHECK======")
    input_pin = input("Enter PIN: (Type \"cancel\" to end): ")

    if(input_pin == "cancel"):
        print("Transaction Cancelled.")
        break
        
    if(correct_pin != int(input_pin)):
        print("Incorrect PIN, try again.")
        continue
    
    if(correct_pin == int(input_pin)):
        print("Access Granted!")
        break
