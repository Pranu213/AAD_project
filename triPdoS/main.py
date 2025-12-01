# import argparse
# from graph import Graph
# from centrality import degree_centrality, closeness_centrality
# from pagerank import pagerank
# from community import label_propagation
# from recommend import recommend_friends
# from visualize import visualize_all, visualize_graph, visualize_centrality, visualize_communities, visualize_components, visualize_recommendations

# def main(argv=None):
#     parser = argparse.ArgumentParser(description="Social Network Analysis System")
#     parser.add_argument('-v', '--visualize', action='store_true',
#                         help='Automatically show all visualizations after analysis')
#     args = parser.parse_args(argv)

#     auto_visualize = args.visualize

    
    
    
#     def _prompt_visualize_choice():
#         return input("Do you want to see visualizations? (yes/no): ").strip().lower()

    
    
    
#     print("\n" + "="*60)
#     print(" SOCIAL NETWORK ANALYSIS SYSTEM")
#     print("="*60)
    
#     print("\n=== GRAPH INPUT ===")
    
#     # Number of nodes
#     try:
#         n = int(input("Enter number of nodes: "))
#         if n <= 0:
#             print("Error: Number of nodes must be positive")
#             return
#     except ValueError:
#         print("Error: Please enter a valid integer")
#         return
    
#     graph = Graph()
    
#     # Add nodes
#     print(f"\nEnter {n} node names:")
#     nodes = []
#     for i in range(n):
#         name = input(f"Node {i+1}: ").strip()
#         if not name:
#             print("Error: Node name cannot be empty")
#             return
#         nodes.append(name)
#         graph.add_node(name)
    
#     # Number of edges
#     try:
#         m = int(input(f"\nEnter number of edges: "))
#         if m < 0:
#             print("Error: Number of edges cannot be negative")
#             return
#     except ValueError:
#         print("Error: Please enter a valid integer")
#         return
    
#     # Add edges
#     if m > 0:
#         print(f"\nEnter {m} edges (format: node1 node2):")
#         for i in range(m):
#             try:
#                 edge_input = input(f"Edge {i+1}: ").strip()
#                 parts = edge_input.split()
#                 if len(parts) != 2:
#                     print(f"Warning: Edge {i+1} skipped - invalid format")
#                     continue
#                 u, v = parts[0], parts[1]
#                 if u not in nodes or v not in nodes:
#                     print(f"Warning: Edge {i+1} skipped - unknown node")
#                     continue
#                 graph.add_edge(u, v)
#             except Exception as e:
#                 print(f"Warning: Edge {i+1} skipped - {e}")
#                 continue
    
#     # ----------------------------------------------------
#     # COMPUTE ALL ANALYSES
#     # ----------------------------------------------------
    
#     print("\n" + "="*60)
#     print(" COMPUTING ANALYSIS...")
#     print("="*60)
    
#     components = graph.connected_components()
#     deg_cent = degree_centrality(graph)
#     close_cent = closeness_centrality(graph)
#     pr = pagerank(graph)
#     communities = label_propagation(graph)
    
#     # ----------------------------------------------------
#     # TEXT OUTPUTS
#     # ----------------------------------------------------
    
#     print("\n" + "="*60)
#     print(" ANALYSIS RESULTS")
#     print("="*60)
    
#     print("\n=== ADJACENCY LIST ===")
#     graph.print_graph()
    
#     print("\n=== NEIGHBORS OF ALL NODES ===")
#     for node in sorted(graph.adj_list.keys()):
#         neighbors = graph.get_neighbors(node)
#         neighbor_str = ', '.join(neighbors) if neighbors else 'None'
#         print(f"{node} → {neighbor_str}")
    
#     print("\n=== CONNECTED COMPONENTS (Union-Find) ===")
#     for comp_name, members in components.items():
#         print(f"{comp_name}: {{{', '.join(members)}}}")
    
#     print("\n=== DEGREE CENTRALITY ===")
#     for node, centrality in deg_cent.items():
#         print(f"{node}: {centrality}")
    
#     print("\n=== CLOSENESS CENTRALITY ===")
#     for node, centrality in close_cent.items():
#         print(f"{node}: {centrality}")
    
#     print("\n=== PAGERANK ===")
#     for node, rank in pr.items():
#         print(f"{node}: {rank}")
    
#     print("\n=== COMMUNITIES (Label Propagation) ===")
#     for comm_name, members in communities.items():
#         print(f"{comm_name}: {{{', '.join(members)}}}")
    
#     print("\n=== FRIEND RECOMMENDATIONS FOR ALL NODES ===")
#     for node in sorted(graph.adj_list.keys()):
#         recs = recommend_friends(graph, node, top_k=5)
#         if recs:
#             formatted = [f"{n} (score: {score})" for n, score in recs]
#             print(f"\n{node}:")
#             for rec in formatted:
#                 print(f"  → {rec}")
#         else:
#             print(f"\n{node}:")
#             print(f"  → No recommendations available")
    
#     print("\n" + "="*60)
#     print(" TEXT ANALYSIS COMPLETE")
#     print("="*60 + "\n")
    
#     # ----------------------------------------------------
#     # VISUALIZATION
#     # ----------------------------------------------------
    
#     # If user passed --visualize, skip prompting and show all visualizations
#     if auto_visualize:
#         visualize_all(graph, deg_cent, close_cent, pr, components, communities)
#     else:
#         visualize_choice = _prompt_visualize_choice()
#         if visualize_choice in ['yes', 'y']:
#             print("\nVisualization Options:")
#             print("1. All visualizations (recommended)")
#             print("2. Basic graph only")
#             print("3. Centrality measures only")
#             print("4. Communities only")
#             print("5. Connected components only")
#             print("6. Friend recommendations (for a specific node)")
#             print("7. Custom selection")
            
#             choice = input("\nEnter your choice (1-7): ").strip()
            
#             if choice == '1':
#                 visualize_all(graph, deg_cent, close_cent, pr, components, communities)
            
#             elif choice == '2':
#                 visualize_graph(graph, "Social Network Graph")
            
#             elif choice == '3':
#                 visualize_centrality(graph, deg_cent, close_cent, pr)
            
#             elif choice == '4':
#                 visualize_communities(graph, communities)
            
#             elif choice == '5':
#                 visualize_components(graph, components)
            
#             elif choice == '6':
#                 target = input("Enter node name for recommendations: ").strip()
#                 if target in graph.get_nodes():
#                     recs = recommend_friends(graph, target)
#                     visualize_recommendations(graph, target, recs)
#                 else:
#                     print(f"Error: Node '{target}' not found in graph")
            
#             elif choice == '7':
#                 print("\nSelect visualizations to show (enter numbers separated by spaces):")
#                 print("1=Graph, 2=Centrality, 3=Communities, 4=Components, 5=Recommendations")
#                 selections = input("Your selection: ").strip().split()
                
#                 for sel in selections:
#                     if sel == '1':
#                         visualize_graph(graph, "Social Network Graph")
#                     elif sel == '2':
#                         visualize_centrality(graph, deg_cent, close_cent, pr)
#                     elif sel == '3':
#                         visualize_communities(graph, communities)
#                     elif sel == '4':
#                         visualize_components(graph, components)
#                     elif sel == '5':
#                         target = input("Enter node name for recommendations: ").strip()
#                         if target in graph.get_nodes():
#                             recs = recommend_friends(graph, target)
#                             visualize_recommendations(graph, target, recs)
            
#             else:
#                 print("Invalid choice. Skipping visualizations.")
    
#     print("\n" + "="*60)
#     print(" ALL DONE! Thank you for using the system.")
#     print("="*60 + "\n")

# if __name__ == "__main__":
#     main()







# from final.graph import Graph
# from final.centrality import degree_centrality, closeness_centrality
# from final.pagerank import pagerank
# from final.community import label_propagation
# from final.recommend import recommend_friends
# from final.visualize import (
#     visualize_all, visualize_graph, visualize_centrality,
#     visualize_communities, visualize_components, visualize_recommendations
# )

import argparse
import shlex
import os
from graph import Graph
from centrality import degree_centrality, closeness_centrality
from pagerank import pagerank
from community import label_propagation
from recommend import recommend_friends
from visualize import (
    visualize_all, visualize_graph, visualize_centrality,
    visualize_communities, visualize_components, visualize_recommendations
)

PLOTS_FOLDER = "plots"

def safe_call_plot(func, *args, **kwargs):
    """Call a visualize function, catch errors and report saved files in PLOTS_FOLDER."""
    try:
        func(*args, **kwargs)
        # list files created/updated in the plots folder
        if os.path.exists(PLOTS_FOLDER):
            files = sorted(os.listdir(PLOTS_FOLDER))
            print(f"[visualize] Saved files in {PLOTS_FOLDER}:")
            for f in files:
                print("  -", f)
        else:
            print(f"[visualize] No files found in {PLOTS_FOLDER}.")
    except Exception as e:
        print(f"[visualize] ERROR running {func.__name__}: {e}")

def main(argv=None):
    parser = argparse.ArgumentParser(description="Social Network Analysis System (debug build)")
    parser.add_argument('-v', '--visualize', action='store_true',
                        help='Automatically show all visualizations after analysis')
    args = parser.parse_args(argv)
    auto_visualize = args.visualize

    def _prompt_visualize_choice():
        return input("Do you want to see visualizations? (yes/no): ").strip().lower()

    print("\n" + "="*60)
    print(" SOCIAL NETWORK ANALYSIS SYSTEM (DEBUG)")
    print("="*60)

    print("\n=== GRAPH INPUT ===")

    # Number of nodes
    try:
        n = int(input("Enter number of nodes: "))
        if n <= 0:
            print("Error: Number of nodes must be positive")
            return
    except ValueError:
        print("Error: Please enter a valid integer")
        return

    graph = Graph()

    # Add nodes
    print(f"\nEnter {n} node names (multi-word allowed). Type exactly how you'll reference them later.")
    nodes = []
    for i in range(n):
        name = input(f"Node {i+1}: ").strip()
        if not name:
            print("Error: Node name cannot be empty")
            return
        if name in nodes:
            print(f"Warning: Duplicate node name '{name}' - ignoring duplicate")
        else:
            nodes.append(name)
            graph.add_node(name)

    print("\nNodes entered (in order):")
    for idx, nm in enumerate(nodes, start=1):
        print(f"  {idx}. '{nm}'")

    # Number of edges
    try:
        m = int(input(f"\nEnter number of edges: "))
        if m < 0:
            print("Error: Number of edges cannot be negative")
            return
    except ValueError:
        print("Error: Please enter a valid integer")
        return

    # Add edges using shlex.split()
    added = 0
    skipped = 0
    if m > 0:
        print(f"\nEnter {m} edges (multi-word supported).")
        print("Format examples:")
        print("  single-word names: A B")
        print('  multi-word names: "John Doe" "Mary Ann"')
        print()
        for i in range(m):
            edge_input = input(f"Edge {i+1}: ").strip()
            try:
                parts = shlex.split(edge_input)
                if len(parts) != 2:
                    print(f"Warning: Edge {i+1} skipped - invalid format (got {len(parts)} tokens)")
                    skipped += 1
                    continue
                u, v = parts
                if u not in nodes or v not in nodes:
                    print(f"Warning: Edge {i+1} skipped - unknown node(s) (u='{u}' v='{v}')")
                    skipped += 1
                    continue
                graph.add_edge(u, v)
                added += 1
            except Exception as e:
                print(f"Warning: Edge {i+1} skipped - parse error: {e}")
                skipped += 1
                continue

    print(f"\nEdges processed: {m}  |  Added: {added}  |  Skipped: {skipped}")

    # Quick sanity: print adjacency counts
    print("\nAdjacency sizes (node: degree):")
    for node in sorted(graph.get_nodes()):
        print(f"  {node}: {len(graph.get_neighbors(node))} neighbors")

    # ----------------------------------------------------
    # RUN ANALYSIS
    # ----------------------------------------------------
    print("\n" + "="*60)
    print(" COMPUTING ANALYSIS...")
    print("="*60)

    components = graph.connected_components()
    deg_cent = degree_centrality(graph)
    close_cent = closeness_centrality(graph)
    pr = pagerank(graph)
    communities = label_propagation(graph)

    # ----------------------------------------------------
    # TEXT RESULTS
    # ----------------------------------------------------
    print("\n" + "="*60)
    print(" ANALYSIS RESULTS")
    print("="*60)

    print("\n=== ADJACENCY LIST ===")
    graph.print_graph()

    print("\n=== NEIGHBORS OF ALL NODES ===")
    for node in sorted(graph.adj_list.keys()):
        neighbors = graph.get_neighbors(node)
        neighbor_str = ', '.join(neighbors) if neighbors else 'None'
        print(f"{node} → {neighbor_str}")

    print("\n=== CONNECTED COMPONENTS (Union-Find) ===")
    for comp_name, members in components.items():
        print(f"{comp_name}: {{{', '.join(members)}}}")

    print("\n=== DEGREE CENTRALITY ===")
    for node, score in deg_cent.items():
        print(f"{node}: {score}")

    print("\n=== CLOSENESS CENTRALITY ===")
    for node, score in close_cent.items():
        print(f"{node}: {score}")

    print("\n=== PAGERANK ===")
    for node, score in pr.items():
        print(f"{node}: {score}")

    print("\n=== COMMUNITIES (Label Propagation) ===")
    for comm_name, members in communities.items():
        print(f"{comm_name}: {{{', '.join(members)}}}")

    print("\n=== FRIEND RECOMMENDATIONS FOR ALL NODES ===")
    for node in sorted(graph.adj_list.keys()):
        recs = recommend_friends(graph, node, top_k=5)
        if recs:
            print(f"\n{node}:")
            for n, score in recs:
                print(f"  → {n} (score: {score})")
        else:
            print(f"\n{node}:")
            print("  → No recommendations available")

    print("\n" + "="*60)
    print(" TEXT ANALYSIS COMPLETE")
    print("="*60 + "\n")

    # ----------------------------------------------------
    # VISUALIZATION
    # ----------------------------------------------------
    if auto_visualize:
        print("[visualize] auto mode: rendering all visualizations...")
        safe_call_plot(visualize_all, graph, deg_cent, close_cent, pr, components, communities, PLOTS_FOLDER)
    else:
        choice = _prompt_visualize_choice()
        if choice in ['yes', 'y']:
            print("\nVisualization Options:")
            print("1. All visualizations (recommended)")
            print("2. Basic graph only")
            print("3. Centrality only")
            print("4. Communities only")
            print("5. Connected components only")
            print("6. Friend recommendations (pick node)")
            print("7. Custom selection")

            sel = input("\nYour choice: ").strip()

            if sel == '1':
                safe_call_plot(visualize_all, graph, deg_cent, close_cent, pr, components, communities, PLOTS_FOLDER)

            elif sel == '2':
                safe_call_plot(visualize_graph, graph, "Social Network Graph", PLOTS_FOLDER)

            elif sel == '3':
                safe_call_plot(visualize_centrality, graph, deg_cent, close_cent, pr, PLOTS_FOLDER)

            elif sel == '4':
                safe_call_plot(visualize_communities, graph, communities, PLOTS_FOLDER)

            elif sel == '5':
                safe_call_plot(visualize_components, graph, components, PLOTS_FOLDER)

            elif sel == '6':
                target = input("Enter node name: ").strip()
                if target in graph.get_nodes():
                    recs = recommend_friends(graph, target)
                    safe_call_plot(visualize_recommendations, graph, target, recs, PLOTS_FOLDER)
                else:
                    print("Error: Node not found.")

            elif sel == '7':
                picks = input("Enter numbers (space-separated): ").strip().split()
                for p in picks:
                    if p == '1':
                        safe_call_plot(visualize_graph, graph, "Social Network Graph", PLOTS_FOLDER)
                    elif p == '2':
                        safe_call_plot(visualize_centrality, graph, deg_cent, close_cent, pr, PLOTS_FOLDER)
                    elif p == '3':
                        safe_call_plot(visualize_communities, graph, communities, PLOTS_FOLDER)
                    elif p == '4':
                        safe_call_plot(visualize_components, graph, components, PLOTS_FOLDER)
                    elif p == '5':
                        target = input("Enter node name: ").strip()
                        if target in graph.get_nodes():
                            recs = recommend_friends(graph, target)
                            safe_call_plot(visualize_recommendations, graph, target, recs, PLOTS_FOLDER)
                        else:
                            print("Error: Node not found.")
            else:
                print("Skipping visualizations.")
        else:
            print("Visualizations skipped by user choice.")

    print("\n" + "="*60)
    print(" ALL DONE! Thank you for using the system.")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
