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
