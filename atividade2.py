import numpy as np 
import statistics as sta
import matplotlib.pyplot as plt
import seaborn as sns

sync1 = np.array([94, 84.9, 82.6, 69.5, 80.1, 79.6, 81.4, 77.8, 81.7, 78.8, 73.2, 87.9, 87.9, 93.5, 82.3, 79.3, 78.3, 71.6, 88.6, 74.6, 74.1, 80.6]) # 22
async1 = np.array([77.1, 71.7, 91, 72.2, 74.8, 85.1, 67.6, 69.9, 75.3, 71.7, 65.7, 72.6, 71.5, 78.2]) # 14

#Distribuição assimetrica a direita
# Nesse caso a média vai ser maior que a mediana
# O valor da média é arrastado pela cauda, nesse caso, valores a direita, maiores valores, maior média

# Distribuição assimetrica a esquerda
# A média ficará menor que a mediana
# O valor da média é arrastado pela cauda, nesse caso, valores a esquerda, menores valores, menor média

# bins: número pra dividir intervalo
# range: é o range né

plt.hist(sync1, 7, (68,round(max(sync1))))
plt.show()
#plt.hist(sync1, 5, (65,95))
#plt.show()

sns.boxplot([sync1, async1])
plt.xticks([0, 1], ['Sync', 'Async'])
plt.xlabel('work type')
plt.ylabel('houry')
plt.show()