#!/usr/bin/python3
"""
   This is a python script that export data in the CSV format.
"""
import requests
import sys
import csv


if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com"

    employee_id = sys.argv[1]

    # get user information
    user_info = f"{api_url}/users/{employee_id}"
    response = requests.get(user_info)
    user_data = response.json()

    employee_name = user_data.get('name')
    username = user_data.get('username')

    # Retrieve task records
    todo_data = f"{api_url}/todos?userId={employee_id}"
    response = requests.get(todo_data)
    todos = response.json()

    csv_file = f"{employee_id}.csv"

    with open(csv_file, mode='w', newline='') as file:
        write_file = csv.writer(file)
        for task in todos:
            status = task['completed']
            title = task['title']

            # To write each row
            write_file.writerow([employee_id, username, status, title])
