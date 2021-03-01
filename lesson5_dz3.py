tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

i = 0
while i == 0:
    if len(tutors) > len(klasses):
        klasses.append(None)
    elif len(klasses) > len(tutors):
        tutors.append(None)
    else:
        i = 1

students = ((tutor, klass) for tutor, klass in zip(tutors, klasses))
print(type(students), students)

for tup in students:
    print(tup)
