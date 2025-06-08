# Telegram Bot + FastAPI Backend

## Описание

Telegram-бот, который показывает список постов и позволяет просматривать их подробности. Бэкэнд написан на FastAPI, SQlite в качестве бд. 


## Запуск

### 1. Указать переменные окружения

Открыть `.env.example` файл, добавить туда свой токен бота и переименовать файл в `.env`.

```
TELEGRAM_TOKEN=your_telegram_bot_token
```

### 2. Запуск через Docker Compose
Для простоты тестового запуска предлагается использовать docker-compose. Достаточно будет использовать команду:

```bash
  docker-compose up --build
```

### 3. Swagger 
После запуска документация должна быть доступна по http://localhost:8000/docs#/ 

![Пример](https://github.com/Ermachok/TGbot_for_posting/blob/main/pictures/Screenshot%20from%202025-06-08%2020-22-17.png)

### 3. Bot
Пример работы бота:

![Пример](https://github.com/Ermachok/TGbot_for_posting/blob/main/pictures/Screenshot%20from%202025-06-08%2020-12-01.png)


## Основные команды бота
Команды боты соответствуют ТЗ
- `/posts` — просмотр списка постов
