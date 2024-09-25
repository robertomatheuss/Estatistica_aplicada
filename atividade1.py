"""## N É PAR

    Q1 = N/4 + 1/2
    Q2 = (n/2) + ((n/2)+1) / 2 (MEDIANA)
    Q3 = 3N/4 + 1/2

## N É ÍMPAR

    Q1 = (N+1) / 4
    Q2 = (N+1)/2 (MEDIANA)
    Q3 = 3*(N+1) / 4"""
import numpy as np
import statistics as sta

sync1 = np.array([94, 84.9, 82.6, 69.5, 80.1, 79.6, 81.4, 77.8, 81.7, 78.8, 73.2, 87.9, 87.9, 93.5, 82.3, 79.3, 78.3, 71.6, 88.6, 74.6, 74.1, 80.6]) # 22
async1 = np.array([77.1, 71.7, 91, 72.2, 74.8, 85.1, 67.6, 69.9, 75.3, 71.7, 65.7, 72.6, 71.5, 78.2]) # 14

def media(lista) -> float:
    return lista.mean()

def mediana(lista) -> float:
    return np.median(lista)
    
def moda(lista) -> float:
    return sta.multimode(lista)
    
def quartil(lista, porcentagem) -> float:
    return np.percentile(lista, porcentagem)

def amplitude(lista) -> float:
    return np.ptp(lista)

def amplitude_interquartil(lista) -> float:
    return np.percentile(lista,75) - np.percentile(lista,25)

def variancia_populacao(lista) -> float:
    return lista.var(ddof=0)

def variancia_amostra(lista) -> float:
    return lista.var(ddof=1)

def desvio_padrao_populacao(lista) -> float:
    return lista.std(ddof=0)

def desvio_padrao_amostra(lista) -> float:
    return lista.std(ddof=1)

def apresenta_medidas_tendencia(lista):
    print("Media: {:.2f}".format(media(lista)))
    print("Mediana: {:.2f}".format(mediana(lista)))
    print("Moda: ", moda(lista))   
    print("Primeiro Quartil (Q1): {:.2f}".format(quartil(lista,25)))
    print("Terceiro Quartil (Q3): {:.2f}".format(quartil(lista,75)))
    print("Amplitude: {:.2f}".format(amplitude(lista)))
    print("Amplitude interquartil: {:.2f}".format(amplitude_interquartil(lista)))
    print("Variancia populacional: {:.2f}".format(variancia_populacao(lista)))
    print("Variancia amostral: {:.2f}".format(variancia_amostra(lista)))
    print("Desvio populacional: {:.2f}".format(desvio_padrao_populacao(lista)))
    print("Desvio amostral: {:.2f}".format(desvio_padrao_amostra(lista)))
    
apresenta_medidas_tendencia(sync1)