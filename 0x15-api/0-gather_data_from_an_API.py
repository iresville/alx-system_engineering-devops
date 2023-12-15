#!/usr/bin/python3
"""This script requests employee todo list through an API"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        employee_id)

    # Fetch employee information
    response = requests.get(user_url)
    if response.status_code != 200:
        print("Failed to retrieve employee information")
        sys.exit(1)
    employee = response.json()
    employee_name = employee.get("name")

    # Fetch TODO list
    response = requests.get(todos_url)
    if response.status_code != 200:
        print("Failed to retrieve TODO list")
        sys.exit(1)
    todos = response.json()

    # Calculate TODO list progress
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]
    number_of_done_tasks = len(done_tasks)

    # Display the result
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
