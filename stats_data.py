import stadistics
class StatsData:
    def __init__(self, lista):
        self.l_data = lista
        self.mean = stadistics.mean(self.l_data)
        self.median = stadistics.median(self.l_data)
        self.varance = stadistics.variance(lista)
