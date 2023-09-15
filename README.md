## Задание:
Написать сервис "Конвертер валют" который работает по REST-API.
### Пример запроса:
```
GET /api/rates?from=USD&to=RUB&value=1
```
### Ответ:
```
{
"result": 62.16
}
```
### Условия
Любой фреймворк в пределах python.

Данные о текущих курсах валют необходимо получать с внешнего сервиса.

Контейнерезация, документация, и прочее — приветствуется.
___

## Запуск проекта

Запуск проекта возможен в трех вариантах:

### Запуск на локальной машине

Для запуска проекта на локальной машине необходимо выполнить следующее:
1. Скачать проект из репозитория на локальный компьютер.
2. В корневой директории проекта создать файл .env содержащий значения следующих переменных:
    - SECRET_KEY=django-insecure-@-4=yotzc2s$rpk@$(=tyx3vrd!wj$t0yz0d-=-#yv+ph+&5-@
    - Настройка доступа к базе данных СУБД PostgreSQL
      - DB_NAME=change_currencies 
      - DB_USER=...
      - DB_PASSWORD=...
      - DB_HOST=localhost
      - DB_PORT=5432
    - Ключ доступа к API сайта openexchangerates.org
      - APP_ID=c28e5e632ef64a8a9472a369d121e327
3. При необходимости создать и активировать виртуальное окружение проекта, выполнив команды в терминале:
```
$ python3 -m venv venv
$ source venv/bin/activate
```
4. Установить зависимости проекта, выполнив команду в терминале:
```
$ pip install -r requirements.txt
```
5. Установить серверы СУБД PostgreSQL и Redis. В СУБД PostgreSQL создать базу данных change_currencies.
6. Применить миграции к базе данных, выполнив команду в терминале:
```
$ python3 manage.py migrate
```
7. Запустить сервер Django выполнив команду в терминале:
```
$ python3 manage.py runserver
```
8. Запустить воркер Celery, выпонив команду в терминале:
```
$ celery -A change_currencies worker --loglevel=info
```
9. Запустить планировщик задач, выполнив команду в терминале:
```
$ celery -A change_currencies beat --loglevel=info
```
10. Для получения доступа в панель администратора создать суперпользователя, выполнив команду в терминале:
```commandline
$ python3 manage.py createsuperuser
```
Панель администратора доступна по URL адресу https://127.0.0.1:8000/admin/

В корневой директории проекта расположена коллекция запросов к API проекта, в файле Change Currencies.postman_collection.json

### Запуск на локальной машине в контейнерах Docker Compose.

1. Установить Docker.
2. В файле .env заменить значение переменной 
   - DB_HOST=postgres
3. В файле settings.py заменить значения переменных:
   - CELERY_BROKER_URL = 'redis://redis:6379/0'
   - CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
4. Проверить соответствие путей к файлу .env указанных как volume.
5. Запустить проект в контейнерах Docker Compose, выполнив команду в терминале:
```commandline
$ sudo docker compose up -d
```

### Запуск на удаленной машине в контейнерах Docker Compose.

1. На удаленной машине устанавливаем Docker.
2. На удаленной машине создаем директорию change_currencies, выполнив команду в удаленном терминале:
```commandline
$ mkdir change_currencies && cd change_currencies
```
2. Создать файл .env содержащий чувствительные данные, с помощью любого текстового редактора.
3. На локальной машине производим копирование файла docker-compose-server.yaml на удаленный сервер.
```commandline
$ scp <путь до проекта>/docker-compose-server.yaml <имя>@<адрес>: change_currencies/docker-compose.yaml 
```
4. Через удаленный терминал выполняем команду:
```commandline
$ sudo docker compose up -d
```