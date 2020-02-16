my_list = [50, 98, 54, 6, 34]
def bubble_sort(unsorted):
    length=len(unsorted)-1
    sortedlist=False
    while not sortedlist:
        sortedlist=True
        for i in range(length):
            if unsorted[i]>unsorted[i+1]:
                sortedlist=False
                unsorted[i], unsorted[i+1]=unsorted[i+1], unsorted[i]
                print ("Swap",(i,i+1),":", my_list)
bubble_sort(my_list)
print ("sorted =",my_list)

