import threading
import db_utils
import gui_utils
import datetime
import swt_utils
import time


swt_bd = "swt.db"

# Определяем класс Task для управления задачами
class Task:
    def __init__(self, project_id, task_id, task_name, start_date, total_duration, start_time, timer_status, end_date, project_frame, last_task):
        self.project_id = project_id  # id проекта в таблице проектов и имя таблицы для этого проекта с записями задач
        self.task_id = task_id
        self.task_name = task_name
        self.start_date = start_date
        self.total_duration = total_duration
        if start_time != "None":
            self.start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S.%f')
        else:
            self.start_time = datetime.datetime(1, 1, 1, 0, 0, 0)
        self.timer_status = timer_status
        self.end_date = end_date
        self.last_task = last_task
        (self.task_frame,
         self.delete_task_widget,
         self.start_task_widget,
         self.timer_task_text,
         self.end_task_widget,
         self.begin_date_task_text,
         self.status_task_widget,
         self.arrow_task) = gui_utils.create_task_gui(project_frame, self.task_name, self.start_date, self.end_date, self.timer_status, self.last_task, self)
        # определяем функцию обработчика событий нажатия на кнопку Удаления Задачи
        self.delete_task_widget.bind("<Button-1>", self.delete_self)
        # определяем функцию обработчика событий нажатия на кнопку Старт таймера Задачи
        self.start_task_widget.bind("<Button-1>", self.start_timer)
        # определяем функцию обработчика событий нажатия на кнопку завершения Задачи
        self.end_task_widget.bind("<Button-1>", self.end_task)

    def start_timer(self, event):
        if self.end_date is None:  # если задача не завершена
            if not self.timer_status:  # если таймер был выключен, запускаем займер
                # ищем по всем остальным задачам всех проектов, если был активный таймер стаим его на паузу
                iter_x = 0
                for projects in main.projects_obj:
                    iter_y = 0
                    for tasks in projects.tasks_obj:
                        if main.projects_obj[iter_x].tasks_obj != []:
                            if main.projects_obj[iter_x].tasks_obj[iter_y].timer_status == True:
                                main.projects_obj[iter_x].tasks_obj[iter_y].pause_timer()
                                print("Active timer finded and paused")
                        iter_y = iter_y + 1
                    iter_x = iter_x + 1
                # Запускаем  таймер
                self.start_time = datetime.datetime.now()
                # сохраняем время старта таймера в бд
                db_utils.update_value(self.project_id, 'start_time', self.task_id, self.start_time.strftime('%Y-%m-%d %H:%M:%S.%f'))
                # изменяем виджеты
                self.start_task_widget.itemconfig(self.start_task_widget.image_id, image=gui_utils.tk_start_task_pause_skin)
                self.end_task_widget.itemconfig(self.end_task_widget.image_id, image=gui_utils.tk_end_task_active_skin)
                self.status_task_widget.itemconfig(self.status_task_widget.image_id, image=gui_utils.tk_task_status_on_skin)
                # таймер активный
                self.timer_status = True
                # сохраняем в бд
                db_utils.update_value(self.project_id, 'timer_status', self.task_id, self.timer_status)
                print(f"Timer started for task '{self.task_name}'")
            else:
                # если таймер был запущен, то ставим задачу на паузу
                self.pause_timer()

    def pause_timer(self):
        if self.timer_status:
            # прибавляем к счетчику общего времени работы на задачей в секундах
            self.total_duration += int(datetime.datetime.now().timestamp() - self.start_time.timestamp())
            # сохраняем в бд
            db_utils.update_value(self.project_id, 'total_duration', self.task_id, self.total_duration)
            print(self.total_duration)
            # стираем время старта таймера
            self.start_time = datetime.datetime.min
            # сохраняем в бд
            db_utils.update_value(self.project_id, 'start_time', self.task_id, "None")
            # изменяем виджеты
            self.start_task_widget.itemconfig(self.start_task_widget.image_id, image=gui_utils.tk_start_task_skin)
            self.end_task_widget.itemconfig(self.end_task_widget.image_id, image=gui_utils.tk_end_task_skin)
            self.status_task_widget.itemconfig(self.status_task_widget.image_id, image=gui_utils.tk_task_status_pause_skin)
            # статус активного таймера в false
            self.timer_status = False
            # сохраняем в бд
            db_utils.update_value(self.project_id, 'timer_status', self.task_id, self.timer_status)
            print(f"Timer paused for task '{self.task_name}'")

    def end_task(self, event):
        if self.end_date is None:
            self.end_date = datetime.datetime.now().strftime('%Y-%m-%d')
            if self.timer_status:
                self.pause_timer()
            # сохраняем дату завершения задачи в бд
            db_utils.update_value(self.project_id, "end_date", self.task_id, self.end_date)
            # выводим значения дат начала и конца задачи
            self.begin_date_task_text.config(text=swt_utils.date_format(self.start_date)+' - '+swt_utils.date_format(self.end_date))
            # изменяем виджеты
            self.end_task_widget.itemconfig(self.end_task_widget.text_id, text="Завершено", fill="black")
            self.end_task_widget.itemconfig(self.end_task_widget.image_id, image=gui_utils.tk_end_task_ok_skin)
            self.end_task_widget.pack(padx=0)
            self.status_task_widget.itemconfig(self.status_task_widget.image_id, image=gui_utils.tk_task_status_off_skin)
            self.start_task_widget.pack_forget()
            print(f"Task '{self.task_name}' completed")

    def delete_self(self, event):
        # Удаляем запись из БД
        db_utils.delete_record(self.project_id, self.task_id)
        # Удаляем графические обьект данной задачи все его дочерние виджеты
        self.task_frame.destroy()  # Удаляет фрейм и все его дочерние виджеты
        # Ищем в каком объекте Project и с каким индексом в его свойстве tasks_obj хранится наш указатель на Задачу
        iter_x = 0
        for projects in main.projects_obj:
            iter_y = 0
            for tasks in projects.tasks_obj:
                if main.projects_obj[iter_x].tasks_obj != []:
                    if main.projects_obj[iter_x].tasks_obj[iter_y] == self:
                        print(main.projects_obj[iter_x].tasks_obj)
                        # если задача была последняя в списке, но не единственная, то перериосвывем стрелу задачи выше
                        if main.projects_obj[iter_x].tasks_obj[iter_y].last_task:
                            if iter_y > 0:
                                main.projects_obj[iter_x].tasks_obj[iter_y-1].last_task = True # признак последней задачи в списке
                                main.projects_obj[iter_x].tasks_obj[iter_y-1].arrow_task.itemconfig(main.projects_obj[iter_x].tasks_obj[iter_y-1].arrow_task.image_id, image=gui_utils.tk_arrow_last_skin)
                        # Удаляем ссылку на обьект Task в свойстве tasks_obj родительского объекта Project
                        del main.projects_obj[iter_x].tasks_obj[iter_y]
                iter_y = iter_y + 1
            iter_x = iter_x + 1
        print(f"Task '{self.task_name}' deleted")

# Определяем класс Project для управления проектами
class Project:
    def __init__(self, main_frame_projects, project_id, project_name, begin_date, end_date):
        self.name = project_name
        self.id = project_id
        self.start_date = begin_date
        self.end_date = end_date
        self.tasks = db_utils.get_list_tasks(project_id)
        self.status = True
        if end_date != None: self.status = False
        self.visible_tasks = True
        self.tasks_obj = []  # список обьектов задач
        # создаем фрейм и графические элементы проекта
        (self.project_frame,
         self.delete_project_widget,
         self.add_task_widget,
         self.timer_project_text,
         self.end_project_widget,
         self.begin_date_project_text,
         self.status_project_widget,
         self.show_tasks_widget) = gui_utils.create_project_gui(main_frame_projects, self.name, self.start_date, self.end_date, self)

        # создаем список задач-проектов
        if self.tasks != []:
            i = 1
            last_task = False
            for tasks_table in self.tasks:
                if i == self.tasks.__len__(): last_task = True  # проверяем, является ли задача последней в списке
                task = Task(self.id, tasks_table[0], tasks_table[1],tasks_table[2],tasks_table[3],tasks_table[4],tasks_table[5],tasks_table[6],self.project_frame, last_task)
                self.tasks_obj.append(task)
                i += 1
        # определяем функцию обработчика событий нажатия на кнопку Удаления проекта
        self.delete_project_widget.bind("<Button-1>", self.delete_self)
        # определяем функцию обработчика событий нажатия на кнопку Добавления Задачи
        self.add_task_widget.bind("<Button-1>", self.add_task)
        # определяем функцию обработчика событий нажатия на кнопку Завершения проекта
        self.end_project_widget.bind("<Button-1>", self.end_project)
        # определяем функцию обработчика событий нажатия на кнопку Скрыть Задачи
        self.show_tasks_widget.bind("<Button-1>", self.show_tasks)

    def delete_self(self, event):
        # удаляем таблицу Проекта c задачами из БД
        db_utils.delete_table(self.id)
        # удаляем запись проекта из таблицы PROJECTS в БД
        db_utils.delete_record("PROJECTS", self.id)
        # удаляем виджет Проекта и все его дочерние виджеты
        self.project_frame.destroy()
        # ищем и удаляем сам обьект класса Project из списка обьектов в свойстве projects_obj классе Main
        iter_x = 0
        for project in main.projects_obj:
            if project == self:
                del main.projects_obj[iter_x]
            iter_x = iter_x + 1
        print(f"Project '{self.name}' deleted")

    def add_task(self, event):
        if self.status is not False:
            # получаем имя через диалоговое окно для ввода имени Задачи
            #new_task_name = gui_utils.add_task_gui()
            new_task_name = "New Task"
            if new_task_name:
                print(f"Task '{new_task_name}' added to project '{self.name}'")
                # добавляем новую Задачу в БД
                start_date, task_id = db_utils.add_record(self.id, new_task_name)  # self.id имя таблицы списка Задач текущего обьекта Проекта
                # ищем последнюю задачу и перерисовываем в ней стрелку
                for task in self.tasks_obj:
                    if task.last_task:
                        task.last_task = False  # помечаем как непоследнюю
                        task.arrow_task.itemconfig(task.arrow_task.image_id, image=gui_utils.tk_arrow_skin)
                # создаем новый обьект класса Task и рисуем его
                task = Task(self.id, task_id, new_task_name, start_date, 0,"None",False,None,self.project_frame, True)
                # добавляем обьект в список обьектов класаа Main
                self.tasks_obj.append(task)
            else:
                print("No Task name entered.")


    def end_project(self, event):
        if self.status is not False:
            # завершаем все задачи проекта
            for tasks in self.tasks_obj:
                tasks.end_task(event)
            self.end_date = datetime.datetime.now().strftime('%Y-%m-%d')
            # пишем в БД
            db_utils.update_value("PROJECTS","end_date",self.id, self.end_date)
            # обновляем виджеты проекта
            self.begin_date_project_text.config(text=swt_utils.date_format(self.start_date)+' - '+swt_utils.date_format(self.end_date))
            self.end_project_widget.itemconfig(self.end_project_widget.text_id, text="Завершено", fill="white")
            self.end_project_widget.itemconfig(self.end_project_widget.image_id, image=gui_utils.tk_end_project_ok_skin)
            self.add_task_widget.pack_forget()
            self.status_project_widget.itemconfig(self.status_project_widget.image_id, image=gui_utils.tk_project_status_off_skin)
            # изменяем статус проекта
            self.status = False
            # скрываем, если выставлено скрытие завершенных проектов
            if main.complete_button is False:
                self.project_frame.pack_forget()
            print(f"Project '{self.name}' completed")

    # показать/спрятать список задач проекта
    def show_tasks(self, event):
        if self.visible_tasks:
            # меняем картинку кнопки
            self.show_tasks_widget.itemconfig(self.show_tasks_widget.image_id, image=gui_utils.tk_show_tasks_off_skin)
            for tasks in self.tasks_obj:
                # прячем все задачи в данном проекте
                tasks.task_frame.pack_forget()
            self.visible_tasks = False
        else:
            # меняем картинку кнопки
            self.show_tasks_widget.itemconfig(self.show_tasks_widget.image_id, image=gui_utils.tk_show_tasks_on_skin)
            for tasks in self.tasks_obj:
                # показываем все задачи в данном проекте
                tasks.task_frame.pack(expand=True, fill='x', side='top', anchor="nw", padx=15, pady=0)
            self.visible_tasks = True


# Определяем основной класс Main для управления проектами
class Main:
    def __init__(self):
        self.projects = db_utils.get_list_projects()  # загружаем из бд список проектов
        self.complete_button = False  # кнопка отображения завершенных проектов
        self.current_button = True  # кнопка отображения активных проектов
        self.projects_obj = []  # список обьектов проектов
        # создаем грфические объекты основной панели
        (self.main_frame_projects,
         self.complete_button_gui,
         self.current_button_gui,
         self.add_project_gui) = gui_utils.create_main_frame()
        # определяем функцию обработчика событий нжатия на кнопку отображения завершенных задач
        self.complete_button_gui.bind("<Button-1>", self.complete_view_button_click)
        # определяем функцию обработчика событий нжатия на кнопку отображения текущих задач
        self.current_button_gui.bind("<Button-1>", self.current_view_button_click)
        # определяем функцию обработчика событий нжатия на кнопку Создания нового проекта
        self.add_project_gui.bind("<Button-1>", self.add_project_button_click)
        # создаем список обьектов-проектов по списку таблиц в базе данных
        if self.projects != []:
            for project_table in self.projects:
                project = Project(self.main_frame_projects, project_table[0], project_table[1], project_table[2], project_table[3])
                self.projects_obj.append(project)
                pass

    # функция обработки события нажатия на кнопку отображения завершенных проектов
    def complete_view_button_click(self, event):
        if self.complete_button:
            self.complete_button_gui.itemconfig(self.complete_button_gui.image_id, image=gui_utils.tk_hide_button_skin)
            self.complete_button_gui.itemconfig(self.complete_button_gui.text_id, fill="black")
            # скрываем все проекты
            for projects in self.projects_obj:
                projects.project_frame.pack_forget()
            # и показываем только активные, если они должны показываться
            if self.current_button == True:
                for projects in self.projects_obj:
                    if projects.end_date == None:
                        projects.project_frame.pack(projects.project_frame.widget_pack_info)
            self.complete_button = False
        else:
            self.complete_button_gui.itemconfig(self.complete_button_gui.image_id, image=gui_utils.tk_show_button_skin)
            self.complete_button_gui.itemconfig(self.complete_button_gui.text_id, fill="white")
            # скрываем все проекты
            for projects in self.projects_obj:
                projects.project_frame.pack_forget()
            # показываем завершенные и активные, если они должны показываться
            for projects in self.projects_obj:
                if projects.end_date != None:
                    projects.project_frame.pack(projects.project_frame.widget_pack_info)
                elif self.current_button == True:
                    projects.project_frame.pack(projects.project_frame.widget_pack_info)
            self.complete_button = True

    # функция обработки события нажатия на кнопку отображения Текущих проектов
    def current_view_button_click(self, event):
        if self.current_button:
            # изменяем виджет кнопки
            self.current_button_gui.itemconfig(self.current_button_gui.image_id, image=gui_utils.tk_hide_button_skin)
            self.current_button_gui.itemconfig(self.current_button_gui.text_id, fill="black")
            # скрываем все проекты
            for projects in self.projects_obj:
                projects.project_frame.pack_forget()
            # и показываем только завершенные, если они должны показываться
            if self.complete_button == True:
                for projects in self.projects_obj:
                    if projects.end_date != None:
                        projects.project_frame.pack(projects.project_frame.widget_pack_info)
            self.current_button = False
        else:
            # изменяем виджет кнопки
            self.current_button_gui.itemconfig(self.current_button_gui.image_id, image=gui_utils.tk_show_button_skin)
            self.current_button_gui.itemconfig(self.current_button_gui.text_id, fill="white")
            # скрываем все проекты
            for projects in self.projects_obj:
                projects.project_frame.pack_forget()
            # показываем активные и завершенные, если они должны показываться
            for projects in self.projects_obj:
                if projects.end_date == None:
                    projects.project_frame.pack(projects.project_frame.widget_pack_info)
                elif self.complete_button == True:
                    projects.project_frame.pack(projects.project_frame.widget_pack_info)
            self.current_button = True

    # функция обработки события нажатия на кнопку Добваить новый проект
    def add_project_button_click(self, event):
        # получем имя через диалоговое окно для ввода имени проекта
        #new_project_name = gui_utils.add_project_gui()
        new_project_name = "New Project"
        if new_project_name:
            print(f"Project Name: {new_project_name}")
            # добавляем новый Проект в БД
            project_table = db_utils.add_project(new_project_name)
            # создаем новый обьект класса Проект
            project = Project(self.main_frame_projects, project_table[0], project_table[1], project_table[2], project_table[3])
            # добавляем обьект в список обьектов класаа Main
            self.projects_obj.append(project)
        else:
            print("No project name entered.")

def main_thread():
    global main, conn
    # Подключаемся к базе данных
    conn = db_utils.create_connection(swt_bd)
    # Содаем таблицу проектов если она не была создана
    db_utils.create_table_projects(conn)
    # Создаем объект Main и загружаем в него обьекты Проекты и Задачи из БД
    main = Main()
    while True:
        # если окно закрыто, то выходим из цикла
        # if not gui_thread.is_alive():
        #     break
        # функция обновления таймеров в грфическом окне
        swt_utils.update_window(main)
        time.sleep(1)
    conn.close()  # Закрываем соединение с базой данных

# Точка входа в программу
if __name__ == "__main__":

    # запускаем основную программу в отдельном потоке
    m_thread = threading.Thread(target=main_thread)
    # Закрыть поток при завершении основного потока
    m_thread.daemon = True
    # Запускаем поток
    m_thread.start()

    # Запускаем графический интерфейс
    gui_utils.run_gui()



