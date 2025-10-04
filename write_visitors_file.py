import os

title = os.getenv("ISSUE_TITLE", "")
prefix = "Visitor Wall--"

user = os.getenv("ISSUE_USER", "")

if title.startswith(prefix):
    visitor_name = user
    with open("visitors.txt", "a") as f:
        if visitor_name in f.read():
            print(f"{visitor_name} already exists in visitors.txt")
        else:
            f.write(visitor_name + "\n")