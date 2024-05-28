import pandas as pd
import networkx as nx
from pyvis.network import Network
from IPython.display import display, HTML
import dash
import dash_core_components as dcc
import dash_html_components as html

def generate_network(data):
    # Replace NaN values with "Home"
    data = data.fillna("Home")

    # Extract information about visited pages
    visited_pages = data[['simulated_detailed_event', 'simulated_subject']].drop_duplicates()

    # Extract visits that led to account creation
    account_creation_visits = data[data['Account_Created_journey'] == 1]

    # Create a network graph
    G = nx.DiGraph()

    # Add nodes for visited pages
    for _, row in visited_pages.iterrows():
        G.add_node(row['simulated_detailed_event'], node_type='page')
        G.add_node(row['simulated_subject'], node_type='subject')
        G.add_edge(row['simulated_subject'], row['simulated_detailed_event'], edge_type='visit')

    # Add the "Account Creation" node and connect all links leading to it
    G.add_node('Account Creation', node_type='account_creation')
    for _, row in account_creation_visits.iterrows():
        G.add_edge(row['simulated_detailed_event'], 'Account Creation', edge_type='account_creation')

    # Create PyVis network
    nt = Network(height='800px', width='100%', notebook=True)

    # Add nodes with their attributes
    for node, node_type in G.nodes(data='node_type'):
        color = 'green' if node_type == 'account_creation' else 'lightblue'
        nt.add_node(node, label=node, color=color, shape='dot')

    # Add edges with their attributes
    for u, v, edge_type in G.edges(data='edge_type'):
        color = 'green' if edge_type == 'account_creation' else 'gray'
        width = 4 if edge_type == 'account_creation' else 1
        nt.add_edge(u, v, color=color, width=width)

    # Set options for the network visualization
    nt.set_options("""
    var options = {
    "nodes": {
        "size": 20,
        "font": {
        "size": 12,
        "color": "black"
        },
        "borderWidth": 2
    },
    "edges": {
        "font": {
        "size": 10,
        "color": "gray"
        }
    },
    "physics": {
        "stabilization": true,
        "forceAtlas2Based": {
        "gravitationalConstant": -50,
        "centralGravity": 0.01,
        "springLength": 200,
        "springConstant": 0.08
        },
        "minVelocity": 0.75
    }
    }
    """)

    # Add legend
    legend_html = '''
    <div class="legend" style="position: absolute; top: 10px; right: 10px; background-color: white; border: 1px solid #ccc; padding: 10px; font-family: Arial, sans-serif;">
        <h6>Legend</h6>
        <hr>
        
        <div>
            <svg height="15" width="15">
                <circle cx="8" cy="8" r="6" fill="lightblue" />
            </svg>
            Node section and action on the website
        </div>
        <div>
            <svg height="15" width="15">
                <circle cx="8" cy="8" r="6" fill="green" />
            </svg>
            Account Creation Node
        </div>
        <div>
            <svg height="10" width="100">
                <line x1="0" y1="8" x2="20" y2="8" style="stroke:gray;stroke-width:1" />
            </svg>
            Node Link
        </div>
        <div>
            <svg height="10" width="60">
                <line x1="0" y1="8" x2="20" y2="8" style="stroke:green;stroke-width:1" />
            </svg>
            Link to Account Creation
        </div>
        <div>
            <svg height="10" width="60">
                <line x1="0" y1="8" x2="20" y2="8" style="stroke:green;stroke-width:4" />
            </svg>
            Multiple Connections
        </div>
    </div>
    '''

    # Save the network visualization as HTML
    nt.save_graph('net.html')

    # Read the HTML file
    with open('net.html', 'r') as file:
        content = file.read()

    # Insert the legend HTML code into the content
    content = content.replace('</body>', legend_html + '</body>')
    return content
