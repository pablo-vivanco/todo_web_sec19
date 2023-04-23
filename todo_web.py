import streamlit as st
import functions as fn

# The way that streamlit web pages work:
#   On initial run, the entire python file is ran (functions are loaded, not called unless they are called in the code)
#   if the widgets have callbacks, when the event happens, the function is called and then the entire python file is ran again.

TODO_FILEPATH='todos.txt'
todos = fn.load_todos(TODO_FILEPATH)

def add_todo():
    todo = st.session_state['new_todo']

    todos.append(todo)
    fn.save_todos(todos=todos, filepath=TODO_FILEPATH)
    st.session_state['new_todo'] = ''

def remove_todo():
    inds = [ind for ind, val in st.session_state.items() if val == True]
    for ind in inds:
        ind = int(ind)
        todos.pop(ind)
        fn.save_todos(todos=todos, filepath=TODO_FILEPATH)

st.title('My Todo App')
st.subheader('This is my todo app')
st.write('This app is to increase your productivity.')

for ind in range(len(todos)):
    st.checkbox(todos[ind], key=str(ind), on_change=remove_todo)

st.text_input(label='Enter a Todo:', placeholder='Add a new todod ...', key='new_todo', on_change=add_todo)
