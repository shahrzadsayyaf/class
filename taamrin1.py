##shahrzad sayyafzadeh thursday 14:00 - 18:00
def counter(list1:list,list2:list,list3:list) -> list:
    list1.extend(list1+list2)
    list1.reverse()
    list1=list1[::-2]
    return list1
list4=counter([1,2,3],[4,5,6],[7,8,9])
print(list4)
