#!/usr/bin/python3
"""Extends API request and exports to JSON using python's module"""
import json
import requests

# Define the URL of the API
users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"

# Send a GET request to the API to retrieve user and todo data
users_response = requests.get(users_url)
todos_response = requests.get(todos_url)

# Check if the requests were successful
if users_response.status_code == 200 and todos_response.status_code == 200:
    # Parse the JSON responses
    users = users_response.json()
    todos = todos_response.json()

    # Create a dictionary to store the tasks of all employees
    all_employees_tasks = {}

    # Loop through each user and their tasks
    for user in users:
        user_id = user['id']
        username = user['username']

        # Filter the tasks for the current user
        user_tasks = [task for task in todos if task['userId'] == user_id]

        # Format the tasks and store them in the dictionary
        all_employees_tasks[user_id] = [
            {"username": username, "task": task['title'],
             "completed": task['completed']}
            for task in user_tasks
        ]

    # Write the dictionary to a JSON file
    with open('todo_all_employees.json', 'w') as f:
        json.dump(all_employees_tasks, f)
else:
    print("Failed to retrieve data from the API")
