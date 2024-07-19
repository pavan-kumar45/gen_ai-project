# config.py
SERVICE_ACCOUNT_FILE_PATH = 'C:/Users/pavan/Downloads/warm-torus-427502-j7-3344d35efeec.json'
PROJECT_ID = 'warm-torus-427502-j7'
LOCATION = 'us-central1'
GOOGLE_SHEET_NAME = 'Question Bank'
# Model parameters
MODEL_PARAMS = {
    "model": "gemini-1.5-pro-001",
    "temperature": 0,
    "max_tokens": 8000,
    "max_retries": 6,
    "stop": None,
    "top_p": 1,
    "top_k": 40,
    "frequency_penalty": 0,
    "presence_penalty": 0,
    "timeout": 60
}


Run_specific_row=False
RUN_SPECIFIC_ROW_INDEX=21

ACCURACY_TEST=False


REPEATABILITY_TEST=True

