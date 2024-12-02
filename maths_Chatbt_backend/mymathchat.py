# import libraries
import ollama
import ast

# function to chat
def maths_chatbot():
    # start the chatbot and inform the user
    print("Maths Bot: I'll help you solve math problems step-by-step.\n")

    # system prompt: defines how the assistant should respond with step-by-step solutions
    system_prompt = """
        You are a helpful assistant who provides step-by-step solutions to math problems.

        For a given math problem,

        Output only a dictionary containing two lists.
        Store the steps to solve the problem in one list.
        Store the answer for each step in the other list.
        For steps that we do not need an answer, store an empty string "". 

        Example 1:- 
        user: Solve 3 + 4 * 2
        assistant: {
                    "steps": ["Multiply 4 by 2.", "Add 8 to 3."],   
                    "answer": [8, 11] 
                    }
        
        Example 2:- 
        user: Solve 7x + 14 = 0
        assistant: {
                    "steps": ["Subtract 14 from both sides.", "Divide by 7."],   
                    "answer": ["", -2] 
                    }

        Do not output anything other than the dictionary, no explanation needed.

        Scope Limitation:
            Do not respond to any queries that are not related to math problems.
        """

    # initialize conversation with the system prompt
    conversation = [{'role': 'system', 'content': system_prompt}]

    # get user input for math problem
    user_input = input("User: ")
    conversation.append({'role': 'user', 'content': user_input})

    # get response from the chatbot model
    response = ollama.chat(model='mathstral:latest', messages=conversation)
    answer = response['message']['content']
    result = ast.literal_eval(answer)  # parse response into dictionary
    steps = result["steps"]  # list of steps
    answers = result["answer"]  # list of answers for each step

    # step prompt: defines how to compare answers
    step_prompt = """
        You will be given a correct answer and the user's answer.
        You have to compare the user's answer with the correct answer and output like below. Thoroughly consider the following instructions. 

            If it is correct, output as "Correct.".
            If it is incorrect, output as "Wrong, the correct answer is answer.".

        Scope Limitation:
            Do not output anything other than what you're instructed.
        """

    # adaptive feedback prompt: generates guidance if the user's answer is wrong
    adaptive_feedback_prompt = """
        You will be provided with a step description, a correct answer, and the user's incorrect answer. Your task is to:
        - Explain why the user's answer is wrong.
        - Provide guidance on how to arrive at the correct answer.
        Respond concisely and clearly.
        
        Example 1:- 
        step: "Multiply 4 by 2."
        user answer: 6
        correct answer: 8
        response: "The user's answer is incorrect because multiplying 4 by 2 gives 8, not 6."

        Example 2:- 
        step: "Subtract 14 from both sides."
        user answer: -10
        correct answer: -14
        response: "The user's answer is incorrect because subtracting 14 from both sides results in -14, not -10."

        Scope Limitation:
            Do not output anything other than the concise feedback.
        """

    # loop through each step and compare answers
    for index, step in enumerate(steps):
        print(f"Maths Bot: Perform this step, {step.lower()}\n")

        # get user input for each step
        step_user_input = input("User: ")

        # prepare conversation for checking user's answer
        step_conversation = [{'role': 'system', 'content': step_prompt}]
        step_user_final_input = f"user answer = {step_user_input}, correct answer = {str(answers[index])}"

        if str(answers[index]) != "":  # check if answer is not empty
            step_conversation.append({'role': 'user', 'content': step_user_final_input})

            # get feedback on user's answer
            step_response = ollama.chat(model='phi3:latest', messages=step_conversation)
            step_feedback = step_response['message']['content']

            if "Wrong" in step_feedback:
                # If user's answer is wrong, generate adaptive feedback
                adaptive_feedback_conversation = [
                    {'role': 'system', 'content': adaptive_feedback_prompt},
                    {
                        'role': 'user',
                        'content': f"step: {step}\nuser answer: {step_user_input}\ncorrect answer: {str(answers[index])}",
                    },
                ]

                # get adaptive feedback response
                adaptive_feedback_response = ollama.chat(
                    model='phi3:latest', messages=adaptive_feedback_conversation
                )
                adaptive_feedback = adaptive_feedback_response['message']['content']
                print(f"Maths Bot: {adaptive_feedback}\n")
            else:
                print(f"Maths Bot: {step_feedback}\n")

# run chatbot
if __name__ == "__main__":
    maths_chatbot()
