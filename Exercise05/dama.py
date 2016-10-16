import math  
import pylab as pl
class bicycle:
    def __init__(self, power=10, mass=1, time_step=0.1,\
        initial_velocity=1 ,initial_x=0,initial_y=0,initial_Vx=50*math.cos(math.pi/6),\
       initial_Vy=50*math.sin(math.pi/6)):
        self.v = [initial_velocity]
        self.x=[initial_x]
        self.y=[initial_y]
        self.Vx=[initial_Vx]
        self.Vy=[initial_Vy]
        self.t = [0]
        self.m = mass
        self.p = power
        self.dt = time_step
    def run(self):
        while(self.y[-1]>=0):
            self.x.append(self.x[-1]+self.Vx[0]*self.dt)
            self.y.append(self.y[-1]+self.Vy[-1]*self.dt)
            self.Vy.append(self.Vy[-1]-9.8*self.dt)
        print("yn=",  self.y[-1])
        print("y(n-1)=",self.y[-2])
        print("xn=",self.x[-1])
        print("x(n-1)=",self.x[-2])
class diff_step_check(bicycle):    
    def show_result1(self,style='b'):
        pl.plot(self.x, self.y,style,label='30')
        pl.title('projectile motion without air resistance')
        pl.xlabel('x')
        pl.ylabel('y')
        pl.legend(loc='best')
a=diff_step_check( power=10, mass=1, time_step=0.1,\
        initial_velocity=1 ,initial_x=0,initial_y=0,initial_Vx=50*math.cos(math.pi/6),\
       initial_Vy=50*math.sin(math.pi/6))
a.run()
a.show_result1('b')
class diff_step_check(bicycle):
     def show_result2(self,style='b'):
        pl.plot(self.x, self.y,'k--',label='35')
        pl.title('projectile motion without air resistance')
        pl.xlabel('x(m)')
        pl.ylabel('y(m)')
        pl.legend(loc='best')
b=diff_step_check( power=10, mass=1, time_step=0.1,\
        initial_velocity=1 ,initial_x=0,initial_y=0,initial_Vx=50*math.cos(math.pi/6*(7/6)),\
       initial_Vy=50*math.sin(math.pi/6*(7/6)))
b.run()
b.show_result2('g')
class diff_step_check(bicycle):
     def show_result2(self,style='b'):
        pl.plot(self.x, self.y,'m-.',label='40')
        pl.title('projectile motion without air resistance')
        pl.xlabel('x(m)')
        pl.ylabel('y(m)')
        pl.legend(loc='best')
c=diff_step_check( power=10, mass=1, time_step=0.1,\
        initial_velocity=1 ,initial_x=0,initial_y=0,initial_Vx=50*math.cos(math.pi/6*(4/3)),\
       initial_Vy=50*math.sin(math.pi/6*(4/3)))
c.run()
c.show_result2('r')
class diff_step_check(bicycle):
     def show_result2(self,style='b'):
        pl.plot(self.x, self.y,'y-',label='45')
        pl.title('projectile motion without air resistance')
        pl.xlabel('x(m)')
        pl.ylabel('y(m)')
        pl.legend(loc='best')
d=diff_step_check( power=10, mass=1, time_step=0.1,\
        initial_velocity=1 ,initial_x=0,initial_y=0,initial_Vx=50*math.cos(math.pi/4),\
       initial_Vy=50*math.sin(math.pi/4))
d.run()
d.show_result2('c')
class diff_step_check(bicycle):
     def show_result2(self,style='b'):
        pl.plot(self.x, self.y,'b:',label='50')
        pl.title('projectile motion without air resistance')
        pl.xlabel('x(m)')
        pl.ylabel('y(m)')
        pl.legend(loc='best')
b=diff_step_check( power=10, mass=1, time_step=0.1,\
        initial_velocity=1 ,initial_x=0,initial_y=0,initial_Vx=50*math.cos(math.pi/4*(10/9)),\
       initial_Vy=50*math.sin(math.pi/4*(10/9)))
b.run()
b.show_result2('m')
class diff_step_check(bicycle):
     def show_result2(self,style='b'):
        pl.plot(self.x, self,'r--',style,label='55')
        pl.title('projectile motion without air resistance')
        pl.xlabel('x(m)')
        pl.ylabel('y(m)')
        pl.legend(loc='best')
b=diff_step_check( power=10, mass=1, time_step=0.1,\
        initial_velocity=1 ,initial_x=0,initial_y=0,initial_Vx=50*math.cos(math.pi/4*(11/9)),\
       initial_Vy=50*math.sin(math.pi/4*(11/9)))
b.run()
b.show_result2('y')
