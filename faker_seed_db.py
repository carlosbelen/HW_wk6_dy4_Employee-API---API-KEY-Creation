from faker import Faker

# Creation of faker profile helper function
def getProfile():
    fake = Faker()
    return fake.profile()

# Gather Data and place inside of database
import os
from flask_employee_api.models import Employee
from flask_employee_api import db

def seedData():
    for seed_num in range(10):
        data = getProfile()
        employee = Employee(data['name'],\
        data['sex'],data['address'], data['ssn'],data['mail'] )

        db.session.add(employee)
        db.session.commit()

seedData()