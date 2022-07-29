# 
FROM python:3.9

# 
WORKDIR /app

# 
COPY ./requirements.txt .

# 
RUN pip install -r ./requirements.txt

RUN python -m spacy download en_core_web_sm

# 
# COPY ./app /code/app
COPY . .

EXPOSE 8000
# 
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]