from pymongo import MongoClient
#from bson.objectid import ObjectId

client = MongoClient('mongodb://admin:widmwidm9527@140.115.54.44:27017') #
db = client['ETL-api-creator']
collection = db['KKBOX_Label_Ken']

async def retrieve_sentences():
	sentences = []
	for sentence in collection.find():
		sentences.append(sentence_helper(sentence))
	return sentences


async def retrieve_sentence(sentence_id: str):
	sentence = collection.find_one({"sentence_id": sentence_id})
	if sentence:
		return sentence_helper(sentence)
	return {'sentence':'can not find this sentence with id'+sentence_id}
		
async def update_aspect(sentid: str, data: dict): 
	# Return false if an empty request body is sent.
	if len(data) < 1:
		return False
	sentence = collection.find_one({"sentence_id":str(sentid)})
	if sentence:
		updated_sentence = collection.update_one(
			{"sentence_id": str(sentid)}, {"$set": data}
		)
		if updated_sentence:
			return True
	return False
	
async def retrieve_pages(): 
	length = await retrieve_sentences()
	return len(length)
	
def sentence_helper(data) -> dict:
	return {
		'sentence_id':str(data['sentence_id']),
		'sentence': str(data['sentence']),
		'aspect': data['aspect'],
		'time': data['time'],
	}