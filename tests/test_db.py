import asyncio

from sqlalchemy import select, func, delete

from schemas.schema import InfoSchema


def test_write_in_db(session_db_fixture, model_fixture, method_write_in_db):
    # Получаем начальное количество записей в БД
    count_query = select(func.count()).select_from(model_fixture)
    start_count = session_db_fixture.execute(count_query).scalar()

    # Добавляем новую запись в бд при помощи метода класса Repo
    data = InfoSchema(
        address="test_case",
        bandwidth=1,
        energy=2,
        trx=3,
        )
    asyncio.run(method_write_in_db(data))

    # Получаем новое количество записей в БД
    end_count = session_db_fixture.execute(count_query).scalar()

    # Сравниваем количество записей - должно стать на одну больше
    assert start_count + 1 == end_count

    # Удаляем из бд тестовые записи
    delete_query = delete(model_fixture).where(model_fixture.address == "test_case")
    session_db_fixture.execute(delete_query)
    session_db_fixture.commit()
