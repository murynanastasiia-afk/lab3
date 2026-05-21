import streamlit as st

def main():
    st.set_page_config(page_title="Task Manager", page_icon="📝", layout="centered")

    todos_page = st.Page("pages/todos.py", title="Список завдань", icon="✅")
    add_page = st.Page("pages/add.py", title="Додати нове завдання", icon="➕")
    archive_page = st.Page("pages/archive.py", title="Архів", icon="📦")

    pg = st.navigation([todos_page, add_page, archive_page])
    pg.run()

if __name__ == "__main__":
    main()