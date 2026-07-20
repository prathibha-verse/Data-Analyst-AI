# Data Analyst AI Assistant

An AI-powered web application that enables users to upload CSV and Excel files, analyze datasets, generate visualizations, and interact with the data using natural language queries.

---

## Overview

Data Analyst AI Assistant simplifies data analysis by combining traditional analytics with artificial intelligence. Users can upload datasets and instantly receive summaries, charts, business insights, and AI-generated responses without writing code.

The application is built using Flask, Pandas, Plotly, and Ollama with the Qwen 2.5 language model.

---

## Features

- Upload CSV and Excel files
- Automatic dataset summary
- Missing-value analysis
- Statistical analysis
  - Mean
  - Median
  - Maximum
  - Minimum
- Interactive charts
  - Bar chart
  - Pie chart
  - Line chart
- AI chatbot for natural language queries
- Automatic business insights generation
- PDF report download
- Clean and responsive user interface

---

## Tech Stack

### Frontend

- HTML
- CSS
- JavaScript

### Backend

- Flask
- Python

### Data Processing and Visualization

- Pandas
- Plotly

### Artificial Intelligence

- Ollama
- Qwen 2.5 (3B)

### Tools

- Git
- GitHub

---

## Project Structure

```text
Data-Analyst-AI/
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── uploads/
│
├── app.py
├── analyzer.py
├── charts.py
├── ai_assistant.py
├── insights.py
├── report_generator.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/prathibha-verse/Data-Analyst-AI.git

cd Data-Analyst-AI
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download and install Ollama:

https://ollama.com

Pull the Qwen 2.5 model:

```bash
ollama pull qwen2.5:3b
```

Start Ollama:

```bash
ollama serve
```

---

## Run the Application

```bash
python app.py
```

Open the browser and visit:

```text
http://127.0.0.1:5000
```

---

## Example Questions

- Which department has the highest marks?
- What is the average attendance?
- Which category has the highest sales?
- Compare different departments.
- Identify missing values in the dataset.
- What insights can be derived from the data?

---

## Future Enhancements

- Add more chart types
- Support additional file formats
- Improve AI-generated insights
- Add advanced filtering options
- Deploy the application online

---

## Screenshots

Add screenshots of your application here.

```text
screenshots/home_page.png

screenshots/dashboard.png
```

---

## Author

### S. Prathibha

- GitHub: https://github.com/prathibha-verse
- LinkedIn: https://www.linkedin.com/in/prathibha-senthilkumar-9b0755326

---

## License

This project was developed for educational and learning purposes.