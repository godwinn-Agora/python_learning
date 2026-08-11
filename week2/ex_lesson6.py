
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
    print(item)"""

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
    print(student)