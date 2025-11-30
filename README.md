<h1 align="center">Modelagem e simulação de Sistemas - Sistema de Filas (Modelo M/M/1 Simples)</h1>

## <p align="center">👨🏽‍🎓Nome completo: Johnny Matheus Nogueira de Medeiro, Nathaniel Nicolas Rissi Soares, Nelson Ramos Rodrigues Junior</p>

<p align="justify">
Objetivo: Desenvolver um algoritmo para modelar o funcionamento de um sistema de filas, que será capaz de calcular e apresentar os seguintes itens:
</p>

- a) Intervalo médio entre chegadas.
- b) Duração média do atendimento.
- c) Tabela de funcionamento do sistema.
- d) Tamanho médio da fila.
- e) Tempo médio de espera na fila.


# Modelo M/M/1

| Letra | Significado                                                                       |
| ----- | --------------------------------------------------------------------------------- |
| **M** | Chegadas com distribuição **Markoviana** (ou seja, Poisson / tempos exponenciais) |
| **M** | Serviços com distribuição **Markoviana** (exponencial)                            |
| **1** | **Um único servidor**                      

# Estrutura do Projeto
```
projeto_fila/
│
├── app.py                 
├── simulador.py           
└── requirements.txt
```  

# Estrutura do Código  
<h3> app.py</h3>

<p>Aqui fica a interface Streamlit:</p>

- Inputs (quantidade de clientes, intervalos etc.)
- Botão para rodar simulação
- Exibição da tabela
- Exibição dos cálculos

# Código app.py
```
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
```

<h3>simulador.py</h3>
<p>Aqui ficam as funções matemáticas:</p>

- Função para gerar tempos de chegada
- Função para gerar tempos de atendimento
- Função que monta a tabela de funcionamento
- Função que calcula médias

```
import pandas as pd

def simular_fila(qtd_clientes, intervalo, duracao):
    chegadas = []
    atendimentos = []
    
    # Gerar tempos de chegada (somatório progressivo)
    tempo = 0
    for _ in range(qtd_clientes):
        tempo += intervalo
        chegadas.append(tempo)
    
    # Gerar duração dos atendimentos
    tempos_atendimento = [duracao] * qtd_clientes
    
    inicio = []
    fim = []
    espera = []
    tamanho_fila = []
    
    fim_anterior = 0
    
    for i in range(qtd_clientes):
        chegada = chegadas[i]
        atendimento = tempos_atendimento[i]
        
        # Início do atendimento
        inicio_atendimento = max(chegada, fim_anterior)
        
        # Tempo de espera
        espera_cliente = inicio_atendimento - chegada
        
        # Fim
        fim_atendimento = inicio_atendimento + atendimento
        
        # Tamanho da fila = quantos chegaram antes mas não foram atendidos ainda
        fila = sum(1 for j in range(i) if fim[j] > chegada)
        
        inicio.append(inicio_atendimento)
        fim.append(fim_atendimento)
        espera.append(espera_cliente)
        tamanho_fila.append(fila)
        
        fim_anterior = fim_atendimento
    
    df = pd.DataFrame({
        "Cliente": range(1, qtd_clientes + 1),
        "Chegada": chegadas,
        "Início Atendimento": inicio,
        "Fim Atendimento": fim,
        "Espera": espera,
        "Tamanho da Fila": tamanho_fila
    })
    
    return df


def calcular_medias(df):
    return {
        "intervalo_medio": df["Chegada"].diff().mean(),
        "atendimento_medio": (df["Fim Atendimento"] - df["Início Atendimento"]).mean(),
        "tempo_medio_espera": df["Espera"].mean(),
        "tamanho_medio_fila": df["Tamanho da Fila"].mean(),
    }

```

# Funcionamento do projeto

<div align="center">
<img src = "https://github.com/JohnnyMatheus/Trabalho-Final-Sistema-de-Filas-Modelagem-e-Simulacao-de-Sistemas/blob/main/demonstra%C3%A7%C3%A3o.gif">
</div>

## 🧠 Desenvolvedores

| [<img src="https://avatars.githubusercontent.com/u/128015032?v=4" width=115><br>👑Game Master👑<br><sub>🐦‍🔥Johnny Matheus Nogueira de Medeiro🐦‍🔥</sub>](https://github.com/JohnnyMatheus) | [<img src="https://avatars.githubusercontent.com/u/166051346?v=4" width=115><br><sub>Nelson Ramos Rodrigues Junior</sub>](#) | [<img src="https://avatars.githubusercontent.com/u/165223471?v=4" width=115><br><sub>Nathaniel Nicolas Rissi Soares</sub>](#) |
| :---: | :---: | :---: |


## 🔷 Professora
| [<img src="https://media.licdn.com/dms/image/v2/D4D03AQGmaG0p9vOt8Q/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1728394332600?e=2147483647&v=beta&t=q33tl94DTaTiWqe_RSpPjQx1QzQdCjVgOpBVdPgbsIo" width=115><br><sub>Tatiele Bolson Moro</sub>](https://br.linkedin.com/in/tatiele-bolson-moro-a1340b25) |
| :---: |
