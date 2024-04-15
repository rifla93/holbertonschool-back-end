#!/usr/bin/python3
"""Module to fetch data from a REST API and display an employee's TODO list progress"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    """Fetch and print an employee's TODO list progress

    Args:
        employee_id (int): The ID of the employee

    Returns:
        None
    """
    # Fetch user data
    user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch todo data
    todos_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')
    todos_data = todos_response.json()

    # Calculate progress
    total_tasks = len(todos_data)
    done_tasks = len([todo for todo in todos_data if todo.get('completed')])
    task_list = [todo.get('title') for todo in todos_data if todo.get('completed')]

    # Print progress
    print(f'Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):')
    for task in task_list:
        print('\t ' + task)

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)