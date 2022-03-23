"""
Houseguest Class
"""
from typing import Dict, List

class Houseguest:
    """
    A houseguest on Big Brother.
    """
    _name: str
    _numHOH: int
    _numVeto: int
    _totalNominated: Dict["Houseguest", int] 
    _totalVotes: Dict["Houseguest", int]
    _totalCompetition: Dict["Houseguest", int]

    def __init__(self, name: str) -> None:
        """
        Initialize this Houseguest, using their name
        """
        self._name = name
        self._totalNominated = {}
        self._totalVotes = {}
        self._totalCompetition = {}

    def getName(self) -> str:
        """
        Returns the name of this Houseguest
        """
        return self._name
    
    def getTotalNominated(self) -> int:
        """
        Returns a dictionary containing information about all of the 
        nominations to evict this Houseguest.

        Structure is as follows:
        {OtherHouseguest: # of nominations against this Houseguest} 
        """
        return self._totalNominated
    
    def setNominations(self, other: "Houseguest", numNominated: int) -> None:
        """
        Modify this Houseguest to indicate that the given Houseguest, other,
        has nominated them numNominated times 
        """
        if other in self._totalNominated:
            self._totalNominated[other] = numNominated
        else:
            self._totalNominated[other] = numNominated
        
        if other in self._totalCompetition:
            self._totalCompetition[other] += numNominated
        else:
            self._totalCompetition[other] = numNominated
    
    def addNomination(self, other: "Houseguest") -> None: 
        """
        Modify this Houseguest to indicate that the given Houseguest, other,
        has nominated them for eviction. 
        """
        if other in self._totalNominated:
            self._totalNominated[other] += 1
        else:
            self._totalNominated[other] = 1
        
        if other in self._totalCompetition:
            self._totalCompetition[other] += 1
        else:
            self._totalCompetition[other] = 1

    def getTotalVotes(self) -> None:
        """
        Returns a dictionary containing information about all of the votes
        to evict this Houseguest.

        Structure is as follows:
        {OtherHouseguest: # of votes against this Houseguest} 
        """
        return self._totalVotes
    
    def setVotes(self, other: "Houseguest", numVotes: int) -> None:
        """
        Modify this Houseguest to indicate that the given Houseguest, other,
        has cast a numVotes votes against them
        """
        if other in self._totalVotes:
            self._totalVotes[other] = numVotes
        else:
            self._totalVotes[other] = numVotes
        
        if other in self._totalCompetition:
            self._totalCompetition[other] += numVotes
        else:
            self._totalCompetition[other] = numVotes
    
    def addVote(self, other: "Houseguest") -> None:
        """
        Modify this Houseguest to indicate that the given Houseguest, other,
        has cast a 1 vote against them
        """
        if other in self._totalVotes:
            self._totalVotes[other] += 1
        else:
            self._totalVotes[other] = 1
        
        if other in self._totalCompetition:
            self._totalCompetition[other] += 1
        else:
            self._totalCompetition[other] = 1
    
    def getTotalCompetition(self) -> Dict["Houseguest", int]:
        """
        Returns a dictionary containing information about all of the acts of
        competition against this Houseguest 

        Structure is as follows:
        {OtherHouseguest: # of acts of competiton against this Houseguest} 
        """
        return self._totalCompetition
    
    def __hash__(self):
        """
        Returns hash value of this Houseguest 
        """
        return hash(self._name)

    def __eq__(self, other: "Houseguest") -> bool:
        """
        Returns True if this Houseguest is equal to the other Houseguest, and
        returns False otherwise
        """
        return type(self) == type(other) and self._name == other._name
    
    def __ne__(self, other: "Houseguest") -> bool:
        """
        Returns True if this Houseguest is not equal to the other Houseguest, and
        returns False otherwise
        """
        return not (self == other)
    
    def __str__(self) -> str:
        """
        Returns a string representation of this Houseguest
        """
        return f"Houseguest {self._name}"


def initNames() -> List[str]:
    """
    Returns a list of the names of the houseguests in Big Brother Season 16
    """
    names = ["Derrick", "Cody", "Victoria", "Caleb", "Frankie", "Christine",
            "Nicole", "Donny", "Zach", "Hayden", "Jocasta", "Amber", 
            "Brittany", "Devin", "Paola", "Joey"]

    return names

def initHouseGuests() -> Dict[str, "Houseguest"]:
    """
    Initialize Big Brother Season 16 Houseguests
    """
    houseguests = {}
    names = initNames()
    
    for name in names:
        newHouseguest = Houseguest(name)
        houseguests[name] = newHouseguest
    
    return houseguests

