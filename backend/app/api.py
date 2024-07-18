from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

'''This is given as i have to connect the local host port of react to backend.'''
#Defining the CORS origins
origins = [                              
            "http://localhost:3000",         
            "localhost:3000",                                
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers=["*"]
)

#Get method route
@app.get("/",tags=["root"])
async def readRoot() -> dict:
    return  {"message":"Welcome User"}



todos = [
    {
        "id":"1",
        "item":"Hiii Shubham"
    },
    {
        "id":"2",
        "item":"Hiii Gajanan"
    },
    {
        "id":"3",
        "item":"Hiii Uparkar"
    }
    

]


#Get todo route
@app.get("/todo",tags=["todos"])
async def getTodos() -> dict:
    return  {"data":todos}


@app.post("/todo",tags=["todos"])
async def add_todo(todo:dict) -> dict:
    todos.append(todo)
    return{
        "data":{"Todo has been done"}
    }