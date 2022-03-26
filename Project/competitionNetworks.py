"""
COMP4602 - FINAL PROJECT
Dynamic Competition Networks Analysis

By: Katrina Ronquillo, Kelvin Tran, Jessica Tiberio
"""
import matplotlib.pyplot as plt
from graphGeneration import *
from graphAnalysis import *

if __name__ == "__main__":
    # Initialize Houseguests
    houseguests = initHouseGuests()

    # Week One
    weekOne = initWeekOneGraph(houseguests)
    drawGraph("Week One", weekOne)
    #displayData(weekOne)

    print(getCloseness(weekOne, "Joey"))

    # Week Nine
    weekNine = initWeekNineGraph(houseguests)
    drawGraph("Week Nine", weekNine)

    print(getCloseness(weekNine, "Zach"))

    # Week Ten
    weekTen = initWeekTenGraph(houseguests)
    drawGraph("Week Ten", weekTen)

    print(getCloseness(weekTen, "Donny"))

    # Week Eleven
    weekEleven = initWeekElevenGraph(houseguests)
    drawGraph("Week Eleven", weekEleven)

    print(getCloseness(weekEleven, "Nicole"))

    # Week Twelve
    weekTwelve = initWeekTwelveGraph(houseguests)
    drawGraph("Week Twelve", weekTwelve)

    print(getCloseness(weekTwelve, "Christine"))

    # Week Thirteen
    weekThirteen = initWeekThirteenGraph(houseguests)
    drawGraph("Week Thirteen", weekThirteen)

    # Week Fourteen
    weekFourteen = initWeekFourteenGraph(houseguests)
    drawGraph("Week Fourteen", weekFourteen)

    print(getCloseness(weekFourteen, "Frankie"))

    # Week Fifteen
    weekFifteen = initWeekFifteenGraph(houseguests)
    drawGraph("Week Fifteen", weekFifteen)

    print(getCloseness(weekFifteen, "Caleb"))

    # Week Sixteen
    weekSixteen = initWeekSixteenGraph(houseguests)
    drawGraph("Week Sixteen", weekSixteen)

    print(getCloseness(weekSixteen, "Victoria"))

    # Show Graphs
    plt.show()
