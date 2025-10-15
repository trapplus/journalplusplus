import httpx
import asyncio
import logging

from fastapi import HTTPException

logger = logging.getLogger(__name__)

class csv_manager:
    def __init__(self):
        self.API_URL = "https://msapi.top-academy.ru/api/v2"
        self.csrf_token: str

    async def get_csrf_token(self):
        async with httpx.AsyncClient(base_url=self.API_URL) as client:

            # Geting CSRF token 
            r = await client.get("/auth/login")
            csrf_token = r.cookies.get("_csrf")
            if r.cookies.get("_csrf") != csrf_token:
                logger.error(f"Invalid CSRF token. csrf:{csrf_token}")
                raise HTTPException(status_code=403, detail="Invalid CSRF token")
            logger.info(f"Valide scrf! csrf: {csrf_token}")
