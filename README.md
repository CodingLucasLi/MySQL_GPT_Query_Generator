# MySQL GPT Query Generator

![Preview](https://github.com/CodingLucasLi/MySQL_GPT_Query_Generator/blob/main/preview.jpg)

MySQL GPT Query Generator is a tool that enables the generation of SQL query statements based on natural language input. It provides an intuitive interface for interactively creating and executing queries, as well as displaying query results. Additionally, it offers a question-answering feature that allows users to inquire about and optimize their data warehouses.

## Features

- Interactive SQL query generation based on natural language input
- Execution of SQL queries and display of query results
- Query optimization suggestions for your data warehouse
- Question-answering capability for advanced database analysis

## Prerequisites

Before using MySQL GPT Query Generator, please ensure the following:

- Python 3.7 or higher is installed
- [Streamlit](https://streamlit.io/) package is installed: `pip install streamlit`
- [OpenAI](https://openai.com/) package is installed: `pip install openai`
- A local MySQL database is set up for experimental and usage purposes

## Installation

To use MySQL GPT Query Generator, follow these steps:

1. Clone the repository: `git clone https://github.com/CodingLucasLi/MySQL_GPT_Query_Generator.git`
2. Install the required dependencies:
   - Streamlit: `pip install streamlit`
   - OpenAI: `pip install openai`
   - Other dependencies: (List any additional dependencies here)
3. Set up a local MySQL database for experimental and usage purposes.

## Usage

1. Run the application: `streamlit run main.py`
2. Open your web browser and navigate to `http://localhost:8501`
3. Fill in the MySQL connection details (username, host, password, port, database)
4. Click the "Get Database Data" button to scan the tables in the database and save them as SQL files
5. Select the desired SQL files to build the index for query generation
6. Use the "Self-Service Query" tab to enter your SQL query and query requirements, and click "Query" to execute the query and view the results
7. Use the "Smart Q&A" tab to ask questions about your database and receive analysis and optimization suggestions

## Contributing

Contributions are welcome! If you would like to contribute to MySQL GPT Query Generator, please follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b my-feature-branch`
3. Make your changes and commit them: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin my-feature-branch`
5. Submit a pull request

## License

This project is licensed under the [MIT License](LICENSE).
