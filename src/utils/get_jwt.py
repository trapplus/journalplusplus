import httpx
from src import container as cont



class jwt_manager:
    def __init__(self):
        self.API_URL = "https://msapi.top-academy.ru/api/v2"  
         
        self.auth_data = {
            "application_key": cont.,
            "username": "",
            "password": "",
            "id_city": None,
        }
 
    async def get_jwt_token(self, csrf: str) -> list[str, str]:
        self.headers = {
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0",
                    "Accept": "application/json, text/plain, */*",
                    "Content-Type": "application/json",
                    "Referer": "https://journal.top-academy.ru/",  
                    "Origin": "https://journal.top-academy.ru",
                    "X-CSRF-TOKEN": str(csrf),
                }
            
        async with httpx.AsyncClient(base_url=self.API_URL):
            