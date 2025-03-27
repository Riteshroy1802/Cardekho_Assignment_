import matplotlib.pyplot as plt
import pandas as pd
from llm_agent import Graph

def generate_graph(graph_data: Graph, df: pd.DataFrame):
    try:
        if not graph_data or not graph_data.type:
            print("⚠ [DEBUG] No graph data provided.")
            return None

        if df is None or df.empty:
            print("⚠ [DEBUG] DataFrame is empty.")
            return None

        print("\n📊 [DEBUG] Graph Data Received:", graph_data)  # Debugging

        x_column = graph_data.x or df.columns[0]
        y_column = graph_data.y or (df.columns[1] if len(df.columns) > 1 else df.columns[0])

        print(f"✅ [DEBUG] Plotting {graph_data.type} graph for {x_column} vs {y_column}")

        # 🔹 Increase figure size for better readability
        fig, ax = plt.subplots(figsize=(12, 6))  # Increased width

        if "bar" in graph_data.type:
            ax.bar(df[x_column], df[y_column])
            ax.set_xticklabels(df[x_column], rotation=45, ha="right")  # 🔹 Rotate labels for readability
        elif "line" in graph_data.type:
            ax.plot(df[x_column], df[y_column], marker="o")
        elif "scatter" in graph_data.type:
            ax.scatter(df[x_column], df[y_column])
        else:
            print("⚠ [DEBUG] Invalid graph type.")
            return None

        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        ax.set_title(f"{graph_data.type.capitalize()} Chart of {x_column} vs {y_column}")

        # 🔹 Improve layout to avoid overlap
        plt.tight_layout()

        print("✅ [DEBUG] Graph successfully created.")
        return fig  # Return the figure for Gradio

    except Exception as e:
        print(f"❌ [DEBUG] Graph Error: {e}")
        return None
