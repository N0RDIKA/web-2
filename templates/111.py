data = [[23, "Mikhail", 6.2, 13], [25, "Semyon", 5.9, 0], [29, "Boris", 6.7, 7]] 
for row in data:
    if row[3] == 0:
        print(row)
    print(row[0] / (row[0] * row[3]))
 