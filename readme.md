Кинопоиск. Книги
-----------------

### Инструкции для разработчиков

* :cookie: Запуск платформы :cookie:
    ```
    set FLASK_APP=kinopoisk_books
    set FLASK_ENV=development
    flask run
    ```

* :honey_pot: Добавить объект в базу данных :honey_pot:
    ```
    db.session.add(...)
    db.session.commit()
    ```

* :cactus: Миграции базы данных :cactus:
    ```
    flask db migrate
    :: Check Alembic migration script ::
    flask db upgrade
    ```

* :8ball: Ошибка `sqlalchemy.exc.OperationalError` :8ball:

  Запустить `cmd` от имени администратора
  ```
  net start mysql80
  ```

* :carrot: В папке `templates` имена файлов начинаются с одного из трёх слов: :carrot: <br>
    `temp` - это шаблоны <br>
    `hunk` - это отдельные ломти (куски) html кода <br>
    `page` - это готовые страницы, созданные на основе *temp* и использующие отдельные *hunk* <br>

* :cow2: Мы используем `MySql Community Edition 8.0.28` :cow2:
    * https://www.mysql.com/products/community/
    * https://dev.mysql.com/downloads/file/?id=510039

* :cheese: Ссылки :cheese:
    * Какие виды изменений в моделях базы данных `Alembic` распознаёт, а какие не понимает
      https://alembic.sqlalchemy.org/en/latest/autogenerate.html#autogenerate-detects
    * Редактирование скрипта миграции `Alembic`
      https://alembic.sqlalchemy.org/en/latest/tutorial.html#create-a-migration-script
