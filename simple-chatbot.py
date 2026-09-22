from google import genai

client = genai.Client()

chat = client.chats.create(
    model="gemini-3.6-flash",
    config={"system_instruction": "Limit your answer to one sentence and say meow at the very end."}
)

print("Type 'quit' or 'exit' to stop.")

while True:
    user_prompt = input("You: ")

    if user_prompt.lower() in ['quit', 'exit']:
        print("Goodbye!")
        break

    response = chat.send_message(user_prompt)

    print(f"Gemini: {response.text}\n")