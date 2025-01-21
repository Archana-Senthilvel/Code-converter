Overview

The Code Converter with Compiler is an interactive web application that allows users to convert source code written in one programming language to another and compile the converted code to verify its functionality. The current version supports the conversion of .NET and Java code into Python.

This application leverages Google Generative AI's advanced capabilities to ensure accurate and functional code conversion while maintaining best practices and efficiency in the target language.

Key Features

Language Conversion: Seamlessly converts .NET or Java code into Python.

File Upload or Manual Input: Supports both file upload and manual text entry for source code.

Code Compilation: Automatically compiles and executes the converted Python code to verify its correctness.

Error Handling: Ensures exceptions and errors are properly handled during conversion.

Download Option: Provides a downloadable version of the converted code.

How It Works

Select Source and Target Languages:

Choose the source language (.NET or Java).

Target language is fixed to Python.

Input Source Code:

Upload a file containing the source code (.cs or .java files supported).

Alternatively, enter the source code manually in the provided text area.

Convert and Compile:

Click the "Convert and Compile" button to start the conversion process.

The source code is sent to Google Generative AI for conversion based on provided instructions.

The converted Python code is displayed and temporarily saved.

The code is compiled and executed to display the output or errors, if any.

Download Converted Code:

After conversion, the Python code can be downloaded using the "Download Converted Code" button.

Installation and Setup

Follow these steps to set up and run the application:

Clone the Repository:

git clone <repository-url>
cd <repository-folder>

Install Dependencies:
Ensure you have Python installed (version 3.7 or higher). Then, install the required libraries:

pip install streamlit google-generativeai

Set Up API Key:

Obtain an API key from Google Generative AI.

Replace AIzaSyAAfS_s-xEx4pFpez6nxjqFqt7pIJdYQDU in the code with your API key.

Run the Application:

streamlit run app.py

Access the Application:

Open the URL displayed in your terminal (usually http://localhost:8501) in a web browser.
