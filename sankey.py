import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt # Added import
import io
import base64

df = pd.read_csv(r'C:\Users\daveb\OneDrive\Documents\Sankey Trials.csv')

# 1. Create a unique list of all nodes (labels)
all_nodes = list(pd.concat([df['Source'], df['Target']]).unique())

# 2. Map node labels to numerical indices
label_to_index = {label: i for i, label in enumerate(all_nodes)}

# 3. Convert source and target columns to numerical indices
source_indices = [label_to_index[s] for s in df['Source']]
target_indices = [label_to_index[t] for t in df['Target']]

# 4. Extract the flow values
values = df['Value'].tolist()

# Create the Sankey diagram
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=all_nodes,
        # color="blue" # Optional: set node color
    ),
    link=dict(
        source=source_indices,
        target=target_indices,
        value=values,
        # color="lightgray" # Optional: set link color
    )
)])

fig.update_layout(title_text="Sankey Diagram from DataFrame", font_size=10)

fig.show()