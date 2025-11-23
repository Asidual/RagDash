from fastapi import APIRouter

router = APIRouter()

@router.get("/", tages=["Health"])
async def health_root():
    return {"message": "Health endpoint is working."}
