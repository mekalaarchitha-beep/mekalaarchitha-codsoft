tasks = []
while True:
    print("\nTo-Do List:")
    for i, (t, done) in enumerate(tasks, 1):
        status = "✔" if done else "X"
        print(f"{i}. {t} [{status}]")
    print("\n1. Add Task  2. Delete Task  3. Mark Done  4. Quit")
    choice = input("Choose:")
    if choice == "1":
        task = input("Enter task:")
        tasks.append([task, False])
    elif choice == "2":
        num = int(input("Enter task number to delete:"))
        if 0 < num <= len(tasks):
            tasks.pop(num-1)
    elif choice == "3":
        num = int(input("Enter task number to mark done:"))
        if 0 < num <= len(tasks):
            tasks[num-1][1] = True
    elif choice == "4":
        break
