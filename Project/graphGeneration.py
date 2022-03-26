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

    return pd.DataFrame({"from": fromColumn, "to": toColumn, "weight": weightColumn})

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
    print(dataframe)
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
    # Head of Household
    derrick, frankie = houseguests["Derrick"], houseguests["Frankie"]

    # Nominations
    christine, donny = houseguests["Christine"], houseguests["Donny"]
    christine.addNomination(derrick)
    donny.addNomination(derrick)

    caleb, cody = houseguests["Caleb"], houseguests["Cody"]
    caleb.addNomination(frankie)
    cody.addNomination(frankie)

    # Power of Veto (+ Nomination after POV)
    zach = houseguests["Zach"]
    zach.addNomination(frankie)

    #Eliminated houseguests
    evicted = [houseguests["Joey"], houseguests["Paola"], houseguests["Devin"], houseguests["Brittany"], houseguests["Amber"], houseguests["Jocasta"], houseguests["Hayden"], houseguests["Nicole"]]

    # Votes
    for houseguest in houseguests.values():
        isHOH = houseguest == frankie
        isNominated = houseguest == zach or houseguest == cody
        isEvicted = houseguest in evicted
        if (not isHOH) and (not isNominated) and (not isEvicted):
            zach.addVote(houseguest)

    # Graph
    dataframe = getDataFrame(houseguests)
    print(dataframe)
    weekNineGraph = nx.from_pandas_edgelist(dataframe, source="from",
        target="to", edge_attr="weight", create_using=nx.DiGraph)

    return weekNineGraph

def initWeekTenGraph(houseguests: Dict[str, "Houseguest"]) -> nx.DiGraph:
        # Head of Household
        cody = houseguests["Cody"]

        # Nominations
        nicole, donny = houseguests["Nicole"], houseguests["Donny"]
        nicole.addNomination(cody)
        donny.addNomination(cody)

        #Eliminated houseguests
        evicted = [houseguests["Joey"], houseguests["Paola"], houseguests["Devin"], houseguests["Brittany"], houseguests["Amber"], houseguests["Jocasta"], houseguests["Hayden"], houseguests["Zach"]]

        # Votes
        for houseguest in houseguests.values():
            isHOH = houseguest == cody
            isNominated = houseguest == nicole or houseguest == donny
            isEvicted = houseguest in evicted
            if (not isHOH) and (not isNominated) and (not isEvicted):
                donny.addVote(houseguest)

        # Graph
        dataframe = getDataFrame(houseguests)
        print(dataframe)
        weekTenGraph = nx.from_pandas_edgelist(dataframe, source="from",
            target="to", edge_attr="weight", create_using=nx.DiGraph)

        return weekTenGraph

def initWeekElevenGraph(houseguests: Dict[str, "Houseguest"]) -> nx.DiGraph:
        # Head of Household
        caleb = houseguests["Caleb"]

        # Nominations
        nicole, christine = houseguests["Nicole"], houseguests["Christine"]
        nicole.addNomination(caleb)
        christine.addNomination(caleb)

        # Power of Veto (+ Nomination after POV)
        victoria = houseguests["Victoria"]
        victoria.addNomination(caleb)

        #Eliminated houseguests
        evicted = [houseguests["Joey"], houseguests["Paola"], houseguests["Devin"], houseguests["Brittany"], houseguests["Amber"], houseguests["Jocasta"], houseguests["Hayden"], houseguests["Zach"], houseguests["Donny"]]

        # Votes
        for houseguest in houseguests.values():
            isHOH = houseguest == caleb
            isNominated = houseguest == nicole or houseguest == victoria
            isEvicted = houseguest in evicted
            if (not isHOH) and (not isNominated) and (not isEvicted):
                nicole.addVote(houseguest)

        # Graph
        dataframe = getDataFrame(houseguests)
        print(dataframe)
        weekElevenGraph = nx.from_pandas_edgelist(dataframe, source="from",
            target="to", edge_attr="weight", create_using=nx.DiGraph)

        return weekElevenGraph

def initWeekTwelveGraph(houseguests: Dict[str, "Houseguest"]) -> nx.DiGraph:
        # Head of Household
        derrick = houseguests["Derrick"]

        # Nominations
        victoria, christine = houseguests["Victoria"], houseguests["Christine"]
        victoria.addNomination(derrick)
        christine.addNomination(derrick)

        #Eliminated houseguests
        evicted = [houseguests["Joey"], houseguests["Paola"], houseguests["Devin"], houseguests["Brittany"], houseguests["Amber"], houseguests["Jocasta"], houseguests["Hayden"], houseguests["Zach"], houseguests["Donny"], houseguests["Nicole"]]

        # Votes
        for houseguest in houseguests.values():
            isHOH = houseguest == derrick
            isNominated = houseguest == christine or houseguest == victoria
            isEvicted = houseguest in evicted
            if (not isHOH) and (not isNominated) and (not isEvicted):
                christine.addVote(houseguest)

        # Graph
        dataframe = getDataFrame(houseguests)
        print(dataframe)
        weekTwelveGraph = nx.from_pandas_edgelist(dataframe, source="from",
            target="to", edge_attr="weight", create_using=nx.DiGraph)

        return weekTwelveGraph

def initWeekThirteenGraph(houseguests: Dict[str, "Houseguest"]) -> nx.DiGraph:
        # Head of Household
        frankie = houseguests["Frankie"]

        # Nominations
        victoria, cody = houseguests["Victoria"], houseguests["Cody"]
        victoria.addNomination(frankie)
        cody.addNomination(frankie)

        # Graph
        dataframe = getDataFrame(houseguests)
        print(dataframe)
        weekThirteenGraph = nx.from_pandas_edgelist(dataframe, source="from",
            target="to", edge_attr="weight", create_using=nx.DiGraph)

        return weekThirteenGraph

def initWeekFourteenGraph(houseguests: Dict[str, "Houseguest"]) -> nx.DiGraph:
    # Head of Household
    caleb = houseguests["Caleb"]

    # Nominations
    victoria, frankie = houseguests["Victoria"], houseguests["Frankie"]
    victoria.addNomination(caleb)
    frankie.addNomination(caleb)

    #Eliminated houseguests
    evicted = [houseguests["Joey"], houseguests["Paola"], houseguests["Devin"], houseguests["Brittany"], houseguests["Amber"], houseguests["Jocasta"], houseguests["Hayden"], houseguests["Zach"], houseguests["Donny"], houseguests["Nicole"], houseguests["Christine"]]

    # Votes
    for houseguest in houseguests.values():
        isHOH = houseguest == caleb
        isNominated = houseguest == frankie or houseguest == victoria
        isEvicted = houseguest in evicted
        if (not isHOH) and (not isNominated) and (not isEvicted):
            frankie.addVote(houseguest)

    # Graph
    dataframe = getDataFrame(houseguests)
    print(dataframe)
    weekFourteenGraph = nx.from_pandas_edgelist(dataframe, source="from",
        target="to", edge_attr="weight", create_using=nx.DiGraph)

    return weekFourteenGraph

def initWeekFifteenGraph(houseguests: Dict[str, "Houseguest"]) -> nx.DiGraph:
    # Head of Household
    derrick = houseguests["Derrick"]

    # Nominations
    victoria, caleb = houseguests["Victoria"], houseguests["Caleb"]
    victoria.addNomination(derrick)
    caleb.addNomination(derrick)

    #Eliminated houseguests
    evicted = [houseguests["Joey"], houseguests["Paola"], houseguests["Devin"], houseguests["Brittany"], houseguests["Amber"], houseguests["Jocasta"], houseguests["Hayden"], houseguests["Zach"], houseguests["Donny"], houseguests["Nicole"], houseguests["Christine"], houseguests["Frankie"]]

    # Votes
    for houseguest in houseguests.values():
        isHOH = houseguest == derrick
        isNominated = houseguest == caleb or houseguest == victoria
        isEvicted = houseguest in evicted
        if (not isHOH) and (not isNominated) and (not isEvicted):
            caleb.addVote(houseguest)

    # Graph
    dataframe = getDataFrame(houseguests)
    print(dataframe)
    weekFifteenGraph = nx.from_pandas_edgelist(dataframe, source="from",
        target="to", edge_attr="weight", create_using=nx.DiGraph)

    return weekFifteenGraph

def initWeekSixteenGraph(houseguests: Dict[str, "Houseguest"]) -> nx.DiGraph:
    # Head of Household
    cody = houseguests["Cody"]

    # Nominations
    victoria, derrick = houseguests["Victoria"], houseguests["Derrick"]
    victoria.addNomination(cody)
    derrick.addNomination(cody)

    #Eliminated houseguests
    evicted = [houseguests["Joey"], houseguests["Paola"], houseguests["Devin"], houseguests["Brittany"], houseguests["Amber"], houseguests["Jocasta"], houseguests["Hayden"], houseguests["Zach"], houseguests["Donny"], houseguests["Nicole"], houseguests["Christine"], houseguests["Frankie"], houseguests["Caleb"]]

    # Votes
    for houseguest in houseguests.values():
        isHOH = houseguest == cody
        isNominated = houseguest == derrick or houseguest == victoria
        isEvicted = houseguest in evicted
        if (not isHOH) and (not isNominated) and (not isEvicted):
            victoria.addVote(houseguest)

    # Graph
    dataframe = getDataFrame(houseguests)
    print(dataframe)
    weekSixteenGraph = nx.from_pandas_edgelist(dataframe, source="from",
        target="to", edge_attr="weight", create_using=nx.DiGraph)

    return weekSixteenGraph
