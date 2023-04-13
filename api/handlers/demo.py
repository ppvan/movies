from fastapi import APIRouter

from api.responses.detail import DetailMessage

router = APIRouter(prefix="/api/v1/demo")


@router.get("/", response_model=DetailMessage)
def hello_world():
    return DetailMessage(message="hello world")
