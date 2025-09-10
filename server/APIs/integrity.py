import asyncio
import httpx
from fastapi import APIRouter, HTTPException
from config import INTEGRITY_CHECK_URL_LIST as urls

router = APIRouter(prefix="/integrity", tags=["integrity"])

@router.get("/integrity")
async def check_external_resourses_integrity():

    async with httpx.AsyncClient(timeout=10.0) as client:
        tasks = [client.get(url) for url in urls]
        responses = await asyncio.gather(*tasks, return_exceptions=True)

    failed = []
    for url, resp in zip(urls, responses):
        if isinstance(resp, Exception):
            failed.append({"url": url, "error": str(resp)})
        elif resp.status_code != 200: # type: ignore
            failed.append({"url": url, "status": resp.status_code}) # type: ignore
    if failed:
        raise HTTPException(status_code=502, detail={"failed": failed})
    
    return {"status": "ok"}
