#Напишите программу, которая принимает на вход список чисел в одной 
#строке и выводит на экран в одну строку значения, которые повторяются
#в нём более одного раза.

def melke():
    mi=[int(i) for i in input().split()];
    bi=list(mi)
    bi.sort()
    return mils(bi)

def mils(x):
    us=[];
    for i in range(len(x)):
        if (len(x)>1) and x[i] == x[(i + 1) - len(x)]:
            if not x[i] in us :
                us.append(x[i]);
                print(x[i], end=' ')


melke()
