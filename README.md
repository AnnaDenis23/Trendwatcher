# Trendwatcher

Скачайте зависимости проекта
```
poetry init
```
*На проекте используется poetry, если вы используете pip, то перенесите зависимости в файл requirements.txt*
```
poetry export --no-interaction > requirements.txt
```
Запустите docker-compose.yaml
```
docker-compose ip -d
```
Зайдите на localhost:8081
Введите учетные данные 

Выполните запрос:
```
CREATE EXTENSION IF NOT EXISTS vector;
```

После в терминале проекта примените миграции:
```
alembic upgrade head
```
