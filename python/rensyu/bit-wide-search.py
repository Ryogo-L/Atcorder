from cgi import print_form


money = 300
item = (("mikan", 100), ('ringo',200), ('budou', 300))
n = len(item)
for i in range(2 ** n):
    bag = []
    total = 0
    for j in range(n):
        if ((i>>j) & 1):
            bag.append(item[j][0])
            total += item[j][1]
    if (total <=money):
        print(total, bag)