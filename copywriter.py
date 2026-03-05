from openai import OpenAI
import os
import json

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None
#client = None

if OPENAI_API_KEY:
    client = OpenAI(api_key=OPENAI_API_KEY)
else:
    print("OPENAI_API_KEY is not set, GPT disabled")





client = OpenAI(api_key=OPENAI_API_KEY)

def generate_marketing_copy(product):

    prompt = f"""
    Create TikTok viral ad copy for product: {product}
    """

    r = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return r.choices[0].message.content
