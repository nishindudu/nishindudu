import os

title = os.getenv("ISSUE_TITLE", "")
prefix = "Visitor Wall--"

user = os.getenv("ISSUE_USER", "")

if title.startswith(prefix):
    visitor_name = user
    with open("visitors.txt", "a+") as f:
        f.seek(0)
        for line in f:
            if line.strip() == visitor_name:
                print(f"{visitor_name} is already in the visitors list.")
                break
        else:
            f.write(visitor_name + "\n")