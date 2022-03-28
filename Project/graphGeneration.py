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
    # Head of Household
    amber, devin = houseguests["Amber"], houseguests["Devin"]

    # Nominations
    hayden, nicole = houseguests["Hayden"], houseguests["Nicole"]
    hayden.addNomination(amber)
    nicole.addNomination(amber)

    paola, brittany = houseguests["Paola"], houseguests["Brittany"]
    paola.addNomination(devin)
    brittany.addNomination(devin)

    # Power of Veto (+ Nomination after POV)
    zach = houseguests["Zach"]
    zach.addNomination(devin)

    # Votes
    for houseguest in houseguests.values():
        isHOH = houseguest == devin
        isNominated = houseguest == paola or houseguest == zach
        if (not isHOH) and (not isNominated):
            paola.addVote(houseguest)
    
    # Graph
    dataframe = getDataFrame(houseguests)
    weekTwoGraph = nx.from_pandas_edgelist(dataframe, source="from",
        target="to", edge_attr="weight", create_using=nx.DiGraph)
    
    return weekTwoGraph

def initWeekThreeGraph(houseguests: Dict[str, "Houseguest"]) -> nx.DiGraph:
    # Head of Household
    nicole, derrick = houseguests["Nicole"], houseguests["Derrick"]

    # Nominations
    amber, donny = houseguests["Amber"], houseguests["Donny"]
    amber.addNomination(nicole)
    donny.addNomination(nicole)

    caleb, jocasta = houseguests["Caleb"], houseguests["Jocasta"]
    caleb.addNomination(donny)
    jocasta.addNomination(donny)

    # Power of Veto (+ Nomination after POV)
    devin = houseguests["Devin"]
    devin.addNomination(derrick)

    # Votes
    for houseguest in houseguests.values():
        isHOH = houseguest == derrick
        isNominated = houseguest == caleb or houseguest == devin
        if (not isHOH) and (not isNominated):
            devin.addVote(houseguest)

    # Graph
    dataframe = getDataFrame(houseguests)
    weekThreeGraph = nx.from_pandas_edgelist(dataframe, source="from",
        target="to", edge_attr="weight", create_using=nx.DiGraph)
    
    return weekThreeGraph

def initWeekFourGraph(houseguests: Dict[str, "Houseguest"]) -> nx.DiGraph:
    # Head of Household
    frankie, cody = houseguests["Frankie"], houseguests["Cody"]

    # Nominations
    jocasta, amber = houseguests["Jocasta"], houseguests["Amber"]
    jocasta.addNomination(frankie)
    amber.addNomination(frankie)

    victoria, brittany = houseguests["Victoria"], houseguests["Brittany"]
    victoria.addNomination(cody)
    brittany.addNomination(cody)

    # Power of Veto (+ Nomination after POV)
    donny = houseguests["Donny"]
    donny.addNomination(cody)

    # Votes
    for houseguest in houseguests.values():
        isHOH = houseguest == cody
        isNominated = houseguest == donny or houseguest == brittany
        if (not isHOH) and (not isNominated):
            brittany.addVote(houseguest)

    # Graph
    dataframe = getDataFrame(houseguests)
    weekFourGraph = nx.from_pandas_edgelist(dataframe, source="from",
        target="to", edge_attr="weight", create_using=nx.DiGraph)
    
    return weekFourGraph

def initWeekFiveGraph(houseguests: Dict[str, "Houseguest"]) -> nx.DiGraph:
    # Head of Household
    zach, frankie = houseguests["Zach"], houseguests["Frankie"]

    # Nominations
    christine, nicole = houseguests["Christine"], houseguests["Nicole"]
    christine.addNomination(zach)
    nicole.addNomination(zach)

    jocasta, victoria = houseguests["Jocasta"], houseguests["Victoria"]
    jocasta.addNomination(frankie)
    victoria.addNomination(frankie)

    # Power of Veto (+ Nomination after POV)
    amber = houseguests["Amber"]
    amber.addNomination(frankie)

    # Votes
    for houseguest in houseguests.values():
        isHOH = houseguest == frankie
        isNominated = houseguest == jocasta or houseguest == amber
        if (not isHOH) and (not isNominated):
            amber.addVote(houseguest)

    # Graph
    dataframe = getDataFrame(houseguests)
    weekFiveGraph = nx.from_pandas_edgelist(dataframe, source="from",
        target="to", edge_attr="weight", create_using=nx.DiGraph)
    
    return weekFiveGraph

def initWeekSixGraph(houseguests: Dict[str, "Houseguest"]) -> nx.DiGraph:
    # Head of Household
    nicole, donny = houseguests["Nicole"], houseguests["Donny"]

    # Nominations
    jocasta, zach = houseguests["Jocasta"], houseguests["Zach"]
    jocasta.addNomination(nicole)
    zach.addNomination(nicole)

    caleb, victoria = houseguests["Caleb"], houseguests["Victoria"]
    caleb.addNomination(donny)
    victoria.addNomination(donny)

    # Power of Veto (+ Nomination after POV)
    # Not used.

    # Votes
    for houseguest in houseguests.values():
        isHOH = houseguest == nicole
        isNominated = houseguest == jocasta or houseguest == zach
        if (not isHOH) and (not isNominated):
            jocasta.addVote(houseguest)

    # Graph
    dataframe = getDataFrame(houseguests)
    weekSixGraph = nx.from_pandas_edgelist(dataframe, source="from",
        target="to", edge_attr="weight", create_using=nx.DiGraph)
    
    return weekSixGraph

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