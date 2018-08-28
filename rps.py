import random
import re
'''import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt'''

def print_choice(user,cpu):
    print("USER chooses ",user,end="")
    print()
    print("CPU chooses ",cpu,end="")
    print()

    f_r= open("P:/VIT/MINE/SEMESTER 3/Theory of Computation and Compiler Design/J Component/RPS/rps.txt","r+")
    r1=f_r.readline()
    r1=f_r.readline()
    r1=f_r.readline()
    r1=f_r.readline()
    win=int(r1[6:])
    p1=f_r.readline()
    lost=int(p1[7:])
    s1=f_r.readline()
    tie=int(s1[6:])
    f_r.close()

    if(user=="rock" and cpu=="paper"):
        print("CPU WINS")
        win=win+1
    if(user=="paper" and cpu=="scissors"):
        print("CPU WINS")
        win=win+1
    if(user=="scissors" and cpu=="rock"):
        print("CPU WINS")
        win=win+1
    if(user==cpu):
        print("NOBODY WINS")
        tie=tie+1
    if(cpu=="rock" and user=="paper"):
        print("USER WINS")
        lost=lost+1
    if(cpu=="paper" and user=="scissors"):
        print("USER WINS")
        lost=lost+1
    if(cpu=="scissors" and user=="rock"):
        print("USER WINS")
        lost=lost+1

    f_r= open("P:/VIT/MINE/SEMESTER 3/Theory of Computation and Compiler Design/J Component/RPS/rps.txt","r+")
    r1=f_r.readline()
    sr=int(r1[7:])
    p1=f_r.readline()
    sp=int(p1[8:])
    s1=f_r.readline()
    ss=int(s1[11:])
    f_r.close()

    if(user=="rock"):
        sr=sr+1
    if(user=="paper"):
        sp=sp+1
    if(user=="scissors"):
        ss=ss+1

    f_w= open("P:/VIT/MINE/SEMESTER 3/Theory of Computation and Compiler Design/J Component/RPS/rps.txt","w")
    s="rock - "+str(sr)+"\n"
    f_w.write(s)
    s="paper - "+str(sp)+"\n"
    f_w.write(s)
    s="scissors - "+str(ss)+"\n"
    f_w.write(s)
    s="win - "+str(win)+"\n"
    f_w.write(s)
    s="lost - "+str(lost)+"\n"
    f_w.write(s)
    s="tie - "+str(tie)
    f_w.write(s)
    f_w.close()
    return

def pattern(text,user):
    f_r= open("P:/VIT/MINE/SEMESTER 3/Theory of Computation and Compiler Design/J Component/RPS/rps_hard.txt","w")
    text=text+user+""
    f_r.write(text)
    f_r.close

def appoint_user(user):
    if(user=="r"):
        user="rock"
    if(user=="p"):
        user="paper"
    if(user=="s"):
        user="scissors"
    return user
def appoint_cpu(cpu):
    if(cpu==1):
        cpu="rock"
    if(cpu==2):
        cpu="paper"
    if(cpu==3):
        cpu="scissors"
    return cpu

print("ROCK PAPER SCISSORS\n")
print("Rules : ")
print("Select which mode you want to play - Easy(1) Medium(2) Hard(3)")
mode=int(input())

rock=paper=scissors=0
if(mode==1):
    print("...THE GAME IS ABOUT TO BEGIN...\n")
    for i in range(0,10):
        print("___________________________\nYou choose from r,p and s ...")
        user=input()
        cpu=random.randint(1,3)
        print(cpu)

        user=appoint_user(user)
        cpu=appoint_cpu(cpu)
        print_choice(user,cpu)

    print("Would you like to see the Stastics of all of the games : y/n")
    ch=input()
    if(ch=="y"):
        
        f_r= open("P:/VIT/MINE/SEMESTER 3/Theory of Computation and Compiler Design/J Component/RPS/rps.txt","r+")
        r1=f_r.readline()
        sr=int(r1[7:])
        p1=f_r.readline()
        sp=int(p1[8:])
        s1=f_r.readline()
        ss=int(s1[11:])
        s1=f_r.readline()
        win=int(r1[6:])
        s1=f_r.readline()
        lost=int(p1[7:])
        s1=f_r.readline()
        tie=int(s1[6:])
        f_r.close()
        
        plt.subplot(2, 1, 1)
        objects = ('ROCK', 'PAPER', 'SCISSORS')
        y_pos = np.arange(len(objects))
        performance = [sr,sp,ss]
        plt.bar(y_pos, performance, align='center', alpha=1,color='blue')
        plt.xticks(y_pos, objects)
        plt.ylabel('NUMBER OF MOVES')
        plt.title('GESTURES')
        '''plt.show()'''

        plt.subplot(2, 1, 2)
        objects = ('WIN', 'LOST', 'TIE')
        y_pos = np.arange(len(objects))
        performance = [win,lost,tie]
        plt.bar(y_pos, performance, align='center', alpha=1,color='red')
        plt.xticks(y_pos, objects)
        plt.ylabel('TOTAL')
        plt.title('RESULTS')
        plt.show()
    

elif(mode==2):
    print("...THE GAME IS ABOUT TO BEGIN...\n")
    for i in range(0,10):
        print("___________________________\nYou choose from r,p and s ...")
        user=input()
        f_r= open("P:/VIT/MINE/SEMESTER 3/Theory of Computation and Compiler Design/J Component/RPS/rps.txt","r+")
        r1=f_r.readline()
        sr=int(r1[7:])
        p1=f_r.readline()
        sp=int(p1[8:])
        s1=f_r.readline()
        ss=int(s1[11:])
        f_r.close()
        cpu=0
        if(sr>=sp and sr>=ss):
            if(cpu==0):
                cpu=2
        if(sp>=sr and sp>=ss):
            if(cpu==0):
                cpu=3
        if(ss>=sr and ss>=sp):
            if(cpu==0):
                cpu=1
        print(cpu)

        user=appoint_user(user)
        cpu=appoint_cpu(cpu)
        print_choice(user,cpu)
    print("Would you like to see the Stastics of all of the games : y/n")
    ch=input()
    if(ch=="y"):
        
        f_r= open("P:/VIT/MINE/SEMESTER 3/Theory of Computation and Compiler Design/J Component/RPS/rps.txt","r+")
        r1=f_r.readline()
        sr=int(r1[7:])
        p1=f_r.readline()
        sp=int(p1[8:])
        s1=f_r.readline()
        ss=int(s1[11:])
        s1=f_r.readline()
        win=int(r1[6:])
        s1=f_r.readline()
        lost=int(p1[7:])
        s1=f_r.readline()
        tie=int(s1[6:])
        f_r.close()
        
        plt.subplot(2, 1, 1)
        objects = ('ROCK', 'PAPER', 'SCISSORS')
        y_pos = np.arange(len(objects))
        performance = [sr,sp,ss]
        plt.bar(y_pos, performance, align='center', alpha=1,color='blue')
        plt.xticks(y_pos, objects)
        plt.ylabel('NUMBER OF MOVES')
        plt.title('GESTURES')
        '''plt.show()'''

        plt.subplot(2, 1, 2)
        objects = ('WIN', 'LOST', 'TIE')
        y_pos = np.arange(len(objects))
        performance = [win,lost,tie]
        plt.bar(y_pos, performance, align='center', alpha=1,color='red')
        plt.xticks(y_pos, objects)
        plt.ylabel('TOTAL')
        plt.title('RESULTS')
        plt.show()
        
elif(mode==3):
    print("...THE GAME IS ABOUT TO BEGIN...\n")
    for i in range(0,15):
        f_r= open("P:/VIT/MINE/SEMESTER 3/Theory of Computation and Compiler Design/J Component/RPS/rps_hard.txt","r+")
        text=f_r.readline()
        f_r.close
        if(i==0):
            cpu=random.randint(1,3)
        elif(text.find("p")==-1 and text.find("s")==-1):
            cpu=2
        elif(text.find("r")==-1 and text.find("s")==-1):
            cpu=3
        elif(text.find("r")==-1 and text.find("p")==-1):
            cpu=1
        elif(re.match("rp",text) or re.match("ps",text) or re.match("sr",text)):
            if(text[len(text)-2:]=="rp"):
                cpu=2
            elif(text[len(text)-2:]=="pr"):
                cpu=3
            if(text[len(text)-2:]=="ps"):
                cpu=3
            elif(text[len(text)-2:]=="sp"):
                cpu=1
            if(text[len(text)-2:]=="sr"):
                cpu=1
            elif(text[len(text)-2:]=="rs"):
                cpu=2
        elif(re.match("sp",text) or re.match("pr",text) or re.match("rs",text)):
            if(text[len(text)-2:]=="rs"):
                cpu=2
            elif(text[len(text)-2:]=="sr"):
                cpu=1
            if(text[len(text)-2:]=="pr"):
                cpu=3
            elif(text[len(text)-2:]=="rp"):
                cpu=2
            if(text[len(text)-2:]=="sp"):
                cpu=1
            elif(text[len(text)-2:]=="ps"):
                cpu=3
        if(re.match("rps",text) or re.match("psr",text) or re.match("srp",text)):
            if(text[len(text)-3:]=="rps"):
                cpu=2
            elif(text[len(text)-3:]=="psr"):
                cpu=3
            elif(text[len(text)-3:]=="srp"):
                cpu=1
        if(re.match("spr",text) or re.match("prs",text) or re.match("rsp",text)):
            if(text[len(text)-3:]=="spr"):
                cpu=1
            elif(text[len(text)-3:]=="prs"):
                cpu=3
            elif(text[len(text)-3:]=="rsp"):
                cpu=2
        if(re.match("rrps",text) or re.match("rrsp",text)):
            if(text[len(text)-4:]=="rrps" or text[len(text)-4:]=="rpsr"):
                cpu=2
            if(text[len(text)-4:]=="psrr"):
                cpu=3
            if(text[len(text)-4:]=="srrp"):
                cpu=1
            if(text[len(text)-4:]=="rrsp" or text[len(text)-4:]=="rspr"):
                cpu=2
            if(text[len(text)-4:]=="sprr"):
                cpu=1
            if(text[len(text)-4:]=="prrs"):
                cpu=3
        if(re.match("pprs",text) or re.match("ppsr",text)):
            if(text[len(text)-4:]=="pprs" or text[len(text)-4:]=="prsp"):
                cpu=3
            if(text[len(text)-4:]=="rspp"):
                cpu=2
            if(text[len(text)-4:]=="sppr"):
                cpu=1
            if(text[len(text)-4:]=="ppsr" or text[len(text)-4:]=="psrp"):
                cpu=3
            if(text[len(text)-4:]=="srpp"):
                cpu=1
            if(text[len(text)-4:]=="rpps"):
                cpu=2
        if(re.match("ssrp",text) or re.match("sspr",text)):
            if(text[len(text)-4:]=="ssrp" or text[len(text)-4:]=="srps"):
                cpu=1
            if(text[len(text)-4:]=="rpss"):
                cpu=2
            if(text[len(text)-4:]=="pssr"):
                cpu=3
            if(text[len(text)-4:]=="sspr" or text[len(text)-4:]=="sprs"):
                cpu=1
            if(text[len(text)-4:]=="prss"):
                cpu=3
            if(text[len(text)-4:]=="rssp"):
                cpu=2
        print("___________________________\nYou choose from r,p and s ...")
        user1=input()
        user=user1
        print(cpu)
        user=appoint_user(user)
        cpu=appoint_cpu(cpu)
        pattern(text,user1)
        print_choice(user,cpu)

    print("Would you like to see the Stastics of all of the games : y/n")
    ch=input()
    if(ch=="y"):

        f_r= open("P:/VIT/MINE/SEMESTER 3/Theory of Computation and Compiler Design/J Component/RPS/rps.txt","r+")
        r1=f_r.readline()
        sr=int(r1[7:])
        p1=f_r.readline()
        sp=int(p1[8:])
        s1=f_r.readline()
        ss=int(s1[11:])
        s1=f_r.readline()
        win=int(r1[6:])
        s1=f_r.readline()
        lost=int(p1[7:])
        s1=f_r.readline()
        tie=int(s1[6:])
        f_r.close()

        plt.subplot(2, 1, 1)
        objects = ('ROCK', 'PAPER', 'SCISSORS')
        y_pos = np.arange(len(objects))
        performance = [sr,sp,ss]
        plt.bar(y_pos, performance, align='center', alpha=1,color='blue')
        plt.xticks(y_pos, objects)
        plt.ylabel('NUMBER OF MOVES')
        plt.title('GESTURES')
        '''plt.show()'''

        plt.subplot(2, 1, 2)
        objects = ('WIN', 'LOST', 'TIE')
        y_pos = np.arange(len(objects))
        performance = [win,lost,tie]
        plt.bar(y_pos, performance, align='center', alpha=1,color='red')
        plt.xticks(y_pos, objects)
        plt.ylabel('TOTAL')
        plt.title('RESULTS')
        plt.show()
