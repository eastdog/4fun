"""
project part of second module for Algorithmic thinking
"""
# -*- coding: utf-8 -*-
__author__ = 'victor'

from collections import deque

def bfs_visited(ugraph, start_node):
    """
    breadth first search
    """
    queue = deque()
    queue.append(start_node)
    visited = set([start_node])

    while len(queue)>0:
        current = queue.pop()
        for neib in ugraph.get(current):
            if not neib in visited:
                visited.add(neib)
                queue.append(neib)
    return visited

def cc_visited(ugraph):
    """
    cc visited
    """
    nodes = set(ugraph.keys())
    cc_result = []
    while len(nodes)>0:
        current = bfs_visited(ugraph, nodes.pop())
        cc_result.append(current)
        nodes -= current
    return cc_result

def largest_cc_size(ugraph):
    """
    largest cc size
    :param ugraph:
    :return:
    """
    cc_result = cc_visited(ugraph)
    return max(map(lambda x:len(x), cc_result))

def compute_resilience(ugraph, attack_order):
    """
    compute resilience
    :param ugraph:
    :param attack_order:
    :return:
    """
    resilience = [largest_cc_size(ugraph)]
    for attack in attack_order:
        ugraph = del_graph(ugraph, attack)
        resilience.append(largest_cc_size(ugraph))
    return resilience

def del_graph(ugraph, node):
    """
    del a node from a graph
    :param ugraph:
    :param node:
    :return:
    """
    for connection in ugraph.get(node):
        ugraph.get(connection).remove(node)
    del ugraph[node]
    return ugraph

if __name__ == '__main__':
    print 'main'
    EX_GRAPH1 = {
    0: set([1, 4, 5]),
    1: set([2, 6]),
    2: set([3]),
    3: set([0]),
    4: set([1]),
    5: set([2]),
    6: set([])
}
    print compute_resilience(EX_GRAPH1,[1])