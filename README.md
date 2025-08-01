# Тестовое задание для компании Forkiteh

## Текст задания: 
    Написать микросервис, который будет выводить информацию по адресу в сети трон, его bandwidth, energy, и баланс trx, 
    ендпоинт должен принимать входные данные - адрес.
    Каждый запрос писать в базу данных, с полями о том какой кошелек запрашивался.
    Написать юнит/интеграционные тесты
    У сервиса 2 ендпоинта
    - POST
    - GET для получения списка последних записей из БД, включая пагинацию
    2 теста
    - интеграционный на ендпоинт
    - юнит на запись в бд


    Примечания: использовать FastAPI, аннотацию(typing), SQLAlchemy ORM, для удобства взаимодействия с троном можно 
    использовать tronpy, для тестов - Pytest.


## Запуск проекта:

### Вариант 1:
    Запуск в Docker контейнере (Рекомендуемый). Для этого выполните следующие шаги:
    1. Скачайте репозиторий проекта на свою локальную машину командой:
        git clone https://github.com/KirillAyvazov/test_case_Forkiteh
    2. Перейдите в корень проекта, где находится dockerfile
    3. Выполните команду: docker build -t test_case_forkiteh_image .
    4. Дождитесь установки всех компонентов
    5. Выполните команду: docker run --name test_case -p 8000:8000 test_case_forkiteh_image
    6. Для тестирования микросервиса перейдите по адресу: http://127.0.0.1:8000/docs#/


### Вариант 2:
    Запуск из командной строки. Для этого выполните следующие шаги:
    1. Скачайте репозиторий проекта на свою локальную машину командой:
        git clone https://github.com/KirillAyvazov/test_case_Forkiteh
    2. Перейдите в корень проекта
    3. Создайте виртуальное окружение выполнив команду: python -m venv myenv
    4. Активируйте виртуальное окружение выполнив команду: 
        myenv\Scripts\activate (Для Windows)
        source myenv/bin/activate (Для Linux/Mac)
    5. При необходимости, выполните команду python -m pip install --upgrade pip
    6. Установите зависимости проекта выполнив команду: pip install -r requirements.txt
    7. Запустите проект выполнив команду: uvicorn app:app --port 8000
    8. Для тестирования микросервиса перейдите по адресу: http://127.0.0.1:8000/docs#/


### Запуск тестов:
    1. Перейдите в корень проекта
    2. Выполните команду pytest
