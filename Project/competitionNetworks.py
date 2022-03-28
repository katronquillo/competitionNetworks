"""
COMP4602 - FINAL PROJECT
Dynamic Competition Networks Analysis

By: Katrina Ronquillo, Kelvin Tran, Jessica Tiberio
"""
from inspect import getcallargs
import matplotlib.pyplot as plt
from graphGeneration import *
from graphAnalysis import *

if __name__ == "__main__":
    # Initialize Houseguests
    houseguests = initHouseGuests()

    # Week One
    weekOne = initWeekOneGraph(houseguests)
    drawGraph("Week One", weekOne)
    displayData(weekOne)

    # Week Two
    weekTwo = initWeekTwoGraph(houseguests)
    drawGraph("Week Two", weekTwo)
    displayData(weekTwo)

    # Week Three
    weekThree = initWeekThreeGraph(houseguests)
    drawGraph("Week Three", weekThree)
    displayData(weekThree)

    # Week Four
    weekFour = initWeekFourGraph(houseguests)
    drawGraph("Week Four", weekFour)
    displayData(weekFour)
    
    # Week Five
    weekFive = initWeekFiveGraph(houseguests)
    drawGraph("Week Five", weekFive)
    displayData(weekFive)
    
    # Week Six
    weekSix = initWeekSixGraph(houseguests)
    drawGraph("Week Six", weekSix)
    displayData(weekSix)
    
    # # Week Seven
    weekSeven = initWeekSevenGraph(houseguests)
    drawGraph("Week Seven", weekSeven)
    displayData(weekSeven)
    
    # # Week Eight
    weekEight = initWeekEightGraph(houseguests)
    drawGraph("Week Eight", weekEight)
    displayData(weekEight)
    
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
