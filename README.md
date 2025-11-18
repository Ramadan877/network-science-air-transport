# Network Science Air Transport Project

Global airline network science project for TU Graz

## 📋 Project Overview

This project applies network science techniques to analyze the global air transport network. The analysis is divided into three main tasks:

1. **Task 1 - Network Representation**: Building and visualizing the air transport network
2. **Task 2 - Accessibility**: Analyzing the accessibility and connectivity of airports
3. **Task 3 - Community Detection**: Identifying communities and clusters in the network

## 🗂️ Repository Structure

```
network-science-air-transport/
│
├── src/                          # Source code for the project
│   ├── __init__.py
│   ├── network_representation.py # Task 1: Network building and properties
│   ├── accessibility.py          # Task 2: Accessibility analysis
│   └── community_detection.py    # Task 3: Community detection
│
├── data/                         # Data directory
│   ├── raw/                      # Raw data files
│   └── processed/                # Processed data files
│
├── notebooks/                    # Jupyter notebooks for analysis
│   ├── 01_network_representation.ipynb
│   ├── 02_accessibility.ipynb
│   └── 03_community_detection.ipynb
│
├── docs/                         # Documentation
├── tests/                        # Unit tests
│
├── requirements.txt              # Python dependencies
├── .gitignore                    # Git ignore file
└── README.md                     # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Ramadan877/network-science-air-transport.git
cd network-science-air-transport
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

1. Place your air transport data in the `data/raw/` directory

2. Run the Jupyter notebooks in order:
```bash
jupyter notebook
```

3. Open and execute the notebooks:
   - `01_network_representation.ipynb` - Build and analyze the network
   - `02_accessibility.ipynb` - Analyze accessibility metrics
   - `03_community_detection.ipynb` - Detect and analyze communities

## 📊 Project Tasks

### Task 1: Network Representation
- Load air transport network data (airports, routes, flights)
- Create graph representations
- Calculate basic network properties:
  - Number of nodes (airports) and edges (routes)
  - Degree distribution
  - Network density
  - Clustering coefficient
- Visualize the network structure

### Task 2: Accessibility
- Calculate centrality measures:
  - Degree centrality
  - Betweenness centrality
  - Closeness centrality
  - Eigenvector centrality
- Analyze shortest paths between airports
- Compute accessibility indices
- Identify key hubs and bottlenecks in the network

### Task 3: Community Detection
- Apply community detection algorithms (Louvain, etc.)
- Analyze community structure and properties
- Visualize communities
- Interpret findings:
  - Regional clusters
  - Airline alliances
  - Hub systems

## 🔧 Dependencies

Key libraries used in this project:
- `networkx` - Network analysis
- `numpy` - Numerical computing
- `pandas` - Data manipulation
- `matplotlib` - Visualization
- `seaborn` - Statistical visualization
- `python-louvain` - Community detection
- `jupyter` - Interactive notebooks

See `requirements.txt` for complete list with versions.

## 📝 Contributing

This is an academic project. If you'd like to contribute or have suggestions, please open an issue or submit a pull request.

## 📄 License

This project is part of coursework at TU Graz.

## 👥 Authors

- Project Team at TU Graz

## 🙏 Acknowledgments

- TU Graz Network Science Course
- OpenFlights database (potential data source)
- NetworkX community
