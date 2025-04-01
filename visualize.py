import json
import networkx as nx
import matplotlib.pyplot as plt

# Load JSON-LD
with open("graph.jsonld", "r") as file:
    data = json.load(file)

# Create a directed graph
G = nx.DiGraph()

# Parse JSON-LD and add nodes & edges
for item in data["@graph"]:
    node_id = item["@id"]
    G.add_node(node_id)  # Add nodes

    if "relatedTo" in item:
        for related in item["relatedTo"]:
            G.add_edge(node_id, related)  # Add edges

# Draw the graph
plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G)  # Position nodes using force-directed algorithm
nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=3000, font_size=9)

plt.title("JSON-LD Knowledge Graph Visualization")
plt.show()
