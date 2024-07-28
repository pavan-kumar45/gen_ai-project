import time
import openpyxl
from openpyxl import load_workbook
import vertexai
from google.api_core.exceptions import ResourceExhausted, InvalidArgument
from langchain_google_vertexai import ChatVertexAI
from langchain_core.messages import HumanMessage
import re
from config import user_answer_written
# Import templates
from prompts_evaluate import theory_prompt_template, coding_prompt_template, design_prompt_template

vertexai.init(project='warm-torus-427502-j7', location='us-central1')

# Initialize the Vertex AI model using LangChain's ChatVertexAI
llm = ChatVertexAI(
    model="gemini-1.5-pro-001",
    temperature=0,
    max_tokens=1000,
    max_retries=6,
    stop=None,
    top_p=1,
    top_k=40,
    frequency_penalty=0,
    presence_penalty=0,
    timeout=60
)

def generate_feedback(prompt_template, question, user_answer, retries=6, delay=1, max_wait_time=300):
    total_wait_time = 0
    prompt = prompt_template.format(question=question, user_answer=user_answer)
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

def extract_score(feedback):
    match = re.search(r'\b\d{1,2}\b', feedback)
    return int(match.group()) if match else None


def process_excel(file_path):
    i=1
    workbook = load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=False):  # Assuming the first row is the header
        question_cell, topic_cell, answer_cell, score_cell, feedback_cell = row

        question = question_cell.value
        topic = topic_cell.value
        user_answer = answer_cell.value

        if question is None or user_answer is None or topic is None:
            continue

        # Determine the prompt template based on the topic
        if topic.startswith("Theory"):
            prompt_template = theory_prompt_template
        elif topic.startswith("Coding"):
            prompt_template = coding_prompt_template
        elif topic.startswith("Design"):
            prompt_template = design_prompt_template
        else:
            print(f"Unrecognized topic: {topic}. Skipping row.")
            continue
        
        print(f"evaluating Question:{i}")
        i=i+1
        feedback = generate_feedback(prompt_template, question, user_answer)
        if feedback:
            score = extract_score(feedback)
            score_cell.value = score if score is not None else "N/A"
            feedback_cell.value = feedback

    workbook.save(file_path)
    print(f"Processed {file_path} and saved results.")


if user_answer_written:
    process_excel(r'C:\Users\pavan\Desktop\projects\gen ai\Generate and evaluation\CSV Files\Questions.xlsx')
