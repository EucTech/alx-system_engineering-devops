#!/usr/bin/python3
"""
   This is a python script that export data in the CSV format.
"""
import json
import requests
import sys


if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com"

    employee_id = sys.argv[1]

    # get the user information
    user_info = f"{api_url}/users/{employee_id}"
    response = requests.get(user_info)
    user_data = response.json()

    employee_name = user_data.get('name')
    username = user_data.get('username')

    # Retrieve task records
    todo_data = f"{api_url}/todos?userId={employee_id}"
    response = requests.get(todo_data)
    todos = response.json()

    info = {employee_id: [{"task": task['title'],
                           "completed": task['completed'],
                           "username": username} for task in todos]}

    json_file = f"{employee_id}.json"

    with open(json_file, mode='w') as file:
        json.dump(info, file)

