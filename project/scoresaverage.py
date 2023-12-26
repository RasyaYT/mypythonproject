# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
# print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# Example Output 78 65 89 86 55 91 64 89

high_score = 0
for scores in student_scores:
    if scores > high_score:
        high_score = scores
print(f"The Highest Score In The Class is: {high_score}")