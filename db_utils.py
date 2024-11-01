import sqlite3
import datetime

swt_bd = "swt.db"
# Функция для создания подключения к базе данных
def create_connection(db_file):
    # Создаем подключение к базе данных SQLite
    conn = sqlite3.connect(db_file)
    return conn

# Функция для получения списка проектов в базе данных
def get_list_projects():
    conn = create_connection(swt_bd)  # Подключаемся к базе данных
    cursor = conn.cursor()  # Создаем курсор для выполнения SQL-запросов
    cursor.execute("SELECT * FROM PROJECTS;")  # Выполняем запрос на получение значений всех строк таблицы проектов
    list_projects = cursor.fetchall()
    cursor.close()  # Закрываем курсор
    print(list_projects)
    conn.close()
    return list_projects

def get_list_tasks(project_id):
    conn = create_connection(swt_bd)  # Подключаемся к базе данных
    cursor = conn.cursor()  # Создаем курсор для выполнения SQL-запросов
    cursor.execute(f"SELECT * FROM '{project_id}';")  # Выполняем запрос на получение значений всех строк таблицы проектов
    list_projects = cursor.fetchall()
    print(list_projects)
    for row in list_projects:
        print([type(value) for value in row])
    cursor.close()  # Закрываем курсор
    conn.close()
    return list_projects

# Функция для создания таблицы проектов в базе данных
def create_table_projects(conn):
    cursor = conn.cursor()  # Создаем курсор для выполнения SQL-запросов
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS PROJECTS (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_name TEXT,
        start_date DATE,
        end_date DATE
    );
    """
    cursor.execute(create_table_sql)  # Выполняем запрос на создание таблицы
    conn.commit()  # Фиксируем изменения в базе данных
    cursor.close()  # Закрываем курсор
    print("Table PROJECTS created")

# Функция для создания таблицы задач в базе данных
def create_table_tasks(conn, table_name):
    cursor = conn.cursor()  # Создаем курсор для выполнения SQL-запросов
    create_table_sql = f"""
    CREATE TABLE IF NOT EXISTS '{table_name}' (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_name TEXT,
        start_date TEXT,
        total_duration INTEGER,
        start_time INTEGER,
        timer_status BOOLEAN,
        end_date TEXT
    );
    """
    cursor.execute(create_table_sql)  # Выполняем запрос на создание таблицы
    conn.commit()  # Фиксируем изменения в базе данных
    cursor.close()  # Закрываем курсор
    print(f"Table '{table_name}' created")

# Функция для удаления таблицы из базы данных
def delete_table(table_name):
    conn = create_connection(swt_bd)  # Подключаемся к базе данных
    cursor = conn.cursor()  # Создаем курсор для выполнения SQL-запросов
    delete_table_sql = f"DROP TABLE IF EXISTS '{table_name}';"  # SQL-запрос для удаления таблицы
    cursor.execute(delete_table_sql)  # Выполняем запрос на удаление таблицы
    conn.commit()  # Фиксируем изменения в базе данных
    cursor.close()  # Закрываем курсор
    conn.close()
    print(f"Table '{table_name}' deleted")

# Функция для добавления записи проекта в таблицу PROJECTS
def add_project(table_name):
    conn = create_connection(swt_bd)  # Подключаемся к базе данных
    cursor = conn.cursor()  # Создаем курсор для выполнения SQL-запросов
    date_now = datetime.datetime.now().strftime('%Y-%m-%d')
    # создаем запись в таблице PROJECTS
    cursor.execute(f"""
        INSERT INTO PROJECTS (project_name, start_date) 
        VALUES (?, ?);
        """, (table_name, date_now))
    # Получение id только что вставленной записи
    id = cursor.lastrowid
    # создаем таблицу Задач для нового проекта
    create_table_tasks(conn, id)
    conn.commit()  # Фиксируем изменения в базе данных
    cursor.close()  # Закрываем курсор
    print(f"New project added to table Projects and create new table {id}")
    conn.close()
    return (id, table_name, date_now, None)

# Функция для добавления записи в таблицу задач
def add_record(table_id, task_name):
    conn = create_connection(swt_bd)  # Подключаемся к базе данных
    cursor = conn.cursor()  # Создаем курсор для выполнения SQL-запросов
    date_now = datetime.date.today().strftime('%Y-%m-%d')
    total_duration = 0
    add_record_sql = f"""
    INSERT INTO '{table_id}' (task_name, start_date, total_duration, start_time)
    VALUES (?, ?, ?, ?);
    """
    cursor.execute(add_record_sql, (task_name, date_now, total_duration, "None"))
    # Получение id только что вставленной записи
    task_id = cursor.lastrowid
    conn.commit()  # Фиксируем изменения в базе данных
    cursor.close()  # Закрываем курсор
    conn.close()
    print(f"Record added to table '{table_id}'")
    return date_now, task_id

# НЕИСПОЛЬЗУЕМАЯ ФУНКЦИЯ
def add_record_(conn, table_name, task):
    cursor = conn.cursor()  # Создаем курсор для выполнения SQL-запросов
    add_record_sql = f"""
    INSERT INTO {table_name} (task_name, start_date, total_duration, start_time, timer_status, end_date)
    VALUES (?, ?, ?, ?, ?, ?);
    """
    cursor.execute(add_record_sql, (
        task,
        datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        str(task.total_duration),
        task.start_time.strftime('%Y-%m-%d %H:%M:%S') if task.start_time else None,
        task.timer_status,
        task.end_date.strftime('%Y-%m-%d %H:%M:%S') if task.end_date else None
    ))
    conn.commit()  # Фиксируем изменения в базе данных
    cursor.close()  # Закрываем курсор
    print(f"Record added to table '{table_name}'")

# Функция для удаления записи из таблицы по id
def delete_record(table_name, record_id):
    conn = create_connection(swt_bd)  # Подключаемся к базе данных
    cursor = conn.cursor()  # Создаем курсор для выполнения SQL-запросов
    delete_record_sql = f"DELETE FROM '{table_name}' WHERE id = ?;"  # SQL-запрос для удаления записи по id
    cursor.execute(delete_record_sql, (record_id,))
    conn.commit()  # Фиксируем изменения в базе данных
    cursor.close()  # Закрываем курсор
    conn.close()
    print(f"Record with id '{record_id}' deleted from table '{table_name}'")


def update_value(table_name, column, row_id, new_value):
    try:
        # Подключение к базе данных
        conn = create_connection(swt_bd)  # Подключаемся к базе данных
        cursor = conn.cursor()  # Создаем курсор для выполнения SQL-запросов
        # Формирование SQL-запроса для обновления значения
        query = f"UPDATE '{table_name}' SET '{column}' = ? WHERE id = ?"
        # Выполнение запроса с подстановкой значений
        cursor.execute(query, (new_value, row_id))
        # Сохранение изменений
        conn.commit()
        print(f"Значение обновлено в строке с id={row_id} в столбце '{column}'")
    except sqlite3.Error as err:
        print(f"Error on update data: {err}")
    finally:
        # Закрытие подключения
        conn.close()
