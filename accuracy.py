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
    # Calculate for partial column (index 5), values between 4 and 6
    count_partial, total_partial, ratio_partial = calculate_ratio_for_column(sheet, 8, 4, 7)
    print(f'For Partial Correct: Score between 4 and 7: {count_partial}, Total number of values: {total_partial}, Accuracy: {ratio_partial}')

    # Calculate for wrong column (index 7), values between 0 and 3
    count_wrong, total_wrong, ratio_wrong = calculate_ratio_for_column(sheet, 10, 0, 4)
    print(f'For Wrong answer: Score between 0 and 4: {count_wrong}, Total number of values: {total_wrong}, Accuracy: {ratio_wrong}')


    count_correct, total_correct, ratio_correct = calculate_ratio_for_column(sheet, 6, 7, 10)
    print(f'For Correct answer: Score between 7 and 10: {count_correct}, Total number of values: {total_correct}, Accuracy: {ratio_correct}')

    # Calculate the average ratio
    ratios = [ratio_partial, ratio_wrong, ratio_correct]
    average_ratio = np.mean(ratios)
    print(f'Average Accuracy: {average_ratio}')

if __name__ == "__main__":
    main()
