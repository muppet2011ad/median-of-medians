import random

def median_of_medians(A, i):
    # Base case
    if len(A) <= 5:
        return sorted(A)[i]
    # Find pivot
    groups = [A[5*x:5*(x+1)] for x in range(len(A)//5)]
    if len(A) % 5 != 0:
        groups.append(A[5*len(groups):])
    medians = [sorted(group)[len(group)//2] for group in groups]
    final_mom = median_of_medians(medians, len(medians)//2)
    # Recurse
    p1 = [x for x in A if x < final_mom] + [final_mom]
    p2 = [x for x in A if x > final_mom]
    pivotindex = len(p1) - 1
    if pivotindex == i:
        return p1[-1]
    elif pivotindex < i:
        return median_of_medians(p2,i-pivotindex-1)
    else:
        return median_of_medians(p1[:-1],i)

median_of_medians([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],3)

for i in range(10):
    A = list(range(50000))
    random.shuffle(A)
    i = random.randint(0, 50000-1)
    x = median_of_medians(A,i)
    if x == i:
        print("OK")
    else:
        print("Something has gone wrong.")