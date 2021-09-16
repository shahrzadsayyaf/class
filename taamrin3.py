#shahrzad sayyafzade 14 - 18
def counting_fruits(fruits:list) -> int:
    fruit_counter = list()
    c=0
    if fruits[c] in fruit_counter:
        c=c+1
    else:
        fruit_counter.append(fruits[c])
        c=c+1
    if fruits[c] in fruit_counter:
        c=c+1
    else:
        fruit_counter.append(fruits[c])
        c=c+1
    if fruits[c] in fruit_counter:
        c=c+1
    else:
        fruit_counter.append(fruits[c])
        c=c+1
    if fruits[c] in fruit_counter:
        c=c+1
    else:
        fruit_counter.append(fruits[c])
        c=c+1
    summery=len(fruit_counter)
    return summery
fruits=['anar','goje','goje','khiar','sib','sib']
resaualt=counting_fruits(fruits)
print(fruits)
