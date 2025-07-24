def test_post(test_client):
    """Тест пост запроса с валидными данными"""
    data = {"address": "TUjx6w55Nx9G4GjjRNEB4e7w5BUH3WmJTZ"}
    response = test_client.post("/address_info", json=data)

    # Проверяем статус-код ответа
    assert response.status_code == 200

    response_data = response.json()

    # Проверяем наличие необходимых полей в ответе
    for i_field in ["address", "bandwidth", "energy", "trx"]:
        assert i_field in response_data.keys()


def test_post_no_valid(test_client):
    """Тест пост запроса с не валидными данными"""
    data = {"address": "не валидный адрес"}
    response = test_client.post("/address_info", json=data)

    # Проверяем статус-код ответа
    assert response.status_code == 400
