n,m=map(int,input().split())
k=int(input())
A=[[0]*(m+2) for i in range(n+2)]
for i in range(k):
	x,y=map(int,input().split())
	A[x][y]=1
for i in range(1,n+1):
	for j in range(1,m+1):
		p=A[i-1][j-1]+A[i-1][j]+A[i-1][j+1]+A[i][j-1]+A[i][j+1]+A[i+1][j-1]+A[i+1][j]+A[i+1][j+1]
		if(A[i][j]==1):
			print('*',end=' ')
		else:
			print(p,end=' ')
	print()

