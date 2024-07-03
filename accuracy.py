import gspread
from oauth2client.service_account import ServiceAccountCredentials
import numpy as np

# Define the scope
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

# Add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('C:/Users/pavan/Downloads/warm-torus-427502-j7-3344d35efeec.json', scope)

# Authorize the client sheet 
client = gspread.authorize(creds)

# Get the sheet
sheet = client.open('Java').sheet1

def calculate_ratio_for_column(sheet, column_index, min_value, max_value):
    # Get all values in the specified column (zero-based indexing)
    column_values = sheet.col_values(column_index + 1)
    
    # Convert to float and filter out non-numeric values
    filtered_values = []
    for value in column_values:
        try:
            filtered_values.append(float(value))
        except ValueError:
            continue

    # Convert list to numpy array for easier computation
    values = np.array(filtered_values)

    # Count the values between min_value and max_value
    count_in_range = np.sum((values >= min_value) & (values <= max_value))

    # Calculate the total number of values
    total_values = values.size

    # Calculate the ratio
    ratio = count_in_range / total_values if total_values != 0 else 0

    return count_in_range, total_values, ratio

def main():
    # Calculate for 6th column (index 5), values between 4 and 6
    count_6th, total_6th, ratio_6th = calculate_ratio_for_column(sheet, 5, 4, 6)
    print(f'For Partial Correct: Score between 4 and 6: {count_6th}, Total number of values: {total_6th}, Accuracy: {ratio_6th}')

    # Calculate for 8th column (index 7), values between 0 and 3
    count_8th, total_8th, ratio_8th = calculate_ratio_for_column(sheet, 7, 0, 3)
    print(f'For Wrong answer: Score between 0 and 3: {count_8th}, Total number of values: {total_8th}, Accuracy: {ratio_8th}')

if __name__ == "__main__":
    main()
