import sqlite3

try:
    with sqlite3.connect('app.db') as conn:
        cursor = conn.cursor()
        # Получаем список всех таблиц в базе
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        print("=== ПРОВЕРКА БАЗЫ ДАННЫХ ===")
        print(f"Найденные таблицы: {tables}")
        
        if ('tasks',) in tables:
            print("Таблица 'tasks' существует и работает корректно!")
        else:
            print("Ошибка: Таблица 'tasks' не найдена.")
            
except sqlite3.Error as e:
    print(f"Ошибка при работе с базой: {e}")