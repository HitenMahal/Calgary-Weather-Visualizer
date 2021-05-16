import numpy as np
import matplotlib.pyplot as plt

class Chart:
    def __init__(self):
        self.years = [90,91,92,93,94,95,96,97,98,99,
        "00","01","02","03","04","05","06","07","08","09",10,11,12,13,14,15,16,17,18,19]
        self.gap = np.arange(len(self.years))

    def barChart(self,values,ylabel,title):
        plt.figure(figsize = (12,6))
        plt.bar(self.gap, values, align='center', alpha=0.5)
        plt.xticks(self.gap, self.years)
        plt.ylabel(ylabel)
        plt.xlabel("Years (1990-2019)")
        plt.title(title)

        plt.show()

    def lineChart(self,values,ylabel,title):
        plt.figure(figsize = (12,6))
        plt.plot(self.years, values)
        plt.ylabel(ylabel)
        plt.xlabel("Years (1990-2019)")
        plt.title(title)
        plt.show()