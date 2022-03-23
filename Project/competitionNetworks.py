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

    # Show Graphs
    plt.show()
    