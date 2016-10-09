import pylab as pl
class uranium_decay:
    def __init__(self, number_of_NA = 100,number_of_NB = 0, time_constant = 0.5, time_of_duration = 5, time_step = 0.05):
        self.na = [number_of_NA]
        self.nb = [number_of_NB]
        self.t = [0]
        self.tau = time_constant
        self.dt = time_step
        self.time = time_of_duration
        self.nsteps = int(time_of_duration//time_step + 1)
        print("The initial number of A:", number_of_NA)
        print("The initial number of B:", number_of_NB)
        print("The initial number of time :", time_constant)
        print("Time_of_duration : ", time_step)
        print("Total step : ", time_of_duration)
    def calculate(self):
        for i in range(self.nsteps):
            tmpa = self.na[i] + (self.nb[i]-self.na[i])/self.tau * self.dt
            tmpb = self.nb[i] + (self.na[i]-self.nb[i])/self.tau * self.dt
            self.nb.append(tmpb)
            self.na.append(tmpa)
            self.t.append(self.t[i] + self.dt)
    def show_results(self):
        pl.plot(self.t, self.na)
        pl.plot(self.t, self.nb)
        pl.xlabel('time ($s$)')
        pl.ylabel('NA/NB')
        pl.show()
a = uranium_decay()
a.calculate()
a.show_results()
