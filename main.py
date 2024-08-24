from openai import OpenAI
from pathlib import Path
import notebooks.env as env

client = OpenAI(api_key=env.OPENAI_API_KEY)
response = client.files.create(
  file=Path('food_suggestion_prompt.jsonl'),
  purpose='fine-tune'
)

fine_tune_response = client.fine_tuning.jobs.create(
  training_file=response.id,  # Use the uploaded file's ID
  model="gpt-4o-mini-2024-07-18"       # Specify the model you want to fine-tune
)

print("Fine-tuning job started with ID:", fine_tune_response.id)