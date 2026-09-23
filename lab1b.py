#fee calculator
order = float(input("Enter the order amount ($): "))
day = input("Enter the day of the week: ")

if order <= 0:
    print("Invalid order amount. Please enter a positive value.")
    exit()
    
valid_days = ["monday", "tuesday","wednesday","thursday", "friday", "saturday", "sunday"]
if day not in valid_days:
    print("Invalid day. Please enter a valid day of the week.")
   
elif order < 20:
    status = "$5 delivery fee"
elif order >= 20 and order < 50:
    status = "$3 delivery fee"
elif order >= 50 and order < 100:
    status = "$1 delivery fee" 
elif order >= 100:
    status = "Free delivery"
print(f"Order amount: ${order:.2f}")
print(f"Delivery fee: {status}")
