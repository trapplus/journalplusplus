import httpx
import logging
from src import container as cont
from fastapi import HTTPException

logger = logging.getLogger(__name__)

class auth:
    def __init__(self):
        self.APPLICATION_KEY = cont.data.APP_KEY
        self.API_URL = cont.data.BASE_API_URL
        
    async def _get_csrf_token(self) -> str:
        async with httpx.AsyncClient(base_url=self.API_URL) as client:

            # Geting CSRF token 
            r = await client.get("/auth/login")

            csrf_token = str(r.cookies.get("_csrf"))

            if not csrf_token:
                logger.error(f"Invalid CSRF token. csrf_str:{csrf_token}")
                raise HTTPException(status_code=403, detail="Invalid CSRF token")
            
            logger.debug(f"csrf returned:{csrf_token}")
            return csrf_token


    async def get_jwt_token(self,
                            username: str, 
                            password: str
                            ) -> list[str, str]:
            
        auth_data = {
            "application_key": self.APPLICATION_KEY,
            "username": str(username),
            "password": str(password),
            "id_city": None,
        }

        headers = {
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0",
                    "Accept": "application/json, text/plain, */*",
                    "Content-Type": "application/json",
                    "Referer": "https://journal.top-academy.ru/",  
                    "Origin": "https://journal.top-academy.ru",
                    "X-CSRF-TOKEN": auth._get_csrf_token(),
                }
        
        logger.debug(f"Auth headers: \n{headers}")
        
        async with httpx.AsyncClient(base_url=self.API_URL) as client:
                  

            # Auth and return JWT
            resp = await client.post(
                "/auth/login", json=self.auth_data, headers=headers)
            
            # raise not standard http code (404, 403, 503 and more..)
            resp.raise_for_status()

            jwt_token = resp.json()["access_token"]

            if not jwt_token:
                logger.error(f"Invalid JWT token. jwt_str:{jwt_token}")
                raise HTTPException(status_code=401, detail="JWT token is missing")
            
            return jwt_token
