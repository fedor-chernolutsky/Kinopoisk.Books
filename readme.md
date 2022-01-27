Кинопоиск. Книги
-----------------

### Инструкции для разработчиков

* :cookie: Запуск платформы :cookie:
    ```
    cd kinopoisk_books
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
    flask db upgrade
    ```

* :carrot: В папке `templates` имена файлов начинаются с одного из трёх слов: :carrot: <br>
    `base` - это шаблоны <br>
    `hunk` - это отдельные ломти (куски) html кода <br>
    `page` - это готовые страницы, созданные на основе *base* и использующие отдельные *hunk* <br>

* :cow2: Мы используем `MySql Community Edition 8.0.28` :cow2:
    * https://www.mysql.com/products/community/
    * https://dev.mysql.com/downloads/installer/

* :cheese: Ссылки :cheese:
    * https://alembic.sqlalchemy.org/en/latest/autogenerate.html#autogenerate-detects
    * https://alembic.sqlalchemy.org/en/latest/tutorial.html#create-a-migration-script