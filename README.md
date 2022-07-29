## This is a simple NER tool for English using FastAPI and Docker.

### This project concentrates not on a good NER performance, but on the setup with the FastAPI and Docker.

* create virtual environment venv and activate it

* use docker commands:
    * docker-compose build
    * docker-compose up 
    * docker-compose down (when you are finished)

* after running the application go to http://localhost:8000/docs
* use the "/extract-entities" endpoint:

1. hit the endpoint "/extract-entities"
2. hit the "try it out" button on the right
3. replace "string" in

  `
  {
  "data": "string"
  }
  `

  with your string, e.g. 

  `
  {
  "data": "Hello, my namme is Tom, I am in New York. I have 5 Dollars in my pocket and I don't know what to do."
  }
  `

  4. In the "response" section below you will find your output. In this case, it will be:

  `
  {
    "response": {
      "PERSON": "Tom",
      "GPE": "New York",
      "MONEY": "5 Dollars"
      }
  }
  `
  
## Task

Нужно написать сервис для поиска интентов во входящем предложении.
Приложение должно представлять собой веб сервис, обернутый в докер контейнер.

Запрос:

`
{ 
  "data":"Привет! Меня зовут Георгий, я хочу улететь на марс." 
}
`

Ответ:

`
{ 
  "response":
    [
      "name":"Георгий",
      "destination":"марс",
      "work":"инженер",
      "time":"12:30", 
    ]
}
`

Можно использовать все что угодно (duckling и etc..) кроме готовые сервисов. 