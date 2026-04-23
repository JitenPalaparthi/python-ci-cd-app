from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Python CI/CD Demo", version="1.0.0")


class EchoRequest(BaseModel):
    message: str


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Hello from Python CI/CD demo"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/echo")
def echo(payload: EchoRequest) -> dict[str, str]:
    return {"echo": payload.message}
