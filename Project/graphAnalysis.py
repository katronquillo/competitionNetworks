"""
COMP4602 - FINAL PROJECT
Dynamic Competition Networks Analysis
Graph Analysis Module 

This module does analysis on dynamic competition networks of Big Brother 16 
""" 
from matplotlib.pyplot import close
import networkx as nx
import pandas as pd
from typing import Set, List

def getCommonOutNeighbours(graph: nx.DiGraph, u: str, v: str) -> Set[str]:
    """
    Returns the set of common-out neighbours for the given nodes u, v in the
    given graph
    """
    return set(graph.successors(u)).intersection(graph.successors(v))

def getConScore(graph: nx.DiGraph, u: str) -> int:
    """
    Returns the CON score of the given node, u, in the given graph

    We define the CON score of a houseguest u as follors...
        CON(u) = \sum_{v in G} CON(u, v)
    where CON(u, v) is the number of common-out neighbours of u and v
    """
    conScore = 0
    for v in graph.nodes:
        if v != u:
            conScore += len(getCommonOutNeighbours(graph, u, v))

    return conScore

def getCloseness(graph: nx.DiGraph, u: str) -> float:
    """
    Returns the closeness centrality of the given node, u, in the given graph
    """
    return nx.closeness_centrality(graph.reverse(), u, distance="weight")

def getEdgeDensity(graph: nx.DiGraph, nodes: List[str]) -> float:
    """
    Returns the Edge Density of the subgraph of graph, induced by the given
    list of nodes
    """
    subgraph = graph.subgraph(nodes)
    return nx.density(subgraph)

def isNearIndependent(graph: nx.DiGraph, epsilon: float) -> bool:
    """
    Returns True if the given graph is epsilon-near independent, where
    epsilon is a non-negative real number
    """
    return getEdgeDensity(graph, graph.nodes) <= epsilon

def displayData(graph: nx.DiGraph) -> pd.DataFrame: 
    """
    Displays data for the given dynamic competiton network

    ID - In-Degree
    OD - Out-Degree
    C - Closeness Centrality
    CON - CON Score
    B - Betweeness Centrality 
    """
    name, inDegree, outDegree, closeness, con = [], [], [], [], [] 
    # Iterate through all nodes and calculate metrics 
    for node in graph.nodes:
        name.append(node)
        inDegree.append(graph.in_degree(node))
        outDegree.append(graph.out_degree(node))
        closeness.append(getCloseness(graph, node))
        con.append(getConScore(graph, node))
    
    df = pd.DataFrame({"name": name, 
                       "ID": inDegree, 
                        "OD": outDegree,
                        "C": closeness, 
                        "CON": con})
    print(df)
    return(df)

