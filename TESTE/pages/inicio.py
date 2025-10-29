import streamlit as TelaIn
import pandas as pd

TelaIn.title ("C O F A T")
TelaIn.title ("T R A N S I T H U B ")

col1, col2 = TelaIn.columns([4,2])

with col1:
    part = TelaIn.text_input("Where is this partnumber?")

with col2:
    invoice = TelaIn.text_input("Where is this invoice?")


    

def procurar_partnumber(partnumber):
    caminho = r"\\192.168.10.252\logistica\06 - Gestão de Transportes (Material Flow & Foreign Trade)\06 - 01 - Comex Inbound (Foreign Trade Inbound)\06 - 01 - 01 - Planilha de Trânsito (Transit File)\01. FOLLOW UP/Planilha de trânsito cópia.xlsx"
    LCITABLE = pd.read_excel(caminho,"LCI")
    TRANSITTABLE = pd.read_excel(caminho,"Transit")
    dflci = pd.DataFrame(LCITABLE)
    dftran = pd.DataFrame(TRANSITTABLE)
    loclci = dflci[dflci["COFAT PN"].astype(str)==partnumber]
    loctran = dftran[(dftran["PN"].astype(str)==partnumber) & (dftran["Status"]!="Received")]
    return loclci, loctran

def procurar_invoice(invoicenumber):
    caminho = r"\\192.168.10.252\logistica\06 - Gestão de Transportes (Material Flow & Foreign Trade)\06 - 01 - Comex Inbound (Foreign Trade Inbound)\06 - 01 - 01 - Planilha de Trânsito (Transit File)\01. FOLLOW UP/Planilha de trânsito cópia.xlsx"
    invoicelci = pd.read_excel(caminho,"LCI")
    invoicetran = pd.read_excel(caminho,"Transit")
    dflci = pd.DataFrame(invoicelci)
    dftran = pd.DataFrame(invoicetran)
    loclci = dflci[dflci["INVOICE"].astype(str) ==invoicenumber]
    loctran = dftran[(dftran["Invoice"].astype(str)==invoicenumber) & (dftran["Status"]!="Received")]
    return loclci, loctran

if invoice:
    lcires, tranres = procurar_invoice(invoice)
    TelaIn.subheader("Results at LCI:")
    TelaIn.dataframe(lcires)
    TelaIn.subheader("Results In Transit:")
    TelaIn.dataframe(tranres)


if part:
    lcires, tranres = procurar_partnumber(part)
    TelaIn.subheader("Results at LCI:")
    TelaIn.dataframe(lcires)
    TelaIn.subheader("Results In Transit:")
    TelaIn.dataframe(tranres)
