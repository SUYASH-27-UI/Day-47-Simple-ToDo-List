tasks = []

while True:
    task = input("Enter a task (or type 'done' to finish): ")

    if task.lower() == "done":
        break

    tasks.append(task)

print("\nYour To-Do List:")

for task in tasks:
    print("-", task)
