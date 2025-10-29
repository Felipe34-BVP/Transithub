import streamlit as aplicativo











if "logged_in" not in aplicativo.session_state:
    aplicativo.session_state.logged_in = False

if "username" not in aplicativo.session_state:
    aplicativo.session_state.username = ""


if not aplicativo.session_state.logged_in:
    aplicativo.title("Tela de Login")

    with aplicativo.form("login_form"):
        username = aplicativo.text_input("Nome de Usuário")
        password = aplicativo.text_input("Senha", type="password")
        login_button = aplicativo.form_submit_button("Entrar")

if login_button:
        # Simulação de verificação de credenciais
        if username == "admin" and password == "senha123":
            aplicativo.session_state.logged_in = True
            aplicativo.session_state.username = username
            aplicativo.success("Login bem-sucedido!")
        else:
            aplicativo.error("Nome de usuário ou senha incorretos.")


