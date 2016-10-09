print('The initial number of A:')
na=input()
print('The initial number of B:')
nb=print('The initial number of time:')
print('time_costant')
t=input()
print('time_of_duration')
tu=input()
print('The time step: ')
dt=input()
import pylab as pl
class uranium_decay:
    def __init__(self, number_of_NA = na,number_of_NB = nb, time_constant = t, time_of_duration = tu, time_step = dt):
        self.na_uranium = [number_of_NA]
        self.nb_uranium = [number_of_NB]
        self.t = [0]
        self.tau = time_constant
        self.dt = time_step
        self.time = time_of_duration
        self.nsteps = int(time_of_duration//time_step + 1)
    def calculate(self):
        for i in range(self.nsteps):
            tmpa = self.na_uranium[i] + (self.nb_uranium[i]-self.na_uranium[i])/self.tau * self.dt
            tmpb = self.nb_uranium[i] + (self.na_uranium[i]-self.nb_uranium[i])/self.tau * self.dt
            self.nb_uranium.append(tmpb)
            self.na_uranium.append(tmpa)
            self.t.append(self.t[i] + self.dt)
    def show_results(self):
        pl.plot(self.t, self.na_uranium)
        pl.plot(self.t, self.nb_uranium)
        pl.xlabel('time ($s$)')
        pl.ylabel('Number of Nuclei')
        pl.show()
a = uranium_decay()
a.calculate()
a.show_results()
