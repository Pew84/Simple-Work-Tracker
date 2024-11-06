import tkinter
import tkinter.simpledialog
import db_utils
import swt_utils
from PIL import ImageTk, Image

root = 0
complete_button = 0
current_button = 0

# Функция возвращает обьект типа TKimage для использования его в виджетах библиотеки tkinter
def img_load(path):
    image = Image.open("skin/"+path)
    return ImageTk.PhotoImage(image)

# Функция для запуска графического интерфейса
def run_gui():
    global root, complete_button, current_button

    root = tkinter.Tk()  # Создаем главное окно приложения
    root.title("Simple Work Tracker")  # Устанавливаем заголовок окна
    root.geometry("900x600")  # Устанавливаем размер окна

    # Загружаем изображение и устанавливаем его как иконку
    favicon = tkinter.PhotoImage(file="skin/favicon.png")
    root.iconphoto(False, favicon)

    # блок загрузки изображений для интерфейса
    # фрейм проекта
    global tk_show_tasks_on_skin
    tk_show_tasks_on_skin = img_load("show_tasks_on.png")
    global tk_show_tasks_off_skin
    tk_show_tasks_off_skin = img_load("show_tasks_off.png")
    global tk_add_project_skin
    tk_add_project_skin = img_load("add_project.png")
    global tk_hide_button_skin
    tk_hide_button_skin = img_load("hide_button.png")
    global tk_show_button_skin
    tk_show_button_skin = img_load("show_button.png")
    global tk_add_task_skin
    tk_add_task_skin = img_load("add_task.png")
    global tk_add_task_off_skin
    tk_add_task_off_skin = img_load("add_task_off.png")
    global tk_del_project_skin
    tk_del_project_skin = img_load("del_project.png")
    global tk_del_task_skin
    tk_del_task_skin = img_load("del_task.png")
    global tk_end_project_skin
    tk_end_project_skin = img_load("end_project.png")
    global tk_end_project_ok_skin
    tk_end_project_ok_skin = img_load("end_project_ok.png")
    global tk_project_status_on_skin
    tk_project_status_on_skin = img_load("project_status_on.png")
    global tk_project_status_off_skin
    tk_project_status_off_skin = img_load("project_status_off.png")
    global tk_profect_frame_right_skin
    tk_profect_frame_right_skin = img_load("project_right.png")
    # фрейм задачи
    global tk_end_task_skin
    tk_end_task_skin = img_load("end_task.png")
    global tk_end_task_ok_skin
    tk_end_task_ok_skin = img_load("end_task_ok.png")
    global tk_end_task_active_skin
    tk_end_task_active_skin = img_load("end_task_active.png")
    global tk_start_task_skin
    tk_start_task_skin = img_load("start_task.png")
    global tk_start_task_pause_skin
    tk_start_task_pause_skin = img_load("start_task_pause.png")
    global tk_start_task_end_skin
    tk_start_task_end_skin = img_load("start_task_end.png")
    global tk_task_status_pause_skin
    tk_task_status_pause_skin = img_load("task_status_pause.png")
    global tk_task_status_on_skin
    tk_task_status_on_skin = img_load("task_status_on.png")
    global tk_task_status_off_skin
    tk_task_status_off_skin = img_load("task_status_off.png")
    global tk_task_frame_left_skin
    tk_task_frame_left_skin = img_load("task_frame_left.png")
    global tk_task_frame_right_skin
    tk_task_frame_right_skin = img_load("task_frame_right.png")

    def on_complete():
        print("Complete button clicked")  # Функция для обработки нажатия кнопки завершения
        db_utils.get_list_tasks()

    def on_current():
        print("Current button clicked")  # Функция для обработки нажатия кнопки текущих задач
        db_utils.get_list_projects()

    root.mainloop()  # Запускаем основной цикл обработки событий для окна

# рисуем интерфейс основного окна
def create_main_frame():
    def resize_frame(event):
        # Растягиваем frame на всю площадь canvas
        canvas.itemconfig(frame_id, width=event.width)

    def on_mouse_wheel(event):
        # Определяем направление прокрутки
        if event.delta > 0:  # Прокрутка вверх
            canvas.yview_scroll(-1, "units")
        elif event.delta < 0:  # Прокрутка вниз
            canvas.yview_scroll(1, "units")

    # РИСУЕМ ФРЕЙМ ГЛАВНОЙ ПАНЕЛИ
    main_frame = tkinter.Frame(root, bg="#efefef", height=120)
    main_frame.pack_propagate(False)
    main_frame.grid(row=0, column=0, columnspan=2, sticky="ew")  # Только горизонтальное расширение, занимает 2 столбца
    # кнопка Завершенные основного фрейма
    complete_view_button = tkinter.Canvas(main_frame, bg="#efefef", width=222, height=42, highlightthickness=0)
    complete_view_button.pack_propagate(False)  # запрет деформации
    complete_view_button.pack(side="left", anchor="sw", padx=15, pady=15)
    # Размещаем изображение в Canvas
    complete_view_button.create_image(111, 21, anchor="center", image=tk_hide_button_skin)
    # Пишем подпись кнопки
    complete_view_button.create_text(111, 21, text="Завершенные", font=("Helvetica", 16), fill="black")

    # кнопка Текущие основного фрейма
    current_view_button = tkinter.Canvas(main_frame, bg="#efefef", width=222, height=42, highlightthickness=0)
    current_view_button.pack_propagate(False)
    current_view_button.pack(side="left", anchor="sw", padx=15, pady=15)
    # Размещаем изображение в Canvas
    current_view_button.create_image(111, 21, anchor="center", image=tk_show_button_skin)
    # Пишем подпись кнопки
    current_view_button.create_text(111, 21, text="Текущие", font=("Helvetica", 16), fill="white")

    # кнопка СОЗДАНИЯ НОВОГО ПРОЕКТА
    # Создаем Canvas для размещения изображения
    add_project_button = tkinter.Canvas(main_frame, bg="#efefef", width=80, height=80, highlightthickness=0)
    add_project_button.pack(side="right", anchor="sw", padx=15, pady=15)
    # Размещаем изображение в Canvas
    add_project_button.create_image(40, 40, anchor="center", image=tk_add_project_skin)

    # Создаем холст для области списка проектов
    canvas = tkinter.Canvas(root, bg="yellow") #, scrollregion=(0, 0, 1000, 1000))
    #canvas.pack(side="left", fill="both", expand=True)
    canvas.grid(row=1, column=0, sticky="nsew")  # Растягиваем по всем направлениям
    root.grid_columnconfigure(0, weight=1)  # Столбец 0 будет растягиваться по ширине
    root.grid_rowconfigure(1, weight=1)  # Строка 1 будет растягиваться по высоте
    canvas.grid_columnconfigure(0, weight=1)  # Столбец 0 будет растягиваться по ширине
    # Добавляем Scrollbar и привязываем его к холсту
    scrollbar = tkinter.Scrollbar(root, orient="vertical", command=canvas.yview)
    #scrollbar.pack(side="right", fill="y")
    scrollbar.grid(row=1, column=1, sticky="ns")
    # Привязываем прокрутку холста к Scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)

    # РИСУЕМ ФРЕЙМ ДЛЯ ПРОЕКТОВ И ПРИВЯЗЫВАЕМ ЕГО К ХОЛСТУ
    main_frame_projects = tkinter.Frame(canvas, bg="#efefef")
    main_frame_projects.grid(row=0, column=0, sticky="ew")  # Только горизонтальное расширение
    # Обновляем область прокрутки при измении размера фрейма
    main_frame_projects.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    # Используем create_window, чтобы поместить фрейм в холст
    frame_id = canvas.create_window((0, 0), window=main_frame_projects, anchor="nw")
    # Меняем ширину фрейма с проектами при изменении размеров главного окна
    canvas.bind('<Configure>', resize_frame)
    # Обработка прокрутки колеса мыши
    canvas.bind_all("<MouseWheel>", on_mouse_wheel)
    root.geometry("901x600")  # меняем размер окна для срабатывания события event, чтобы все элементы растянулись на всю ширину окна
    return main_frame_projects, complete_view_button, current_view_button, add_project_button


# рисуем интерфейс проекта
def create_project_gui(main_frame_projects, project_name, begin_date, end_date):
    # основной фрейм
    main_project_frame = tkinter.Frame(main_frame_projects, bg="#cfcfcf", width=800, height=100)
    main_project_frame.pack(expand=True, fill='x', side='bottom', anchor="nw", padx=15, pady=15)
    # фрейм управления проектом
    project_frame = tkinter.Frame(main_project_frame, bg="#556c95", width=800, height=80)
    project_frame.pack_propagate(False)
    project_frame.pack(expand=True, fill='x', side='top', anchor="nw", padx=10, pady=10)
    # РАЗДЕЛ ГРАФИЧЕСКИХ ЭЛЕМЕНТОВ ПЛАШКИ УПРАВЛЕНИЯ ПРОЕКТАМИ
    project_frame.grid_columnconfigure(3, weight=5, minsize=80)  # Столбец 3 будет растягиваться по ширине
    project_frame.grid_columnconfigure(2, weight=1)  # Столбец 2 будет растягиваться по ширине
    #project_frame.grid_columnconfigure(1, minsize=40, weight=0)  # 1 столбец фиксированной ширины
    # кнопка показа списка задач
    show_tasks_button = tkinter.Canvas(project_frame, bg="#cfcfcf", width=70, height=80, highlightthickness=0)
    show_tasks_button.grid(row=0, column=0, rowspan=2)
    show_tasks_button.create_image(35, 40, anchor="center", image=tk_show_tasks_on_skin)  # Размещаем изображение в Canvas
    # ферейм для размещения Имя проекта и кнопки удаления
    project_name_frame = tkinter.Frame(project_frame, bg="#556c95", width=40, height=40)
    project_name_frame.grid(row=0, column=1, columnspan=2, sticky="w")
    # текст с названием проекта
    name_project_text = tkinter.Label(project_name_frame, text=project_name)
    name_project_text.pack(side=tkinter.LEFT)
    # кнопка удаления проекта
    delete_project_button = tkinter.Canvas(project_name_frame, bg="#556c95", width=40, height=40, highlightthickness=0)
    delete_project_button.pack_propagate(True)
    delete_project_button.pack(side=tkinter.RIGHT)
    delete_project_button.create_image(20, 20, anchor="center", image=tk_del_project_skin)  # Размещаем изображение в Canvas
    # ферейм для размещения кнопок добавления задачи и завершения проекта
    project_addend_frame = tkinter.Frame(project_frame, bg="#556c95", width=40, height=40)
    project_addend_frame.grid(row=1, column=1, sticky="w")
    # кнопка добавления задачи
    add_task_button = tkinter.Canvas(project_addend_frame, bg="#556c95", width=40, height=40, highlightthickness=0)
    add_task_button.pack(side=tkinter.LEFT)
    if end_date is None:
        add_task_button.create_image(20, 20, anchor="center", image=tk_add_task_skin)  # Размещаем изображение в Canvas
    # кнопка завершения проекта
    end_project_button = tkinter.Canvas(project_addend_frame, bg="#556c95", width=122, height=34, highlightthickness=0)
    end_project_button.pack(side=tkinter.LEFT)
    if end_date is None:
        end_project_button.image_id = end_project_button.create_image(61, 17, anchor="center", image=tk_end_project_skin)  # Размещаем изображение в Canvas
        end_project_button.text_id = end_project_button.create_text(61, 17, text="Завершить", font=("Helvetica", 13), fill="white")  # Пишем подпись кнопки
    else:
        add_task_button.pack_forget()
        end_project_button.image_id = end_project_button.create_image(61, 17, anchor="center", image=tk_end_project_ok_skin)  # Размещаем изображение в Canvas
        end_project_button.text_id = end_project_button.create_text(61, 17, text="Завершено", font=("Helvetica", 13), fill="black")  # Пишем подпись кнопки
    # текст с датой начала проекта
    if end_date is None:
        begin_date_project_text = tkinter.Label(project_frame, text=swt_utils.date_format(begin_date)+' - ...')
    else:
        begin_date_project_text = tkinter.Label(project_frame, text=swt_utils.date_format(begin_date)+' - '+swt_utils.date_format(end_date))
    begin_date_project_text.grid(row=0, column=3, rowspan=2)
    # текст общее время затраченное на проект
    timer_project_text = tkinter.Label(project_frame, text="Общий таймер проекта")
    timer_project_text.grid(row=0, column=4, rowspan=2, padx=10)
    # иконка статуса проекта
    status_project_icon = tkinter.Canvas(project_frame, bg="#556c95", width=30, height=30, highlightthickness=0)
    status_project_icon.grid(row=0, column=5, rowspan=2, padx=0)
    if end_date is None:
        status_project_icon.image_id = status_project_icon.create_image(15, 15, anchor="center", image=tk_project_status_on_skin)  # Размещаем изображение в Canvas
    else:
        status_project_icon.image_id = status_project_icon.create_image(15, 15, anchor="center", image=tk_project_status_off_skin)  # Размещаем изображение в Canvas
    # элемент закругления справа
    project_right_frame = tkinter.Canvas(project_frame, bg="#cfcfcf", width=20, height=80, highlightthickness=0)
    project_right_frame.grid(row=0, column=6, rowspan=2, padx=0)
    project_right_frame.create_image(10, 40, anchor="center", image=tk_profect_frame_right_skin)
    return main_project_frame, delete_project_button, add_task_button, timer_project_text, end_project_button, begin_date_project_text, status_project_icon

# рисуем интерфейс задачи
def create_task_gui(project_frame, task_name, start_date, end_date, timer_status):
    # # фрейм управления задачей
    task_frame = tkinter.Frame(project_frame, bg="#ececec", width=800, height=60)
    task_frame.pack_propagate(False)
    task_frame.pack(expand=True, fill='x', side='top', anchor="nw", padx=10, pady=10)
    # РАЗДЕЛ ГРАФИЧЕСКИХ ЭЛЕМЕНТОВ ПЛАШКИ УПРАВЛЕНИЯ ЗАДАЧЕЙ
    task_frame.grid_columnconfigure(6, weight=5, minsize=80)  # Столбец 5 будет растягиваться по ширине
    task_frame.grid_columnconfigure(4, weight=1)  # Столбец 3 будет растягиваться по ширине
    task_frame.grid_columnconfigure(2, minsize=40, weight=0)  # 1 столбец фиксированной ширины
    task_frame.grid_columnconfigure(3, minsize=80)  # 2 столбец фиксированной ширины
    # стрелка древовидной структуры
    narrow_task = tkinter.Canvas(task_frame, bg="#cfcfcf", width=40, height=70, highlightthickness=0)
    narrow_task.grid(row=0, column=0, rowspan=2)
    # фигура закругления слева
    task_frame_left = tkinter.Canvas(task_frame, bg="#cfcfcf", width=20, height=70, highlightthickness=0)
    task_frame_left.grid(row=0, column=1, rowspan=2)
    task_frame_left.create_image(10, 35, anchor="center", image=tk_task_frame_left_skin)  # Размещаем изображение
    # текст с названием Задачи
    name_task_text = tkinter.Label(task_frame, text=task_name)
    name_task_text.grid(row=0, column=2, columnspan=3, sticky="w")
    # кнопка удаления Задачи
    delete_task_button = tkinter.Canvas(task_frame, bg="#ececec", width=30, height=30, highlightthickness=0)
    delete_task_button.grid(row=0, column=5, sticky="e")
    delete_task_button.create_image(15, 15, anchor="center", image=tk_del_task_skin)  # Размещаем изображение
    # кнопка старт/пауза Задачи
    start_task_button = tkinter.Canvas(task_frame, bg="#ececec", width=28, height=28, highlightthickness=0)
    if end_date is None:
        start_task_button.grid(row=1, column=2, sticky="w", padx=0, pady=5)
        if timer_status:
            start_task_button.image_id = start_task_button.create_image(14, 14, anchor="center", image=tk_start_task_pause_skin)  # Размещаем изображение
        else:
            start_task_button.image_id = start_task_button.create_image(14, 14, anchor="center", image=tk_start_task_skin)  # Размещаем изображение
    else:
        start_task_button.grid_forget()
    # кнопка завершения Задачи
    end_task_button = tkinter.Canvas(task_frame, bg="#ececec", width=100, height=28, highlightthickness=0)
    end_task_button.grid(row=1, column=3, sticky="e", padx=0, pady=5)
    if end_date is None:
        if timer_status:
            end_task_button.image_id = end_task_button.create_image(50, 14, anchor="center", image=tk_end_task_active_skin)  # Размещаем изображение в Canvas
        else:
            end_task_button.image_id = end_task_button.create_image(50, 14, anchor="center", image=tk_end_task_skin)  # Размещаем изображение в Canvas
        end_task_button.text_id = end_task_button.create_text(50, 14, text="Завершить", font=("Helvetica", 10), fill="white")  # Пишем подпись кнопки
    else:
        end_task_button.grid(row=1, column=2, sticky="e", padx=0, pady=5)
        end_task_button.image_id = end_task_button.create_image(50, 14, anchor="center", image=tk_end_task_ok_skin)  # Размещаем изображение в Canvas
        end_task_button.text_id = end_task_button.create_text(50, 14, text="Завершено", font=("Helvetica", 10), fill="black")  # Пишем подпись кнопки
    # текст с датой начала Задачи
    if end_date is None:
        label_text = swt_utils.date_format(start_date)
    else:
        label_text = swt_utils.date_format(start_date)+' - '+swt_utils.date_format(end_date)
    begin_date_task_text = tkinter.Label(task_frame, text=label_text)
    begin_date_task_text.grid(row=0, column=6, rowspan=2)
    # текст общее время затраченное на Задачу
    timer_task_text = tkinter.Label(task_frame, text="0")
    timer_task_text.grid(row=0, column=7, rowspan=2)
    # иконка статуса Задачи
    status_task_icon = tkinter.Canvas(task_frame, bg="#ececec", width=24, height=24, highlightthickness=0)
    status_task_icon.grid(row=0, column=8, rowspan=2, padx=0)
    if end_date is None:
        if timer_status:
            status_task_icon.image_id = status_task_icon.create_image(12, 12, anchor="center", image=tk_task_status_on_skin)  # Размещаем изображение
        else:
            status_task_icon.image_id = status_task_icon.create_image(12, 12, anchor="center", image=tk_task_status_pause_skin)
    else:
        status_task_icon.image_id = status_task_icon.create_image(12, 12, anchor="center", image=tk_task_status_off_skin)
    # фигура закругления справа
    task_frame_right = tkinter.Canvas(task_frame, bg="#cfcfcf", width=20, height=70, highlightthickness=0)
    task_frame_right.grid(row=0, column=9, rowspan=2)
    task_frame_right.create_image(10, 35, anchor="center", image=tk_task_frame_right_skin)  # Размещаем изображение
    return task_frame, delete_task_button, start_task_button, timer_task_text, end_task_button, begin_date_task_text, status_task_icon

# Диалоговое окно создания нового Проекта
def add_project_gui():
    return tkinter.simpledialog.askstring("Новый Проект", "Введите имя проекта:")

# Диалоговое окно создания новой Задачи
def add_task_gui():
    return tkinter.simpledialog.askstring("Новая Задача", "Введите имя задачи:")