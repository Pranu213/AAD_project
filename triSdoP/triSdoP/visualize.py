# import matplotlib.pyplot as plt
# import matplotlib.patches as mpatches
# from math import cos, sin, pi
# import random

# def visualize_graph(graph, title="Social Network Graph"):
#     """
#     Visualize the basic graph structure.
    
#     Args:
#         graph: Graph object
#         title: Title for the plot
#     """
#     nodes = graph.get_nodes()
#     if not nodes:
#         print("No nodes to visualize")
#         return
    
#     fig, ax = plt.subplots(figsize=(10, 10))
    
#     # Generate circular layout
#     pos = circular_layout(nodes)
    
#     # Draw edges
#     for node in nodes:
#         for neighbor in graph.get_neighbors(node):
#             if node < neighbor:  # Draw each edge only once
#                 x = [pos[node][0], pos[neighbor][0]]
#                 y = [pos[node][1], pos[neighbor][1]]
#                 ax.plot(x, y, 'gray', linewidth=1.5, alpha=0.6, zorder=1)
    
#     # Draw nodes
#     for node in nodes:
#         ax.scatter(pos[node][0], pos[node][1], s=800, c='lightblue', 
#                   edgecolors='darkblue', linewidth=2, zorder=2)
#         ax.text(pos[node][0], pos[node][1], node, ha='center', va='center',
#                fontsize=10, fontweight='bold', zorder=3)
    
#     ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
#     ax.axis('off')
#     ax.set_aspect('equal')
#     plt.tight_layout()
#     plt.show()

# def visualize_centrality(graph, deg_cent, close_cent, pr):
#     """
#     Visualize degree centrality, closeness centrality, and PageRank.
    
#     Args:
#         graph: Graph object
#         deg_cent: Dictionary of degree centrality scores
#         close_cent: Dictionary of closeness centrality scores
#         pr: Dictionary of PageRank scores
#     """
#     nodes = graph.get_nodes()
#     if not nodes:
#         print("No nodes to visualize")
#         return
    
#     fig, axes = plt.subplots(1, 3, figsize=(18, 6))
#     pos = circular_layout(nodes)
    
#     centralities = [
#         (deg_cent, "Degree Centrality", axes[0]),
#         (close_cent, "Closeness Centrality", axes[1]),
#         (pr, "PageRank", axes[2])
#     ]
    
#     for cent_dict, title, ax in centralities:
#         # Normalize sizes
#         max_val = max(cent_dict.values()) if cent_dict else 1
#         min_val = min(cent_dict.values()) if cent_dict else 0
        
#         # Draw edges
#         for node in nodes:
#             for neighbor in graph.get_neighbors(node):
#                 if node < neighbor:
#                     x = [pos[node][0], pos[neighbor][0]]
#                     y = [pos[node][1], pos[neighbor][1]]
#                     ax.plot(x, y, 'gray', linewidth=1, alpha=0.4, zorder=1)
        
#         # Draw nodes with size based on centrality
#         for node in nodes:
#             val = cent_dict.get(node, 0)
#             if max_val > min_val:
#                 normalized = (val - min_val) / (max_val - min_val)
#             else:
#                 normalized = 0.5
#             size = 300 + normalized * 1500
#             color_intensity = 0.2 + normalized * 0.8
            
#             ax.scatter(pos[node][0], pos[node][1], s=size, 
#                       c=[(1-color_intensity, 0.5, color_intensity)],
#                       edgecolors='darkblue', linewidth=2, zorder=2, alpha=0.8)
#             ax.text(pos[node][0], pos[node][1], node, ha='center', va='center',
#                    fontsize=9, fontweight='bold', zorder=3)
            
#             # Add score label
#             score_text = f"{val:.3f}" if isinstance(val, float) else str(val)
#             ax.text(pos[node][0], pos[node][1] - 0.15, score_text,
#                    ha='center', va='top', fontsize=7, style='italic', zorder=3)
        
#         ax.set_title(title, fontsize=14, fontweight='bold', pad=10)
#         ax.axis('off')
#         ax.set_aspect('equal')
    
#     plt.suptitle("Centrality Measures Comparison", fontsize=16, fontweight='bold', y=0.98)
#     plt.tight_layout()
#     plt.show()

# def visualize_communities(graph, communities):
#     """
#     Visualize community structure with different colors.
    
#     Args:
#         graph: Graph object
#         communities: Dictionary of communities
#     """
#     nodes = graph.get_nodes()
#     if not nodes:
#         print("No nodes to visualize")
#         return
    
#     fig, ax = plt.subplots(figsize=(12, 10))
#     pos = circular_layout(nodes)
    
#     # Assign colors to communities
#     colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', 
#               '#F7DC6F', '#BB8FCE', '#85C1E2', '#F8B739', '#52B788']
    
#     node_to_community = {}
#     community_colors = {}
    
#     for i, (comm_name, members) in enumerate(communities.items()):
#         color = colors[i % len(colors)]
#         community_colors[comm_name] = color
#         for member in members:
#             node_to_community[member] = (comm_name, color)
    
#     # Draw edges
#     for node in nodes:
#         for neighbor in graph.get_neighbors(node):
#             if node < neighbor:
#                 x = [pos[node][0], pos[neighbor][0]]
#                 y = [pos[node][1], pos[neighbor][1]]
                
#                 # Check if edge is within community or between communities
#                 node_comm = node_to_community.get(node, (None, 'gray'))[0]
#                 neighbor_comm = node_to_community.get(neighbor, (None, 'gray'))[0]
                
#                 if node_comm == neighbor_comm:
#                     ax.plot(x, y, color=node_to_community[node][1], 
#                            linewidth=2, alpha=0.6, zorder=1)
#                 else:
#                     ax.plot(x, y, 'gray', linewidth=1, alpha=0.3, 
#                            linestyle='--', zorder=1)
    
#     # Draw nodes
#     for node in nodes:
#         comm_name, color = node_to_community.get(node, ('Unknown', 'lightgray'))
#         ax.scatter(pos[node][0], pos[node][1], s=1000, c=color,
#                   edgecolors='darkblue', linewidth=2.5, zorder=2, alpha=0.9)
#         ax.text(pos[node][0], pos[node][1], node, ha='center', va='center',
#                fontsize=10, fontweight='bold', zorder=3)
    
#     # Create legend
#     legend_elements = [mpatches.Patch(facecolor=color, edgecolor='darkblue', 
#                                      label=comm_name, linewidth=1.5)
#                       for comm_name, color in community_colors.items()]
#     ax.legend(handles=legend_elements, loc='upper right', fontsize=10,
#              title='Communities', title_fontsize=12, framealpha=0.9)
    
#     ax.set_title("Community Detection (Label Propagation)", 
#                 fontsize=16, fontweight='bold', pad=20)
#     ax.axis('off')
#     ax.set_aspect('equal')
#     plt.tight_layout()
#     plt.show()

# def visualize_components(graph, components):
#     """
#     Visualize connected components.
    
#     Args:
#         graph: Graph object
#         components: Dictionary of connected components
#     """
#     nodes = graph.get_nodes()
#     if not nodes:
#         print("No nodes to visualize")
#         return
    
#     fig, ax = plt.subplots(figsize=(12, 10))
    
#     # Assign colors to components
#     colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
    
#     node_to_component = {}
#     component_colors = {}
    
#     for i, (comp_name, members) in enumerate(components.items()):
#         color = colors[i % len(colors)]
#         component_colors[comp_name] = color
#         for member in members:
#             node_to_component[member] = (comp_name, color)
    
#     # Create separate layouts for each component
#     pos = {}
#     comp_index = 0
#     for comp_name, members in components.items():
#         comp_pos = circular_layout(members, 
#                                    center_x=comp_index * 3, 
#                                    center_y=0, 
#                                    radius=1)
#         pos.update(comp_pos)
#         comp_index += 1
    
#     # Draw edges
#     for node in nodes:
#         for neighbor in graph.get_neighbors(node):
#             if node < neighbor:
#                 x = [pos[node][0], pos[neighbor][0]]
#                 y = [pos[node][1], pos[neighbor][1]]
#                 color = node_to_component.get(node, ('Unknown', 'gray'))[1]
#                 ax.plot(x, y, color=color, linewidth=2, alpha=0.6, zorder=1)
    
#     # Draw nodes
#     for node in nodes:
#         comp_name, color = node_to_component.get(node, ('Unknown', 'lightgray'))
#         ax.scatter(pos[node][0], pos[node][1], s=1000, c=color,
#                   edgecolors='darkblue', linewidth=2.5, zorder=2, alpha=0.9)
#         ax.text(pos[node][0], pos[node][1], node, ha='center', va='center',
#                fontsize=10, fontweight='bold', zorder=3)
    
#     # Create legend
#     legend_elements = [mpatches.Patch(facecolor=color, edgecolor='darkblue',
#                                      label=f"{comp_name} ({len(components[comp_name])} nodes)",
#                                      linewidth=1.5)
#                       for comp_name, color in component_colors.items()]
#     ax.legend(handles=legend_elements, loc='upper right', fontsize=10,
#              title='Connected Components', title_fontsize=12, framealpha=0.9)
    
#     ax.set_title("Connected Components (Union-Find)", 
#                 fontsize=16, fontweight='bold', pad=20)
#     ax.axis('off')
#     ax.set_aspect('equal')
#     plt.tight_layout()
#     plt.show()

# def visualize_recommendations(graph, target_node, recommendations):
#     """
#     Visualize friend recommendations for a specific node.
    
#     Args:
#         graph: Graph object
#         target_node: Node to show recommendations for
#         recommendations: List of (node, score) tuples
#     """
#     nodes = graph.get_nodes()
#     if not nodes:
#         print("No nodes to visualize")
#         return
    
#     fig, ax = plt.subplots(figsize=(12, 10))
#     pos = circular_layout(nodes)
    
#     # Get existing friends
#     existing_friends = set(graph.get_neighbors(target_node))
#     recommended_nodes = {node for node, score in recommendations}
    
#     # Draw edges
#     for node in nodes:
#         for neighbor in graph.get_neighbors(node):
#             if node < neighbor:
#                 x = [pos[node][0], pos[neighbor][0]]
#                 y = [pos[node][1], pos[neighbor][1]]
                
#                 # Highlight edges connected to target
#                 if target_node in (node, neighbor):
#                     ax.plot(x, y, 'green', linewidth=3, alpha=0.8, zorder=1)
#                 else:
#                     ax.plot(x, y, 'gray', linewidth=1, alpha=0.4, zorder=1)
    
#     # Draw potential recommendation edges (dashed)
#     for rec_node, score in recommendations[:5]:  # Top 5
#         x = [pos[target_node][0], pos[rec_node][0]]
#         y = [pos[target_node][1], pos[rec_node][1]]
#         ax.plot(x, y, 'red', linewidth=2, alpha=0.5, 
#                linestyle='--', zorder=1)
    
#     # Draw nodes
#     for node in nodes:
#         if node == target_node:
#             # Target node - large and highlighted
#             ax.scatter(pos[node][0], pos[node][1], s=1500, c='gold',
#                       edgecolors='darkred', linewidth=3, zorder=3, alpha=0.9)
#         elif node in existing_friends:
#             # Existing friends - green
#             ax.scatter(pos[node][0], pos[node][1], s=1000, c='lightgreen',
#                       edgecolors='darkgreen', linewidth=2, zorder=2, alpha=0.8)
#         elif node in recommended_nodes:
#             # Recommended friends - red/orange
#             ax.scatter(pos[node][0], pos[node][1], s=1000, c='salmon',
#                       edgecolors='darkred', linewidth=2, zorder=2, alpha=0.8)
#         else:
#             # Other nodes - gray
#             ax.scatter(pos[node][0], pos[node][1], s=800, c='lightgray',
#                       edgecolors='gray', linewidth=1.5, zorder=2, alpha=0.6)
        
#         ax.text(pos[node][0], pos[node][1], node, ha='center', va='center',
#                fontsize=9, fontweight='bold', zorder=4)
    
#     # Add recommendation scores as text
#     for i, (rec_node, score) in enumerate(recommendations[:5]):
#         ax.text(pos[rec_node][0], pos[rec_node][1] - 0.15, 
#                f"Score: {score:.2f}",
#                ha='center', va='top', fontsize=7, style='italic',
#                bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))
    
#     # Create legend
#     legend_elements = [
#         mpatches.Patch(facecolor='gold', edgecolor='darkred', 
#                       label='Target User', linewidth=2),
#         mpatches.Patch(facecolor='lightgreen', edgecolor='darkgreen',
#                       label='Current Friends', linewidth=2),
#         mpatches.Patch(facecolor='salmon', edgecolor='darkred',
#                       label='Recommended', linewidth=2),
#         mpatches.Patch(facecolor='lightgray', edgecolor='gray',
#                       label='Other Users', linewidth=1.5)
#     ]
#     ax.legend(handles=legend_elements, loc='upper right', fontsize=10,
#              title='Node Types', title_fontsize=12, framealpha=0.9)
    
#     ax.set_title(f"Friend Recommendations for {target_node}", 
#                 fontsize=16, fontweight='bold', pad=20)
#     ax.axis('off')
#     ax.set_aspect('equal')
#     plt.tight_layout()
#     plt.show()

# def circular_layout(nodes, center_x=0, center_y=0, radius=2):
#     """
#     Generate circular layout for nodes.
    
#     Args:
#         nodes: List of node names
#         center_x: X coordinate of center
#         center_y: Y coordinate of center
#         radius: Radius of circle
        
#     Returns:
#         Dictionary mapping nodes to (x, y) positions
#     """
#     pos = {}
#     n = len(nodes)
#     if n == 0:
#         return pos
    
#     if n == 1:
#         pos[nodes[0]] = (center_x, center_y)
#         return pos
    
#     angle_step = 2 * pi / n
#     for i, node in enumerate(sorted(nodes)):
#         angle = i * angle_step
#         x = center_x + radius * cos(angle)
#         y = center_y + radius * sin(angle)
#         pos[node] = (x, y)
    
#     return pos

# def visualize_all(graph, deg_cent, close_cent, pr, components, communities):
#     """
#     Create a comprehensive visualization with all analyses.
    
#     Args:
#         graph: Graph object
#         deg_cent: Degree centrality dictionary
#         close_cent: Closeness centrality dictionary
#         pr: PageRank dictionary
#         components: Connected components dictionary
#         communities: Communities dictionary
#     """
#     print("\n" + "="*60)
#     print(" GENERATING VISUALIZATIONS...")
#     print("="*60)
    
#     # 1. Basic graph
#     print("\n[1/5] Basic Graph Structure...")
#     visualize_graph(graph, "Social Network Graph - Input Structure")
    
#     # 2. Centrality measures
#     print("[2/5] Centrality Measures...")
#     visualize_centrality(graph, deg_cent, close_cent, pr)
    
#     # 3. Connected components
#     print("[3/5] Connected Components...")
#     visualize_components(graph, components)
    
#     # 4. Communities
#     print("[4/5] Community Detection...")
#     visualize_communities(graph, communities)
    
#     # 5. Sample recommendation (for first node)
#     print("[5/5] Friend Recommendations...")
#     nodes = graph.get_nodes()
#     if nodes:
#         from recommend import recommend_friends
#         sample_node = sorted(nodes)[0]
#         recs = recommend_friends(graph, sample_node)
#         visualize_recommendations(graph, sample_node, recs)
    
#     print("\n✓ All visualizations complete!")
#     print("="*60 + "\n")





import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from math import cos, sin, pi
import os

# ----------------------
# Circular layout helper
# ----------------------
def circular_layout(nodes, center_x=0, center_y=0, radius=2):
    pos = {}
    n = len(nodes)
    if n == 0:
        return pos
    if n == 1:
        pos[nodes[0]] = (center_x, center_y)
        return pos
    angle_step = 2 * pi / n
    for i, node in enumerate(sorted(nodes)):
        angle = i * angle_step
        x = center_x + radius * cos(angle)
        y = center_y + radius * sin(angle)
        pos[node] = (x, y)
    return pos

# ----------------------
# Graph visualization
# ----------------------
def visualize_graph(graph, title="Graph", folder="plots"):
    nodes = graph.get_nodes()
    if not nodes:
        return
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    fig, ax = plt.subplots(figsize=(8,8))
    pos = circular_layout(nodes)
    
    # Draw edges
    for u in nodes:
        for v in graph.get_neighbors(u):
            if u < v:
                ax.plot([pos[u][0], pos[v][0]], [pos[u][1], pos[v][1]],
                        'gray', alpha=0.6)
    
    # Draw nodes
    for u in nodes:
        ax.scatter(pos[u][0], pos[u][1], s=600, c='lightblue',
                   edgecolors='darkblue', linewidth=2)
        ax.text(pos[u][0], pos[u][1], u, ha='center', va='center', fontsize=9)
    
    ax.set_title(title)
    ax.axis('off')
    plt.savefig(f"{folder}/graph.png")
    plt.close()

# ----------------------
# Centrality visualization
# ----------------------
def visualize_centrality(graph, deg_cent, close_cent, pr, folder="plots"):
    nodes = graph.get_nodes()
    if not nodes:
        return
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    fig, axes = plt.subplots(1,3,figsize=(18,6))
    pos = circular_layout(nodes)
    
    cent_list = [(deg_cent,"Degree Centrality",axes[0]),
                 (close_cent,"Closeness Centrality",axes[1]),
                 (pr,"PageRank",axes[2])]
    
    for cent_dict, title, ax in cent_list:
        max_val = max(cent_dict.values()) if cent_dict else 1
        min_val = min(cent_dict.values()) if cent_dict else 0
        for u in nodes:
            for v in graph.get_neighbors(u):
                if u<v:
                    ax.plot([pos[u][0], pos[v][0]], [pos[u][1], pos[v][1]], 'gray', alpha=0.3)
        for u in nodes:
            val = cent_dict.get(u,0)
            normalized = (val-min_val)/(max_val-min_val) if max_val>min_val else 0.5
            size = 300 + normalized*1500
            color_intensity = 0.2 + normalized*0.8
            ax.scatter(pos[u][0], pos[u][1], s=size,
                       c=[(1-color_intensity,0.5,color_intensity)],
                       edgecolors='darkblue', linewidth=2, alpha=0.8)
            ax.text(pos[u][0], pos[u][1], u, ha='center', va='center', fontsize=8)
            score_text = f"{val:.3f}" if isinstance(val,float) else str(val)
            ax.text(pos[u][0], pos[u][1]-0.15, score_text, ha='center', va='top', fontsize=7)
        ax.set_title(title)
        ax.axis('off')
    
    plt.suptitle("Centrality Measures", fontsize=16)
    plt.tight_layout()
    plt.savefig(f"{folder}/centrality.png")
    plt.close()

# ----------------------
# Communities visualization
# ----------------------
def visualize_communities(graph, communities, folder="plots"):
    nodes = graph.get_nodes()
    if not nodes:
        return
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    fig, ax = plt.subplots(figsize=(10,10))
    pos = circular_layout(nodes)
    
    colors = ['#FF6B6B','#4ECDC4','#45B7D1','#FFA07A','#98D8C8','#F7DC6F','#BB8FCE','#85C1E2','#F8B739','#52B788']
    
    node_to_comm = {}
    comm_colors = {}
    for i,(comm_name,members) in enumerate(communities.items()):
        color = colors[i % len(colors)]
        comm_colors[comm_name] = color
        for m in members:
            node_to_comm[m] = (comm_name,color)
    
    for u in nodes:
        for v in graph.get_neighbors(u):
            if u<v:
                u_comm = node_to_comm.get(u,('Unknown','gray'))[0]
                v_comm = node_to_comm.get(v,('Unknown','gray'))[0]
                if u_comm==v_comm:
                    ax.plot([pos[u][0],pos[v][0]],[pos[u][1],pos[v][1]],color=node_to_comm[u][1], alpha=0.6)
                else:
                    ax.plot([pos[u][0],pos[v][0]],[pos[u][1],pos[v][1]],'gray', alpha=0.3, linestyle='--')
    
    for u in nodes:
        comm_name,color = node_to_comm.get(u,('Unknown','lightgray'))
        ax.scatter(pos[u][0], pos[u][1], s=800, c=color, edgecolors='darkblue', linewidth=2)
        ax.text(pos[u][0], pos[u][1], u, ha='center', va='center', fontsize=9)
    
    legend_elements = [mpatches.Patch(facecolor=color, edgecolor='darkblue', label=comm, linewidth=1.5)
                       for comm,color in comm_colors.items()]
    ax.legend(handles=legend_elements, loc='upper right', fontsize=9, title='Communities')
    ax.set_title("Communities")
    ax.axis('off')
    plt.savefig(f"{folder}/communities.png")
    plt.close()

# ----------------------
# Connected components
# ----------------------
def visualize_components(graph, components, folder="plots"):
    nodes = graph.get_nodes()
    if not nodes:
        return
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    fig, ax = plt.subplots(figsize=(10,10))
    
    colors = ['#FF6B6B','#4ECDC4','#45B7D1','#FFA07A','#98D8C8']
    node_to_comp = {}
    comp_colors = {}
    
    for i,(comp_name,members) in enumerate(components.items()):
        color = colors[i%len(colors)]
        comp_colors[comp_name] = color
        for m in members:
            node_to_comp[m] = (comp_name,color)
    
    pos = {}
    for idx,(comp_name,members) in enumerate(components.items()):
        comp_pos = circular_layout(members, center_x=idx*3, radius=1)
        pos.update(comp_pos)
    
    for u in nodes:
        for v in graph.get_neighbors(u):
            if u<v:
                color = node_to_comp.get(u,('Unknown','gray'))[1]
                ax.plot([pos[u][0],pos[v][0]],[pos[u][1],pos[v][1]],color=color, alpha=0.6)
    
    for u in nodes:
        comp_name,color = node_to_comp.get(u,('Unknown','lightgray'))
        ax.scatter(pos[u][0], pos[u][1], s=800, c=color, edgecolors='darkblue', linewidth=2)
        ax.text(pos[u][0], pos[u][1], u, ha='center', va='center', fontsize=9)
    
    legend_elements = [mpatches.Patch(facecolor=color, edgecolor='darkblue', label=f"{comp_name} ({len(components[comp_name])} nodes)")
                       for comp_name,color in comp_colors.items()]
    ax.legend(handles=legend_elements, loc='upper right', fontsize=9, title='Components')
    ax.set_title("Connected Components")
    ax.axis('off')
    plt.savefig(f"{folder}/components.png")
    plt.close()

# ----------------------
# Friend recommendations
# ----------------------
def visualize_recommendations(graph, target_node, recommendations, folder="plots"):
    nodes = graph.get_nodes()
    if not nodes:
        return
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    fig, ax = plt.subplots(figsize=(10,10))
    pos = circular_layout(nodes)
    
    existing_friends = set(graph.get_neighbors(target_node))
    recommended_nodes = {node for node, score in recommendations}
    
    for u in nodes:
        for v in graph.get_neighbors(u):
            if u<v:
                color = 'green' if target_node in (u,v) else 'gray'
                ax.plot([pos[u][0],pos[v][0]],[pos[u][1],pos[v][1]],color=color, alpha=0.6)
    
    for u in nodes:
        if u==target_node:
            ax.scatter(pos[u][0],pos[u][1],s=1200,c='gold',edgecolors='darkred',linewidth=2)
        elif u in existing_friends:
            ax.scatter(pos[u][0],pos[u][1],s=800,c='lightgreen',edgecolors='darkgreen',linewidth=2)
        elif u in recommended_nodes:
            ax.scatter(pos[u][0],pos[u][1],s=800,c='salmon',edgecolors='darkred',linewidth=2)
        else:
            ax.scatter(pos[u][0],pos[u][1],s=600,c='lightgray',edgecolors='gray',linewidth=1.5)
        ax.text(pos[u][0], pos[u][1], u, ha='center', va='center', fontsize=9)
    
    for rec_node, score in recommendations[:5]:
        ax.text(pos[rec_node][0], pos[rec_node][1]-0.15, f"{score:.2f}",
                ha='center', va='top', fontsize=7)
    
    legend_elements = [
        mpatches.Patch(facecolor='gold', edgecolor='darkred', label='Target'),
        mpatches.Patch(facecolor='lightgreen', edgecolor='darkgreen', label='Current Friends'),
        mpatches.Patch(facecolor='salmon', edgecolor='darkred', label='Recommended'),
        mpatches.Patch(facecolor='lightgray', edgecolor='gray', label='Other Users')
    ]
    ax.legend(handles=legend_elements, loc='upper right', fontsize=9)
    ax.set_title(f"Friend Recommendations for {target_node}")
    ax.axis('off')
    plt.savefig(f"{folder}/recommendations_{target_node}.png")
    plt.close()

# ----------------------
# Full visualization
# ----------------------
def visualize_all(graph, deg_cent, close_cent, pr, components, communities, folder="plots"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    visualize_graph(graph, "Social Network Graph", folder)
    visualize_centrality(graph, deg_cent, close_cent, pr, folder)
    visualize_components(graph, components, folder)
    visualize_communities(graph, communities, folder)
    nodes = graph.get_nodes()
    if nodes:
        from recommend import recommend_friends
        sample_node = sorted(nodes)[0]
        recs = recommend_friends(graph, sample_node)
        visualize_recommendations(graph, sample_node, recs, folder)
