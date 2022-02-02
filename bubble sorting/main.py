items = [2, 1, 4, 3, 7, 6, 5]

def swap(a):
    item_a = items[a]
    items[a] = items[a+1]
    items[a+1] = item_a


for i in range(len(items)-1):
    for n in range(len(items)-1):
        if items[n] > items[n+1]:
            swap(n)
            print(items)
    #print(items)

print(items)
