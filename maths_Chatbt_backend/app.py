# import libraries
import ollama
import ast

# function to chat
def maths_chatbot():
    # start
    print("Maths Bot: I'll help you solve math problems step-by-step.\n")

    # set system prompt
    system_prompt = """
        You are a helpful assistant who provides step-by-step solutions to math problems.

        For a give math problem,

        Output only a dictionary containing two lists.
        Store the steps to solve the problem in one list.
        Store the answer for the each step in the other list.
        For the steps that we do not need an answer, you can store an empty string "". 

        Example 1:-
        user: Solve 3 + 4 * 2
        assistant: {
                    "steps": ["Multiply 4 by 2.", "Add 8 to 3."],   
                    "answer"" [8, 11] 
                    }
        
        Example 2:-
        user: Solve 7x + 14 = 0
        assistant: {
                    "steps": ["Subtract 14 from both sides.", "Divide by 7."],   
                    "answer"" ["", -2] 
                    }
        
        Do not output anything than the dictionary, no explanation needed.

        Scope Limitation:
            Do not respond to any queries that are not related to math problems.
        """

    # conversation
    conversation = [{'role': 'system', 'content': system_prompt}]

    # get user input
    user_input = input("User: ")
    conversation.append({'role': 'user', 'content': user_input})

    # get response
    response = ollama.chat(model='mathstral:latest', messages=conversation)
    answer = response['message']['content']
    result = ast.literal_eval(answer)
    steps = result["steps"]
    answers = result["answer"]

    # set step prompt
    step_prompt = """
        You will be given a correct answer and the user's answer.
        You have to compare the user's answer with the correct answer and output like below. Thorouly consider the following instructions. 

            If it is correct, output as "Correct.".

            If it is incorrect, output as "Wrong, the correct answer is answer.".
        
        Example 1:-
        user: user answer = 8, correct answer = 8
        "Correct"
        
        Example 2:-
        user: user answer = 8, correct answer = 4
        "Wrong, the correct answer is 4."

        Scope Limitation:
            Do not output anything other than what you're instructed.
        """

    # chat loop
    for index, step in enumerate(steps):
        step_conversation = []

        print(f"Maths Bot: Perform this step, {step.lower()}\n")

        step_user_input = input("User: ")

        step_conversation = [{'role': 'system', 'content': step_prompt}]

        step_user_final_input = f"user answer = {step_user_input}, correct answer = {str(answers[index])}"

        if str(answers[index]) != "":

            step_conversation.append({'role': 'user', 'content': step_user_final_input})

            step_response = ollama.chat(model='phi3:latest', messages=step_conversation)

            step_feedback = step_response['message']['content']

            print(f"Maths Bot: {step_feedback}\n")

# run chatbot
if __name__ == "__main__":
    maths_chatbot()