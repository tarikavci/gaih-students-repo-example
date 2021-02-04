#GLOBALAIHUB PYTHON COURSE - HW3 - DAY4
#TARIK AVCI - tarikaavci@gmail.com

lists=[]

def prime_numbers(lower,upper):
    for i in range(lower,upper):
        for prime in range(2,i):
            if (i % prime) == 0:
                break
            elif(i % prime !=0) and (prime == i-1):
                lists.append(i)

    print(f'PRIME NUMBERS BETWEEN {lower} and {upper}: \n {lists}')



prime_numbers(1,100)