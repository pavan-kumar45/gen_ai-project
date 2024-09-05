#prompts_generate.py


# Define the number of questions and difficulty level
number_of_questions_coding = 6
number_of_questions_theory = 7
number_of_questions_design = 4
difficulty_level = "medium"  # Options: "easy", "medium", "hard"

# Generate question distribution based on difficulty level
if difficulty_level == "easy":
    easy, medium, hard = 0.6, 0.2, 0.2
elif difficulty_level == "medium":
    easy, medium, hard = 0.2, 0.6, 0.2
elif difficulty_level == "hard":
    easy, medium, hard = 0.2, 0.2, 0.6

# Define the primary and secondary skills (example skills, replace with actual)
primary_skills = ['Python', 'Data Structures']
secondary_skills = ['Algorithms', 'OOP']

# Create the prompts for generating questions with examples
coding_prompt = (f"Generate {number_of_questions_coding} coding questions based on the primary skills (more priority): "
                f"{', '.join(primary_skills)} and secondary skills: {', '.join(secondary_skills)}. "
                f"Distribute the questions based on the difficulty level: {difficulty_level}. "
                f"If the difficulty level is easy, then {easy*100}% of the questions should be easy, "
                f"{medium*100}% medium, and {hard*100}% hard. "
                f"If the difficulty level is medium, then {easy*100}% easy, {medium*100}% medium, and {hard*100}% hard. "
                f"If the difficulty level is hard, then {easy*100}% easy, {medium*100}% medium, and {hard*100}% hard. "
                "Please provide the questions in the format: 'Question (Coding - Skill - Difficulty)'. "
                "Ensure each question is on a single line. "
                "dont provide any numbering to questions and no bold characters or special characters and no headings or side headings , just only question specified in example format below"
                "For example: 'Write a Python function to reverse a string. (Coding - Python - Medium)'.")

theory_prompt = (f"Generate {number_of_questions_theory} theory questions based on the primary skills (more priority): "
                f"{', '.join(primary_skills)} and secondary skills: {', '.join(secondary_skills)}. "
                f"Distribute the questions based on the difficulty level: {difficulty_level}. "
                f"If the difficulty level is easy, then {easy*100}% of the questions should be easy, "
                f"{medium*100}% medium, and {hard*100}% hard. "
                f"If the difficulty level is medium, then {easy*100}% easy, {medium*100}% medium, and {hard*100}% hard. "
                f"If the difficulty level is hard, then {easy*100}% easy, {medium*100}% medium, and {hard*100}% hard. "
                "Please provide the questions in the format: 'Question (Theory - Skill - Difficulty)'. "
                "Ensure each question is on a single line. "
                "dont provide any numbering to questions and no bold characters or special characters and no headings or side headings , just only question specified in example format below"
                "For example: 'Explain the concept of inheritance in Object-Oriented Programming. (Theory - OOP - Easy)'.")

design_prompt = (f"Generate {number_of_questions_design} design questions based on the primary skills (more priority): "
                f"{', '.join(primary_skills)} and secondary skills: {', '.join(secondary_skills)}. "
                f"Distribute the questions based on the difficulty level: {difficulty_level}. "
                f"If the difficulty level is easy, then {easy*100}% of the questions should be easy, "
                f"{medium*100}% medium, and {hard*100}% hard. "
                f"If the difficulty level is medium, then {easy*100}% easy, {medium*100}% medium, and {hard*100}% hard. "
                f"If the difficulty level is hard, then {easy*100}% easy, {medium*100}% medium, and {hard*100}% hard. "
                "Please provide the questions in the format: 'Question (Design - Skill - Difficulty)'. "
                "Ensure each question is on a single line."
                "dont provide any numbering to questions and no bold characters or special characters and no headings or side headings , just only question specified in example format below"
                " For example: 'Design a RESTful API for a library management system. (Design - API Design - Hard)'.")
