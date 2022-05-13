import sys
from itertools import combinations

def list_sum(my_list):
    di={}
    subs = []
    for i in range(0, len(my_list)+1):
        temp = [tuple(x) for x in combinations(my_list, i)]
        for i in temp:
            di[i]=sum(i)
    return di




a=[1,2,3,4,5,6]
b=[9,10,11,12,13,14]

possible_sum_a=list_sum(a)
possible_sum_b=list_sum(b)
possible_sum_b= dict(sorted(possible_sum_b.items()))
possible_sum_a= dict(sorted(possible_sum_a.items()))
flag =0


for (b_key,b_val) in possible_sum_b.items() :
        for(a_key,a_val) in possible_sum_a.items():
            if a_val==b_val and a_val :
                print(list(a_key),list(b_key))
                #sys.exit()
                flag =1
if flag==0:
    print(0)
            
                
