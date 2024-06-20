from openai import OpenAI

client = OpenAI()
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do som
# ething like:
client = OpenAI(

    api_key="sk-proj-OIbY24fgySDRTpGsEPxMT3BlbkFJKqOIzvgcBkiuvAIxriwq"
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named kumar, skilled in skilled in general taskslike Alexa and google cloude."},
    {"role": "user", "content": "What is coding?."}
  ]
)

print(completion.choices[0].message.content)