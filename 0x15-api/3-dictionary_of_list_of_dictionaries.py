#!/usr/bin/python3
"""
   This is a python script that export data in the json format.
"""
import json
import requests


if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com"

    # get the user information
    user_info = f"{api_url}/users"
    response = requests.get(user_info)
    user_data = response.json()

    all_data = {}

    for user in user_data:
        employeeId = user['id']
        username = user['username']

        # Retrieve task records
        todo_data = f"{api_url}/todos?userId={employeeId}"
        response = requests.get(todo_data)
        todos = response.json()

        info = [{"username": username,
                "task": task['title'],
                "completed": task['completed']} for task in todos]

        all_data[employeeId] = info

        json_file = "todo_all_employees.json"

        with open(json_file, mode='w') as file:
            json.dump(all_data, file)
