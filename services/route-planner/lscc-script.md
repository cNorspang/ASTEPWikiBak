---
title: Largest Strongly Connected Component script
description: This page explains how SW601F20 found the LSCC of the graph from DB2/mapdata database.
published: true
date: 2020-08-27T07:28:25.222Z
tags: 
editor: undefined
---

# LSCC script

This page presents and explains the python script used to find the largest strongly connected component (LSCC) of the road network graph from [`DB2/mapdata`](/databases/DB2/mapdata) and to store this LSCC in the [`DB2/sw601f20_routing`](/databases/DB2/sw601f20_routing) database. The script is seen below (usernames and passwords have been censored).

The script uses the python library called `networkx` first to load the `mapdata` graph and then to find the LSCC of that graph. The library `psycopg2` is used to connect to the databases in question.

In the function calls `G.add_node(...)` and `G.add_edge(...)` we store not only the nodes' ID and the edges' start/end node IDs, but also all the data from the database related to that node/edge in a tuple (the `data=(...)` part). This is such that we can upload that data to `sw601f20_routing` later.

When the script inserts the LSCC nodes and edges into `sw601f20_routing` (lines 69 and 76), we build two queries that each insert all nodes and all edges. If done separately, the insert would take hours.

```python
import networkx as nx
import psycopg2
import datetime

print("Started:", datetime.datetime.now())
print()

# Make graph
G = nx.DiGraph()

# Get graph
conn = None
try:
    # connect to the PostgreSQL server
    print('Connecting to mapdata...')
    conn = psycopg2.connect("host=db2-astep.cs.aau.dk dbname=mapdata user=[username] password=[password]")
    cur = conn.cursor()

    # Load all nodes from DB2/mapdata
    print("Getting nodes...")
    cur.execute('SELECT * FROM node')
    print("Loading nodes...")
    row = cur.fetchone()
    while row is not None:
        G.add_node(int(row[0]), data=(row[0],row[1],row[2]))
        row = cur.fetchone()
    print("Nodes loaded!")

    # Load all edges from DB2/mapdata
    print("Getting edges...")
    cur.execute('SELECT * FROM edge')
    print("Loading edges...")
    row = cur.fetchone()
    while row is not None:
        G.add_edge(int(row[1]), int(row[6]), data=(row[0],row[1],row[2],row[3].replace('\'', '\'\''),row[4],row[5],row[6]))
        row = cur.fetchone()
    print("Nodes and edges loaded!")

    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print('Database connection to mapdata closed.')
        print()

print("Loaded:", datetime.datetime.now())
print()

# Get largest strongly connected component
print("Full graph (n, e):", G.number_of_nodes(), ",", G.number_of_edges())
component = max(nx.strongly_connected_components(G), key=len)
G2 = G.subgraph(component)
print("Largest component (n, e):", G2.number_of_nodes(), ",", G2.number_of_edges())
print()

print("Prepared:", datetime.datetime.now())
print()
        
# Upload largest strongly connected component
conn = None
try:
    print("Connecting to routing...")
    conn = psycopg2.connect("host=db2-astep.cs.aau.dk dbname=sw601f20_routing user=sean password=seanPasswordLol")
    cur = conn.cursor()

    # Insert LSCC nodes into sw601f20_routing
    print("Inserting nodes...")
    query1 = ",".join(['{}'.format(a) for (u, a) in G2.nodes.data('data')])
    cur.execute("INSERT INTO node VALUES {};".format(query1))
    conn.commit()
    print("Inserting nodes done!")

    # Insert LSCC edges into sw601f20_routing
    print("Inserting edges...")
    query2 = ",".join(['{}'.format(a).replace('\"', '\'') for (u, v, a) in G2.edges.data('data')])
    cur.execute("INSERT INTO edge VALUES {};".format(query2))
    conn.commit()
    print("Inserting edges done!")
    
    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print('Database connection to routing closed.')
        print()

print("Finished:", datetime.datetime.now())


```
