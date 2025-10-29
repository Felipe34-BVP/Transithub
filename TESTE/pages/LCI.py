import streamlit as aplicativo
import pandas as pd

aplicativo.title("IN L C I")

caminho = r"\\192.168.10.252\logistica\06 - Gestão de Transportes (Material Flow & Foreign Trade)\06 - 01 - Comex Inbound (Foreign Trade Inbound)\06 - 01 - 01 - Planilha de Trânsito (Transit File)\01. FOLLOW UP/Planilha de trânsito cópia.xlsx"

transito = pd.read_excel(caminho,"LCI")


dflci = pd.DataFrame(transito)


aplicativo.dataframe(dflci)


col1, col2, col3 = aplicativo.columns([1,2,1])


