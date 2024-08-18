student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
test_score = [8, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))
low_score = student_scores[0]
high_score = student_scores[0]
high_test_score = test_score[0]
for score in test_score:
    if score > high_test_score:
        high_test_score = score

for score in student_scores:
    if score < low_score:
        low_score = score
    if score > high_score:
        high_score = score
print(f"the lowest score is {low_score}")
print(f"the highest score is {high_score}")
print(f"the highest test score is {high_test_score}")