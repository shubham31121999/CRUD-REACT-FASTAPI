from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


#Defining the CORS origins
origins = [                              '''This is given as i have to connect the local host port of react to backend.'''
            "http://localhost:3000",         
            "localhost:3000"                                
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
