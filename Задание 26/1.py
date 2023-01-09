####1. sort
####2. summa(n)
####3. maxa
##
##f=open('26.txt')
##a=[]
##s,n= map(int,f.readline().split())
##a= list(map(int,f.readlines()))
##
##a.sort()
##
##count = sm =0
##
##for i in range(n):
##    if sm + a[i] < s:
##        sm+=a[i]
##    else:
##        count = i
##        break
##m = 0
##sm -= a[count - 1] # 30
##x= s - sm #70
##for i in range(n):
##    if a[i] > m and a[i]<=x:
##        m = a[i]
##print(count,m)

##21
####1. sort
####2. summa(n)
####3. maxa
##f= open('26-k1.txt')
##s,n= map(int,f.readline().split())
##a = list(map(int,f.readlines()))
##a.sort(reverse=True)
##t=0
##
##for i in range(n):
##    t += a[i] * 0.2
##
##    
##print(a[100])
##print(t)

##22
##f = open('26-k2.txt')
##s,n = map(int,f.readline().split())
##a= list(map(int,f.readlines()))
##a.sort(reverse=True)
##for i in range(50):
##    a.pop(i)
##a.sort()
##for i in range(50):
##    a.pop(i)
##print(a[-1],sum(a)/len(a))


##23
##f= open('26-k3.txt')
##n,k,m = map(int,f.readline().split())
##a=list(map(int,f.readlines()))
##a.sort(reverse=True)
##print(a[k-1])
##print(a[m+k - 1])


##24
##f = open('26-k4.txt')
##n,k = map(int, f.readline().split())
##a=list(map(int,f.readlines()))
##a.sort(reverse=True)
##b=[]
##print(k)
##print(a)
##print(' ')
##for i in range(70):
##    b.append(a[i])
##print(sum(b)/len(b), sum(a[70:141])/len(a[70:141]))

##25
##f=open('26-k5.txt')
##s,n,k = map(int, f.readline().split())
##a=list(map(int,f.readlines()))
##a.sort(reverse=True)
##print(a[k])
##a.sort()
##print(sum(a[0:n])// n)
