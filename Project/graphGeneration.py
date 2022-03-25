"""
COMP4602 - FINAL PROJECT
Dynamic Competition Networks Analysis
Graph Generation Module 

This module generates the dynamic competition networks for Big Brother 16
"""
import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Dict
from classes.houseguest import *

def drawGraph(figureNum: str, graph: nx.DiGraph) -> None:
    """
    Draw the given graph with the given unique identifier for the figure, 
    figureNum
    """
    plt.figure(figureNum)
    positions = nx.spring_layout(graph, k=100, iterations=20)
    nx.draw(graph, pos=positions,
        node_size=500, node_color="#6944a3")
    nx.draw_networkx_labels(graph, pos=positions, 
        font_size=5, font_color="white")
    labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos=positions, edge_labels=labels,
        font_size=5)

def getDataFrame(houseguests: Dict[str, "Houseguest"]) -> pd.DataFrame:
    """
    Returns an dataframe representing the given competition data, 
    houseguests.

    Adds an edge between two houseguests if 
    """
    fromColumn, toColumn, weightColumn = [], [], []

    # Iterate through all houseguests
    for houseguest in houseguests.values():
        # Add acts of competition against the current houseguest
        currHouseguestName = houseguest.getName()

        # Competition
        for competitor in houseguest.getTotalCompetition():
            fromColumn.append(competitor.getName())
            toColumn.append(currHouseguestName)
            numCompetition = houseguest.getTotalCompetition()[competitor]
            weightColumn.append(1/numCompetition)

    return pd.DataFrame({"from": fromColumn, 
                        "to": toColumn, 
                        "weight": weightColumn})

def initWeekOneGraph(houseguests: Dict[str, "Houseguest"]) -> nx.DiGraph:
    # Head of Household
    frankie, caleb = houseguests["Frankie"], houseguests["Caleb"]

    # Nominations
    victoria, brittany = houseguests["Victoria"], houseguests["Brittany"]
    victoria.addNomination(frankie)
    brittany.addNomination(frankie)

    donny, paola = houseguests["Donny"], houseguests["Paola"]
    donny.addNomination(caleb)
    paola.addNomination(caleb)

    # Power of Veto (+ Nomination after POV)
    joey = houseguests["Joey"]
    joey.addNomination(caleb)

    # Votes
    for houseguest in houseguests.values():
        isHOH = houseguest == caleb
        isNominated = houseguest == paola or houseguest == joey
        if (not isHOH) and (not isNominated):
            joey.addVote(houseguest)
    
    # Graph
    dataframe = getDataFrame(houseguests)
    weekOneGraph = nx.from_pandas_edgelist(dataframe, source="from",
        target="to", edge_attr="weight", create_using=nx.DiGraph)

    return weekOneGraph

def initWeekTwoGraph(houseguests: Dict[str, "Houseguest"]) -> nx.DiGraph:
    pass

def initWeekThreeGraph(houseguests: Dict[str, "Houseguest"]) -> nx.DiGraph:
    pass

def initWeekFourGraph(houseguests: Dict[str, "Houseguest"]) -> nx.DiGraph:
    pass

def initWeekFiveGraph(houseguests: Dict[str, "Houseguest"]) -> nx.DiGraph:
    pass

def initWeekSixGraph(houseguests: Dict[str, "Houseguest"]) -> nx.DiGraph:
    pass

def initWeekSevenGraph(houseguests: Dict[str, "Houseguest"]) -> nx.DiGraph:
    pass

def initWeekEightGraph(houseguests: Dict[str, "Houseguest"]) -> nx.DiGraph:
    pass

def initWeekNineGraph(houseguests: Dict[str, "Houseguest"]) -> nx.DiGraph:
    pass

def initWeekTenGraph(houseguests: Dict[str, "Houseguest"]) -> nx.DiGraph:
    pass

def initWeekElevenGraph(houseguests: Dict[str, "Houseguest"]) -> nx.DiGraph:
    pass

def initWeekTwelveGraph(houseguests: Dict[str, "Houseguest"]) -> nx.DiGraph:
    pass

def initWeekThirteenGraph(houseguests: Dict[str, "Houseguest"]) -> nx.DiGraph:
    pass

def initWeekFourteenGraph(houseguests: Dict[str, "Houseguest"]) -> nx.DiGraph:
    pass

def initWeekFifteenGraph(houseguests: Dict[str, "Houseguest"]) -> nx.DiGraph:
    pass

def initWeekSixteenGraph(houseguests: Dict[str, "Houseguest"]) -> nx.DiGraph:
    pass