LLM Wrapper App
This project deploys a Language Model (LLM) wrapper as a Serverless function using Flask and Vercel.
The wrapper interacts with the OpenAI API to generate text based on user prompts while handling rate limit errors, maintaining conversation history, and formatting prompts.

Features
1.Rate Limit Handling: The wrapper handles rate limit errors by retrying after waiting for a specific period.

2.Conversation History: The wrapper maintains the history of the conversation to ensure a sequence of user inputs and prompts.

3.Token Limit: The conversation is formatted to ensure it doesn't exceed the token limit of the model.

4.Formatted Prompts: The prompts are dynamically updated at each step of the conversation to include variables while maintaining the history.

Execution Image

![image](https://github.com/Vivek17020/LLM-Wrapper/assets/116427464/1e41586c-9057-4ecb-aaba-bd999bc208fb)
