#prompts_evaluate.py

theory_prompt_template = """
Question: {question}
User Answer: {user_answer}

-**Always display the score first for user answer based on its question. This is mandatory.**
-Focus on the thoroughness and accuracy of the technical information provided. 
-Minor omissions such as practical guidance should not heavily impact the overall score.
-Ensure the answer includes detailed explanations and additional context where necessary related to the question.
-A correct answer (8-10 marks) should have most of the key parts and demonstrate an in-depth understanding of the topic.
-A partially correct answer (4-6 marks) should have some key parts but may have minor inaccuracies or omissions.
-A wrong answer (0-3 marks) should have significant inaccuracies or be missing key parts.
-Emphasize concept understanding but consider missing details more critically to lower the overall score.
"""


coding_prompt_template = """
Question: {question}
User Answer: {user_answer}

-**Always display the score first, based on the user answer code. This is mandatory.**
- Focus on the overall algorithm, its correctness, and efficiency. Minor syntax or initialization details should not affect the overall score significantly.
-Minor best practice issues that do not affect core functionality should not heavily impact the score.(reduce atmost 1 mark)
- A correct answer (8-10 marks) should have optimal logic and concept perfectly written.
- A partial correct answer (5-6 marks) either have slightly more than partial correct implementation of optimal logic or higher time complexity code.
- A wrong answer (0-1 marks) should have completely wrong logic.
- Give more weightage to logic and concept.

"""


design_prompt_template = """
Question: {question}
User Answer: {user_answer}

-**Always display the score first, based on the user answer code. This is mandatory.**
- Focus on the overall algorithm, its correctness, and efficiency. Minor syntax or initialization details should not affect the overall score significantly.
-Minor best practice issues that do not affect core functionality should not heavily impact the score.(reduce atmost 1 mark)
- A correct answer (8-10 marks) should have optimal logic and concept perfectly written.
- A partial correct answer (5-6 marks) either have slightly more than partial correct implementation of optimal logic or higher time complexity code.
- A wrong answer (0-1 marks) should have completely wrong logic.
- Give more weightage to logic and concept.

"""