# debug mode on cli
#import pdb

m1 = [ [1,2,3],
       [2,3,4],
       [3,4,5]]

m2 = [ [1,1,1],
       [1,1,1],
       [1,1,1]]

m3 = [[0,0,0], 
      [0,0,0], 
      [0,0,0]]

#pdb.set_trace()

for i in range(len(m1)):
    print(i)
    for j in range(len(m1[0])):
        print(j) 
        m3[i][j] = m1[i][j] + m2[i][j]
for r in m3: 
    print(r)
