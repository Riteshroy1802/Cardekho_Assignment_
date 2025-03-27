📊 AI-Powered CSV Analysis & SQL Querying
Unlock deep insights from your CSV data using natural language! This AI-driven tool transforms CSV files into an interactive SQLite database, allowing users to ask questions in plain English. Powered by an Ollama-based AI model, it intelligently converts queries into SQL, executes them, and delivers clear, structured results. When relevant, it also generates dynamic visualizations to enhance data understanding.

🚀 Why Use This?
✔ No SQL Knowledge Needed – Just ask questions in natural language!
✔ Instant Data Processing – Convert CSVs into a fully functional database in seconds.
✔ AI-Generated SQL Queries – Let the AI handle complex query generation.
✔ Auto-Generated Charts – Get visual insights when needed.
✔ Intuitive Gradio UI – A simple interface for seamless interaction.

⚙️ How It Works

1️⃣ Upload Your CSV File
The system reads and extracts column names.

It automatically converts the CSV into an SQLite database.

A statistical summary of the data is generated for reference.


2️⃣ AI-Powered Query Processing
The Ollama AI model receives:

A list of column names.

A data summary for better query precision.

The AI translates user questions into optimized SQL queries.


3️⃣ Ask Questions in Natural Language
Type your query in plain English (e.g., "What is the average sales per month?").

The system processes your request in four steps:

AI interprets the question and generates an SQL query.

Query executes, fetching relevant data.

Results are displayed in a structured format.

If applicable, a graph is generated for better visualization.
🛠️ Setup & Installation
1️⃣ Install Dependencies
Ensure you have all required libraries installed:
```
pip install -r requirements.txt
```
2️⃣ Run the Application
Start the system with:
```
python main.py
