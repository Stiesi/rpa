from fastapi import FastAPI
import numpy as np
app = FastAPI()


def add(a,b):
    return a+b

@app.get("/")
async def root():    
    return "Hello World! MannJens"


@app.post("/add/")
async def getadd(a: float, b:float):    
    c=add(a,b)
    return { "c" : c }