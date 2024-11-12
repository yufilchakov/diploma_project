# Дипломная работа 

## Название проекта: OB3 Сервис обработки загружаемых документов

## Описание
Этот проект представляет собой веб-приложение, разработанное с использованием 
Django и Django Rest Framework (DRF). Приложение позволяет пользователям загружать документы и получать 
уведомления по электронной почте. Для хранения данных используется PostgreSQL, а для обработки фоновых 
задач — Celery. Проект контейнеризирован с помощью Docker и Docker Compose.

## Технологии
- **Фреймворк**: Django, Django Rest Framework (DRF)
- **База данных**: PostgreSQL
- **Контейнеризация**: Docker, Docker Compose
- **Очередь сообщений**: Celery
- **Отправка уведомлений**: Django Email
- **Документация API**: Swagger
- **Качество кода**: PEP8

## Установка и запуск
1. Клонируйте репозиторий:
```
   git clone https://github.com/yufilchakov/diploma_project
   cd diploma_project
```
********************************
2. Установите зависимости с помощью Poetry:
```
   poetry install
```
********************************
3. Миграция базы данных:

   Выполните следующие команды для создания таблиц в базе данных:
```
   python manage.py makemigrations
   python manage.py migrate
```
********************************
4. Создайте суперпользователя для доступа к админке:
```
   python manage.py csu
```
********************************
5. Запуск локального сервера:
```
   python manage.py runserver
```
********************************
6. Создайте файл .env на основе .env.sample и заполните необходимые переменные окружения.
********************************
7. Запустите проект с помощью Docker Compose:
```
   docker-compose up -d --build
```
********************************
## Использование
Доступ к административной панели по адресу http://127.0.0.1:8000/admin/
********************************
## Документация API
Автогенерируемая документация API доступна по адресу http://127.0.0.1:8000/swagger/. 
Она предоставляет информацию о доступных эндпоинтах и их использовании.
********************************
## CORS
Для обеспечения безопасности и разрешения запросов из других доменов, в проекте настроен CORS.
Вы можете настроить разрешенные источники в файле settings.py вашего Django проекта, 
добавив необходимые домены в список CORS_ALLOWED_ORIGINS.
********************************
## Тестирование
Код проекта покрыт тестами с покрытием не менее 75%. 
Для запуска тестов используйте следующую команду:
```
docker-compose exec app python manage.py test
```
********************************