n = int (input("enter the number of series: "))
n1 ,n2 = 0, 1
sum = 0
if n >=0:
    for i in range (0,n):
        print (sum)
        n1 = n2
        n2 = sum
        sum = n1 + n2
        
