# bug-free-octo-enigma

## Инструкция к использованию
- Первым шагом клонируем репозиторий
- Далее создаем телеграмбота
- Присваиваем переменной TOKEN в dockerfile значение полученного токена
- Открываем терминал в директории, в которую клонировался репозиторий
- Вводим команду сборки образа в данной директории:
```bash
docker build .
```
- Проверяем доступные docker образы:
```bash
docker images
```
- Выбираем наш образ(только созданный) и запускаем:
```bash
docker run -d "id образа"
#-d -- запуск на фоне
```
- Бот готов к использованию

- Чтобы остановить контейнер, просмотрим все доступные контейнеры:
```bash
docker ps -a
```
- Остановим контейнер с ботом:
```bash
docker stop "id контейнера"
```

**Удачи!**
