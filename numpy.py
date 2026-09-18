import numpy as np

data_type = [('name', 'U15'), ('class', int), ('height', float)]

students_details = [
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.10),
    ('Pit', 5, 40.11)
]

students = np.array(students_details, dtype=data_type)

print("Original array:")
print(students)

print("\nNames of students:")
print(students['name'])

print("\nClasses of students:")
print(students['class'])

print("\nHeights of students:")
print(students['height'])

print("\nSort by height:")
print(np.sort(students, order='height'))

print("\nSort by name:")
print(np.sort(students, order='name'))

print("\nTallest student:")
print(students[np.argmax(students['height'])])

print("\nShortest student:")
print(students[np.argmin(students['height'])])

print("\nAverage height:")
print(np.mean(students['height']))

print("\nMaximum height:")
print(np.max(students['height']))

print("\nMinimum height:")
print(np.min(students['height']))

print("\nTotal number of students:")
print(len(students))

print("\nStudents in class 5:")
print(students[students['class'] == 5])

print("\nStudents taller than 45:")
print(students[students['height'] > 45])