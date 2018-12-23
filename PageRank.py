
import numpy as np
def read_data(loc):
    data=open(loc, 'r').readlines()
    dataset=[]
    for line in range(len(data)):
        dataset.append([int(x) for x in data[line].split()[0].split(',')])
    #dataset=[[1,2],[2,3],....]
    max_num=np.amax(dataset)
    A=np.zeros((max_num,max_num))#Adjacency_matrix
    for lines in dataset:
        A[lines[0]-1,lines[1]-1]=1

    for row in range(max_num):
        if np.sum(A[row])!=0:
            A[row]=A[row]/np.sum(A[row])
    return A,max_num
def calc_PR_values(A,max_num):
    d=0.1
    PR=np.ones((max_num,1))/max_num
    for i in range(10000):
        PR_new=np.dot(A.T,PR)*(1-d)+(1/max_num)*d
        if np.sqrt(np.sum(np.square(PR - PR_new)))<0.000001:
            break
        PR=PR_new
    return PR

for i in range(6):
    A,max_num=read_data('hw3dataset/graph_'+str(i+1)+'.txt')
    PR=calc_PR_values(A,max_num)
    print('graph_'+str(i+1)+':')
    print('PR values')
    print(PR)

#print('5'in a)

