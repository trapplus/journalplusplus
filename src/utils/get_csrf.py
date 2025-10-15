import httpx
import asyncio
import logging

from fastapi import HTTPException

logger = logging.getLogger(__name__)


class csv_manager:
    def __init__(self):
        self.API_URL = "https://msapi.top-academy.ru/api/v2"

    async def get_csrf_token(self) -> str:
        async with httpx.AsyncClient(base_url=self.API_URL) as client:

            # Geting CSRF token 
            r = await client.get("/auth/login")
            csrf_token = r.cookies.get("_csrf")
            if not csrf_token:
                logger.error(f"Invalid CSRF token. csrf_str:{csrf_token}")
                raise HTTPException(status_code=403, detail="Invalid CSRF token")
            logger.debug(f"csrf returned:{csrf_token}")
            return csrf_token 
