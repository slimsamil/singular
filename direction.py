NORDEN = 1
SÜDEN = 2
WESTEN = 3
OSTEN = 4

l = [NORDEN, OSTEN, WESTEN, SÜDEN, WESTEN, WESTEN, NORDEN]

def clearList(lst):
    j = 0
    while j < len(lst)-1:
        m = lst[j] + lst[j+1]
        if (m == 3) or (m == 7): 
            lst.remove(lst[j+1])
            lst.remove(lst[j])
            j = 0
        else:
            j+=1

def formatList(lst):
    for i in range(len(lst)):
        if lst[i] == 1:
            lst[i] = "NORDEN"
        if lst[i] == 2:
            lst[i] = "SÜDEN"
        if lst[i] == 3:
            lst[i] = "WESTEN"
        if lst[i] == 4:
            lst[i] = "OSTEN"

clearList(l)
formatList(l)
print(l)