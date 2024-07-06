# prompts.py

theory_prompt_template = """
Question: {question}
User Answer: {user_answer}
Fully Correct Answer: {correct_answer}

Generate feedback with scores for the given user answer, comparing it with the fully correct answer.
-always display score first ,only for user answer
-Focus on the thoroughness and accuracy of the technical information provided. Minor omissions such as practical guidance should not heavily impact the overall score.
- A correct answer (8-10 marks) should have more than 80 percent of the key parts present.
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
- Focus on the overall algorithm, its correctness, and efficiency. Minor syntax or initialization details should not affect the overall score significantly.
-Minor best practice issues that do not affect core functionality should not heavily impact the score.(reduce atmost 1 mark)
- A correct answer (8-10 marks) should have optimal logic and concept perfectly written.
- A partial correct answer (5-6 marks) either have slightly more than partial correct implementation of optimal logic or higher time complexity code.
- A wrong answer (0-1 marks) should have completely wrong logic.
- Give more weightage to logic and concept.

"""
