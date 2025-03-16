import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

def generate_definition(word):
    """ Génère une définition automatique pour un mot donné. """
    prompt = f"Donne une définition simple et claire du mot '{word}' en Hassaniya."

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]
