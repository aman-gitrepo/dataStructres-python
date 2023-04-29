def selection_sort(A):
    for i in range(len(A)):
        least =i
        for k in range(i+1,len(A)):
            if A[k]<A[least]:
                least =k
        swap(A,least,i)
        print (A )      
def swap(A,x,y):
    temp=A[x]
    A[x]=A[y]
    A[y]=temp