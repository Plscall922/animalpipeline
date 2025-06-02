import os
import random
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Cute animal list
cute_animals = [
    "red panda", "quokka", "otter", "penguin", "hedgehog",
    "pika", "capybara", "koala", "baby elephant", "arctic fox",
    "fennec fox", "sea otter", "slow loris", "fluffy bunny", "baby seal"
]

# Pick one randomly
chosen_animal = random.choice(cute_animals)

# Construct prompt for a short cute post
prompt = (
    f"Write a heartwarming, adorable fact or mini-story about a {chosen_animal}. "
    "Keep it under 500 characters. It should be short enough for an Instagram or Telegram post."
)

# Messages for chat
messages = [
    {"role": "system", "content": "You write extremely short and cute animal facts or stories for social media."},
    {"role": "user", "content": prompt}
]

# Call OpenAI
try:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0.8,
        max_tokens=200
    )
    output = response.choices[0].message.content.strip()

    print(f"🐾 Chosen animal: {chosen_animal}\n")
    print("💖 Post-ready text:\n")
    print(output)

except Exception as e:
    print("❌ Error:", e)
