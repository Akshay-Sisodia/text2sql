# Text2SQL: Natural Language to SQL Query Generator

## Overview

Text2SQL is an intelligent database query interface that bridges the gap between natural language and SQL queries. Leveraging advanced language models, this application enables users to interact with databases using plain English, making data exploration more accessible and intuitive.

## Key Features

- **Intelligent Query Generation**: Transform natural language descriptions into precise SQL queries
- **Multi-Model Support**: Compatible with various Ollama language models
- **Dynamic Database Exploration**: Automatic schema detection and visualization
- **User-Friendly Interface**: Streamlit-powered web application
- **Flexible Database Handling**: Support for SQLite database files

## System Requirements

### Minimum Requirements
- Python 3.8+
- Ollama
- Pip package manager

### Recommended Language Models
- Llama3.1
- Mistral
- Phi

## Getting Started

### 1. Installation

#### Clone the Repository
```bash
git clone https://github.com/akshay-sisodia/text2sql.git
cd text2sql
```

#### Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Unix/macOS
venv\Scripts\activate     # Windows
```

#### Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Prepare Ollama Models
```bash
ollama pull llama2
ollama pull mistral
```

### 3. Run the Application
```bash
streamlit run main.py
```

## Usage Guide

1. **Database Selection**
   - Upload a new SQLite database
   - Or select from existing databases in the `databases` directory

2. **Explore Database Schema**
   - View detailed information about tables and columns
   - Understand the structure of your database

3. **Query Generation**
   - Enter a natural language description of your data request
   - Select preferred Ollama language model
   - Generate and execute SQL queries with a single click

### Example Queries
- "Retrieve the top 5 customers by total purchase amount"
- "List all orders from the previous month"
- "Calculate average product prices by category"

## Technical Details

### Supported Database Formats
- SQLite (.db)
- SQLite (.sqlite)

### Supported Language Models
- Llama2
- Mistral
- Phi
- Extensible to other Ollama models

## Best Practices

- Always review generated SQL queries before execution
- Ensure database file integrity
- Validate query results against expected outcomes

## Troubleshooting

### Common Issues
- Verify Ollama installation and model availability
- Check Python and dependency versions
- Confirm database file format and accessibility

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Submit a pull request

## Security Considerations

- Use only trusted and sanitized database sources
- Avoid executing queries on production databases without thorough review

## Acknowledgments

- [Ollama](https://ollama.com/) for language model integration
- [Streamlit](https://streamlit.io/) for the application framework
- Open-source community for continuous inspiration

## Contact

For support, feature requests, or collaboration:
- Email: [akshaysisodia.studies@gmail.com]