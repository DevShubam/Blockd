f = open("blockd.txt")
list1 = [i.strip() for i in f.readlines()]
f.close()
f = open("whitelist.txt")
list2 = [i.strip() for i in f.readlines()]
f.close()
def Diff(list1, list2):
    return list(set(list1) - set(list2)) + list(set(list2) - set(list1))
list1 = Diff(list1, list2)
f = open("blockd.txt","w")
for i in list1:
    f.write(f"{i}\n")
f.close()
