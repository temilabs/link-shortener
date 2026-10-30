from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, backend!"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/search")
def search(q: str, limit: int = 10):
    return {"q": q, "limit": limit}


class LinkCreate(BaseModel):
    url: HttpUrl
    custom_code: str | None = None


@app.post("/links", status_code=201)
def create_link(link: LinkCreate):
    return {"url": str(link.url), "custom_code": link.custom_code}
