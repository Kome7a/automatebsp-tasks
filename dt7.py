students = { "Mike": 1,
             "Rumen": 5,
             "Krasi": 8,
             "Mitko": 2}
students_list = students.values()
student_number = len(students_list)
grade_sum = sum(students_list)
mean_grade = grade_sum / student_number
print(mean_grade)

