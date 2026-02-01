validGrades = 0
unvalidGrades = 0
sumGrade = 0
avg = 0
highestGrade = 0

while True:
    grade = int(input("Enter grade: "))
    if grade < 0:
        unvalidGrades += 1
        continue
    elif grade > 100:
        break
    else:
        validGrades += 1
        sumGrade += grade
        if grade > highestGrade:
            highestGrade = grade

if validGrades > 0:
    avg = sumGrade / validGrades
print("Valid Grades:", validGrades)
print("Unvalid Grades:", unvalidGrades)
print("Highest Grade:", highestGrade)
print("Avg:", avg)
