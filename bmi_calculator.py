print("=" * 35)
print("       BMI CALCULATOR")
print("=" * 35)

try:
    # User Input
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (meters): "))

    # Validation
    if weight <= 0 or height <= 0:
        print("Weight and height must be greater than 0.")

    else:
        # BMI Calculation
        bmi = weight / (height ** 2)

        print("\nYour BMI is:", round(bmi, 2))

        # BMI Category
        if bmi < 18.5:
            print("Category: Underweight")

        elif bmi < 25:
            print("Category: Normal Weight")

        elif bmi < 30:
            print("Category: Overweight")

        else:
            print("Category: Obese")

except ValueError:
    print("Please enter valid numeric values.")