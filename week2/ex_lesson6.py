
"""dico = { "name": "Ouriel", 
        "Age": 17, 
        "country": "Chine", 
        "field of study": "Informatique" 
        }
print(dico)

dico["field of study"] = "IA/ML"
print(dico)

dico["city"] = "Suzhou"
print(dico)

for item in dico.items():
    print(item)

student1 = { "name": "Alice",
            "Age": 18, 
            "country": "Chine", 
            "field of study": "Informatique" 
            }

student2 = { "name": "Bob",
            "Age": 19,
            "country": "Chine", 
            "field of study": "Informatique" 
            }

student3 = { "name": "Charlie",
            "Age": 20,
            "country": "Chine", 
            "field of study": "Informatique" 
            }

students = [student1, student2, student3]
for student in students:
    print(student)"""

tasks = []

task = {"name": "Tâche 1", "completed": False}

name = input("Entrez le nom de la tâche : ")
task = {"name": name, "completed": False}
tasks.append(task)
completed = input("La tâche est-elle terminée ? (oui/non) : ")
if completed.lower() == "oui":
    task["completed"] = True
else:
    task["completed"] = False
tasks.append(task)