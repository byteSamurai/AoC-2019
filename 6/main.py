#!/usr/bin/python3.7
from typing import Dict

from anytree import Node

nodeMap: Dict[Node, Node] = {}

lines = [line.rstrip('\n') for line in open('input.txt')]
for line in lines:
    ref, orbiter = line.split(')')

    if ref not in nodeMap:
        nodeMap[ref] = Node(ref)

    if orbiter not in nodeMap:
        nodeMap[orbiter] = Node(orbiter, parent=nodeMap[ref])

    if orbiter in nodeMap and ref in nodeMap:
        nodeMap[orbiter].parent = nodeMap[ref]

# manual debugging :)
# from anytree.exporter import DotExporter
# DotExporter(nodeMap['COM']).to_picture("graph.png")

count = 0
for node in nodeMap.values():
    count += node.depth

# Total number or orbits
print("Total number of orbits: " + str(count))

san = nodeMap['SAN'].parent.path
you = nodeMap['YOU'].parent.path

differ = []
for path in [san, you]:
    for e in path:
        if e in san and e in you:
            continue
        else:
            differ.append(e)

# 1 node is missing, but the starting point does not count anyway
print("Orbital distance between Santa and you: " + str(len(set(differ))))
