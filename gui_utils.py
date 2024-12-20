import tkinter
import tkinter.simpledialog
import tkinter.font
import tkextrafont
import db_utils
import swt_utils
from PIL import ImageTk, Image

root = 0
#complete_button = 0
#current_button = 0

# Функция возвращает обьект типа TKimage для использования его в виджетах библиотеки tkinter
def img_load(path):
    image = Image.open("skin/"+path)
    return ImageTk.PhotoImage(image)

# обработка событию закрытия окна
def on_close():
    # Сохраняем пложение и размер окна в БД
    db_utils.update_value('OPTIONS', 'window_geometry', 1, root.geometry())
    root.destroy()  # Закрыть главное окно

# уменьшение ширины главного окна на 1
def resize_width():
    # Получаем текущие размеры окна
    current_geometry = root.geometry()
    # Парсинг строки geometry "WxH+X+Y"
    dimensions, position = current_geometry.split("+", 1)
    width, height = map(int, dimensions.split("x"))
    x, y = map(int, position.split("+"))
    # Уменьшаем ширину на 1 пиксель
    new_width = max(width - 1, 1)  # Не позволяем ширине быть меньше 1
    root.geometry(f"{new_width}x{height}+{x}+{y}")


def parse_geometry(geometry):
    # Парсинг строки geometry "WxH+X+Y"
    dimensions, position = geometry.split("+", 1)
    width, height = map(int, dimensions.split("x"))
    x, y = map(int, position.split("+"))
    return width, height, x, y

# Функция для запуска графического интерфейса
def run_gui():
    global root

    root = tkinter.Tk()  # Создаем главное окно приложения
    root.title("Simple Work Tracker")  # Устанавливаем заголовок окна
    root.geometry(db_utils.get_value('OPTIONS', 'window_geometry', 1))  # Устанавливаем размер окна

    # Загружаем изображение и устанавливаем его как иконку
    favicon = tkinter.PhotoImage(file="skin/favicon.png")
    root.iconphoto(False, favicon)

    # Привязываем функцию к событию закрытия окна
    root.protocol("WM_DELETE_WINDOW", on_close)

    # загружаем шрифты
    """Represents a named font.

        Constructor options are:

        font -- font specifier (name, system font, or (family, size, style)-tuple)
        name -- name to use for this font configuration (defaults to a unique name)
        exists -- does a named font by this name already exist?
           Creates a new named font if False, points to the existing font if True.
           Raises _tkinter.TclError if the assertion is false.

           the following are ignored if font is specified:

        family -- font 'family', e.g. Courier, Times, Helvetica
        size -- font size in points
        weight -- font thickness: NORMAL, BOLD
        slant -- font slant: ROMAN, ITALIC
        underline -- font underlining: false (0), true (1)
        overstrike -- font strikeout: false (0), true (1)
        """
    # импорт шрифта из файла в объект для tkinter
    Onest_Regular = tkextrafont.Font(root=root, file="fonts/Onest-Regular.ttf", family="Onest", size=18, weight="bold")
    global project_name_font
    project_name_font = tkinter.font.Font(family="Onest", size=18, weight="bold")
    global project_data_font
    project_data_font = tkinter.font.Font(family="Onest", size=16, weight="normal")
    global project_time_font
    project_time_font = tkinter.font.Font(family="Onest", size=16, weight="bold")
    global task_name_font
    task_name_font = tkinter.font.Font(family="Onest", size=14, weight="bold")
    global task_data_font
    task_data_font = tkinter.font.Font(family="Onest", size=12, weight="normal")
    global task_time_font
    task_time_font = tkinter.font.Font(family="Onest", size=14, weight="bold")

    # блок загрузки изображений для интерфейса
    # главный фрейм
    global tk_add_project_skin
    tk_add_project_skin = img_load("add_project.png")
    global tk_add_project_hover_skin
    tk_add_project_hover_skin = img_load("add_project_hover.png")
    global tk_hide_button_skin
    tk_hide_button_skin = img_load("hide_button.png")
    global tk_hide_button_hover_skin
    tk_hide_button_hover_skin = img_load("hide_button_hover.png")
    global tk_show_button_skin
    tk_show_button_skin = img_load("show_button.png")
    global tk_show_button_hover_skin
    tk_show_button_hover_skin = img_load("show_button_hover.png")
    # фрейм проекта
    global tk_show_tasks_on_skin
    tk_show_tasks_on_skin = img_load("show_tasks_on.png")
    global tk_show_tasks_on_hover_skin
    tk_show_tasks_on_hover_skin = img_load("show_tasks_on_hover.png")
    global tk_show_tasks_off_skin
    tk_show_tasks_off_skin = img_load("show_tasks_off.png")
    global tk_show_tasks_off_hover_skin
    tk_show_tasks_off_hover_skin = img_load("show_tasks_off_hover.png")
    global tk_add_task_skin
    tk_add_task_skin = img_load("add_task.png")
    global tk_add_task_hover_skin
    tk_add_task_hover_skin = img_load("add_task_hover.png")
    global tk_add_task_off_skin
    tk_add_task_off_skin = img_load("add_task_off.png")
    global tk_del_project_skin
    tk_del_project_skin = img_load("del_project.png")
    global tk_del_task_skin
    tk_del_task_skin = img_load("del_task.png")
    global tk_end_project_skin
    tk_end_project_skin = img_load("end_project.png")
    global tk_end_project_hover_skin
    tk_end_project_hover_skin = img_load("end_project_hover.png")
    global tk_end_project_ok_skin
    tk_end_project_ok_skin = img_load("end_project_ok.png")
    global tk_project_status_on_skin
    tk_project_status_on_skin = img_load("project_status_on.png")
    global tk_project_status_off_skin
    tk_project_status_off_skin = img_load("project_status_off.png")
    global tk_profect_frame_right_skin
    tk_profect_frame_right_skin = img_load("project_right.png")
    global tk_rectangleNW_skin
    tk_rectangleNW_skin = img_load("rectangleNW.png")
    global tk_rectangleNE_skin
    tk_rectangleNE_skin = img_load("rectangleNE.png")
    global tk_rectangleSW_skin
    tk_rectangleSW_skin = img_load("rectangleSW.png")
    global tk_rectangleSE_skin
    tk_rectangleSE_skin = img_load("rectangleSE.png")
    global tk_project_pay_free_skin
    tk_project_pay_free_skin = img_load("project_pay_free.png")
    global tk_project_pay_free_hover_skin
    tk_project_pay_free_hover_skin = img_load("project_pay_free_hover.png")
    global tk_project_pay_ok_skin
    tk_project_pay_ok_skin = img_load("project_pay_ok.png")
    global tk_project_pay_ok_hover_skin
    tk_project_pay_ok_hover_skin = img_load("project_pay_ok_hover.png")
    global tk_project_pay_wait_skin
    tk_project_pay_wait_skin = img_load("project_pay_wait.png")
    global tk_project_pay_wait_hover_skin
    tk_project_pay_wait_hover_skin = img_load("project_pay_wait_hover.png")
    # фрейм задачи
    global tk_end_task_skin
    tk_end_task_skin = img_load("end_task.png")
    global tk_end_task_hover_skin
    tk_end_task_hover_skin = img_load("end_task_hover.png")
    global tk_end_task_ok_skin
    tk_end_task_ok_skin = img_load("end_task_ok.png")
    global tk_end_task_active_skin
    tk_end_task_active_skin = img_load("end_task_active.png")
    global tk_end_task_active_hover_skin
    tk_end_task_active_hover_skin = img_load("end_task_active_hover.png")
    global tk_start_task_skin
    tk_start_task_skin = img_load("start_task.png")
    global tk_start_task_pause_skin
    tk_start_task_pause_skin = img_load("start_task_pause.png")
    global tk_start_task_hover_skin
    tk_start_task_hover_skin = img_load("start_task_hover.png")
    global tk_start_task_pause_hover_skin
    tk_start_task_pause_hover_skin = img_load("start_task_pause_hover.png")
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
    global tk_arrow_skin
    tk_arrow_skin = img_load("arrow.png")
    global tk_arrow_last_skin
    tk_arrow_last_skin = img_load("arrow_last.png")
    global tk_task_pay_free_skin
    tk_task_pay_free_skin = img_load("task_pay_free.png")
    global tk_task_pay_free_hover_skin
    tk_task_pay_free_hover_skin = img_load("task_pay_free_hover.png")
    global tk_task_pay_ok_skin
    tk_task_pay_ok_skin = img_load("task_pay_ok.png")
    global tk_task_pay_ok_hover_skin
    tk_task_pay_ok_hover_skin = img_load("task_pay_ok_hover.png")
    global tk_task_pay_wait_skin
    tk_task_pay_wait_skin = img_load("task_pay_wait.png")
    global tk_task_pay_wait_hover_skin
    tk_task_pay_wait_hover_skin = img_load("task_pay_wait_hover.png")


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
    # кнопка ЗАВЕРШЕННЫЕ основного фрейма
    complete_view_button = tkinter.Canvas(main_frame, bg="#efefef", width=222, height=42, highlightthickness=0)
    complete_view_button.pack_propagate(False)  # запрет деформации
    complete_view_button.pack(side="left", anchor="sw", padx=15, pady=0)
    # Размещаем изображение в Canvas
    if db_utils.get_value('OPTIONS', 'complete_visible', 1) == 0:
        complete_view_button.image_id = complete_view_button.create_image(111, 21, anchor="center", image=tk_hide_button_skin)
        # Пишем подпись кнопки
        complete_view_button.text_id = complete_view_button.create_text(95, 21, text="Завершенные", font=("Helvetica", 16), fill="black")
    else:
        complete_view_button.image_id = complete_view_button.create_image(111, 21, anchor="center", image=tk_show_button_skin)
        # Пишем подпись кнопки
        complete_view_button.text_id = complete_view_button.create_text(95, 21, text="Завершенные", font=("Helvetica", 16), fill="white")
    complete_view_button.create_image(185, 21, anchor="center", image=tk_task_status_off_skin)

    # кнопка ТЕКУЩИЕ основного фрейма
    current_view_button = tkinter.Canvas(main_frame, bg="#efefef", width=222, height=42, highlightthickness=0)
    current_view_button.pack_propagate(False)
    current_view_button.pack(side="left", anchor="sw", padx=0, pady=0)
    # Размещаем изображение в Canvas
    if db_utils.get_value('OPTIONS', 'current_visible', 1) == 1:
        current_view_button.image_id = current_view_button.create_image(111, 21, anchor="center", image=tk_show_button_skin)
        # Пишем подпись кнопки
        current_view_button.text_id = current_view_button.create_text(95, 21, text="Текущие", font=("Helvetica", 16), fill="white")
    else:
        current_view_button.image_id = current_view_button.create_image(111, 21, anchor="center", image=tk_hide_button_skin)
        # Пишем подпись кнопки
        current_view_button.text_id = current_view_button.create_text(95, 21, text="Текущие", font=("Helvetica", 16), fill="black")
    current_view_button.create_image(165, 21, anchor="center", image=tk_task_status_on_skin)


    # кнопка СОЗДАНИЯ НОВОГО ПРОЕКТА
    # Создаем Canvas для размещения изображения
    add_project_button = tkinter.Canvas(main_frame, bg="#efefef", width=80, height=80, highlightthickness=0)
    add_project_button.pack(side="right", anchor="sw", padx=50, pady=0)
    # Размещаем изображение в Canvas
    add_project_button.image_id = add_project_button.create_image(40, 40, anchor="center", image=tk_add_project_skin)

    # Создаем холст для области списка проектов
    canvas = tkinter.Canvas(root, bg="#efefef", highlightthickness=0) #, scrollregion=(0, 0, 1000, 1000))
    canvas.grid(row=1, column=0, sticky="nsew", padx=15, pady=15)  # Растягиваем по всем направлениям
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
    #main_frame_projects.grid(row=0, column=0, sticky="ew")  # Только горизонтальное расширение
    # Обновляем область прокрутки при измении размера фрейма
    main_frame_projects.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    # Используем create_window, чтобы поместить фрейм в холст
    frame_id = canvas.create_window((0, 0), window=main_frame_projects, anchor="nw")
    # Меняем ширину фрейма с проектами при изменении размеров главного окна
    canvas.bind('<Configure>', resize_frame)
    # Обработка прокрутки колеса мыши
    canvas.bind_all("<MouseWheel>", on_mouse_wheel)
    resize_width() # меняем размер окна для срабатывания события event, чтобы все элементы растянулись на всю ширину окна
    return main_frame_projects, complete_view_button, current_view_button, add_project_button


# рисуем интерфейс проекта
def create_project_gui(main_frame_projects, project_name, begin_date, end_date, project_class):
    # функция редактирования имени проекта
    def edit_project_name(event):
        name_project_text.pack_forget()
        name_project_text_edit.delete(0, tkinter.END)
        name_project_text_edit.insert(0, name_project_text["text"])
        adjust_entry_width()
        name_project_text_edit.pack(side=tkinter.LEFT, anchor=tkinter.SW, padx=15)
        name_project_text_edit.focus()
        root.bind("<Button-1>", click_outside)  # Включаем отслеживание кликов вне Entry

    # функция сохранения введенного имени проекта
    def save_project_name(event=None):
        name_project_text.config(text=name_project_text_edit.get())
        name_project_text_edit.pack_forget()
        name_project_text.pack(side=tkinter.LEFT, anchor=tkinter.SW, padx=15)
        root.unbind("<Button-1>")  # Отключаем отслеживание кликов
        # сохраняем в БД
        db_utils.update_value("PROJECTS", "project_name", project_class.id, name_project_text_edit.get())
        # сохраняем в свойство объекта
        project_class.name = name_project_text_edit.get()

    # функция ввода имени проекта при клике вне виджета редактирования имени
    def click_outside(event):
        if event.widget != name_project_text_edit:
            save_project_name()

    # функция расширения ширины виджета при вводе имени проекта
    def adjust_entry_width(*args):
        font = tkinter.font.Font(font=name_project_text_edit["font"])
        text_width = font.measure(name_project_text_edit.get())
        name_project_text_edit.config(width=max(text_width // font.measure("0") + 1, 1))  # +1 для корректировки

    # основной фрейм
    main_project_frame = tkinter.Frame(main_frame_projects, bg="#cfcfcf", width=800, height=100)
    main_project_frame.pack(expand=True, fill='x', side='bottom', anchor="nw", padx=0, pady=15) # Только горизонтальное расширение
    main_project_frame.widget_pack_info = main_project_frame.pack_info() # Сохраняем параметры компоновки
    # проверка на фильтр видимости ТЕКУЩИХ и ЗАВЕРШЕННЫХ проектов
    if (project_class.end_date is None) and (bool(db_utils.get_value('OPTIONS', 'current_visible', 1)) == False):
        main_project_frame.pack_forget()
    if (project_class.end_date is not None) and (bool(db_utils.get_value('OPTIONS', 'complete_visible', 1)) == False):
        main_project_frame.pack_forget()
    # область верхнего скругления фрейма проекта
    main_frame_rectangle_top = tkinter.Frame(main_project_frame, bg="#cfcfcf", width=800, height=15)
    main_frame_rectangle_top.pack(expand=True, fill='x', side='top', anchor="nw", padx=0, pady=0)  # Только горизонтальное расширение
    main_frame_rectangle_top.grid_columnconfigure(1, weight=1)  # Столбец 1 будет растягиваться по ширине
    rectangleNW_canvas = tkinter.Canvas(main_frame_rectangle_top, bg="#efefef", width=15, height=15, highlightthickness=0)
    rectangleNW_canvas.pack_propagate(False)
    rectangleNW_canvas.grid(row=0, column=0)
    rectangleNW_canvas.create_image(7, 7, anchor="center", image=tk_rectangleNW_skin)
    middle_frame_top = tkinter.Frame(main_frame_rectangle_top, bg="#cfcfcf", height=15)
    middle_frame_top.grid(row=0, column=1)
    rectangleNE_canvas = tkinter.Canvas(main_frame_rectangle_top, bg="#efefef", width=15, height=15, highlightthickness=0)
    rectangleNE_canvas.pack_propagate(False)
    rectangleNE_canvas.grid(row=0, column=2)
    rectangleNE_canvas.create_image(7, 7, anchor="center", image=tk_rectangleNE_skin)
    # область нижнего скругления фрейма проекта
    main_frame_rectangle_bottom = tkinter.Frame(main_project_frame, bg="#cfcfcf", width=800, height=15)
    main_frame_rectangle_bottom.pack(expand=True, fill='x', side='bottom', anchor="nw", padx=0, pady=0)  # Только горизонтальное расширение
    main_frame_rectangle_bottom.grid_columnconfigure(1, weight=1)  # Столбец 1 будет растягиваться по ширине
    rectangleSW_canvas = tkinter.Canvas(main_frame_rectangle_bottom, bg="#efefef", width=15, height=15, highlightthickness=0)
    rectangleSW_canvas.pack_propagate(False)
    rectangleSW_canvas.grid(row=0, column=0)
    rectangleSW_canvas.create_image(7, 7, anchor="center", image=tk_rectangleSW_skin)
    middle_frame_bottom = tkinter.Frame(main_frame_rectangle_bottom, bg="#cfcfcf", height=15)
    middle_frame_bottom.grid(row=0, column=1)
    rectangleSE_canvas = tkinter.Canvas(main_frame_rectangle_bottom, bg="#efefef", width=15, height=15, highlightthickness=0)
    rectangleSE_canvas.pack_propagate(False)
    rectangleSE_canvas.grid(row=0, column=2)
    rectangleSE_canvas.create_image(7, 7, anchor="center", image=tk_rectangleSE_skin)

    # ФРЕЙМ УПРАВЛЕНИЯ ПРОЕКТОМ
    project_frame = tkinter.Frame(main_project_frame, bg="#556c95", width=800, height=90)
    project_frame.pack_propagate(False)
    project_frame.pack(expand=True, fill='x', side='top', anchor="nw", padx=15, pady=0)
    # раздел графических элементов плашки управления проектами
    project_frame.grid_columnconfigure(3, weight=5, minsize=80)  # Столбец 3 будет растягиваться по ширине
    project_frame.grid_columnconfigure(2, weight=1)  # Столбец 2 будет растягиваться по ширине
    project_frame.grid_columnconfigure(4, minsize=300, weight=0)  # Столбец будет растягиваться по ширине
    #project_frame.grid_columnconfigure(1, minsize=40, weight=0)  # 1 столбец фиксированной ширины
    # кнопка показа списка задач
    show_tasks_button = tkinter.Canvas(project_frame, bg="#cfcfcf", width=80, height=90, highlightthickness=0)
    show_tasks_button.grid(row=0, column=0, rowspan=2)
    show_tasks_button.image_id = show_tasks_button.create_image(40, 45, anchor="center", image=tk_show_tasks_on_skin)  # Размещаем изображение в Canvas
    # ферейм для размещения Имя проекта и кнопки удаления
    project_name_frame = tkinter.Frame(project_frame, bg="#556c95", width=40, height=44)
    project_name_frame.grid(row=0, column=1, columnspan=2, sticky="w")
    # текст с названием проекта
    name_project_text = tkinter.Label(project_name_frame, text=project_name, bg="#556c95", fg="white", font=project_name_font)
    name_project_text.bind("<Button-1>", edit_project_name)
    name_project_text.pack(side=tkinter.LEFT, anchor=tkinter.SW, padx=15)
    # виджет для редактирования текста
    name_project_text_edit = tkinter.Entry(project_name_frame, bg="#556c95", fg="white", font=project_name_font, relief=tkinter.FLAT, insertbackground="white", selectbackground="#8899b6")
    name_project_text_edit.bind("<KeyRelease>", adjust_entry_width)  # Перехватываем событие при вводе текста
    name_project_text_edit.bind("<Return>", save_project_name) # функция при завершении ввода текста
    # кнопка удаления проекта
    delete_project_button = tkinter.Canvas(project_name_frame, bg="#556c95", width=40, height=40, highlightthickness=0)
    delete_project_button.pack_propagate(True)
    delete_project_button.pack(side=tkinter.RIGHT)
    delete_project_button.create_image(20, 20, anchor="center", image=tk_del_project_skin)  # Размещаем изображение в Canvas
    # ферейм для размещения Cтатуса оплаты, кнопок добавления задачи и завершения проекта
    project_addend_frame = tkinter.Frame(project_frame, bg="#556c95", width=40, height=44)
    project_addend_frame.grid(row=1, column=1, sticky="sw", padx=10, pady=0)
    # кнопка статус оплаты проекта
    project_payment_button = tkinter.Canvas(project_addend_frame, bg="#556c95", width=43, height=40, highlightthickness=0)
    project_payment_button.pack_propagate(True)
    project_payment_button.pack(side=tkinter.LEFT, anchor=tkinter.CENTER, padx=0, pady=0)
    # Размещаем изображение в Canvas в зависимости от статуса оплаты
    if project_class.project_pay == 'wait':
        project_payment_button.image_id = project_payment_button.create_image(24, 17, anchor="center", image=tk_project_pay_wait_skin)
    if project_class.project_pay == 'ok':
        project_payment_button.image_id = project_payment_button.create_image(24, 17, anchor="center", image=tk_project_pay_ok_skin)
    if project_class.project_pay == 'free':
        project_payment_button.image_id = project_payment_button.create_image(24, 17, anchor="center", image=tk_project_pay_free_skin)
    # кнопка добавления задачи bg="#556c95"
    add_task_button = tkinter.Canvas(project_addend_frame, bg="#556c95", width=34, height=42, highlightthickness=0)
    add_task_button.pack(side=tkinter.LEFT, anchor=tkinter.S, padx=5, pady=0)
    if end_date is None:
        add_task_button.image_id = add_task_button.create_image(17, 17, anchor="center", image=tk_add_task_skin)  # Размещаем изображение в Canvas
    # кнопка завершения проекта
    end_project_button = tkinter.Canvas(project_addend_frame, bg="#556c95", width=122, height=42, highlightthickness=0)
    end_project_button.pack(side=tkinter.LEFT, padx=5, pady=0)
    if end_date is None:
        end_project_button.image_id = end_project_button.create_image(61, 17, anchor="center", image=tk_end_project_skin)  # Размещаем изображение в Canvas
        end_project_button.text_id = end_project_button.create_text(61, 17, text="Завершить", font=("Helvetica", 14), fill="white")  # Пишем подпись кнопки
    else:
        add_task_button.pack_forget()
        end_project_button.image_id = end_project_button.create_image(61, 17, anchor="center", image=tk_end_project_ok_skin)  # Размещаем изображение в Canvas
        end_project_button.text_id = end_project_button.create_text(61, 17, text="Завершено", font=("Helvetica", 14), fill="white")  # Пишем подпись кнопки
    # текст с датой начала проекта
    begin_date_project_text = tkinter.Label(project_frame, text="", bg="#556c95", fg="#8cc939", font=project_data_font)
    if end_date is None:
        begin_date_project_text.config(text=swt_utils.date_format(begin_date)+' - ...      ')
    else:
        begin_date_project_text.config(text=swt_utils.date_format(begin_date)+' - '+swt_utils.date_format(end_date))
    begin_date_project_text.grid(row=0, column=3, rowspan=2)
    # текст общее время затраченное на проект
    timer_project_text = tkinter.Label(project_frame, text="", bg="#556c95", fg="#8cc939", font=project_time_font)
    timer_project_text.grid(row=0, column=4, rowspan=2, padx=15, sticky="e")
    # иконка статуса проекта
    status_project_icon = tkinter.Canvas(project_frame, bg="#556c95", width=30, height=30, highlightthickness=0)
    status_project_icon.grid(row=0, column=5, rowspan=2, padx=0)
    if end_date is None:
        status_project_icon.image_id = status_project_icon.create_image(15, 15, anchor="center", image=tk_project_status_on_skin)  # Размещаем изображение в Canvas
    else:
        status_project_icon.image_id = status_project_icon.create_image(15, 15, anchor="center", image=tk_project_status_off_skin)  # Размещаем изображение в Canvas
    # элемент закругления справа
    project_right_frame = tkinter.Canvas(project_frame, bg="#cfcfcf", width=20, height=90, highlightthickness=0)
    project_right_frame.grid(row=0, column=6, rowspan=2, padx=0)
    project_right_frame.create_image(10, 45, anchor="center", image=tk_profect_frame_right_skin)
    return (main_project_frame,
            delete_project_button,
            add_task_button,
            timer_project_text,
            end_project_button,
            begin_date_project_text,
            status_project_icon,
            show_tasks_button,
            project_payment_button)

# рисуем интерфейс задачи
def create_task_gui(main_project_frame, task_name, start_date, end_date, timer_status, last_task, task_class):
    def edit_task_name(event):
        name_task_text.pack_forget()
        name_task_text_edit.delete(0, tkinter.END)
        name_task_text_edit.insert(0, name_task_text["text"])
        adjust_entry_width()
        name_task_text_edit.pack(side=tkinter.LEFT, anchor=tkinter.SW)
        name_task_text_edit.focus()
        root.bind("<Button-1>", click_outside)  # Включаем отслеживание кликов вне Entry

        # функция сохранения введенного имени проекта
    def save_task_name(event=None):
        name_task_text.config(text=name_task_text_edit.get())
        name_task_text_edit.pack_forget()
        name_task_text.pack(side=tkinter.LEFT, anchor=tkinter.SW)
        root.unbind("<Button-1>")  # Отключаем отслеживание кликов
        # сохраняем в БД
        db_utils.update_value(task_class.project_id, "task_name", task_class.task_id, name_task_text_edit.get())
        # сохраняем в свойство объекта
        task_class.name = name_task_text_edit.get()

        # функция ввода имени проекта при клике вне виджета редактирования имени
    def click_outside(event):
        if event.widget != name_task_text_edit:
            save_task_name()

        # функция расширения ширины виджета при вводе имени проекта
    def adjust_entry_width(*args):
        font = tkinter.font.Font(font=name_task_text_edit["font"])
        text_width = font.measure(name_task_text_edit.get())
        name_task_text_edit.config(width=max(text_width // font.measure("0") + 1, 1))  # +1 для корректировки


    # фрейм управления задачей
    task_frame = tkinter.Frame(main_project_frame, bg="#ececec", width=800, height=60)
    task_frame.pack_propagate(False)
    task_frame.pack(expand=True, fill='x', side='top', anchor="nw", padx=15, pady=0)
    # РАЗДЕЛ ГРАФИЧЕСКИХ ЭЛЕМЕНТОВ ПЛАШКИ УПРАВЛЕНИЯ ЗАДАЧЕЙ
    task_frame.grid_columnconfigure(3, minsize=5)  # Столбец 3 будет растягиваться по ширине
    task_frame.grid_columnconfigure(4, weight=10, minsize=80)  # Столбец будет растягиваться по ширине
    task_frame.grid_columnconfigure(5, minsize=250, weight=0)  # 5 столбец фиксированной ширины
    # имитация пространства сверху панели задач
    tasks_space = tkinter.Frame(task_frame, bg="#cfcfcf", width=40, height=7)
    tasks_space.grid(row=0, column=1, columnspan=7, sticky="we")
    # стрелка древовидной структуры
    arrow_task = tkinter.Canvas(task_frame, bg="#cfcfcf", width=40, height=77, highlightthickness=0)
    arrow_task.grid(row=0, column=0, rowspan=3)
    if last_task:
        arrow_task.image_id = arrow_task.create_image(30, 38, anchor="center", image=tk_arrow_last_skin)  # Размещаем изображение
    else:
        arrow_task.image_id = arrow_task.create_image(30, 38, anchor="center", image=tk_arrow_skin)  # Размещаем изображение
    # фигура закругления слева
    task_frame_left = tkinter.Canvas(task_frame, bg="#cfcfcf", width=20, height=70, highlightthickness=0)
    task_frame_left.grid(row=1, column=1, rowspan=2)
    task_frame_left.create_image(10, 35, anchor="center", image=tk_task_frame_left_skin)  # Размещаем изображение
    # ферейм для размещения Имя задачи и кнопки удаления
    task_name_frame = tkinter.Frame(task_frame, bg="#ececec", width=30, height=30)
    task_name_frame.grid(row=1, column=2, columnspan=3, sticky="w")
    # текст с названием Задачи
    name_task_text = tkinter.Label(task_name_frame, text=task_name, bg="#ececec", fg="black", font=task_name_font)
    name_task_text.bind("<Button-1>", edit_task_name)
    name_task_text.pack(side=tkinter.LEFT, anchor=tkinter.SW)
    # виджет для редактирования текста
    name_task_text_edit = tkinter.Entry(task_name_frame, bg="#ececec", fg="black", font=task_name_font, relief=tkinter.FLAT, insertbackground="black", selectbackground="#556c95")
    name_task_text_edit.bind("<KeyRelease>", adjust_entry_width)  # Перехватываем событие при вводе текста)
    name_task_text_edit.bind("<Return>", save_task_name)
    # кнопка удаления Задачи
    delete_task_button = tkinter.Canvas(task_name_frame, bg="#ececec", width=30, height=30, highlightthickness=0)
    delete_task_button.pack(side=tkinter.RIGHT, padx=5)
    delete_task_button.create_image(15, 15, anchor="center", image=tk_del_task_skin)  # Размещаем изображение
    # ферейм для размещения кнопки оплаты, кнопок старта и завершения
    task_startend_frame = tkinter.Frame(task_frame, bg="#ececec", width=30, height=30)
    task_startend_frame.grid(row=2, column=2, sticky="w")
    # кнопка статус оплаты проекта
    task_payment_button = tkinter.Canvas(task_startend_frame, bg="#ececec", width=33, height=35, highlightthickness=0)
    task_payment_button.pack_propagate(True)
    task_payment_button.pack(side=tkinter.LEFT, padx=0, pady=0)
    # Размещаем изображение в Canvas в зависимости от статуса оплаты
    if task_class.task_pay == 'wait':
        task_payment_button.image_id = task_payment_button.create_image(15, 14, anchor="center", image=tk_task_pay_wait_skin)
    if task_class.task_pay == 'ok':
        task_payment_button.image_id = task_payment_button.create_image(15, 14, anchor="center", image=tk_task_pay_ok_skin)
    if task_class.task_pay == 'free':
        task_payment_button.image_id = task_payment_button.create_image(15, 14, anchor="center", image=tk_task_pay_free_skin)
    # кнопка старт/пауза Задачи
    start_task_button = tkinter.Canvas(task_startend_frame, bg="#ececec", width=28, height=35, highlightthickness=0)
    if end_date is None:
        start_task_button.pack(side=tkinter.LEFT)
        if timer_status:
            start_task_button.image_id = start_task_button.create_image(14, 14, anchor="center", image=tk_start_task_pause_skin)  # Размещаем изображение
        else:
            start_task_button.image_id = start_task_button.create_image(14, 14, anchor="center", image=tk_start_task_skin)  # Размещаем изображение
    else:
        start_task_button.pack_forget()
    # кнопка завершения Задачи
    end_task_button = tkinter.Canvas(task_startend_frame, bg="#ececec", width=100, height=35, highlightthickness=0)
    end_task_button.pack(side=tkinter.RIGHT, padx=7)
    if end_date is None:
        if timer_status:
            end_task_button.image_id = end_task_button.create_image(50, 14, anchor="center", image=tk_end_task_active_skin)  # Размещаем изображение в Canvas
        else:
            end_task_button.image_id = end_task_button.create_image(50, 14, anchor="center", image=tk_end_task_skin)  # Размещаем изображение в Canvas
        end_task_button.text_id = end_task_button.create_text(50, 14, text="Завершить", font=("Helvetica", 12), fill="white")  # Пишем подпись кнопки
    else:
        end_task_button.image_id = end_task_button.create_image(50, 14, anchor="center", image=tk_end_task_ok_skin)  # Размещаем изображение в Canvas
        end_task_button.text_id = end_task_button.create_text(50, 14, text="Завершено", font=("Helvetica", 12), fill="black")  # Пишем подпись кнопки
        end_task_button.pack(padx=0)
    # текст с датой начала Задачи
    if end_date is None:
        label_text = swt_utils.date_format(start_date)
    else:
        label_text = '      '+swt_utils.date_format(start_date)+' - '+swt_utils.date_format(end_date)
    begin_date_task_text = tkinter.Label(task_frame, text=label_text, bg="#ececec", fg="#333333", font=task_data_font)
    begin_date_task_text.grid(row=2, column=4, sticky="n") # rowspan=2
    # текст общее время затраченное на Задачу
    timer_task_text = tkinter.Label(task_frame, text="0", bg="#ececec", fg="#333333", font=task_time_font)
    timer_task_text.grid(row=1, column=5, rowspan=2, sticky="e", padx=10)
    # иконка статуса Задачи
    status_task_icon = tkinter.Canvas(task_frame, bg="#ececec", width=24, height=24, highlightthickness=0)
    status_task_icon.grid(row=1, column=6, rowspan=2, padx=0)
    if end_date is None:
        if timer_status:
            status_task_icon.image_id = status_task_icon.create_image(12, 12, anchor="center", image=tk_task_status_on_skin)  # Размещаем изображение
        else:
            status_task_icon.image_id = status_task_icon.create_image(12, 12, anchor="center", image=tk_task_status_pause_skin)
    else:
        status_task_icon.image_id = status_task_icon.create_image(12, 12, anchor="center", image=tk_task_status_off_skin)
    # фигура закругления справа
    task_frame_right = tkinter.Canvas(task_frame, bg="#cfcfcf", width=20, height=70, highlightthickness=0)
    task_frame_right.grid(row=1, column=7, rowspan=2)
    task_frame_right.create_image(10, 35, anchor="center", image=tk_task_frame_right_skin)  # Размещаем изображение
    return (task_frame,
            delete_task_button,
            start_task_button,
            timer_task_text,
            end_task_button,
            begin_date_task_text,
            status_task_icon,
            arrow_task,
            task_payment_button)

# Диалоговое окно создания нового Проекта
# Убрано из проекта
# def add_project_gui():
#     return tkinter.simpledialog.askstring("Новый Проект", "Введите имя проекта:")

# Диалоговое окно создания новой Задачи
# Убрано из проекта
# def add_task_gui():
#     return tkinter.simpledialog.askstring("Новая Задача", "Введите имя задачи:")

