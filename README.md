# EC2 Random Name Generator

This Python script is designed to create unique ec2 instance names. The script allows approved departments (Marketing, Accounting, and FinOps) to generate custom EC2 instance names by entering their department name and the number of instance names needed.



## Features
The application uses Python functions, loops, sets, conditional statements, and the random/string libraries to generate unique names containing randomized letters and numbers. The project also includes input validation to ensure only authorized departments can use the generator while handling incorrect uppercase and lowercase user inputs.

## Example Output
Enter your department name (Marketing, Accounting, FinOps): Accounting

How many names would your department like? 3

Generated EC2 Names:
Accounting-ec2-926jp
Accounting-ec2-0fk91
Accounting-ec2-nnqdq

If a non-allowed department is entered: Human Resources
You should not use this Name Generator.

# Conclusion
This project demonstrates foundational cloud automation concepts, Python scripting, and user input handling used in AWS environments.
