import streamlit as st
import functions

todos = functions.get_todos()
def addtodo():
    tdo=st.session_state['newtodo']+'\n'
    todos.append(tdo)
    functions.write_todos(todos)

st.set_page_config(layout="wide")

st.title("Your Todos App")
st.header("Welcome! Get your day more productive!")
st.subheader("Get Started!")

st.text_input(label='',placeholder="Type in a To-Do", on_change=addtodo, key='newtodo')

for index, i in enumerate(todos):
    check = st.checkbox(i,key=i)
    print(check)
    if check:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[i]
        st.experimental_rerun()

# st.session_state

