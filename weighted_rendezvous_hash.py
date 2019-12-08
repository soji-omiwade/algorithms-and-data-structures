"""
this code is from wikipedia
"""

def int_to_float(value: int) -> float: 
    """converts a uniformly random ([64-bit computing|64-bit]] integer
        to uniformly random floating point number on the interval [0,1)
    """
    
    #below: 0...0000011111111111111111111 and 0...000010000000000000000
    fifty_three_ones = (0xFFFFFFFFFFFFFFFF >> (64-53))
    fifty_three_zeros = float(1 << 53)
    return (value & fifty_three_ones) / fifty_three_zeros
    
# class Node:
    # """class representing a node that is assigned keys as part of a 
        # weighted rendezvous hash"""
        
    # def __init__(self, name, seed, weight):
        # self.name,self.seed, self.weight = name, seed, weight
        
    # def __str__(self):
        # return f"({}{}{}").forma