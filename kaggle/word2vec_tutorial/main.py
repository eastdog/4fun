#coding: utf-8
__author__ = 'Victor'

import pandas as pd

train = pd.read_csv("labeledTrainData.tsv", header=0, delimiter="\t", quoting=3)