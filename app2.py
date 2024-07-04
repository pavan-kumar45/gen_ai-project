import time
import vertexai
from vertexai.generative_models import GenerativeModel
import gspread
from google.oauth2.service_account import Credentials
from google.api_core.exceptions import ResourceExhausted
import re

# Set up the Vertex AI environment
vertexai.init(project='warm-torus-427502-j7', location='us-central1')

# Load the Gemini 1.5 Pro model
model = GenerativeModel(model_name='gemini-1.5-pro-001')

# Define the scope and authenticate using service account
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file('C:/Users/pavan/Downloads/warm-torus-427502-j7-3344d35efeec.json', scopes=scope)
client = gspread.authorize(creds)

# List available spreadsheets
spreadsheet_list = client.openall()
for spreadsheet in spreadsheet_list:
    print(spreadsheet.title)

# Open the Google Sheet
sheet = client.open('Java').sheet1  # Replace with the actual name of your Google Sheet

# Fetch data from the Google Sheet
questions = sheet.col_values(1)  # Assuming questions are in the first column
correct_answers = sheet.col_values(2)  # Assuming correct answers are in the second column
user_answers = sheet.col_values(5)  # Assuming user answers are in the third column

# Function to generate feedback with retry mechanism
def generate_feedback(prompt, retries=2, delay=60):
    for attempt in range(retries):
        try:
            response = model.generate_content(prompt)
            return response.text
        except ResourceExhausted as e:
            if attempt < retries - 1:
                print(f"Quota exceeded. Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                print("Max retries exceeded. Please check your quota.")
                return None

# Function to extract score from feedback
def extract_score(feedback):
    match = re.search(r'\b\d{1,2}\b', feedback)
    return int(match.group()) if match else None

# Iterate through the answers and generate feedback
for i in range(1, len(user_answers)):  # Assuming the first row is the header
    question = questions[i]
    user_answer = user_answers[i]
    correct_answer = correct_answers[i]

    prompt = (
        f"Question: {question}\n"
        f"User Answer: {user_answer}\n"
        f"Correct Answer: {correct_answer}\n\n"
        "Evaluate the user's answer compared to the correct answer and give a score out of 10. Strictly follow these guidelines:\n"
        "1. For a fully correct answer (all key parts are there), give a score of 7 to 10.\n"
        "2. For a mostly correct answer with small mistakes or missing parts, give a score of 5 to 6.\n"
        "3. For a partially correct answer (many key parts missing), give a score of 3 to 5.\n"
        "4. For an answer that's mostly wrong but has some correct parts, give a score of 1 to 2.\n"
        "5. For a completely wrong answer, give a score of 0 to 1.\n"
        "Provide detailed feedback and suggestions for improvement, explaining why you gave the score."
    )



    feedback = generate_feedback(prompt)
    if feedback:
        score = extract_score(feedback)
       
        sheet.update_cell(i + 1, 7, score)  # Assuming scores go in the 4th column
        sheet.update_cell(i + 1, 8, feedback)  # Assuming feedback goes in the 5th column

        print(f"Question: {question}")
        print(f"Score: {score}")
        print(f"Feedback: {feedback}\n")
