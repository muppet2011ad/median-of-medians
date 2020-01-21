import random, datetime
import matplotlib.pyplot as plt

def median_of_medians(A, i, gsize = 5):
    # Base case
    if len(A) <= gsize:
        return sorted(A)[i]
    # Find pivot
    groups = [A[gsize*x:gsize*(x+1)] for x in range(len(A)//gsize)]
    if len(A) % gsize != 0:
        groups.append(A[gsize*len(groups):])
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

times = []
for g in range(1,99,2):
    start = datetime.datetime.now()
    for i in range(100):
        A = list(range(50000))
        random.shuffle(A)
        i = random.randint(0, 50000-1)
        x = median_of_medians(A,i,g)
        if x == i:
            pass
        else:
            print("Something has gone wrong.")
    end = datetime.datetime.now()
    elapsed = end - start
    times.append(elapsed)

xdata = [2*x + 1 for x in range(len(times))]
ydata = [y.seconds + y.microseconds/1E6 for y in times]
plt.plot(xdata,ydata)
plt.show()