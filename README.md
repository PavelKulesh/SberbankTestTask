# Process Data Service

***

### Требования:

- [X] Принятие дерева извлечений (в формате JSON или XML)
- [X] Перевод дерева в словарь
- [X] Нормализация дат и сроков

### Установка зависимостей

```
pipenv install
```

### Запуск приложения

```
python run.py
```

### Запуск тестов

```
pytest
```

### Endpoints

| Method | Url                                    | Description  | Headers                        |
|:-------|:---------------------------------------|:-------------|:-------------------------------|
| POST   | http://127.0.0.1:8000/api/v1/documents | Process json | Content-Type: application/json |
| POST   | http://127.0.0.1:8000/api/v1/documents | Process xml  | Content-Type: application/xml  |

### Тестовые xml и json файлы находятся в директории `examples/`
