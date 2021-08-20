from fastapi import APIRouter, Body

from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from server.database import (
#    add_sentence,
#    delete_sentence,
    retrieve_sentences,
    retrieve_sentence,
    update_aspect,
	retrieve_pages,
#	add_aspect,
)

from server.models.dataformat import (
    ErrorResponseModel,
    ResponseModel,
    DataSchema,
    UpdateDataModel,
	AddEntityModel,
	AddAspectModel,
)

router = APIRouter()



@router.get("/{sentence_id}", response_description='Sentences retrieved')
async def get_one_data(sentence_id:str):
	sentence = await retrieve_sentence(sentence_id)
	if sentence:
		return ResponseModel(sentence, "Sentences data retrieved successfully")
	return ResponseModel(sentence, "Empty list returned")

#--------------------------------
@router.get("/", response_description='Sentences retrieved')
async def get_data():
    sentences = await retrieve_sentences()
    if sentences:
        return ResponseModel(sentences, "Sentences data retrieved successfully")
    return ResponseModel(sentences, "Empty list returned")
#--------------------------------
@router.put("/{sentence_id}", response_description='Update Aspect')
async def update_data(sentence_id: str, req: UpdateDataModel=Body(...)):
	req = {k: v for k, v in req.dict().items() if v is not None}
	updated_aspect = await update_aspect(sentence_id, req)
	if updated_aspect:
		return ResponseModel(
		"Aspect with ID: {} update is successful".format(sentence_id),
		"Aspect content update successfully",
		)
	return ErrorResponseModel(
		"An error occurred, update faild!",
		404,
	)

#--------------------------------
