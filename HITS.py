
import numpy as np
def calc_hub_aut(A,max_num):
    hub=np.ones((max_num,1))
    authority=np.ones((max_num,1))
    for i in range(10000):
        aut_new=np.dot(A.T,hub)
        aut_new=aut_new/np.sum(aut_new)
        hub_new=np.dot(A,authority)
        hub_new=hub_new/np.sum(hub_new)
        if np.sqrt(np.sum(np.square(authority - aut_new)))+np.sqrt(np.sum(np.square(hub - hub_new)))<0.000001:
            break
        authority=aut_new
        hub=hub_new
    return (authority,hub)
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
for i in range(6):
    A,max_num=read_data('hw3dataset/graph_'+str(i+1)+'.txt')
    authority,hub=calc_hub_aut(A,max_num)
    print('graph_'+str(i+1)+'\nauthority:')
    print(authority)
    print('hub:')
    print(hub)
#print('5'in a)
