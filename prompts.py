# prompts.py

theory_prompt_template = """
Question: {question}
User Answer: {user_answer}
Fully Correct Answer: {correct_answer}

Generate feedback with scores for the given user answer, comparing it with the fully correct answer.
-always display score first ,only for user answer
- A correct answer (8-10 marks) should have all key parts present.
- A partial correct answer (4-5 marks) should have half of the key parts, concepts missing or wrongly written.
- A wrong answer (0-1 marks) should have the key parts or concepts completely wrongly written or missing.
- Give more weightage to concept understanding

"""

coding_prompt_template = """
Question: {question}
User Answer: {user_answer}
Fully Correct Answer: {correct_answer}

Generate feedback with scores for the given user answer, comparing it with the fully correct answer.
-always display score first ,only for user answer
- A correct answer (8-10 marks) should have optimal logic and concept perfectly written, ignoring small syntax errors.
- A partial correct answer (5-6 marks) either have slightly more than partial correct implementation of optimal logic or higher time complexity code, ignore small syntax errors.
- A wrong answer (0-1 marks) should have completely wrong logic.
- Give more weightage to logic and concept.
-always score first only for user answer
"""
