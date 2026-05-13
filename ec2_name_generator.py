import random
import string

# Approved departments
allowed_departments = ["Marketing", "Accounting", "Finops"]

# Display department options
print("Approved Departments:")
for dept in allowed_departments:
    print(f"- {dept}")

# Ask user for department name
department = input("\nEnter your department name: ")

# Standardize capitalization for comparison
formatted_department = department.title()

# Check if department is approved
if formatted_department not in allowed_departments:
    print("\nYou should not use this Name Generator.")
else:
    # Ask user how many EC2 names they need
    num_of_ec2s = int(input("How many EC2 instances do you need names for? "))

    # Store unique names
    generated_names = set()

    # Function to generate random characters and numbers
    def generate_random_string(length=5):
        characters = string.ascii_lowercase + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    # Generate unique EC2 names
    while len(generated_names) < num_of_ec2s:
        random_string = generate_random_string()
        ec2_name = f"{formatted_department}-ec2-{random_string}"
        generated_names.add(ec2_name)

    # Print results
    print("\nGenerated EC2 Names:")

    for name in generated_names:
        print(name)
