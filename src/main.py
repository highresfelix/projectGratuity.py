def calculate_meal_cost():
    # get the charge for the food from the user
    food_charge = float(input("Enter the charge for the food: $"))

    # calculate the tip (18% of food charge)
    tip = food_charge * 0.18

    # calculate the sales tax (7% of food charge)
    tax = food_charge * 0.07

    # calculate the total cost
    total_cost = food_charge + tip + tax

    # display the caluated amounts
    print(f"\nCharge for the food: ${food_charge:.2f}")
    print("")
    print("")
    print("")