# Performance Evaluation of LLM vs SLM on CS Q&A Tasks


## 📝 Description

This project aims to evaluate the performance of **Large Language Models (LLMs)** versus **Small Language Models (SLMs)** on Computer Science Question and Answer (Q&A) tasks. Specifically, we experiment with the **Llama-3** model series for entity extraction and generation from given questions.

Previously, Llama-2 models were utilized for such tasks. With the advent of Llama-3 models, we explore their capabilities using the **Groq API**, leveraging models like **llama-3.1-70b-versatile** due to their speed and availability for developers.

We utilize datasets from prestigious universities such as **NYU**, **CMU**, and **Stanford**, along with publicly available datasets, to generate comprehensive Q&A data for our evaluations.

## ✨ Features

- **Experimentation with Llama-3 Models:**
  - Utilize Llama-3 models (8B and 70B) for entity extraction tasks.
- **Groq API Integration:**
  - Leverage the Groq API for fast and efficient model inference.
- **Prompt Engineering:**
  - Explore different prompting techniques to optimize entity extraction.
- **Dataset Diversity:**
  - Use a variety of datasets from top universities for robust evaluation.
- **Result Generation:**
  - Output results in JSON format for easy analysis and comparison.


## 🚀 Getting Started

### Prerequisites

- **Python 3.7** or higher
- **pip** package installer
- **Groq API Key** (Sign up at [Groq Console](https://console.groq.com/))
- **Git**

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/YOUR_USERNAME/llm-vs-slm-cs-qna.git
   cd llm-vs-slm-cs-qna
   ```
2. **Set Up a Virtual Environment (Optional but Recommended):**

   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   # On Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```
  
3. **Set Up Environment Variables:**

Create a .env file in the project root directory:

  ```plaintext
  GROQ_API_KEY=your_groq_api_key_here
  ```
Note: Replace your_groq_api_key_here with your actual Groq API key.
