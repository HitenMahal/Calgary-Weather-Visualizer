from Date import Date

class TemperatureData:
    def __init__(self,data):
        self.date = Date(int(data[0]),int(data[1]))
        self.maxTemp = float(data[2])
        self.minTemp = float(data[3])
        self.snowFall = float(data[4])