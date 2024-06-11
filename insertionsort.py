def insertionsort(seq):
    for i in range(len(seq)):
        pos=i
        while(pos>0 and seq[pos]<seq[pos-1]):
            (seq[pos],seq[pos-1])=(seq[pos-1],seq[pos])
            pos=pos-1
list1=list(range(54,0,-3))
insertionsort(list1)
print(list1)

#whatsapp self audio