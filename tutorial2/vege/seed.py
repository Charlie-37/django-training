from faker import Faker
import random
from .models import *

fake = Faker()

def seed_db(n=20) -> None:
    try:
        for _ in range(n):
            dept_obj = Department.objects.all()
            random_index = random.randint(0,len(dept_obj)-1)
            department = dept_obj[random_index]
            student_id = random.randint(103,999)
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(20,40)
            student_address = fake.address()

            std_id_obj = StudentID.objects.create(student_id = student_id )
            std_obj = Student.objects.create(
            department = department,
            student_id = std_id_obj,
            student_name = student_name,
            student_email = student_email,
            student_age = student_age,
            student_address = student_address
            )
    except Exception as e: 
        print(e)       
