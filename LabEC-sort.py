def merge_sort(unsorted):
    if  len(unsorted)>1: #recursive case
        half=len(unsorted)//2
        beginning=unsorted[:half]
        end=unsorted[half:]
        merge_sort(beginning)
        merge_sort(end)
        original=0
        fresh=0
        new=0
        while original<len(beginning) and fresh<len(end):
            if beginning[original]<end[fresh]:
                unsorted[new] =beginning[original]
                original=original+1
            else:
                unsorted[new]=end[fresh]
                fresh=fresh+1
            new=new+1
        while original<len(beginning):
            unsorted[new]=beginning[original]
            original=original+1
            new=new+1
        while fresh<len(end):
            unsorted[new]=end[fresh]
            fresh=fresh+1
            new=new+1
        print('Sorted:',unsorted)
        
#implementation
import random
random.seed(-1)
orig=list(range(1,11))
random.shuffle(orig)
print(orig)
new_list=merge_sort(orig)
#print(new_list)
