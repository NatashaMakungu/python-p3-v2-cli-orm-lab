#!/usr/bin/env python3

from classes.__init__ import CONN, CURSOR
import random
from classes.department import Department
from classes.employee import Employee

import ipdb


def reset_database():
    Employee.drop_table()
    Department.drop_table()
    Department.create_table()
    Employee.create_table()

    # Create seed data
    payroll = Department.create("Payroll", "Building A, 5th Floor")
    human_resources = Department.create(
        "Human Resources", "Building C, East Wing")
    departments = [payroll, human_resources]

    jobs = ["Accountant", "Manager",
            "Benefits Coordinator", "New Hires Coordinator"]
    Employee.create("Amir", jobs[0], departments[0])
    Employee.create("Bola", jobs[1], departments[0])
    Employee.create("Charlie", jobs[1], departments[1])
    Employee.create("Dani", jobs[2], departments[1])
    Employee.create("Hao", jobs[3], departments[1])


reset_database()
print("Seeded database")
ipdb.set_trace()
