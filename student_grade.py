number_of_student = int(input("Enter number of students: "))
number_of_subject = int(input("Enter number of subjects: "))

subject_names = []
student_scores = []
print(f"Enter details of Subjects")
for i in range(1, number_of_subject + 1):
    subject_names.append(input(f"Name of Subject {i}: "))

for i in range(1, number_of_student + 1):
    print(f"Enter details of Student {i}")
    student_name = input("Name of Student: ")

    subject_scores = []
    print(f"Enter scores for {student_name}")
    for j in range(1, number_of_subject + 1):
        subject_scores.append(float(input(f"Score for {subject_names[j - 1]}: ")))

    student_scores.append({student_name: subject_scores})

# print(subject_names)
# print(student_scores)
student_scores = [{k: v + [sum(v), round(sum(v) / len(v), 2)] for k, v in student_score.items()} for student_score in
                  student_scores]
student_scores.sort(key=lambda x: list(x.values())[0][-2], reverse=True)

print("""
###################################################################
                Iyan Foworogi College
                    Report Sheet
###################################################################       
""")
headline = f"{'Name':<15}"
for subject in subject_names:
    headline += f"{subject:<10}"
headline += f"{'Total': <10}{'Average': <10}{'Position': <10}"

print(headline)
for i, student_score in enumerate(student_scores, start=1):
    res = ""
    for student in student_score:
        res = f"{student:<15}"
        for score in student_score[student]:
            res += f"{score:<10}"
    res += f"{i:<10}"
    print(res)