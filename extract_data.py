import PyPDF2
import re

def extract_mcq_questions_answers(pdf_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        # Extract text from each page
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    # Split the text into lines
    lines = text.split('\n')
    mcq_data = []
    question = ""
    options = []
    answer = ""
    # Regex to detect questions starting with a letter like "(a)"
    question_pattern = re.compile(r'\([a-zA-Z]\)\s')
    option_pattern = re.compile(r'^\([iv]+\)')
    solution_pattern = re.compile(r'Solution:\s*(.*)')
    for line in lines:
        # Look for a question starting with (a), (b), etc.
        if question_pattern.match(line):
            if question:
                # Store the previous question and its options/answer before starting a new one
                mcq_data.append((question, options, answer))
            # Reset for the new question
            question = line.strip()
            options = []
            answer = ""
        # Check if line contains options (i), (ii), etc.
        elif option_pattern.match(line):
            options.append(line.strip())
        # Capture the solution for the MCQ
        match = solution_pattern.search(line)
        if match:
            answer = match.group(1).strip()
    # Append the last question
    if question:
        mcq_data.append((question, options, answer))
    return mcq_data
pdf_path = "Datasets gathered/cs230exam_win21_soln.pdf"
mcq_questions_answers = extract_mcq_questions_answers(pdf_path)

# Print extracted questions and answers
for idx, (q, opts, ans) in enumerate(mcq_questions_answers):
    print(f"Question {idx+1}: {q}")
    print("Options:")
    for opt in opts:
        print(f"  {opt}")
    print(f"Correct Answer: {ans}\n")
