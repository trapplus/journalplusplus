import httpx
from src import container as cont
from src.utils.auth import auth

class Schedule:
    def __init__(self):
        self.auth_manager = auth()
    
    async def get_schedule(self, username: str, password: str):
        async with httpx.AsyncClient(base_url=cont.data.BASE_API_URL) as client:
            # Update current session headers with JWT for get data
            client.headers.update({
                "Authorization": f"Bearer {await self.auth_manager.get_jwt_token(username, password)}",
                "Accept": "application/json",
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0",
                "Referer": "https://journal.top-academy.ru/",
                "Origin": "https://journal.top-academy.ru",
            })
            
            # Request schedule data
            schedule_resp = await client.get(
                "/schedule/operations/get-by-date",
                params={"date_filter": f"{cont.data.current_date}"}
            )
            schedule_resp.raise_for_status()
            
            lessons = schedule_resp.json()
            
            if not lessons:
                return "📅 На этот день расписание отсутствует или не отмечено!"
            
            date = lessons[0]['date']
            
            result = f"📚 <b>Расписание на {date}</b>\n\n"
            
            for lesson in lessons:
                lesson_num = lesson['lesson']
                time_start = lesson['started_at']
                time_end = lesson['finished_at']
                subject = lesson['subject_name']
                teacher = lesson['teacher_name']
                room = lesson['room_name']
                
                result += (
                    f"<b>{lesson_num} пара</b> • {time_start} - {time_end}\n"
                    f"📖 {subject}\n"
                    f"👨‍🏫 {teacher}\n"
                    f"🚪 {room}\n\n"
                )
            
            return result
