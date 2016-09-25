a1='  #  '
a2=' # # '
a3='#####'
a4='#   #'
a5='#   #'
b1='#### '
b2='#   #'
b3='#####'
b4='#   #'
b5='#### '
c1=' ####'
c2='#    '
c3='#    '
c4='#    '
c5=' ####'
d1='###  '
d2='#  # '
d3='#   #'
d4='#  # '
d5='###  '
e1='#####'
e2='#    '
e3='#####'
e4='#    '
e5='#####'
f1='#####'
f2='#    '
f3='#####'
f4='#    '
f5='#    '
g1='#####'
g2='#    '
g3='#  ##'
g4='#   #'
g5='#####'
h1='#   #'
h2='#   #'
h3='#####'
h4='#   #'
h5='#   #'
i1=' ### '
i2='  #  '
i3='  #  '
i4='  #  '
i5=' ### ' 
j1=' ### '
j2='  #  '
j3='  #  '
j4='# #  '
j5='###  '
k1='#  ##'
k2='# #  '
k3='##   '
k4='# #  '
k5='#  ##'
l1='#    '
l2='#    '
l3='#    '
l4='#    '
l5='#####'
m1='## ##'
m2='# # #'
m3='# # #'
m4='# # #'
m5='#   #'
n1='#   #'
n2='##  #'
n3='# # #'
n4='#  ##'
n5='#   #'
o1=' ### '
o2='#   #'
o3='#   #'
o4='#   #'
o5=' ### '
p1='#### '
p2='#   #'
p3='#### '
p4='#    '
p5='#    '
q1='#### '
q2='#  # '
q3='# ## '
q4='#### '
q5='    #'
r1='#### '
r2='#   #'
r3='#### '
r4='# #  '
r5='#  ##'
s1='#####'
s2='#    '
s3='#####'
s4='    #'
s5='#####'
t1='#####'
t2='  #  '
t3='  #  '
t4='  #  '
t5='  #  '
u1='#   #'
u2='#   #'
u3='#   #'
u4='#   #'
u5=' ### '
v1='#   #'
v2='#   #'
v3=' # # '
v4=' # # '
v5='  #  '
w1='# # #'
w2='# # #'
w3='# # #'
w4='# # #'
w5=' # # '
x1='#   #'
x2=' # # '
x3='  #  '
x4=' # # '
x5='#   #'
y1='#   #'
y2=' # # '
y3='  #  '
y4='  #  '
y5='  #  '
z1='#####'
z2='   # '
z3='  #  '
z4=' #   '
z5='#####'
kg1='     '
kg2='     '
kg3='     '
kg4='     '
kg5='     '
A=[a1,a2,a3,a4,a5]
B=[b1,b2,b3,b4,b5]
C=[c1,c2,c3,c4,c5]
D=[d1,d2,d3,d4,d5]
E=[e1,e2,e3,e4,e5]
F=[f1,f2,f3,f4,f5]
G=[g1,g2,g3,g4,g5]
H=[h1,h2,h3,h4,h5]
I=[i1,i2,i3,i4,i5]
J=[j1,j2,j3,j4,j5]
K=[k1,k2,k3,k4,k5]
L=[l1,l2,l3,l4,l5]
M=[m1,m2,m3,m4,m5]
N=[n1,n2,n3,n4,n5]
O=[o1,o2,o3,o4,o5]
P=[p1,p2,p3,p4,p5]
Q=[q1,q2,q3,q4,q5]
R=[r1,r2,r3,r4,r5]
S=[s1,s2,s3,s4,s5]
T=[t1,t2,t3,t4,t5]
U=[u1,u2,u3,u4,u5]
V=[v1,v2,v3,v4,v5]
W=[w1,w2,w3,w4,w5]
X=[x1,x2,x3,x4,x5]
Y=[y1,y2,y3,y4,y5]
Z=[z1,z2,z3,z4,z5]
kong=[kg1,kg2,kg3,kg4,kg5]
engdic={'a':A,'b':B,'c':C,'d':D,'e':E,'f':F,'g':G,'h':H,'i':I,'j':J,'k':K,'l':L,'m':M,'n':N,'o':O,'p':P,'q':Q,'r':R,'s':S,'t':T,'u':U,'v':V,'w':W,'x':X,'y':Y,'z':Z,' ':kong}
def line0(x):
    y=list(x)
    length=len(y)
    line_0=''
    for i in y:
        line_0=line_0+' '+engdic[i][0]
    return line_0

def line1(x):
    y=list(x)
    length=len(y)
    line_1=''
    for i in y:
        line_1=line_1+' '+engdic[i][1]
    return line_1

def line2(x):
    y=list(x)
    length=len(y)
    line_2=''
    for i in y:
        line_2=line_2+' '+engdic[i][2]
    return line_2

def line3(x):
    y=list(x)
    length=len(y)
    line_3=''
    for i in y:
        line_3=line_3+' '+engdic[i][3]
    return line_3

def line4(x):
    y=list(x)
    length=len(y)
    line_4=''
    for i in y:
        line_4=line_4+' '+engdic[i][4]
    return line_4

def bigpattern(x):
    import time 
    import os
    os.system('cls')
    time.sleep(1)
    os.system('cls')
    for i in range(0,20):
        print(i*' '+line0(x))
        print(i*' '+line1(x))
        print(i*' '+line2(x))
        print(i*' '+line3(x))
        print(i*' '+line4(x))
    
        time.sleep(0.2)
        os.system('cls')

y=raw_input('What is your name?: ')
x=y.lower()
bigpattern(x)
raw_input('Press enter to exit')
