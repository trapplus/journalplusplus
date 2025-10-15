import asyncio
import logging
import httpx
import datetime
from fastapi import HTTPException

logger = logging.getLogger(__name__)

class journal_service:
    def __init__(self) -> None:
        self.APP_KEY = "6a56a5df2667e65aab73ce76d1dd737f7d1faef9c52e8b8c55ac75f565d8e8a6"
        self.API_URL = "https://msapi.top-academy.ru/api/v2"
        self.date =  datetime.date.today()

    async def get_schedule_data(self, 
            username: str,
            password: str,
            ) -> dict:
        
        # setup auth data
        self.auth_data = {
            "application_key": self.APP_KEY,
            "username": username,
            "password": password,
            "id_city": None,
        }
        
        # Create session for getting data is faster
        async with httpx.AsyncClient(base_url=self.API_URL) as client:

            # Geting CSRF token 
            r = await client.get("/auth/login")
            csrf_token = r.cookies.get("_csrf")
            if r.cookies.get("_csrf") != csrf_token:
                logger.error(f"Invalid CSRF token. csrf:{csrf_token}")
                raise HTTPException(status_code=403, detail="Invalid CSRF token")
            logger.info(f"Valide scrf! csrf: {csrf_token}")
            
            # Headers for auth
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0",
                "Accept": "application/json, text/plain, */*",
                "Content-Type": "application/json",
                "Referer": "https://journal.top-academy.ru/",  
                "Origin": "https://journal.top-academy.ru",
                "X-CSRF-TOKEN": str(csrf_token),
            }
            logger.debug(f"Auth headers: {headers}")

            # Auth and return JWTmethod
            resp = await client.post(
                "/auth/login", json=self.auth_data, headers=headers
                )
            jwt_token = resp.json()["access_token"]
            resp.raise_for_status()
            if not jwt_token:
                raise HTTPException(status_code=401, detail="JWT token is missing")
            
            # Masked JWT for user logging
            masked_jwt = ".".join(part[:7] + "*" * (len(part) - 7) for part in jwt_token.split("."))
            logger.info(f"JWT is valide! JWT:{masked_jwt}")
                  
            # Update current session headers whis JWT for get data
            client.headers.update({
                "Authorization": f"Bearer {jwt_token}",
                "Accept": "application/json",
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0",
                "Referer": "https://journal.top-academy.ru/",
                "Origin": "https://journal.top-academy.ru",
            })

            # Request schedule data
            schedule_resp = await client.get(
                "/schedule/operations/get-by-date", 
                params={"date_filter": f"{self.date}"}
                )
            
            schedule_resp.raise_for_status()

            return schedule_resp.json()
        

    async def get_homewrok_data(self, 
            username: str,
            password: str,
            ) -> dict:
        
        # setup auth data
        self.auth_data = {
            "application_key": self.APP_KEY,
            "username": username,
            "password": password,
            "id_city": None,
        }
        
        # Create session for getting data is faster
        async with httpx.AsyncClient(base_url=self.API_URL) as client:

            # Geting CSRF token 
            r = await client.get("/auth/login")
            csrf_token = r.cookies.get("_csrf")
            if r.cookies.get("_csrf") != csrf_token:
                logger.error(f"Invalid CSRF token. csrf:{csrf_token}")
                raise HTTPException(status_code=403, detail="Invalid CSRF token")
            logger.info(f"Valide scrf! csrf: {csrf_token}")
            
            # Headers for auth
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0",
                "Accept": "application/json, text/plain, */*",
                "Content-Type": "application/json",
                "Referer": "https://journal.top-academy.ru/",  
                "Origin": "https://journal.top-academy.ru",
                "X-CSRF-TOKEN": str(csrf_token),
            }
            logger.debug(f"Auth headers: {headers}")

            # Auth and return JWTmethod
            resp = await client.post(
                "/auth/login", json=self.auth_data, headers=headers
                )
            jwt_token = resp.json()["access_token"]
            resp.raise_for_status()
            if not jwt_token:
                raise HTTPException(status_code=401, detail="JWT token is missing")
            
            # Masked JWT for user logging
            masked_jwt = ".".join(
                part[:7] + "*" * (len(part) - 7) for part in jwt_token.split("."))
            logger.info(f"JWT is valide! JWT:{masked_jwt}")
            logger.debug(f"JWT: {jwt_token}")
            
            # Update current session headers whis JWT for get data
            client.headers.update({
                "Authorization": f"Bearer {jwt_token}",
                "Accept": "application/json",
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0",
                "Referer": "https://journal.top-academy.ru/",
                "Origin": "https://journal.top-academy.ru",
            })

            # Request schedule data
            schedule_resp = await client.get(
                "/schedule/operations/get-by-date", 
                params={"date_filter": f"{self.date}"}
                )
            
            schedule_resp.raise_for_status()

            return schedule_resp.json()

