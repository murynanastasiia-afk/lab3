import core
import functions

def get_all_todos():
    return functions.get_todos()

def get_archived_todos():
    return functions.get_todos_done()

def create_todo(task, count, date):
    return core.add_todo(task, count, date)

def update_todo(number, new_task, new_count, new_date):
    return core.edit_todo(number, new_task, new_count, new_date)

def finish_todo(number):
    return core.complete(number)