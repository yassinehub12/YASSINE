import time
time_str=time.strftime("%H:%M",time.localtime())
#Databases
reset = '\033[0m'
database=0
nl='\n'
var='_'*16
esp='  '*15
#RGB
r='\033[31m'
g='\033[32m'
b='\033[34m'
esq='_'*18
yell='\033[33m'
org='\033[38;5;208m'
cy='\033[36m'
txt="←"
scr=0
#ask_user
ask_a=b+" 1) What time is it now in Morocco?"
ask_b="2) What is Capital Of Morocco?"
ask_c="3) What is Number of cities in Morocco?"+reset

while True:
    ask_user=input(nl+"\nClick ENTER ▶ to play :  ")
    if ask_user=="":
        print(yell+'\n'*3,var,' STARTING ',var,nl)
        print(ask_a,'\n'*2,ask_b,'\n'*2,ask_c+'\n')
        print(yell+esq," ANSWER",esq,'\n'+reset)
        one_ask=input(nl+cy+"Answer 1) : "+org)
        if one_ask==time_str:
            database += 10
            print(f"{g}Great! your Points is:{reset}",database)
        else:
            print (f"{r}Wrong, your Points is:{reset}",database)
        two_ask=input(nl+cy+"Answer 2) : " + org)
        if two_ask=="rabat":
            database += 10
            print(f"{g}Nice, your Points is:{reset}",database)
        elif database==0:
            database -= 0
            print (f"{r}Wrong, your Points is:{reset}",database)
        elif database>=0:
            database -= 5
            print (f"{r}Wrong, your Points is:{reset}",database)
        three_ask=input(nl+cy+"Answer 3) : " + org)
        if three_ask=="103":
            database += 10
            print(f"{g}God job, your Points is:{reset}",database)
        elif database==0:
            database -= 0
            print (f"{r}Wrong, your Points is:{reset}",database)
        elif database>=0:
            database -= 5
            print (f"{r}Wrong, your Points is:{reset}",database,)
    elif database==20:
        scr+=70
    elif database==30:
        scr+=100
    print(nl+nl+nl+esp+"total: (",database,')')
    print(nl*6)
    break