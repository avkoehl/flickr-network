import networkx as nx

## OBJECTS: file and graph
f = open ("flickr_matches_and_cluster_10_2017.csv", "r")
G = nx.Graph()

## MAIN: read in adjacency list and write as GEXF format

# add edges to graph
for line in f:
    line = line.rstrip()
    elements = line.split(',')
    source = elements[0]
    targets = elements[3:]
    c = elements[1]
    G.add_node(source, cluster=c)
    for t in targets:
        exploded = t.split(' ')
        G.add_edge(source, exploded[0], weight=exploded[1])

# write in GEXF format
nx.write_gexf(G, "flickr_10_2017.gexf")



