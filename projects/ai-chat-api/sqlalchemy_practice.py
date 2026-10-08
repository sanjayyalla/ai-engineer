from fastapi import FastAPI, File, UploadFile
from pydantic import ConfigDict,BaseModel

class LLMRequest(BaseModel):
    model_config =  ConfigDict(
        extra="forbid",
        
    )

app = FastAPI()


@app.post("/upload")
def upload_document(file : UploadFile = File(...)):
    content = file.read()
    return {"data":content}