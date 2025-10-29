import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")


colunas_iniciais = ['Material', 'Quantidade', 'Data', 'Centro']
df_vazio = pd.DataFrame(columns=colunas_iniciais).astype('object')

edited_df = st.data_editor(
    df_vazio, 
    num_rows="dynamic",
    use_container_width=True,
    height=300
)
st.subheader("Dados Colados:")
if not edited_df.empty:
    st.write("Aqui está o DataFrame resultante da sua colagem:")
    st.dataframe(edited_df)
else:
    st.info("A grade acima está vazia. Cole seus dados para vê-los aqui.")
