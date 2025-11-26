# How many airports are connected globally?

## Total airports (nodes): 3214
## Airports in the giant connected component: 3188
## Fraction connected: 0.9919 → ~99.2%

Almost all airports in the dataset are globally connected through the air route network.
About 99.2% of airports belong to a single giant connected component, meaning we can reach nearly any airport from any other with only a few intermediate connections.

This indicates a highly integrated global air transportation system, with only a very small number of isolated or peripheral airports.





# Is the network dominated by a few hubs?

## the degree distribution plot shows:

A very steep drop-off: most airports have low degree.

A few airports have extremely high degree (reaching over 400–500 connections).

Yes, the network is clearly hub-dominated.
A small number of major airports (global hubs like London Heathrow, Frankfurt, Dubai, Istanbul, etc.) hold a very large fraction of the global connectivity, while most airports have only a few direct connections.

This confirms a hub-and-spoke structure, which is typical for airline networks due to efficiency and cost optimization.




# Does it show scale-free properties?

## From tje log-log degree distribution:

The distribution forms an approximate straight-line in log-log scale.

There is a long tail of rare, very high-degree nodes.

so yes — the network shows strong evidence of scale-free behavior.

The log-log plot suggests that the degree distribution approximately follows a power-law form, where:

Most nodes have small degrees, and a few nodes have extremely large degrees.




# How dense or sparse is it?

## The network is extremely sparse.

Even though there are tens of thousands of flight routes, only 0.36% of all possible connections between airports actually exist.

This is inevitable due to geography and economic constraints — we simply don’t have flights between every pair of airports.





# Is global air travel highly centralized or decentralized?

## Average degree: 23.12
## Average path length: 3.96
## Presence of extreme hubs
## Strong hub domination + scale-free structure

so global air travel is highly centralized, not decentralized.

Despite the network being sparse, its average path length is only ~3.96, meaning we can get almost anywhere with about 4 flights.

This is only possible because central hubs act as connectors between distant regions.

If hubs were removed, global connectivity would collapse significantly.

So the system relies heavily on central airports — indicating structural centralization.
