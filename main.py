
input_number = input("How many modules do you have? "'\n')
marks = dict()
input_number = int(input_number)
while(input_number > len(marks)):
    subject = input("Name the module")
    if subject in marks:
        print("Please enter subject that is not already in the list")
    else:
        mark = input("what was your mark from the module?")
        marks[subject] = mark

mark_values = marks.values()
marks_sum = 0
j = 0
for i in mark_values:
    marks_sum = marks_sum + int(i)
    j = j + 1

marks_sum = marks_sum/j
print(marks_sum)
