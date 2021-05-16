from WeatherAnalyzer import WeatherAnalyzer
from Chart import Chart

def main():
    analyzer = WeatherAnalyzer("CalgaryWeather.csv")
    chart = Chart()
    on = True
    menu = ("1- Get Maximum Temperature of 1990-2019"
    "\n2- Get Minimum Temperature of 1990-2019"
    "\n3- Get Maximum Temperature of 1990-2019 Annually"
    "\n4- Get Minimum Temperature of 1990-2019 Annually"
    "\n5- Get Average Snowfall Between 1990-2019 Annually"
    "\n6- Get Average Temperature of 1990-2019 Annually"
    "\n7- Line Graph of Maximum Temperature by Year"
    "\n8- Line Graph of Minimum Temperature by Year"
    "\n9- Bar Graph of Average Snow Fall by Year"
    "\n10- Bar Graph of Average Temperature by Year"
    "\nType 'Exit' to End Program")
    while on == True:
        print(menu)
        selection = input("Choose a Selection: ")
        if selection == "1":
            print("----------------------")
            analyzer.getMaxTemp()
        elif selection == "2":
            print("----------------------")
            analyzer.getMinTemp()
        elif selection == "3":
            print("----------------------")
            analyzer.getMaxTempAnnually()
        elif selection == "4":
            analyzer.getMinTempAnnually()
            print("----------------------")
        elif selection == "5":
            print("----------------------")
            analyzer.getAverageSnowFallAnnually()
        elif selection == "6":
            print("----------------------")
            analyzer.getAverageTempAnnually()
        elif selection == "7":
            print("----------------------")
            chart.lineChart(analyzer.getMaxTempAnnually("Off"),"Max Temp by Year", "Max Temp by Year")
        elif selection == "8":
            print("----------------------")
            chart.lineChart(analyzer.getMinTempAnnually("Off"),"Min Temp by Year","Min Temp by Year")
        elif selection == "9":
            print("----------------------")
            chart.barChart(analyzer.getAverageSnowFallAnnually("Off"),"Average Snow Fall","Average Snow Fall")
        elif selection == "10":
            print("----------------------")
            chart.barChart(analyzer.getAverageTempAnnually("Off"),"Average Temp","Average Temp")
        elif selection == "exit" or selection == "Exit":
            on = False
            print("----------------------")
        else:
            print("Please Input an Valid Integer Response")
        if input("Press Enter to Continue or Type 'Exit' to End Program: ") == "Exit": on = False
        print("----------------------")

if __name__ == "__main__":
    main()

