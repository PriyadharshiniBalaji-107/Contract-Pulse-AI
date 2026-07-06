import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_contract(text):
    prompt = f"""
    Extract key contract information:

    Return JSON:
    - parties
    - renewal_date
    - payment_terms
    - obligations
    - risks

    Contract:
    {text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
