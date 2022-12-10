
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

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

h = histogram('brontosaurus')
print(h)

#Looping
def print_hist(h):
    for c in h:
        print(c, h[c])

h = histogram('parrot')
print_hist(h)

#Reverse look up
def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()

h = histogram('parrot')
key = reverse_lookup(h, 1)
print(key)

#Task  8
#Get function of dictionary
csf = {
'cw1-weight': 0.4,
'cw1-mark':79,
'exam-weight':0.6,
'exam-mark':65
}
weight_1 = csf.get('cw1-weight', 0)
weight_2 = csf.get('exam-weight', 0)
mark_1 = csf.get('cw1-mark', 0)
mark_2 = csf.get('exam-mark', 0)

marks_csf = weight_1*mark_1+weight_2*mark_2
print(marks_csf)

