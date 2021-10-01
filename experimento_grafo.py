import networkx as nx
import matplotlib.pyplot as plt

G1 = nx.Graph()
G = nx.Graph()
G.add_node("jipa")
G.add_node("OPO")
G.add_node("MEDICE")

G.add_edge("jipa","OPO",weight=67)
G.add_edge("jipa","MEDICE",weight=25)

G1.add_node("jipa")
G1.add_node("OPO")
G1.add_edge("jipa","OPO",weight=67)

edges = G.edges()
edges = G1.edges()

pos = nx.spring_layout(G)
nx.draw(G,pos,node_color = 'green',with_labels=True)
nx.draw(G1,pos,with_labels=True)
edge_weight = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weight)

plt.show()