import streamlit as st
import google.generativeai as genai
import subprocess
import tempfile
import re


# Configure Google Generative AI with your API key
genai.configure(api_key="AIzaSyAAfS_s-xEx4pFpez6nxjqFqt7pIJdYQDU")
model = genai.GenerativeModel(model_name="gemini-pro")


# Title of the app
st.title("Language Converter with Compiler")


# Option to select source and target language
source_lang = st.selectbox("Select the source language", [".Net", "Java"])
target_lang = st.selectbox("Select the target language", ["Python"])


# File upload or manual code input option
st.subheader("Upload your source code file or enter code manually")


# Option 1: Upload the file containing source code
uploaded_file = st.file_uploader("Upload your source code file", type=["cs", "java"])


# Option 2: Manual code input
code_input = st.text_area("Or enter your source code here")


# Variable to store the code to be converted
code = None


# Determine the source code input method
if uploaded_file is not None:
    code = uploaded_file.read().decode("utf-8")
elif code_input:
    code = code_input


# Conversion process button to trigger conversion
if st.button("Convert and Compile"):
    if code:
        prompt_parts = f"""
        Please convert the following code from {source_lang} to {target_lang}.
        You are a seasoned code conversion expert with deep expertise in both .NET and Python.
        Your primary goal is to ensure that the converted Python code maintains the same functionality as the original .NET code while handling all potential exceptions.
        You prioritize code efficiency, clarity, and compliance with Python best practices.
        VERY IMPORTANT THING IS IT SHOULD CONVERT THE SOURCE CODE INTO TARGET CODE COMPLETELY
        Convert the following .NET code to Python seamlessly. Make sure that you follow these instructions:
       
        1. Ensure that the Python code is functionally equivalent to the original .NET code, handling any potential exceptions that may arise during the conversion process.
        2. The conversion should include all necessary imports, module references, and handle key parameters such as database connections, file handling, and threading.
        3. Ensure the converted code adheres to Python best practices, is well-documented, and includes meaningful error handling.
        4. The output should be optimized for performance and be free of any conversion errors.
        5. Ensure all exceptions in the .NET code are appropriately converted to Python's exception handling mechanisms.
        6. Address any differences in data types between .NET and Python, including explicit typecasting where necessary.
        7. Replace .NET-specific libraries with their Python equivalents, ensuring similar functionality.
        8. Convert .NET's async/await patterns to Python's async equivalents where applicable.
        9. Adapt database connection code from .NET to Python, considering differences in database connectivity libraries (e.g., ADO.NET to SQLAlchemy or PyODBC).
        10. Optimize the Python code for performance, leveraging Python’s strengths while avoiding potential bottlenecks.
        11. Make sure that you do not include any additional comments, explanations, or metadata.
        12. Ensure that the conversion has a decreased likelihood of bugs and errors.
        13. Your conversion should maintain the original logic and functionality while adhering to the structure of the target language.
        14. Your code should not have any syntax or semantic errors.
        Convert the following code:\n\n{code}\n\n
        """


        # Generate response using Generative AI
        response = model.generate_content(prompt_parts)
        converted_code = response.text
       
        # Clean up the converted code by removing markdown formatting
        converted_code = re.sub(r'```[a-z]*\n', '', converted_code)  # Remove opening code block tags
        converted_code = re.sub(r'\n```', '', converted_code)  # Remove closing code block tags
        converted_code = converted_code.strip()
       
        # Display the converted code
        st.subheader("Converted Code")
        st.code(converted_code, language=target_lang.lower())


        # Save the converted code to a temporary file
        with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as temp_file:
            temp_file.write(converted_code.encode('utf-8'))
            temp_file.flush()
           
            try:
                # Compile and run the converted Python code
                output = subprocess.check_output(["python", temp_file.name], stderr=subprocess.STDOUT, text=True)
            except subprocess.CalledProcessError as e:
                output = e.output
       
        # Display the output of the converted code
        st.subheader("Output")
        st.text(output)


        # Provide download option for the converted code
        st.download_button(
            label="Download Converted Code",
            data=converted_code,
            file_name=f"converted_code.{target_lang.lower()}"
        )
    else:
        st.warning("Please upload a file or enter code to convert.")
