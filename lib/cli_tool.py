# cli_tool.py

import argparse
from lib.models import Task, User

# Global dictionary to store users and their tasks
users = {}
alice = User("Alice")
unit_test_task = Task("Write unit tests")
alice.add_task(unit_test_task)
users["Alice"] = alice

def add_task(args):
    user = users.get(args.user) or User(args.user)
    users[args.user] = user
    task = Task(args.title)
    user.add_task(task)


def complete_task(args):
    user = users.get(args.user)
    if user:
        for task in user.tasks:
            if task.title == args.title:
                task.complete()
                return
        print("❌ Task not found.")
    else:
        print("❌ User not found.")
