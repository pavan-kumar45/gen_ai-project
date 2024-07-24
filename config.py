# config.py
SERVICE_ACCOUNT_FILE_PATH = 'C:/Users/pavan/Downloads/warm-torus-427502-j7-3344d35efeec.json'
PROJECT_ID = 'warm-torus-427502-j7'
LOCATION = 'us-central1'
GOOGLE_SHEET_NAME = 'Question Bank'
# Model parameters
MODEL_PARAMS = {
    "model": "gemini-1.5-pro-001",
    "temperature": 0,
    "max_tokens": 1000,
    "max_retries": 6,
    "stop": None,
    "top_p": 1,
    "top_k": 40,
    "frequency_penalty": 0,
    "presence_penalty": 0,
    "timeout": 60
}

GEMINI_TEST=False
OPENAI_TEST=True

Run_specific_row=False #if true u can access below 2 rows
run_column=0 #0:correct answer column, 1:partial correct column , 2: wrong answer column
RUN_SPECIFIC_ROW_INDEX=None
Run_All_Rows=False

ACCURACY_TEST=False
REPEATABILITY_TEST=False


if GEMINI_TEST==True:
    Run_specific_row=False #if true u can access below 2 rows
    run_column=0 #0:correct answer column, 1:partial correct column , 2: wrong answer column
    RUN_SPECIFIC_ROW_INDEX=21
    ACCURACY_TEST=False
    Run_All_Rows=True
    REPEATABILITY_TEST=False


if OPENAI_TEST==True:
    Run_specific_row=True #if true u can access below 2 rows
    run_column=1 #0:correct answer column, 1:partial correct column , 2: wrong answer column
    RUN_SPECIFIC_ROW_INDEX=34
    ACCURACY_TEST=True
    Run_All_Rows=False
    # REPEATABILITY_TEST=False #not implemented repeatability yet.
