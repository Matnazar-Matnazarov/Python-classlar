# n,m=map(int,input().split())
def betlash_algoritmi(n,m):
    mas=list(range(n,m+1))
    a,b=[],[]
    urta=len(mas)//2
    for i in range(urta-1):
        if i%2==0 or i==0:
            a.append(mas[i])
        else:
            b.append(mas[i])
    b.append(mas[urta-1])
    b.append(mas[urta])
    t=mas[urta+1:len(mas)]
    # print(t)
    for i in range(len(t)):
        if i%2==0 or i==0:
            a.append(t[i])
        else:
            b.append(t[i])
    pp=[]
    ff=[]
    # print(a)
    # print(b)
    len_a=len(a)//2
    len_b=len(b)//2
    for i in range(len_a):
        pp.append(a[-(i+1)])
        pp.append(a[i])
    for i in range(len_b):
        ff.append(b[len_b-i-1])
        ff.append(b[len_b+i])
    return [','.join(map(str,pp)),','.join(map(str,ff))]
def ikki_tomonlama(a,b):
    d=list(range(a, b + 1))
    aa = [i for i in  d if i % 2 == 0]
    bb = [i for i in d if i % 2== 1]
    if a%2==0:
        return [','.join(map(str, aa)), ','.join(map(str, bb[::-1]))]
    else:
        return [','.join(map(str, bb)), ','.join(map(str, aa[::-1]))]
print(ikki_tomonlama(int(input()),int(input())))