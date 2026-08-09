
activities = [ 'programming', 'reading', 'exercising', 'cooking', 'traveling' ]
print(activities[0])
print(activities[-1])
print(activities[1:4])
print(activities)

activities.append('painting')
print(activities)

activities.remove('reading')
print(activities)

for activity in activities:
    print(activity)

task1 = input("Enter your first task: ")
task2 = input("Enter your second task: ")
task3 = input("Enter your third task: ")
tasks = [task1, task2, task3]
print("Your tasks are:")
for task in tasks:
    print(task)