l = ["NORDEN", "OSTEN", "WESTEN", "SÜDEN", "WESTEN", "WESTEN", "NORDEN"]
k = ["NORDEN", "SÜDEN"]


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
        if lst[i] == "NORDEN":
            lst[i] = 1
        if lst[i] == "SÜDEN":
            lst[i] = 2
        if lst[i] == "WESTEN":
            lst[i] = 3
        if lst[i] == "OSTEN":
            lst[i] = 4


def deformatList(lst):
    for i in range(len(lst)):
        if lst[i] == 1:
            lst[i] = "NORDEN"
        if lst[i] == 2:
            lst[i] = "SÜDEN"
        if lst[i] == 3:
            lst[i] = "WESTEN"
        if lst[i] == 4:
            lst[i] = "OSTEN"

formatList(l)
clearList(l)
deformatList(l)
print(l)
formatList(k)
clearList(k)
deformatList(k)
print(k)