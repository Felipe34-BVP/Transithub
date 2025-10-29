import streamlit as aplicativo
import pandas as pd

aplicativo.sidebar.image("LOGO.PNG")

pg = aplicativo.navigation([
    aplicativo.Page("pages/inicio.py",title= "Página inicial"),
    aplicativo.Page("pages/Transit.py",title= "In Transit"),
    aplicativo.Page("pages/LCI.py",title= "At LCI"),
    aplicativo.Page("pages/_LTPA.py",title= "Lançar Trânsito"),
    aplicativo.Page("pages/TESTANDO.py",title= "LANÇAR TUDO")
    ])


pg.run()


    

    



