##Inputs from user 
#total rent 
#total food ordered for sncaking 
#Electricity uints spend 
#charge per unit 
#Inout persons living in room

##output 
#total amount you've to pay is


rent = int(input("Enter your hostel/flat rent = "))
food =int(input("Enter the amount of foode ordered = "))
electricty_spend =int(input("Enter the total of electricty spend = "))
charge_per_unit =int(input("Enter the charge per unit = "))

persons =int(input("Enter the number of persons living in room/flat = "))

total_bill = electricty_spend * charge_per_unit

output = (food+rent +total_bill)  // persons

print("Each person will pay = ",output)
