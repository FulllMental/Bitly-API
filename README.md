# Обрезка ссылок с помощью Битли
Данный скрипт сокращает одной командой ссылку, через API сервиса [bitly.com](https://bitly.com/)
или получает статистику переходов по уже имеющейся ссылке.

### Как установить
Python3 должен быть уже установлен. 

Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```
Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html)

Для корректного создания короткой ссылки необходимо в `.env` фйле указать access token, из [раздела API](https://app.bitly.com/settings/api/) личного аккаунта данного сервиса

### Примеры запуска скриптов
```bash
$ python main.py 
Введите ссылку: google.com
https://bit.ly/3OAconI

$ python main.py
Введите ссылку: https://bit.ly/3OAconI
0
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).