if __name__ == "__main__":
	import uvicorn
	uvicorn.run("server.app2:app", host="0.0.0.0", port=8001, reload=True)