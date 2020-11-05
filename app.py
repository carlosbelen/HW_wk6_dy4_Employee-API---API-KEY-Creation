from flask_employee_api import app

# import for faker file for seed data
from faker_seed_db import seedData


if __name__ == '__main__':
    app.run(debug=True)