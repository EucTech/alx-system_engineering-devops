#!/usr/bin/python3
"""
   This is a python script that, using this REST API, for
   a given employee ID, returns information about his/her TODO list
   progress
"""
import requests
import sys


if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com"

    employee_id = sys.argv[1]

    # get user information
    user_info = f"{api_url}/users/{employee_id}"
    response = requests.get(user_info)
    user_data = response.json()

    employee_name = user_data.get('name')

    # Retrieve task records
    todo_data = f"{api_url}/todos?id={employee_id}"
    response = requests.get(todo_data)
    todos = response.json()

    complete_tasks = len(todos)
    done_task = 0

    for task in todos:
        if task['completed']:
            done_task += 1

    print(f"Employee {employee_name} is done with tasks({done_task}/\
{complete_tasks}):")
    for tsk in todos:
        if tsk['completed']:
            print(f"\t {tsk['title']}")
