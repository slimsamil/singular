l = ["NORDEN", "OSTEN", "WESTEN", "SÜDEN", "WESTEN", "WESTEN", "NORDEN"]

def clearList(l):
    j = 0
    while j < len(l)-1:
        if (l[j] == "NORDEN" and l[j+1] == "SÜDEN") or (l[j] == "SÜDEN" and l[j+1] == "NORDEN") or (l[j] == "OSTEN" and l[j+1] == "WESTEN") or (l[j] == "WESTEN" and l[j+1] == "OSTEN"): 
            l.remove(l[j+1])
            l.remove(l[j])
            j = 0
        else:
            j+=1

clearList(l)
print(l)