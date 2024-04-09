
import openai

openai.api_key = "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"

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "write a cover letter for a company"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)




