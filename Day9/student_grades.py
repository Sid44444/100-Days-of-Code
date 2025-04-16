student_scores = {
    "Harry": 88,
    "Ron": 78,
    "Hermione": 95,
    "Draco": 75,
    "Neville": 60
}#given dictionary


student_grades = {} #new empty dictionary

for student in student_scores: #for loop iterating through the student
    # scores
    #Get the value (student_scores) by using the key each time
    score = student_scores[student]
    #assigning the correct grade as words depending on scores
    if score >= 91:
        student_grades[student] = "Outstanding"
    elif score >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif score >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print (student_grades)
