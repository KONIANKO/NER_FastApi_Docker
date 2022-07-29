import spacy
from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()
nlp = spacy.load("en_core_web_sm")

class Item(BaseModel):
    data: str

# output = {}

# @app.get("/")
# def instruction():
#     #rendpoint."}
#     return {"Data": "Test"}

@app.post("/extract-entities")
def extract_entities(item: Item):
    
    doc = nlp(str(item.data))

    entities = {}
    for ent in doc.ents:
        #entities[ent.text] = ent.label_
        entities[ent.label_] = ent.text
  
    return {"response": entities}
