"""
COMP4602 - FINAL PROJECT
Dynamic Competition Networks Analysis

By: Katrina Ronquillo, Kelvin Tran, Jessica Tiberio
"""
import os
import matplotlib.pyplot as plt
from graphGeneration import *
from graphAnalysis import *

if __name__ == "__main__":
    # User Prompts
    drawGraphs = input("Do you want to display the graphs? (Y/N): ").upper()
    while (drawGraphs not in ["Y", "N"]):
        drawGraphs = input("Do you want to display the graphs? (Y/N): ")
        drawGraphs = drawGraphs.upper()
    drawGraphs = True if (drawGraphs == "Y") else False

    writeLists = input("Do you want to save the edgelists? (Y/N): ").upper()
    while (writeLists not in ["Y", "N"]):
        writeLists = input("Do you want to save the edgelists? (Y/N): ")
        writeLists = writeLists.upper()
    writeLists = True if (writeLists == "Y") else False

    analyzeAlliances = input("Do you want to analyze alliances? (Y/N): ").upper()
    while (analyzeAlliances not in ["Y", "N"]):
        analyzeAlliances = input("Do you want to analyze alliances? (Y/N): ")
        analyzeAlliances = analyzeAlliances.upper()
    analyzeAlliances = True if (analyzeAlliances == "Y") else False

    # Initialize Houseguests
    houseguests = initHouseGuests()

    # Initialize Graphs
    graphs = []
    graphs.append(initWeekOneGraph(houseguests))
    graphs.append(initWeekTwoGraph(houseguests))
    graphs.append(initWeekThreeGraph(houseguests))
    graphs.append(initWeekFourGraph(houseguests))
    graphs.append(initWeekFiveGraph(houseguests))
    graphs.append(initWeekSixGraph(houseguests))
    graphs.append(initWeekSevenGraph(houseguests))
    graphs.append(initWeekEightGraph(houseguests))
    graphs.append(initWeekNineGraph(houseguests))
    graphs.append(initWeekTenGraph(houseguests))
    graphs.append(initWeekElevenGraph(houseguests))
    graphs.append(initWeekTwelveGraph(houseguests))
    graphs.append(initWeekThirteenGraph(houseguests))
    graphs.append(initWeekFourteenGraph(houseguests))
    graphs.append(initWeekFifteenGraph(houseguests))
    graphs.append(initWeekSixteenGraph(houseguests))

    # Write Edgelists (Optional)
    if (writeLists):
        for week in range(len(graphs)):
            if not os.path.exists("edgelists"):
                os.makedirs("edgelists")
            writeEdgeList(graphs[week][0], \
                f"./edgelists/mid_w{week + 1}_edgelist.txt")
            writeEdgeList(graphs[week][1], \
                f"./edgelists/final_w{week + 1}_edgelist.txt")
        print("=== All Edgelists saved to dir ./edgelists ===\n")
    
    # Analyze Alliances (Optional):
    if (analyzeAlliances):
        print("=== Alliance Analysis Module ===\n")

        currWeek = input("\nEnter week number (1-16): ")
        while (not currWeek.isdigit() and int(currWeek) not in range(17)):
            currWeek = input("\nEnter week number (1-16) or 0 to exit: ")
        currWeek = int(currWeek)

        print(f"Total Week {currWeek} Graph Edge Density: " +\
            f"{getEdgeDensity(graphs[currWeek - 1][1], [])}\n")

        while (analyzeAlliances):
            # Get Sublist of Houseguests to Analyze + Do ED analysis
            names = input("Enter list of names for houseguests in alliance. " \
                        + "Separate names by one space.\n")
            names = names.split(" ")
            alliance = [name.title() for name in names]

            print(f"\nAlliance Week {currWeek} Sub-Graph Edge Density: " +\
                f"{getEdgeDensity(graphs[currWeek - 1][1], alliance)}\n")
            
            print(f"Most Likely Alliance Leader on Week {currWeek} based on CON Score: " +\
                f"{getMaxConScore(graphs[currWeek - 1][1], alliance)}\n")

            # Loop Condition 
            analyzeAlliances = input("Do you want to analyze more alliances? (Y/N): ").upper()
            while (analyzeAlliances not in ["Y", "N"]):
                analyzeAlliances = input("Do you want to analyze alliances? (Y/N): ")
                analyzeAlliances = analyzeAlliances.upper()
            analyzeAlliances = True if (analyzeAlliances == "Y") else False
        
    # Draw and Show Graphs (Optional)
    if (drawGraphs):
        print("\n=== Graphs and Data Module ===")
        while (True):
            currWeek = input("\nEnter week number (1-16) or 0 to exit: ")
            while (not currWeek.isdigit() and int(currWeek) not in range(17)):
                currWeek = input("\nEnter week number (1-16) or 0 to exit: ")
            currWeek = int(currWeek)
            midGraph, finalGraph = graphs[currWeek - 1][0], graphs[currWeek - 1][1]

            if currWeek > 0:
                print("\nTable Sorted From Most Likely Leaders to Less Likely Leaders...")
                print(f"\nMid Week {currWeek} Graph (Before Votes)")
                displayData(midGraph)

                print(f"\nFinal Week {currWeek} Graph (After Votes)")
                displayData(finalGraph)

                drawGraph(f"Mid Week {currWeek}", midGraph)
                plt.show()

                drawGraph(f"Final Week {currWeek}", finalGraph)
                plt.show()
            else:
                break
    