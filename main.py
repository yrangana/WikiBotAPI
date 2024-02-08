import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

from scrapebot.bot import get_wikipedia_summary

app = FastAPI()


class WikipediaSummaryRequest(BaseModel):
    title: str
    sentences: int


@app.post("/wikipedia_summary")
async def wikipedia_summary(request: WikipediaSummaryRequest):
    summary = get_wikipedia_summary(request.title, request.sentences)
    return JSONResponse(content=jsonable_encoder(summary))


@app.get("/")
async def root():
    return {"message": "WikiBot API"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)
