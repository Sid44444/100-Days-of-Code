student_scores = [ 150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86]

#using conditionals, == != < <= > >= for loops and lists.
#replicate this function print(max(student_scores))
highest_score = student_scores[0]

for score in student_scores:
    if score > highest_score:
        highest_score = score

print (highest_score)

#range function
for number in range(1, 11, 3):
    print (number)

gauss_challenge_total= 0
for number_one_hundred in range (1, 101):
    gauss_challenge_total += number_one_hundred

print (gauss_challenge_total)

