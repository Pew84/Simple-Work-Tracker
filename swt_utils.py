import datetime
# Переводит общее количество секунд в формат гг мм дд чч мм сс в виде строки
def timer_format(seconds):
    # Рассчитываем компоненты времени
    years = seconds // (365 * 24 * 3600)
    seconds %= (365 * 24 * 3600)
    months = seconds // (30 * 24 * 3600)
    seconds %= (30 * 24 * 3600)
    days = seconds // (24 * 3600)
    seconds %= (24 * 3600)
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    # Формируем результат
    result = []
    if years > 0:
        result.append(f"{years} " + ("год" if years == 1 else "года" if 2 <= years <= 4 else "лет"))
    if months > 0:
        result.append(f"{months} мес")
    if days > 0:
        result.append(f"{days} д")
    if hours > 0:
        result.append(f"{hours} ч")
    if minutes > 0:
        result.append(f"{minutes} мин")
    if seconds > 0:
        result.append(f"{seconds} сек")
    # Если ничего не было добавлено, значит время 0 минут
    if not result:
        return "0 мин"
    # Возвращаем строку с результатом
    return ' '.join(result)

# обновляем таймеры на графических виджетах
def update_window(main):
    # перебираем все созданные обьеты task во всех проектах projects
    for projects in main.projects_obj:
        # обнуляем общий счетчик времени работы над проектом
        total_in_project = 0
        for tasks in projects.tasks_obj:
            # если таймер активен
            if tasks.start_time.second != 0:
                # прибавляем к счетчику общего времени работы на задачей время с момента старта таймера в секундах
                # total_task = tasks.total_duration + (datetime.datetime.now() - tasks.start_time).seconds
                total_task = tasks.total_duration + int((datetime.datetime.now().timestamp() - tasks.start_time.timestamp()))
                txt = timer_format(total_task)
                tasks.timer_task_text.config(text=txt)
            # если таймер выключен
            else:
                # выводми значение свойства обьекта task "общее время затраченное на задачу" total_duration
                total_task = tasks.total_duration
                tasks.timer_task_text.config(text=timer_format(total_task))
            # суммируем вермя всех задач в прокете
            total_in_project = total_in_project + total_task
        # выводим значение суммы всех счетчиков задач в общий счетчик времени проекта
        projects.timer_project_text.config(text=timer_format(total_in_project))
    pass

# переводит строку формата "гггг-мм-дд" в строку формата "дд месяц гггг"
def date_format(date_str):
    months = {
        1: "января", 2: "февраля", 3: "марта", 4: "апреля", 5: "мая", 6: "июня",
        7: "июля", 8: "августа", 9: "сентября", 10: "октября", 11: "ноября", 12: "декабря"
    }
    # Преобразуем строку в объект даты
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    # Получаем день, месяц и год
    day = date_obj.day
    month = months[date_obj.month]  # Название месяца на русском языке
    year = date_obj.year
    # Формируем строку в нужном формате
    return f"{day} {month} {year}"


