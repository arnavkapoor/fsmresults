import os
from functools import reduce

# reads the name of the benchmark from the top of the data file
def getbmrkname(datafile):
    with open(datafile) as f:
        bmrkname = f.readlines()[0]
    f.close()
    return bmrkname.strip()

# zips the items and returns a list of the sum of the two zips
def sumzip(*items):
    return [sum(values) for values in zip(*items)]

# returns all datafiles from a directory
def getdatafiles(directory):
    datafiles = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".data"):
                datafiles.append(os.path.join(root, file))
    return datafiles

#calculates geometric mean
def geomean(nums):
    return (reduce(lambda x, y: x*y, nums))**(1.0/len(nums))
