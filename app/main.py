if __name__ == "__main__":
	import uvicorn
	uvicorn.run("server.app:app", host="0.0.0.0", port=7999, reload=True)