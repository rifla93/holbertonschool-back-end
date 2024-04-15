#!/usr/bin/python3
import requests
import sys

def get_employee_todo_progress(employee_id):
    # Fetch user data
    user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    user_data = user_response.json()
    employee_name = user_data['name']

    # Fetch todo data
    todos_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')
    todos_data = todos_response.json()

    # Calculate progress
    total_tasks = len(todos_data)
    done_tasks = len([todo for todo in todos_data if todo['completed']])
    task_list = [todo['title'] for todo in todos_data if todo['completed']]

    # Print progress
    print(f'Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):')
    for task in task_list:
        print('\t ' + task)

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
