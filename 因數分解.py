def factorization (num):
    print(num ,'的因數有:')
    for e in range(1 , num + 1):
        if num%e ==0:
            print(e,end=',')

factorization(int(input('請輸入正整數:')))
