# Наладка станка 0,2-0,5
# Время выполнения задачи 0.5 и среднекв. отклонение 0.1
# Поломка 20 и среднекв. отклонение 2
# Устранение поломки 0,1-0,5
# 500 деталей

import numpy as np


def get_time_before_next_task():
    return round(np.random.exponential(1.), 2)  # экс. распред


def get_time_before_machine_break():
    return round(np.random.normal(20., 2.), 2)  # норм. распред


def get_setting_machine():
    return round(np.random.uniform(.2, .5), 2)  # равномерное распр


def get_task_execution():
    return round(np.random.normal(.5, .1), 2)


def get_repair_time():
    return round(np.random.uniform(.1, .5), 2)


def work(tasks_cnt, total_work_time=0):
    details = tasks_cnt
    downtime = 0  # время простоя
    eff_work_time = 0.0  # время эффективной работы
    det_in_queue_cnt = 0
    breaks_cnt = 0
    total_repair_time = 0
    time_before_next_task = get_time_before_next_task()
    time_to_break = get_time_before_machine_break()

    while details > 0:
        if time_before_next_task > 0:
            total_work_time += time_before_next_task
            downtime += time_before_next_task
            time_before_next_task = 0

        set_machine = get_setting_machine()
        task_execution = get_task_execution()
        time_one_task = set_machine + task_execution

        if time_one_task < time_to_break:  # время отладки + выполнения меньше чем время до поломки
            eff_work_time += time_one_task
            time_before_next_task += get_time_before_next_task()
            total_work_time += time_one_task
            time_to_break -= time_one_task
            time_before_next_task -= time_one_task
            details -= 1
        else:
            breaks_cnt += 1  # если до поломки не успели выполнить задание
            total_work_time += time_to_break  # общее время работы станка + время простоя
            time_before_next_task -= time_to_break
            repair_time = get_repair_time()
            downtime += time_to_break + repair_time
            total_work_time += repair_time
            time_before_next_task -= repair_time
            time_to_break = get_time_before_machine_break()
            total_repair_time += repair_time

    while time_before_next_task < 0:
        time_before_next_task += get_time_before_next_task()
        det_in_queue_cnt += 1

    return breaks_cnt, total_work_time, total_work_time / tasks_cnt, \
        det_in_queue_cnt, total_repair_time, downtime, eff_work_time


tasks_cnt = 500
res = work(tasks_cnt)
print(f'Количество деталей: {tasks_cnt}\n'
      f'Количество поломок станка: {res[0]}\n'
      f'Время работы: {int(res[1])} ч. {int(res[1] % 60)} мин.\n'
      f'Деталей в очереди (после выполнения 500 заданий): {res[3]}\n'
      f'Общее время починки: {int(res[4])} ч. {int(res[4] % 60)} мин.\n'
      f'Время простоя: {int(res[5])} ч. {int(res[5] % 60)} мин\n'
      f'Эффективное рабочее время:{int(res[6])} ч. {int(res[6] % 60)} мин')
