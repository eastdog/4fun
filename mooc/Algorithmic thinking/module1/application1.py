# -*- coding: utf-8 -*-
__author__ = 'victor'
"""
for application number 1
"""

import random
import matplotlib.pyplot as plt
from project1 import in_degree_distribution
from project1 import make_complete_graph
from math import log

class DPATrial:
    """
    Simple class to encapsulate optimized trials for DPA algorithm

    Maintains a list of node numbers with multiple instances of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities

    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a DPATrial object corresponding to a
        complete graph with num_nodes nodes

        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        """
        Conduct num_node trials using by applying random.choice()
        to the list of node numbers

        Updates the list of node numbers so that the number of instances of
        each node number is in the same ratio as the desired probabilities

        Returns:
        Set of nodes
        """

        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for dummy_idx in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))

        # update the list of node numbers so that each node number
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))

        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors


def load_graph(path):
    """
    load the graph from file path
    :param path
    :return:a graph
    """
    graph = {}
    with open(path) as f:
        for line in f:
            graph[int(line.split()[0])] = set(map(int, line.strip().split()[1:]))
    return graph

def question1():
    graph = in_degree_distribution(load_graph('alg_phys-cite.txt'))
    del graph[0]
    plot(graph)


def plot(graph):
    total = sum(graph.values())
    X, Y = [], []
    for k,v in graph.iteritems():
        X.append(k)
        Y.append(float(v)/total)
    plt.loglog(X, Y, 'ro')
    plt.grid(True)
    plt.title('log/log plot of in-degree distribution')
    plt.xlabel('in-degree')
    plt.ylabel('count')
    plt.show()

def generate_DPA(m, n):
    graph = make_complete_graph(m)
    dpatrail = DPATrial(m)
    for i in xrange(m, n):
        graph[i] = dpatrail.run_trial(m)
    return graph

def question4():
    graph = in_degree_distribution(generate_DPA(12, 27770))
    del graph[0]
    plot(graph)




if __name__ == '__main__':
    # graph = load_graph('alg_phys-cite.txt')
    # print len(graph.keys()), sum(map(lambda x:len(x), graph.values()))/len(graph.keys())
    question4()