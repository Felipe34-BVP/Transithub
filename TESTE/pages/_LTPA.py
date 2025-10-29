import streamlit as LT
import pandas as pd
from sqlalchemy import  create_engine
from urllib.parse import quote_plus



LT.set_page_config(layout="wide")

LT.markdown("""
<style>
/* O seletor 'div.stButton > button' foca especificamente nos botões do Streamlit */
div.stButton > button {
            
    width: 100%;
    
    /* Cor do texto do botão */
    color: white;
    
    /* Remove a borda padrão */
    border: none;
    
    /* Cantos arredondados */
    border-radius: 8px;
    
    /* Sombra suave (opcional) */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    
    /* O mais importante: O GRADIENTE */
    /* Você pode gerar o seu próprio em sites como 'cssgradient.io' */
    background-image: linear-gradient(to right, #4e54c8 0%, #8f94fb 51%, #4e54c8 100%);
    
    /* Efeito de transição ao passar o mouse (opcional) */
    transition: 0.5s;
    
    /* Ajusta o tamanho do background para o efeito de 'hover' */
    background-size: 200% auto; 
    
    /* Peso da fonte */
    font-weight: bold;
}

/* Efeito 'Hover' (quando o mouse está em cima) */
div.stButton > button:hover {
    /* Move o gradiente para a direita */
    background-position: right center; 
    
    /* Garante que o texto ainda seja legível */
    color: #fff;
    text-decoration: none;
}
</style>
""", unsafe_allow_html=True)
#--------------------------------------------------------------------------
def add_data_to_database(data_df):
    """
    Função para adicionar um DataFrame ao banco de dados usando pandas.
    """
    usuário = "root"
    senha = "12345"
    host = "127.0.0.1"
    porta = "3305"
    banco_de_dados = "transithub"

    # Criar a string de conexão
    conexao_str = f'mysql+mysqlconnector://{usuário}:{senha}@{host}:{porta}/{banco_de_dados}'
    
    try:
        engine = create_engine(conexao_str)
        
        # O método 'to_sql' faz todo o trabalho:
        # - Conecta
        # - Insere TODOS os dados do DataFrame de uma vez
        # - 'if_exists='append'' diz para adicionar os dados sem apagar o que já existe
        # - 'index=False' evita que o índice do DataFrame seja salvo como uma coluna no SQL
        data_df.to_sql('partnumbers', con=engine, if_exists='append', index=False)
        
        return True  # Retorna True em caso de sucesso

    except Exception as e:
        LT.error(f"Erro ao conectar ou salvar no banco de dados: {e}")
        return False # Retorna False em caso de falha


LT.title("Lançar transito")

col1,col2,col3,col4,col5,col6 = LT.columns([2,2,2,2,2,2])

with col1:
    InvoiceNum = LT.text_input("Invoice")
    Modal = LT.selectbox("Modal",["By Air","by Sea"," by Land"])


with col2:
    SupplierCode = LT.text_input("Supplier Code")
    Agency = LT.text_input("Agency company")

with col3:

    Supplier= LT.text_input("Supplier")
    if Modal == "By Air":
        with col3:
            STA = LT.text_input("STA")

with col5:
    Status = LT.selectbox("Status",["To Ship", "In LCI","In transit","Customs Cleared","Delivered"])


    if Status.upper() == "IN LCI":
        with col6:
            LT.button("Add LCI Info")

    ETA = LT.date_input("ETA")


colunas_iniciais = ['PN', 'Qty', 'PO', 'Weight','UW']

DF_PN = pd.DataFrame(columns=colunas_iniciais).astype('object')

edited_df = LT.data_editor(
    DF_PN, 
    num_rows="dynamic",
    use_container_width=True,
    height=300
)

if LT.button("Lançar Trânsito"):
    TABELAFINAL = pd.DataFrame(edited_df)
    TABELAFINAL['Invoice'] = InvoiceNum
    #LT.dataframe(TABELAFINAL)

    sucesso = add_data_to_database(TABELAFINAL)
    if sucesso:
        LT.success("Dados lançados com sucesso no banco de dados!")
    else:
        LT.error("Falha ao lançar os dados no banco de dados.")






