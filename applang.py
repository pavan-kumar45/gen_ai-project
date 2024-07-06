import time
import vertexai
import gspread
from google.oauth2.service_account import Credentials
from google.api_core.exceptions import ResourceExhausted, InvalidArgument
import re
from prompts import theory_prompt_template, coding_prompt_template  # Import the prompts
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_google_vertexai import ChatVertexAI
from langchain_core.messages import HumanMessage

# Set up the Vertex AI environment
vertexai.init(project='warm-torus-427502-j7', location='us-central1')

# Initialize the Vertex AI model using LangChain's ChatVertexAI
llm = ChatVertexAI(
    model="gemini-1.5-pro-001",
    temperature=1,
    max_tokens=8000,
    max_retries=6,
    stop=None,
    top_p=1,
    top_k=40,  # Adjusted top_k value to be within the valid range
    frequency_penalty=0,
    presence_penalty=0,
    timeout=60
)

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
user_answers = sheet.col_values(4)  # Assuming user answers are in the third column

# Function to generate feedback with retry mechanism using ChatVertexAI
def generate_feedback(prompt, retries=6, delay=1, max_wait_time=300):
    total_wait_time = 0
    for attempt in range(retries):
        if total_wait_time >= max_wait_time:
            print("Total wait time exceeded. Stopping retries.")
            return None

        try:
            message = HumanMessage(content=prompt)
            response = llm.invoke([message])
            return response.content
        except (ResourceExhausted, InvalidArgument) as e:
            if isinstance(e, InvalidArgument) and "topK" in str(e):
                print("Invalid topK value. Please update the value to be within the supported range.")
                return None
            if attempt < retries - 1:
                backoff_time = delay * (2 ** attempt)  # Exponential backoff
                total_wait_time += backoff_time
                print(f"Quota exceeded. Retrying in {backoff_time} seconds...")
                time.sleep(backoff_time)
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

    if 'program' in question.lower():
        prompt = coding_prompt_template.format(question=question, user_answer=user_answer, correct_answer=correct_answer)
    else:
        prompt = theory_prompt_template.format(question=question, user_answer=user_answer, correct_answer=correct_answer)

    feedback = generate_feedback(prompt)
    if feedback:
        score = extract_score(feedback)
       
        sheet.update_cell(i + 1, 11, score)  # Assuming scores go in the 9th column
        sheet.update_cell(i + 1, 12, feedback)  # Assuming feedback goes in the 10th column

        print(f"Question: {question}")
        print(f"Score: {score}")
        print(f"Feedback: {feedback}\n")

        print("-----------------------------------------------------------------------------------")
