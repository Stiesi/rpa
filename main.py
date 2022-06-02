#from typing import List
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

import numpy as np
import pandas as pd
from scipy.optimize import leastsq
app = FastAPI()


def add(a,b):
    return a+b


@app.post("/add/")
async def getadd(a: float, b:float):    
    c=add(a,b)
    return { "c" : c }

@app.post("/files/")
async def create_files(files: list[bytes]):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(files: list[UploadFile]):
    return {"filenames": [file.filename for file in files]}


@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)