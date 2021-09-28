people=['ali','negin','reza','hosein','mehrdad','x']
for passnum in range(len(people)-1,0,-1):
    for i in range(passnum):
        if people[i]>people[i+1]:
            people[i],people[i+1]=people[i+1],people[i]
print(people)
