import streamlit as aplicativo
import pandas as pd

aplicativo.title("I N  T R A N S I T")
caminho = r"\\192.168.10.252\logistica\06 - Gestão de Transportes (Material Flow & Foreign Trade)\06 - 01 - Comex Inbound (Foreign Trade Inbound)\06 - 01 - 01 - Planilha de Trânsito (Transit File)\01. FOLLOW UP/Planilha de trânsito cópia.xlsx"

transito = pd.read_excel(caminho,"LCI")

transittable = pd.read_excel(caminho,"Transit")


dflci = pd.DataFrame(transito)

dftran = pd.DataFrame(transittable)

trac = dftran[dftran["Status"]!="Received"]

if aplicativo.button("Add more",icon="➕"):
    aplicativo.switch_page("pages/_LTPA.py")

aplicativo.dataframe(trac)




