# -*- coding: utf-8 -*-
__author__ = 'victor'

EX_GRAPH0 = {
    0: set([1, 2]),
    1: set(),
    2: set()
}

EX_GRAPH1 = {
    0: set([1, 4, 5]),
    1: set([2, 6]),
    2: set([3]),
    3: set([0]),
    4: set([1]),
    5: set([2]),
    6: set([])
}

EX_GRAPH2 = {
    0: set([1, 4, 5]),
    1: set([2, 6]),
    2: set([3, 7]),
    3: set([7]),
    4: set([1]),
    5: set([2]),
    6: set([]),
    7: set([3]),
    8: set([1, 2]),
    9: set([0, 3, 4, 5, 6, 7])
}

def make_complete_graph(num_nodes):
    return {i:(set(xrange(num_nodes))-set([i])) for i in xrange(num_nodes)} if num_nodes>0 else {}

def compute_in_degrees(digraph):
    indegree = dict.fromkeys(digraph.iterkeys(), 0)
    for heads in digraph.itervalues():
        for head in heads:
            indegree[head] += 1
    return indegree

def in_degree_distribution(digraph):
    indist = {}
    for v in compute_in_degrees(digraph).itervalues():
        indist[v] = indist.get(v, 0)+1
    return indist

if __name__ == '__main__':
    print compute_in_degrees(EX_GRAPH1)
    print in_degree_distribution(EX_GRAPH1)
