from fastapi import FastAPI, Request

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from server.routes.sentence2 import router as DataRouter
from server.database2 import retrieve_sentence,retrieve_pages

app = FastAPI()

app.include_router(DataRouter, tags=['Data'], prefix='/data')

template = Jinja2Templates(directory="templates")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Homepage"}

@app.get("/{sentence_id}", response_class=HTMLResponse, tags=['HTML'])
async def read(request: Request, sentence_id:str):
	#sentence = await retrieve_sentence(sentence_id)
	total_sentence = await retrieve_pages()
	return template.TemplateResponse("template.html", {"request": request, "sentence_id": sentence_id, "total_sentence":total_sentence})

