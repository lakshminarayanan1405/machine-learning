import openai
openai.api_key = "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"
openai.api_base = "https://openrouter.ai/api/v1"
user_input = input("You: ")
reply=""
response = openai.ChatCompletion.create(
        model="mistralai/mistral-7b-instruct", # or another supported model
        messages = [
        {"role": "system", "content": "You are an expert translator."},
        {"role": "user", "content": "English: Good morning\nFrench: Bonjour"},
        {"role": "user", "content": f"English: {user_input}\nFrench:"}]
    )
reply = response['choices'][0]['message']['content']
print(f"Chatbot: {reply}\n")
