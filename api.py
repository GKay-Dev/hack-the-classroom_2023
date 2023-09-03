import openai

api_key = ' enter key here '


def grade_essay(essay_text):
    prompt = """
                Please analyze and grade the following essay

                Consider the following criteria and provide a percentage and letter grade (e.g., A, B, C, D, F) along with detailed feedback:
                
                1. **Content and Understanding (40%):** Assess the depth of understanding of the topic, the accuracy of information presented, and the overall quality of the arguments and supporting evidence.

                2. **Organization and Structure (20%):** Evaluate the essay's overall organization, clarity of thesis statement, logical flow of ideas, and transitions between paragraphs.

                3. **Coherence and Clarity (20%):** Examine the coherence and clarity of the writing, including sentence structure, clarity of expression, and the use of appropriate vocabulary.

                4. **Grammar and Mechanics (20%):** Check for grammatical errors, spelling mistakes, punctuation issues, and adherence to standard conventions of written English.


                Please provide specific feedback on strengths and weaknesses in each of these areas and justify the assigned grade. Your evaluation should be comprehensive and constructive, offering suggestions for improvement where necessary.

                Essay:
    {}
    """.format(essay_text)

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=3000,  # equals around 350ish words not including prompt
            api_key=api_key,
            #other avilable options are temperature (randomness) and top_p for output diversity 
        )

        graded_essay = response.choices[0].text
        print(graded_essay)
    except Exception as error:
        print(f"An error occurred: {str(error)}")

if __name__ == "__main__": 
    user_input = input("Enter the essay text: ")
    grade_essay(user_input)
