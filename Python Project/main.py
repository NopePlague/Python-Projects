def get_students(noOfStudent):
    data={}
    for i in range(noOfStudent):
        name=input(f"Enter the name of Student-{i+1}: ")
        marks=int(input(f"Marks obtained by {name}: "))
        data[name]=marks
    return data


def calculate_average(students):
    totalMarks=0
    for value in students.values():
        totalMarks+=value
    return totalMarks/(len(students))

def get_top_scorer(students):
    high=0
    nameOfBest=""
    for bestname, bestscore in students.items():
        if bestscore>high:
            high=bestscore
            nameOfBest=bestname
    return nameOfBest

def get_passed_students(students):
    passing=[]
    for studentName, studentScore in students.items():
        if studentScore>=40:
            passing.append(studentName)
    return passing
        

noOfStudent=int(input("Please Enter the Stregth of The Class: "))
students=get_students(noOfStudent)

avgMarks=calculate_average(students)
highestScorer=get_top_scorer(students)
passedStudents=get_passed_students(students)

print(f"Average Marks: {round(avgMarks)}")
print(f"Top Scorer: {highestScorer} ({students[highestScorer]})")
print(f"Passed Students: {', '.join(passedStudents)}")