# Полный поиск/Поиск аптеки 2.0/10 аптек
## Консольное приложение для получения изображения объекта на карте

## Использование

### Получение изображения карты с меткой объекта
-  **выполните команду передав в качестве аргументов адрес или наименование объекта:**
```
python search.py adress or name of toponym
```
- **Также можно вызвать _get_objects_data_ из _get_objects.py_, передав в качестве аргумента адрес или наименование объекта: функция возратит кортеж, состоящий из spn и списка инстансов дата-класса, содержащих координаты объекта и часы работы, если таковые указаны.**


### Получение изображения карты с меткой ближайших к объекту 10 аптек
-  **выполните команду передав в качестве аргументов адрес или наименование объекта:**
```
python pharmacy_search.py adress or name of toponym
```
