dataset = [
    [20, 90, "hiking, football, basketball, singing"],
    [22, 85, "hiking, singing"],
    [24, 80, "football, basketball"],
    [26, 75, "hiking, basketball, singing"],
    [28, 70, "football, singing"],
    [30, 65, "hiking, football"],
    [32, 60, "basketball, singing"],
    [34, 55, "hiking, basketball"],
    [36, 50, "football"],
    [38, 45, "hiking, singing"],
    [40, 40, "basketball"],
    [42, 35, "football, singing"],
    [44, 30, "hiking, basketball"],
    [46, 25, "football"],
    [48, 20, "hiking, singing"],
    [50, 15, "basketball"],
    [52, 10, "football, singing"],
    [54, 5, "hiking, basketball"],
    [56, 0, "football"]
]
import math

def match_user(age, grade, hobbies):
    min_distance = float('inf')
    best_match = None
    
    for user in dataset:
        # Calculate the Euclidean distance between the input user and the current user in the dataset
        distance = math.sqrt((user[0] - age)**2 + (user[1] - grade)**2)
        
        # If the distance is smaller than the current minimum, update the minimum and the best match
        if distance < min_distance:
            min_distance = distance
            best_match = user
    
    return best_match

# Get the input from the user
age = int(input("Enter your age: "))
grade = int(input("Enter your grade (between 0 and 100): "))
hobbies = input("Enter your hobbies (should be one of the followings : hiking, football, basketball, singing and separated by commas): ").split(", ")

# Find the best match for the input user
best_match = match_user(age, grade, hobbies)

# Print the result
print("Your best match is:")
print("Age:", best_match[0])
print("Grade:", best_match[1])
print("Hobbies", best_match[2])
