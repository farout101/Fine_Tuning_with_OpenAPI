from pydantic import BaseModel
from openai import OpenAI

client = OpenAI()

from pydantic import BaseModel
from typing import List

class Dish(BaseModel):
    name: str
    calories: float
    category: str
    ingredients: List[str]
    how_to_cook: str
    meal_time: str

class Meal(BaseModel):
    main_dish: Dish
    side_dish: Dish

class ResponseModel(BaseModel):
    breakfast: Meal
    lunch: Meal
    dinner: Meal

class FullResponse(BaseModel):
    response: ResponseModel

completion = client.beta.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=[
        {"role": "system", "content": """{
            "weight": 70,
            "height": 180,
            "age": 30,
            "diseases": ["None"],
            "allergies": ["None"],
            "gender": "Male",
            "exercise": "High"
            }
            """ },
        {"role": "user", "content": "..."}
    ],
    
    response_format = FullResponse,
)

research_paper = completion.choices[0].message.parsed

print(research_paper)