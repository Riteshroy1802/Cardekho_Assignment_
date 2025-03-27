# import gradio as gr
# from file_handler import create_sqlite_db_from_csv
# from llm_agent import initialize_agent, ask_ai
# from query_processor import execute_sql_query
# from graph_plotter import generate_graph
# from utils import format_response

# agent = None 
# df = None 

# # Handles CSV file upload and AI system initialization.
# def upload_csv_and_initialize(csv_path):
#     global agent
#     global df
#     df = create_sqlite_db_from_csv(csv_path)   
#     columns = ", ".join(df.columns)
#     describe_data = df.describe().to_string()
#     describe_data += "\n" + df.head().to_string()
#     agent = initialize_agent(columns, describe_data)
    
#     return "CSV uploaded & AI system updated!"

# # Processes the user's question and returns AI + SQL response.
# def process_query(user_prompt: str):
#     global agent
#     global df
#     if agent is None:
#         return "Please upload a CSV file first.", None

#     response_data = ask_ai(agent, user_prompt)
#     if "error" in response_data:
#         return response_data["error"], None

#     final_response = ""
#     graph_image = None

#     if response_data.query:
#         sql_result, column_names = execute_sql_query(response_data.query)
#         if sql_result:
#             final_response += "\n" + format_response(user_prompt, sql_result, column_names)

#     if response_data.graph:
#         graph_image = generate_graph(response_data.graph, df=df)

#     return final_response, graph_image

# with gr.Blocks() as demo:
#     gr.Markdown("### 📊 CSV Data Q&A with Graphs")
#     csv_file = gr.File(label="Upload CSV")
#     upload_status = gr.Textbox(label="Status", interactive=False)
#     user_prompt = gr.Textbox(label="Ask a question")
#     submit_btn = gr.Button("Get Answer")
#     response_box = gr.Textbox(label="Response", interactive=False)
#     graph_output = gr.Plot(label="Generated Graph")

#     csv_file.upload(upload_csv_and_initialize, inputs=[csv_file], outputs=[upload_status])
#     submit_btn.click(process_query, inputs=[user_prompt], outputs=[response_box, graph_output])

# demo.launch()


import gradio as gr
from file_handler import create_sqlite_db_from_csv
from llm_agent import initialize_agent, ask_ai
from query_processor import execute_sql_query
from graph_plotter import generate_graph
from utils import format_response

agent = None
df = None

# Handles CSV file upload and AI system initialization.
def upload_csv_and_initialize(csv_path):
    global agent
    global df
    df = create_sqlite_db_from_csv(csv_path)
    if isinstance(df, str):
        return df, None  # Return error message if CSV is invalid

    columns = ", ".join(df.columns)
    describe_data = df.describe().to_string()
    describe_data += "\n" + df.head().to_string()
    agent = initialize_agent(columns, describe_data)

    return "✅ CSV uploaded successfully!", gr.update(visible=True)

# Processes the user's question and returns AI + SQL response.
def process_query(user_prompt: str, graph_type: str):
    global agent
    global df
    if agent is None:
        return "⚠ Please upload a CSV file first.", None

    response_data = ask_ai(agent, user_prompt)
    if "error" in response_data:
        return response_data["error"], None

    final_response = ""
    graph_image = None

    if response_data.query:
        sql_result, column_names = execute_sql_query(response_data.query)
        if sql_result:
            final_response += "\n" + format_response(user_prompt, sql_result, column_names)

    # Debugging: Print the received graph data
    print("🔍 Debug - Received Graph Data:", response_data.graph)

    # Ensure graph data exists before plotting
    if response_data.graph and response_data.graph.type:
        response_data.graph.type = graph_type.lower()  # Override with user selection
        graph_image = generate_graph(response_data.graph, df=df)

        # Debugging: Print if graph was successfully generated
        if graph_image:
            print("✅ Debug - Graph successfully generated")
        else:
            print("❌ Debug - Graph generation failed")

    return final_response, graph_image


# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("## 📊 AI-Powered CSV Data Explorer")

    with gr.Tab("📂 Upload CSV"):
        with gr.Row():
            csv_file = gr.File(label="Upload CSV File")
            upload_status = gr.Textbox(label="Status", interactive=False)

        csv_file.upload(upload_csv_and_initialize, inputs=[csv_file], outputs=[upload_status])

    with gr.Tab("🔎 Ask Questions"):
        with gr.Row():
            user_prompt = gr.Textbox(label="Ask a Question about the CSV Data", placeholder="E.g., Show me sales trends")

        with gr.Row():
            graph_type = gr.Dropdown(choices=["Bar", "Line", "Scatter"], label="Select Graph Type", value="Bar")

        submit_btn = gr.Button("Get Answer")

        response_box = gr.Textbox(label="Response", interactive=False)

        # **📌 FIXED: Graph Display Section**
        graph_output = gr.Plot(label="Generated Graph", visible=True)  # Ensure it's visible!

        submit_btn.click(process_query, inputs=[user_prompt, graph_type], outputs=[response_box, graph_output])

demo.launch()
