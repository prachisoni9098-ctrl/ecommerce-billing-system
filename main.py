print("==========================================================")
print("🛍️ E-COMMERCE RETAIL ORDER BILLING ENGINE (v1.0)")
print("==========================================================\n")

# Taking the customer name,bill amount, and membership status from input
customer_name = input("Enter Customer Name: ")
bill_amount = float(input("Enter Total Shopping Bill Amount (₹): "))
is_prime_member = input("Is the customer a Prime Member? (yes/no): ").strip().lower()

print("\n" + "-" * 55)
print(f"📦 PROCESSING INVOICE FOR: {customer_name.upper()}")
print("-" * 55)

# Checking bill amount and membership to apply the right discount rates
if bill_amount >= 5000:
    if is_prime_member == 'yes':
        discount_percentage = 20  
    else:
        discount_percentage = 15  
elif bill_amount >= 2000:
    discount_percentage = 10      
else:
    discount_percentage = 0       

# Simple math to calculate the discount value and final price
discount_value = (bill_amount * discount_percentage) / 100
final_payable_amount = bill_amount - discount_value

# Printing the final clear invoice summary on the screen
print(f"• Raw Bill Amount     : ₹{bill_amount:.2f}")
print(f"• Applied Discount    : {discount_percentage}% (Saved: ₹{discount_value:.2f})")
print(f"• Final Net Payable   : ₹{final_payable_amount:.2f}")
print("==========================================================")
