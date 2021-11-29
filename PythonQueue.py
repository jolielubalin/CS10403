names = [ ]
x = 0
for x in range (10):
        name = input ("EnterName")
        names.append(name)

for i in range (len(names)):
    print(names.pop(0))
