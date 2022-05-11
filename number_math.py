import timeit
dig=[0,1,2,3,4,5,6,7,8,9]

for i in range(1000):
    for j in range(1000):
        list=[int(x) for x in str(i)]+[int(x) for x in str(j)]+[int(x) for x in str(i+j)]
        if (sorted(dig)==sorted(list)):
            print('\n\n'+str(i)+'+\n'+str(j)+'\n------\n'+str(i+j))
print('finished')


