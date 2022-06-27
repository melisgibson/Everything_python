# EC2 Random Name Generator

while True: 
    dept_name = input("Name of your department: ").lower()
    dept = ['marketing', 'accounting', 'finops']
    if dept_name not in dept:
        print("Access Denied")
        exit ()
    else:
       break
   
import random
import string
def ec2_id(length = 6):
    letters = string.letters
    numbers = string.digits
    characters = letters + digits
    return ''.join(random.choice(characters) for i in range(length)

ec2_num = input("How many EC2 instances do you want names for?: ")
ec2_num = int(ec2_num)
for _ in range(ec2_num):
    print("Random generated name is: ")
    print(ec2_id, dept_name)