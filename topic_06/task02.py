students = [{'name': 'Rom', 'grade': 60},
            {'name': 'Liza', 'grade': 85},
            {'name': 'Emma', 'grade': 110},
            {'name': 'Zak', 'grade': 70}]

getName = lambda student: student['name']
getGrade = lambda student: int(student['grade'])

while True:
    whichSort = input("Sort by descending or ascending: ")
    if whichSort == "ascending":
        sortType = True
        break
    elif whichSort == "descending":
        sortType = False
        break
    else: 
        print("Invalid option. Try againg...")

sortedName = sorted(students, key=getName, reverse=sortType)
print("\n Сортування за ім'ям:")
for student in sortedName:
    print(f"Name: {student['name']}, Grade: {student['grade']}")

sortedGrade = sorted(students, key=getGrade, reverse=sortType)
print("\n Сортування за оцінкою:")
for student in sortedGrade:
    print(f"Name: {student['name']}, Grade: {student['grade']}")

