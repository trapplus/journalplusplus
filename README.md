<div align="center">

# 📓 Journal++

**A smart Telegram bot for Top Academy students — schedules, grades, attendance and more, right in your pocket.**

[![Python](https://img.shields.io/badge/Python-3.13%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![aiogram](https://img.shields.io/badge/aiogram-3.x-009688?logo=telegram&logoColor=white)](https://docs.aiogram.dev/)
[![top\_journal\_sdk](https://img.shields.io/badge/powered%20by-top__journal__sdk-6c63ff)](https://github.com/ITTopTools/top_journal_sdk)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

</div>

---

## ✨ Features

| Feature | Description |
|---|---|
| 📅 **Schedule** | View your daily and weekly timetable at a glance |
| 📊 **Grades** | Check your current marks for any subject |
| ✅ **Attendance** | Track your attendance stats and skips |
| 🔔 **Notifications** | Get reminders before classes and alerts for new grades |
| 📎 **Homework** | Upload and download homework files directly in chat |

---

## 🏗️ Project Structure

```
journal-plus-plus/
├── bot/
│   ├── handlers/          # Telegram command & callback handlers
│   │   ├── schedule.py
│   │   ├── grades.py
│   │   ├── attendance.py
│   │   ├── homework.py
│   │   └── notifications.py
│   ├── keyboards/         # Inline & reply keyboards
│   ├── middlewares/       # Auth, logging, throttling
│   └── filters/           # Custom aiogram filters
├── services/              # Business logic layer
├── db/                    # Database models & migrations
├── config.py              # Settings via pydantic-settings
├── main.py                # Entry point
├── pyproject.toml         # Global Python project config
├── .env.example           # Example for .env config
├── Dockerfile             # Config for build docker image 
└── README.md
```

---

## 🔗 Powered by `top_journal_sdk`

Journal++ is built on top of **[top\_journal\_sdk](https://github.com/ITTopTools/top_journal_sdk)** — an async Python library for the Top Academy journal API.

```python
from top_journal_sdk import JournalClient

async def get_schedule(token: str):
    async with JournalClient(token=token) as client:
        schedule = await client.get_schedule()
        return schedule
```

All data — schedule, grades, attendance — is fetched through the SDK. If you find a bug in the data layer, it's likely worth opening an issue in the [sdk repo](https://github.com/ITTopTools/top_journal_sdk/issues) rather than here.

---

## 🚀 Getting Started

### Prerequisites

- Python **3.13+**
- [uv](https://docs.astral.sh/uv/) package manager
- A Telegram bot token from [@BotFather](https://t.me/BotFather)
- Top Academy credentials

### Installation

```bash
# 1. Clone the repo
git clone https://github.com/your-username/journal-plus-plus.git
cd journal-plus-plus

# 2. Install dependencies (uv handles the venv automatically)
uv sync

# 3. Configure environment
cp .env.example .env
# Fill in your BOT_TOKEN and other secrets in .env
```

### Running

```bash
uv run main.py
```

---

## ⚙️ Configuration

Copy `.env.example` to `.env` and fill in the values:

```env
BOT_TOKEN=your_telegram_bot_token

# Database url
DB_URL=sqlite:///./database.db

# Optional
LOG_LEVEL=INFO
```

---

## 🤝 Contributing

Contributions are what make open-source great. Any improvements are **welcome**!

### How to contribute

1. **Fork** the repository
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'feat: add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a **Pull Request**

### Commit convention

We use [Conventional Commits](https://www.conventionalcommits.org/):

| Prefix | When to use |
|---|---|
| `feat:` | New feature |
| `fix:` | Bug fix |
| `docs:` | Documentation only |
| `refactor:` | Code change, no feature/fix |
| `chore:` | Dependency updates, tooling |

### Reporting bugs

Please open an [issue](https://github.com/your-username/journal-plus-plus/issues) and include:
- What you did
- What you expected
- What actually happened
- Python version & OS

> ⚠️ If the issue is related to data fetching (wrong schedule, empty grades, etc.), please check whether it reproduces with `top_journal_sdk` directly before filing here.

---

## 📬 Contact & Support

- **SDK issues** → [ITTopTools/top\_journal\_sdk](https://github.com/ITTopTools/top_journal_sdk/issues)
- **Bot issues** → [Issues tab](https://github.com/your-username/journal-plus-plus/issues)
- **Questions** → open a [Discussion](https://github.com/your-username/journal-plus-plus/discussions)

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for more information.

---

<div align="center">

Made with ❤️ using [top\_journal\_sdk](https://github.com/ITTopTools/top_journal_sdk)

</div>