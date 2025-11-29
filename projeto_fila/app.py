import streamlit as st
from simulador import simular_fila, calcular_medias

st.title("Simulador de Sistema de Filas — Python + Streamlit")

st.write("Preencha os dados abaixo:")

qtd = st.number_input("Quantidade de clientes", min_value=1, value=10)
intervalo = st.number_input("Intervalo entre chegadas (minutos)", min_value=1, value=3)
duracao = st.number_input("Duração do atendimento (minutos)", min_value=1, value=5)

if st.button("Simular Sistema"):
    df = simular_fila(qtd, intervalo, duracao)
    medias = calcular_medias(df)
    
    st.subheader("Tabela de Funcionamento do Sistema")
    st.dataframe(df)
    
    st.subheader("Resultados Médios")
    st.write(f"**Intervalo médio entre chegadas:** {medias['intervalo_medio']:.2f} min")
    st.write(f"**Duração média do atendimento:** {medias['atendimento_medio']:.2f} min")
    st.write(f"**Tempo médio de espera na fila:** {medias['tempo_medio_espera']:.2f} min")
    st.write(f"**Tamanho médio da fila:** {medias['tamanho_medio_fila']:.2f} clientes")
