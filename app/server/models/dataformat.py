from typing import Optional

from pydantic import BaseModel, Field


class DataSchema(BaseModel):
	sentence: str = Field(...)
	sentence_id: str = Field(...)
	aspect: list = Field(...)
	time: int = Field(...)
	class Config:
		schema_extra = {
			'example':{
				'sentence': 'this is test sentence',
				'sentence_id': '123456789',
				'aspect':'[]',
				'time':'0',
			}
		}

class UpdateDataModel(BaseModel):
	aspect: Optional[list]
	time: Optional[int]
	class Config:
		schema_extra = {
			'example':{
				'aspect':[{
					'product_name': "冷氣",
					'product_brand': "國際牌",
					'aspect_category': "品質" ,
					'aspect_term': "過濾",
					'opinion_word': "不是很好" ,
					'sentiment': "負向"				
				},{
					'product_name': "冷氣",
					'product_brand': "日立",
					'aspect_category': "品質" ,
					'aspect_term': None,
					'opinion_word': "很好" ,
					'sentiment': "正向"								
				  }
				]
			}
		}

class AddEntityModel(BaseModel): #unusable
	entity_name: Optional[str]
	entity_brand: Optional[str]
	class Config:
		schema_extra = {
			'example':{
				'entity_name': 'TV',
				'entity_brand': 'Samsung',
				
			}
		}
class AddAspectModel(BaseModel):
	product_name: Optional[str]
	product_brand: Optional[str]
	aspect_category: Optional[str]
	aspect_term: Optional[str]
	opinion_word: Optional[str]
	sentiment: Optional[str]
	product_name_start: Optional[int]
	product_brand_start: Optional[int]
	aspect_term_start: Optional[int]
	opinion_word_start: Optional[int]
	class Config:
		schema_extra = {
			'example':{
				'product_name': "冷氣",
				'product_brand': "國際牌",
				'aspect_category': "品質" ,
				'aspect_term': "過濾",
				'opinion_word': "不是很好" ,
				'sentiment': "負向"
			}
		}
	
def ResponseModel(data, message):
    return {
        "data": [data],
        "message": message,
    }


def ErrorResponseModel(error, message):
    return {"error": error, "message": message}