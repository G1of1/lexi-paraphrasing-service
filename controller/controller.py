from fastapi import APIRouter
from service import service
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from pydantic import BaseModel
from typing import Optional

class SummarizeRequest(BaseModel):
    text: str
    level: Optional[str] = None


router = APIRouter()

@router.post("/paraphrase-standard")
async def paraphrase_standard(request: SummarizeRequest):
    try:
        data = await service.paraphrase_standard(request)
        if data.get('error'):
            return JSONResponse(status_code=400, content=data)
        return JSONResponse(status_code=200, content=data)
    except Exception as e:
        print(f"An error occurred: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})

@router.post('/paraphrase-simplify')
async def paraphrase_simplify(request: SummarizeRequest):
    try:
        data = await service.paraphrase_simplify(request)
        if data.get('error'):
            return JSONResponse(status_code=400, content=data)
        return JSONResponse(status_code=200, content=data)
    except Exception as e:
        print(f"An error occured: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})

@router.post('/paraphrase-shorten')
async def paraphrase_shorten(request: SummarizeRequest):
    try:
        data = await service.paraphrase_shorten(request)
        if data.get('error'):
            return JSONResponse(status_code=400, content=data)
        return JSONResponse(status_code=200, content=data)
    except Exception as e:
        print(f"An error occured: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})

@router.post('/paraphrase-expand')
async def paraphrase_expand(request: SummarizeRequest):
    try:
        data = await service.paraphrase_expand(request)
        if data.get('error'):
            return JSONResponse(status_code=400, content=data)
        return JSONResponse(status_code=200, content=data)
    except Exception as e:
        print(f"An error occured: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})

@router.post('/paraphrase-academic')
async def paraphrase_academic(request: SummarizeRequest):
    try:
        data = await service.paraphrase_academic(request)
        if data.get('error'):
            return JSONResponse(status_code=400, content=data)
        return JSONResponse(status_code=200, content=data)
    except Exception as e:
        print(f"An error occured: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})

@router.post('/paraphrase-formal')
async def paraphrase_formal(request: SummarizeRequest):
    try:
        data = await service.paraphrase_formal(request)
        if data.get('error'):
            return JSONResponse(status_code=400, content=data)
        return JSONResponse(status_code=200, content=data)
    except Exception as e:
        print(f"An error occured: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})