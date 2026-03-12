#====================================
# AI Sentiment Analyzer
#====================================
# analyses text and return structured data
# built with python and googl gemini api
# =================================

from google import genai
import json

# setup

client = genai.Client(api_key="AIzaSyAwTgh0zT9PCUZwNivIHdzAfJnDNc9hJfE")

# welcome message

print("=" * 50)
print("     AI SENTIMENT ANALYZER - by NJR")
print("=" * 50)
print("analyzes any sentences and returns:")
print(" - sentiment (positive/negative/mixed)")
print(" - emotion (happy/sad/angry/neutral)")
print(" - summary")
print(" - score out of 10")
print("=" * 50)

# get user input

user_input = input("\nEnter a sentence for analysis: ")

# send to ai

prompt = f"""analyze the sentence and return only a json object.
no extra text, just json!

sentence = {user_input}

Return exctly this format:
{{
  "sentiment": "positive/negative/mixed",
  "emotion": "happy/sad/angry/neutral",
  "summary": "a short summary of the sentence",
  "score": a number from 1 to 10
}}"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)


# parse and display results

raw_text = response.text
raw_text = raw_text.replace("```json", "").replace("```", "").strip()
result = json.loads(raw_text)

print("\n" + "=" * 50)
print("         ANALYSIS RESULTS")
print("=" * 50)
print(f"  Sentiment : {result['sentiment']}")
print(f"  Emotion   : {result['emotion']}")
print(f"  Summary   : {result['summary']}")
print(f"  Score     : {result['score']}/10")
print("=" * 50)