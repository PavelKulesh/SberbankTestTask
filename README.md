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
uvicorn src.main:app --reload --host 0.0.0.0 --port 80
```

### Endpoints

| Method | Url                                  | Description  | Headers                        |
|:-------|:-------------------------------------|:-------------|:-------------------------------|
| POST   | http://localhost/api/v1/process_tree | Process json | Content-Type: application/json |
| POST   | http://localhost/api/v1/process_tree | Process xml  | Content-Type: application/xml  |

### Тестовые xml и json файлы находятся в директории `examples/`
