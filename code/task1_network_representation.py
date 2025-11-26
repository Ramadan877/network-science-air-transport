import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import os
import pickle

# ================================
# Directory Setup
# ================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "..", "data")
RESULTS_DIR = os.path.join(BASE_DIR, "..", "results")
GRAPHS_DIR = os.path.join(BASE_DIR, "..", "graphs")

os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(GRAPHS_DIR, exist_ok=True)

# ================================
# Load Dataset
# ================================

df = pd.read_csv(os.path.join(DATA_DIR, "combined_routes_dataset.csv"))

print("Dataset loaded successfully.")
print("Rows:", len(df))
print(df.head())

# ================================
# Build Directed Graph
# ================================

G = nx.DiGraph()

for _, row in df.iterrows():
    G.add_edge(
        row["Source_ID"],
        row["Dest_ID"],
        airline=row["Airline_Name"],
        equipment=row["Equipment"],
        source_country=row["Source_Country"],
        dest_country=row["Dest_Country"]
    )

print("Graph created!")
print("Nodes:", G.number_of_nodes())
print("Edges:", G.number_of_edges())

# ================================
# Add Node Attributes
# ================================

for _, row in df.iterrows():
    G.nodes[row["Source_ID"]]["airport_name"] = row["Source_Name"]
    G.nodes[row["Source_ID"]]["city"] = row["Source_City"]
    G.nodes[row["Source_ID"]]["country"] = row["Source_Country"]

    G.nodes[row["Dest_ID"]]["airport_name"] = row["Dest_Name"]
    G.nodes[row["Dest_ID"]]["city"] = row["Dest_City"]
    G.nodes[row["Dest_ID"]]["country"] = row["Dest_Country"]

# ================================
# Largest Connected Component
# ================================

wcc = list(nx.weakly_connected_components(G))
largest_cc = max(wcc, key=len)
G_lcc = G.subgraph(largest_cc).copy()

print("Largest connected component size:", len(G_lcc))
print("Fraction of total:", len(G_lcc) / G.number_of_nodes())

# ================================
# Core Network Metrics
# ================================

num_nodes = G_lcc.number_of_nodes()
num_edges = G_lcc.number_of_edges()
density = nx.density(G_lcc)
avg_degree = sum(dict(G_lcc.degree()).values()) / num_nodes
num_strong = nx.number_strongly_connected_components(G_lcc)
num_weak = nx.number_weakly_connected_components(G_lcc)

print("===== Network Summary =====")
print("Nodes:", num_nodes)
print("Edges:", num_edges)
print("Density:", density)
print("Average degree:", avg_degree)
print("Strong components:", num_strong)
print("Weak components:", num_weak)

# ================================
# Degree Distribution Plots
# ================================

degrees = [G_lcc.degree(n) for n in G_lcc.nodes()]

# Linear histogram
plt.figure(figsize=(8, 6))
plt.hist(degrees, bins=100)
plt.xlabel("Degree")
plt.ylabel("Number of Airports")
plt.title("Degree Distribution of Global Airline Network")
plt.savefig(os.path.join(RESULTS_DIR, "degree_distribution.png"))
plt.show()

# Log–log histogram
plt.figure(figsize=(8, 6))
plt.hist(degrees, bins=100)
plt.yscale("log")
plt.xscale("log")
plt.xlabel("Degree (log)")
plt.ylabel("Frequency (log)")
plt.title("Log-Log Degree Distribution")
plt.savefig(os.path.join(RESULTS_DIR, "degree_loglog.png"))
plt.show()

# ================================
# Average Shortest Path Length
# ================================

try:
    avg_path = nx.average_shortest_path_length(G_lcc.to_undirected())
    print("Average shortest path length:", avg_path)
except:
    avg_path = "Not computed (graph too large)"
    print("Graph too big, use sampling if needed.")

# ================================
# Save Graph Objects
# ================================

nx.write_gexf(G_lcc, os.path.join(GRAPHS_DIR, "global_airline_LCC.gexf"))

with open(os.path.join(GRAPHS_DIR, "global_airline_LCC.pkl"), "wb") as f:
    pickle.dump(G_lcc, f)

# ================================
# Save Summary Results
# ================================

results_file = os.path.join(RESULTS_DIR, "network_summary.txt")

with open(results_file, "w") as f:
    f.write("===== Network Summary =====\n")
    f.write(f"Nodes: {num_nodes}\n")
    f.write(f"Edges: {num_edges}\n")
    f.write(f"Density: {density}\n")
    f.write(f"Average degree: {avg_degree}\n")
    f.write(f"Strong components: {num_strong}\n")
    f.write(f"Weak components: {num_weak}\n")
    f.write(f"Average shortest path length: {avg_path}\n")

print("✅ All results and graphs saved correctly!")


