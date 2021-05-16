from FileIO import FileIO
from TemperatureData import TemperatureData

class WeatherAnalyzer:
    def __init__(self,fileName):
        self.TempDataList = []
        fileObj = FileIO(fileName)
        for i in fileObj.data:
            self.TempDataList.append(TemperatureData(i))
    
    def getMaxTemp(self,onOff = "print"):
        maxObj = self.TempDataList[0]
        for i in self.TempDataList:
            if i.maxTemp >= maxObj.maxTemp:
                maxObj = i
        if onOff == "obj":
            return maxObj
        else:
            print("The Maximum Temperature between 1990 and 2019 is",maxObj.maxTemp,"degrees")
    
    def getMinTemp(self,onOff = "print"):
        minObj = self.TempDataList[0]
        for i in self.TempDataList:
            if i.minTemp <= minObj.minTemp:
                minObj = i
        if onOff == "obj":
            return minObj
        else:
            print("The Minimum Temperature between 1990 and 2019 is",minObj.minTemp,"degrees")
    
    def getMaxTempAnnually(self,printOnOff = "On"):
        output = "Max Temperatures by Year\n"
        outputList = []
        year, maxTemp, counter = 1990, self.TempDataList[0].maxTemp, 0
        for i in self.TempDataList:
            if i.date.year == year:
                if i.maxTemp > maxTemp:
                    maxTemp = i.maxTemp
            else: 
                outputList.append(maxTemp)
                output += f"{i.date.year - 1}: {maxTemp:.2f}"
                if counter == 3: 
                    output += '\n'
                    counter = 0
                else: 
                    output += " "*10
                    counter += 1
                year += 1
                maxTemp = i.maxTemp
            if i.date.year == 2019 and i.date.month == 11:
                outputList.append(maxTemp)
                output += f"{i.date.year}: {maxTemp:.2f}\n"
        if printOnOff == "On":
            print(output)
        else:
            return outputList

    def getMinTempAnnually(self,printOnOff = "On"):
        output = "Min Temperatures by Year\n"
        outputList = []
        year, minTemp,counter = 1990, self.TempDataList[0].minTemp, 0
        for i in self.TempDataList:
            if i.date.year == year:
                if i.minTemp < minTemp:
                    minTemp = i.minTemp
            else: 
                outputList.append(minTemp)
                output += f"{i.date.year - 1}: {minTemp:.2f}"
                if counter == 3:
                    output += "\n"
                    counter = 0
                else:
                    output += " "*10
                    counter += 1
                year += 1
                minTemp = i.minTemp
            if i.date.year == 2019 and i.date.month == 11:
                outputList.append(minTemp)
                output += f"{i.date.year}: {minTemp:.2f}\n"
        if printOnOff == "On": 
            print(output)
        else:
            return outputList
    
    def getAverageSnowFallAnnually(self,printOnOff= "On"):
        if printOnOff == "On":
            output = "Snow fall by Year\n"
        outputList = []
        year, counter, average, a = 1990, 0, 0, 0
        for i in self.TempDataList:
            if i.date.year == year:
                average += i.snowFall
                counter += 1
                #print(i.date.year,i.snowFall,counter)
            else: 
                outputList.append([i.date.year - 1, average / counter])
                year += 1
                average = i.snowFall
                counter = 1
            if i.date.year == 2019 and i.date.month == 11:
                outputList.append([i.date.year, average / counter])
        if printOnOff == "Off":
            outputList2 = []
            for i in outputList:
                outputList2.append(i[1])
            return outputList2
        else:
            for i in outputList:
                output += f"{i[0]}: {i[1]:.2f}"
                if a == 3:
                    output += "\n"
                    a = 0
                else:
                    output += " " * 10
                    a += 1
            print(output)

    def getAverageTempAnnually(self, printOnOff = "On"):
        if printOnOff == "On":
            output = "Average Temperature by Year\n"
        outputList = []
        year, counter, average, a = 1990, 0, 0, 0
        for i in self.TempDataList:
            if i.date.year == year:
                average += (i.maxTemp + i.minTemp) / 2
                counter += 1
            else: 
                outputList.append([i.date.year - 1, average / counter])
                year += 1
                average = (i.maxTemp + i.minTemp) / 2
                counter = 1
            if i.date.year == 2019 and i.date.month == 11:
                outputList.append([i.date.year, average / counter])
        if printOnOff == "Off":
            outputList2 = []
            for i in outputList:
                outputList2.append(i[1])
            return outputList2
        else:
            for i in outputList:
                output += f"{i[0]}: {i[1]:.2f}"
                if a == 3:
                    output += "\n"
                    a = 0
                else:
                    output += " " * 10
                    a += 1
            print(output)
