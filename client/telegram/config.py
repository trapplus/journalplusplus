ADMIN_ID = {
    1199971207, # Eviltrapgod 1 account
    8067399176, # Eviltrapgod 2 account
    }

WEATHER_API_URL = "http://127.0.0.1:8000/weather/weather?location={location}&lang={language}"

LOGGING_CONFIG = {          # Конфигурация логгера
    'version': 1,               # Версия логгера
    'formatters': {             # Режимы форматирвоания текста для вывода\записи логгером
        'default': {            # Стандартный режим форматирования
            "format":           # Формат сообщения
            ("%(asctime)s [%(levelname)s] %(name)s: %(message)s"),
            "datefmt": "%Y-%m-%d %H:%M:%S"
    },
        'full': {               # Полный режим форматирования
            "format": (         # Формат сообщения
                "%(asctime)s.%(msecs)03d "
                "[%(levelname)s] "
                "%(name)s | %(module)s.%(funcName)s():%(lineno)d "
                "[PID:%(process)d | TID:%(threadName)s] — %(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S"

    }
        },

    'handlers': {                       # Конфиг обработчика логгера
        'console': {                        # Конфиг для stdout в консоль
            'class': 'logging.StreamHandler',   # Выбор обработчика
            'formatter': 'default',             # Выбор форматирования
        },
        'file': {                           # Конфиг для записи stdout в файл app.log
            'class': 'logging.FileHandler',     # Выбор обработчика
            'filename': 'app.log',              # Имя файла для записи лога
            'formatter': 'default',             # Выбор режима форматирвоания
            'encoding': 'utf-8',                # Выбор кодировки текста
        },
        'file-verdose':{                    # Конфиг для записи stdout в файл app-verdose.log
            'class': 'logging.FileHandler',     # Выбор обработчика
            'filename': 'app-verbose.log',      # Имя файла для записи лога
            'formatter': 'full',                # Выбор режима форматирвоания
            'encoding': 'utf-8',                # Выбор кодировки текста
        },
    },
    'root': {                   # Настройка логгера
        'handlers': [               # Выбор обработчиков лога
            'console',              # Вывод в stdout
            'file',                 # Запись в app.log
            'file-verdose'          # Запись в app-verdose.log
            ],
        'level': 'DEBUG',       # Уровень логгирования
    },
}
