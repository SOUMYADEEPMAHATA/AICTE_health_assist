# AICTE Health Assist

## Overview
AICTE Health Assist is a project aimed at providing health assistance and resources to users. This repository contains the code and documentation for the project.

## Features
- Health tips and advice
- Symptom checker

## Installation
To use this repository, you need to install Ollama. Follow the instructions below to set up your environment.

### Install Ollama

```bash
pip install ollama
```

To install the project, clone the repository and install the necessary dependencies:
```bash
git clone https://github.com/yourusername/AICTE_health_assist.git
cd AICTE_health_assist
pip install -r requirements.txt
```

## Model Information

This repository uses a finetuned version of Distilled Deepseek which is run using Ollama. Please ensure you have Ollama installed and change the model name in the `utils/llm_code.py` file in the line:

```python
llm = OllamaLLM(model="Deepseek-R1-medical:latest")
```

with your own model or models available in Ollama.

## Usage
To start the application, run:
```bash
streamlit run My_Healthcare-chatbot.py
```
Open your browser and navigate to `http://localhost:8501` to access the application.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or feedback, please contact us at soumyadeep15mahata@gmail.com

