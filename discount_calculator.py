# Discount Calculator Program
# This script calculates the final price of an item after applying a discount (if applicable)

def calculate_discount(price, discount_percent):
    """
    Calculates the discounted price if the discount is 20% or more
    Args:
        price (float): Original item price
        discount_percent (float): Discount percentage (e.g., 20 for 20%)
    Returns:
        float: The final price after discount (or original price if discount too low)
    """
    # Only apply discount if it's 20% or more
    if discount_percent >= 20:
        # Calculate how much money we're taking off
        discount_amount = price * (discount_percent / 100)
        # Subtract discount from original price
        return price - discount_amount
    else:
        # Return original price if discount is too small
        return price

# Get user input and show results
def run_program():
    print("\nWelcome to the Discount Calculator")
    print("--------------------------------------")
    
    try:
        # Ask for price and validate input
        original_price = float(input("What's the item's original price? $"))
        if original_price <= 0:
            print("Price must be greater than zero!")
            return
            
        discount_percent = float(input("What's the discount percentage? (e.g., 25 for 25%) "))
        
        # Calculate the final price
        final_price = calculate_discount(original_price, discount_percent)
        
        # Display results in a user-friendly way
        if final_price < original_price:
            print(f"\nYou saved ${original_price - final_price:.2f}!")
            print(f"Original price: ${original_price:.2f}")
            print(f"Discount applied: {discount_percent}%")
            print(f"Final price: ${final_price:.2f}")
        else:
            print("\nNo discount applied (must be 20% or higher)")
            print(f"Your price remains at ${original_price:.2f}")
            
        print("\nThank you for shopping with us!\n")
        
    except ValueError:
        print("\nOops! Please enter valid numbers only.\n")

# Run the program when this file is executed
if __name__ == "__main__":
    run_program()
