class Task:
    def __init__(self, description):
        self.description = description
        self.status = 'Не начата'  # Изначальный статус

    def update_status(self, status):
        if status in ['Не начата', 'В процессе', 'Завершена']:
            self.status = status
        else:
            raise ValueError("Недопустимый статус. Выберите один из: 'Не начата', 'В процессе', 'Завершена'.")


class ToDoList:
    def __init__(self):
        self.tasks = {}  # Словарь для хранения задач по id

    def add_task(self, description):
        task_id = len(self.tasks) + 1  # Генерация уникального id для задачи
        self.tasks[task_id] = Task(description)
        print(f"Задача c ID {task_id} добавлена: {description} (Статус: {self.tasks[task_id].status})")

    def remove_task(self, task_id):
        if task_id in self.tasks:
            removed_task = self.tasks.pop(task_id)
            print(f"Задача c ID {task_id} удалена: {removed_task.description}")
        else:
            print(f"Задача с ID {task_id} не найдена.")

    def update_status(self, task_id, status):
        if task_id in self.tasks:
            self.tasks[task_id].update_status(status)
            print(f"Статус задачи c ID {task_id} обновлён на: {self.tasks[task_id].status}")
        else:
            print(f"Задача с ID {task_id} не найдена.")

    def view_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
        else:
            print("Список задач:")
            for task_id, task in self.tasks.items():
                print(f"{task_id} {task.description} (Статус: {task.status})")


def main():
    todo_list = ToDoList()

    # Добавление задач
    todo_list.add_task("Завершить дз по python")
    todo_list.add_task("Купить продукты")
    todo_list.add_task("Купить абонемент в спортзал")

    # Отображение всех задач
    todo_list.view_tasks()

    # Изменение статуса одной из задач
    todo_list.update_status(1, "В процессе")

    # Удаление задачи
    todo_list.remove_task(2)

    # Отображение обновленного списка задач
    todo_list.view_tasks()


if __name__ == "__main__":
    main()