import sqlite3

def init_db():
    # 1. Подключение к базе данных (файл app.db создастся автоматически, если его нет)
    # Используем with для автоматического закрытия соединения
    with sqlite3.connect('app.db') as conn:
        cursor = conn.cursor()

        # 2. Создание таблицы. IF NOT EXISTS защищает от ошибки при повторном запуске
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id     INTEGER PRIMARY KEY AUTOINCREMENT,
                title  TEXT NOT NULL,
                status TEXT DEFAULT 'new'
            )
        """)

        # 3. Фиксация изменений (commit)
        conn.commit()
        print("База данных 'app.db' и таблица 'tasks' успешно созданы.")

if __name__ == "__main__":
    init_db()