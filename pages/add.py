import streamlit as st
import controller
import time

def render_add_page():
    st.title("➕ Створення нового завдання")
    st.write("Будь ласка, заповніть форму нижче:")

    date = st.text_input("Дата виконання: ", max_chars=4)
    task = st.text_input("Назва завдання:")
    count = st.number_input("Кількість повторень:", min_value=1, step=1, value=1)

    if st.button("Додати у список"):
        errors = []
        
        if not task.strip():
            errors.append("Назва завдання не може бути порожньою")
            
        if not date.isdigit() or len(date) != 4:
            errors.append("Дата повинна складатися рівно з 4 цифр")
        else:
            current_date_str = time.strftime('%d%m')
            if date < current_date_str:
                errors.append("Введена дата вже застаріла! Вкажіть сьогоднішню або майбутню дату.")

        if errors:
            for error in errors:
                st.error(error)
        else:
            success = controller.create_todo(task.strip(), int(count), date)
            if success:
                st.success(f"Завдання '{task}' успішно додано!")
                time.sleep(1)
                st.rerun()

render_add_page()