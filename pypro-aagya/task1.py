def pos_int(num):
    '''function to take a positive integer'''
    while True:
        try:
            value = int(input(num))
            if value > 0:
                return value
            elif value == 0:
                print("You cannot order nothing!")
            elif value < 0:
                print("Please, enter the positive integer!")
        except:
            print("Please enter a valid value!")

# Function to get a yes/no input from the user

def user_input(inp):
    while True:
        response = input(inp).lower()
        if response == 'y' or response == 'yes':
            return 'y'
        elif response == 'n' or response == 'no':
            return 'n'
        else:
            print('Please answer "Y" or "N"!')

# Function to calculate the total price of the pizza order

def final_total(num_pizzas, requires_delivery, is_tuesday, used_app):
    # Constants given in the question
    pizza_price = 12
    if num_pizzas < 5 and requires_delivery == 'y':
         delivery_cost = 2.50
    else:
         delivery_cost = 0
         
    if is_tuesday == 'y':
       tuesday_discount = 0.5 
    else:
        tuesday_discount = 0
        
    if used_app == 'y':
       app_discount = 0.25
    else:
        app_discount = 0

    total_cost = num_pizzas * pizza_price + delivery_cost
    
    # Applying required discounts
    discounted_cost = total_cost * (1 - tuesday_discount) * (1 - app_discount) #simplified version of discount formula
    return round(discounted_cost, 2)


print("BPP Pizza Price Calculator")
print("GET UPTO 50% DISCOUNT ON TUESDAY'SS!!!!\n")


# Get user input 
num_pizzas = pos_int("How many pizzas ordered? ")
requires_delivery = user_input("Is delivery required? (Y/N) ")
is_tuesday = user_input("Is it Tuesday? (Y/N) ")
used_app = user_input("Did the customer use the app? (Y/N) ")

# calling the function and displaying the total price
total_price = final_total(num_pizzas, requires_delivery, is_tuesday, used_app)
print(f"\nTotal Price: £{total_price:.2f}.")



