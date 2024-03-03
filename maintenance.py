def calculate_bmr(gender, weight, height, age):
    if gender.lower() == "male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    elif gender.lower() == "female":
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    else:
        raise ValueError("Invalid gender. Please enter 'Men' or 'Women'.")
    return bmr

def calculate_maintenance_calories(bmr, activity_factor):
    maintenance_calories = bmr * activity_factor
    return maintenance_calories

def main():
    gender = input("Enter gender (Male/Female): ")
    age = int(input("Enter age (in years): "))
    weight = float(input("Enter weight (in kg): "))
    height = float(input("Enter height (in cm): "))
    
    print("\nChoose activity level:")
    print("1. Sedentary")
    print("2. Moderately active")
    print("3. Vigorously active")
    print("4. Extremely active")
    
    activity_choice = int(input("Enter the number corresponding to your activity level: "))
    
    activity_factors = {1: 1.55, 2: 1.85, 3: 2.2, 4: 2.4}
    
    if activity_choice not in activity_factors:
        print("Invalid activity level choice. Please select a number between 1 and 4.")
        return
    
    activity_factor = activity_factors[activity_choice]
    
    bmr = calculate_bmr(gender, weight, height, age)
    maintenance_calories = calculate_maintenance_calories(bmr, 1.85)
    
    print("\nResults:")
    print(f"BMR: {bmr} calories/day")
    print(f"Maintenance Calories: {maintenance_calories} calories/day")

if __name__ == "__main__":
    main()
