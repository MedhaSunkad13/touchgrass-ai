import ollama

available_time = input("How much time do you have? ")
mood = input("How are you feeling? ")
interest = input("What do you enjoy doing outdoors? ")

prompt = f"""
Create an outdoor activity for someone who has {available_time},
is feeling {mood}, and enjoys {interest}.

The activity should encourage them to stay away from screens.

Rules:
- The activity MUST be centered around the user's outdoor interest.
- Treat the user's outdoor interest as the main activity, not just inspiration.
- The Duration must be exactly {available_time}.
- Never choose a different duration.
- Use the full available time.
- The activity must be completely screen-free.
- Always provide a specific screen rule. Never write "None".
- Do not suggest phones, cameras, social media, filming, apps, or photography.
- Keep the response short and practical.
- Put each step on a separate numbered line.
- Do not put instructions before the numbered steps.
- Do not ask any follow-up questions.

Output exactly in this format:

Activity:
Duration:
Steps:
1.
2.
3.

Screen Rule:
"""

response = ollama.chat(
    model="gemma3:1b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(response.message.content)

# models = ollama.list()

# print("Available models:")

# for model in models.models:
#     print(model.model)