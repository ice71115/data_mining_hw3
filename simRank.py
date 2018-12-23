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
    return A,max_num
def calu_S(A,C=0.8):
    max_num=len(A)
    B=np.sum(A,axis=1)
    for i in range(max_num):
        if B[i] ==0:
            B[i]=1
    Q=A/B
    S=np.identity(max_num)
    for i in range(1000):
        S_new=C*np.dot(np.dot(Q.T,S),Q)
        for j in range(max_num):
            S_new[j][j]=1
        if np.allclose(S, S_new, atol=0.000001):
            break
        S=S_new
    return S
for i in range(5):
    A,max_num=read_data("hw3dataset/graph_"+str(i+1)+".txt")
    S=calu_S(A,0.8)
    print('graph_'+str(i+1))
    print('S=')
    print(S)