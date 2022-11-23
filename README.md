# REST API для проекта Yatube.

## Описание
Аутентификация по JWT-токену

Работает со всеми модулями социальной сети Yatube: постами, комментариями, группами, подписчиками

Поддерживает методы GET, POST, PUT, PATCH, DELETE

Предоставляет данные в формате JSON


### Технологии:
REST API, JSON, OAuth 2.0, DRF

***

### Запуск проекта:

Скопировать репозиторий:
```
git clone git@github.com:APanov13/REST_API_for_YaTube.git
```
Создать и активировать виртуальное окружение:
```
python -m venv venv

source venv/bin/activate
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python manage.py migrate
```
Запустить сервер:
```
python manage.py runserver
```
***
### Примеры запросов и ответов API  

#### Добавление публикации  

  
  `POST /api/v1/posts`
##### Ответ API:

```json
{
    "id": 3,
    "author": "monicageller",
    "text": "Chandler and I are getting married!",
    "pub_date": "2020-12-25T10:40:32.710136Z",
    "group": null
}
```
