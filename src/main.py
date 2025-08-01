from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

def main():
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0", # fixme pydantic-settings
        port=8000, # fixme pydantic-settings
        reload=True, # fixme pydantic-settings

    )


if __name__ == "__main__":
    main()
