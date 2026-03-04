import matplotlib.pyplot as plt


def draw_dynamic_ishikawa(problem, data):
    # Настройки масштабирования
    x_step = 3.0  # Расстояние между категориями на хребте
    y_unit = 0.8  # Высота одной строки причины
    angle_offset = 1.5  # Наклон ребра

    categories = list(data.keys())
    num_cats = len(categories)

    # 1. Рассчитываем длину хребта
    spine_length = (num_cats // 2) * x_step + 0.5

    fig, ax = plt.subplots(figsize=(spine_length + 4, 8))

    # РИСУЕМ ХРЕБЕТ КАК СТРЕЛКУ (используем annotate вместо plot)
    ax.annotate('', xy=(spine_length, 0), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', lw=2, color='black', shrinkA=0, shrinkB=0))

    # Голова рыбы
    ax.text(spine_length+0.1, 0, f"  {problem}", fontsize=14, fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.5", fc="white", ec="black"),
            va='center', ha='left')

    max_y_reach = 0

    x_attach = 0
    for i, category in enumerate(categories):
        side = 1 if i % 2 == 0 else -1

        causes = data[category]
        y_sentences = [(len(cause.split('\n')) * 0.5 - 0.5 + 1) * y_unit
                     for cause in causes]
        x_sentences = max([(max([len(sentence) for sentence in cause.split('\n')]) * 0.0625) * x_step
                     for cause in causes])

        # Позиция крепления к хребту
        x_attach += x_sentences * ((i+1) % 2 )
        x_attach_ = x_attach

        # 2. Динамическая длина ребра
        # Длина зависит от количества причин + небольшой запас
        y_start = (sum(y_sentences)+ 1 * y_unit) * side
        x_start = x_attach_ - angle_offset

        # Обновляем границы для отрисовки
        max_y_reach = max(max_y_reach, abs(y_start))

        # Рисуем ребро (кость)
        ax.annotate('', xy=(x_attach_, 0), xytext=(x_start, y_start),
                    arrowprops=dict(arrowstyle='->', lw=2, color='navy', shrinkA=0, shrinkB=0))

        # Название категории
        ax.text(x_start, y_start + (0.3 * side), category, fontsize=12,
                fontweight='bold', ha='center', va='bottom' if side > 0 else 'top')

        # 3. Рисуем причины
        y_cause = (-y_unit - y_unit * side) / 4 + (y_unit * side)
        for j, cause in enumerate(causes):
            sentences = cause.split('\n')
            len_lines = len(cause.split('\n'))

            # Математический расчет точки касания на динамическом ребре
            # Линия от (x_start, y_start) до (x_attach, 0)
            t = y_cause / y_start
            x_contact = x_start + (x_attach_ - x_start) * (1 - t)

            x_text_start = x_contact - 1.0

            # Текст причины
            ax.text(x_text_start + 0.6 - len_lines * 0.05, y_cause+0.2, cause, fontsize=10, ha='right', va='bottom')


            max_x_len_size = max(map(len, sentences))
            x_len_text = max_x_len_size * 0.08
            x_len = x_text_start-x_len_text
            # Стрелка причины
            ax.annotate('', xy=(x_contact , y_cause), xytext=(x_len - len_lines * 0.05, y_cause),
                        arrowprops=dict(arrowstyle='->', lw=1, color='gray', shrinkA=0, shrinkB=0))

            y_cause += (len_lines * 0.5 - 0.5 + 1) * 1 * y_unit * side

    # Настройка лимитов осей для центрирования «рыбы»
    ax.set_xlim(-1, spine_length + 5)
    ax.set_ylim(-max_y_reach - 2, max_y_reach + 2)
    ax.axis('off')

    plt.title(f"Динамическая диаграмма Исикавы", fontsize=16, pad=20)
    plt.tight_layout()
    plt.show()


# --- ПРИМЕР С РАЗНЫМ КОЛИЧЕСТВОМ ПРИЧИН ---
problem_name = "ОБРЫВ НИТИ"
data_set = {
    "Машины": ["Износ подшипника\nИзнос подшипника\nИзнос подшипника\nИзнос подшипника\nИзнос подшипника\nИзнос подшипника",
               "Вибрация", "Старая игла\nСтарая игла", "Перегрев"],  # 4 причины (длинное ребро)
    "Люди": ["Усталость"],  # 1 причина (короткое ребро)
    "Методы": ["Скорость выше нормы", "Нет смазки"],  # 2 причины
    "Материалы": ["Тонкая нить", "Брак сырья", "Влажность"],  # 3 причины
    "Среда": ["Пыль"],
    "Измерения": ["Ошибка датчика", "Калибровка"]
}

if __name__ == "__main__":
    draw_dynamic_ishikawa(problem_name, data_set)