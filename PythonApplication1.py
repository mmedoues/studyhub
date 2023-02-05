dataset = [
    [16, "11th", 90, "John Doe", "hiking, football, basketball, singing"],
    [18, "12th", 85, "Jane Doe", "hiking, singing"],
    [20, "12th", 80, "Jim Smith", "football, basketball"],
    [14, "9th", 75, "Alice Johnson", "hiking, basketball, singing"],
    [15, "10th", 70, "Bob Brown", "football, singing"],
    [16, "11th", 65, "Emily Davis", "hiking, football"],
    [17, "12th", 60, "Michael Wilson", "basketball, singing"],
    [18, "12th", 55, "Sarah Davis", "hiking, basketball"],
    [19, "12th", 50, "David Lee", "football"],
    [20, "12th", 45, "William Smith", "hiking, singing"],
    [14, "9th", 40, "Emily Wilson", "basketball"],
    [15, "10th", 35, "James Davis", "football, singing"],
    [16, "11th", 30, "John Brown", "hiking, basketball"],
    [17, "12th", 25, "Jane Smith", "football"],
    [18, "12th", 20, "William Johnson", "hiking, singing"],
    [19, "12th", 15, "Sarah Lee", "basketball"],
    [20, "12th", 10, "Michael Davis", "football, singing"],
    [14, "9th", 5, "David Wilson", "hiking, basketball"],
    [15, "10th", 0, "Emily Brown", "football"]
]
import math

def match_user(age, level, grade, hobbies):
    min_distance = float('inf')
    best_match = None
    
    for user in dataset:
        # Check if the user is within the required age range (14-20) and level range (9th-12th)
        if not (14 <= user[0] <= 20) or user[1] not in ["9th", "10th", "11th", "12th"]:
            continue
        
        # Calculate the Euclidean distance between the input user and the current user in the dataset
        distance = math.sqrt((user[0] - age)**2 + (user[2] - grade)**2)
        
        # If the distance is smaller than the current minimum, update the minimum and the best match
        if distance < min_distance:
            min_distance = distance
            best_match = user
    
    return best_match

# Get the input from the user
age = int(input("Enter your age: "))
level = input("Enter your level (9th, 10th, 11th, or 12th): ")
grade = int(input("Enter your grade (between 0 and 100): "))
hobbies = input("Enter your hobbies (should be one of the followings : hiking, football, basketball, singing and separated by commas): ").split(", ")

# Find the best match for the input user
best_match = match_user(age, level, grade, hobbies)

# Print the result
if best_match:
      print("Your best match is:")
      print("Full Name:", best_match[3])
      print("Age:", best_match[0])
      print("Level:", best_match[1])
      print("Grade:", best_match[2])
      print("Hobbies:", best_match[4])
else:
      print("No match found.")



