import numpy as np 
import statistics as sta
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import scipy.stats as stats

IRIS = pd.read_csv("./data/Iris.csv")

# 1) Qual espécie de íris (Setosa, Versicolor, Virginica) tem a maior média de comprimento de pétala? 
#PetalLengthCm

def get_name_species():
    return pd.unique(IRIS["Species"])

def filter_data_name_specie(name):
    return pd.DataFrame(IRIS.loc[IRIS["Species"]==name])

def mean_petal_length_species():
    name_especies = get_name_species()
    for name in name_especies:  
        print(name) 
        mean_petal_length_species = filter_data_name_specie(name)["PetalLengthCm"].mean()
        print(f"Mean petal length : {mean_petal_length_species:.3f}")

mean_petal_length_species()
print("-"*40)

# 2) Há uma correlação significativa entre o comprimento da sépala e o comprimento da pétala?

sepal = IRIS["SepalLengthCm"]
petal = IRIS["PetalLengthCm"]

# É visto que existe uma relação aparente entre os dois dados com a visualização do 
# grafico de dispersão e é uma correlação forte e positiva
sns.regplot(data=IRIS, x=sepal, y=petal, line_kws={"color":"blue"})
#sns.scatterplot(data=IRIS,x=sepal,y=petal)
plt.xlabel('Comprimento da Sépala')
plt.ylabel('Comprimento da Pétala')
plt.title('Relação entre Comprimento da Sépala e da Pétala')
plt.show()

# Com isso se torna necessario fazer o teste de shapiro para identificar a normalidade dos dados

# Para sepal deu 0.01
sepal_p_value = stats.shapiro(sepal).pvalue
print(f"Teste de Shapiro-Wilk para comprimento sepala: {sepal_p_value}")

# Para petal deu 7.54e-10
petal_p_value = stats.shapiro(petal).pvalue
print(f"Teste de Shapiro-Wilk para comprimento petala: {petal_p_value}")

# Os dois valores são menores que o limit ou sejá é usado o spearman 
LIMIT = 0.05
correlation_coefficient,p_value_correlation = 0, 0 

if (petal_p_value > LIMIT ) and ( sepal_p_value > LIMIT):
    # Ambas segue uma distribuição normal portanto executar o teste de pearson
    correlation_coefficient, p_value_correlation = stats.pearsonr(sepal, petal)
    print(f"Correlação de Pearson: {correlation_coefficient}, p-valor: {p_value_correlation}")

else:
    #Ou Ambas segue não segue uma distribuição normal ou apenas uma portanto 
    # executar o teste de spearman
    correlation_coefficient, p_value_correlation = stats.spearmanr(sepal, petal)
    print(f"Correlação de Spearman para comprimento de petala e comprimento de sepala: {correlation_coefficient}, p-valor: {p_value_correlation}")
    
# o resultado para o coeficiente de correlação foi 0.88 e o p-valor 4.64e-50

# Coeficiente de correlação
# 1: Correlação positiva perfeita.
# -1: Correlação negativa perfeita.
# 0: Nenhuma correlação.

# p-valor
# p-valor for menor que 0,05 : estatisticamente significativa.
# p-valor for maior que 0.05 : não há correlação significativa


# Então se pode concluir que existe uma correlação positiva forte e significativa 
# entre o comprimento da sépala e o comprimento da pétala.
print("-"*40)

# 3) Qual a distribuição das especies no banco de dados?

setosa = IRIS.loc[IRIS['Species'] == 'Iris-setosa']
versicolor = IRIS.loc[IRIS['Species'] == 'Iris-versicolor']
virginica =IRIS.loc[IRIS['Species'] == 'Iris-virginica']


def test_normality(data,specie_name):
    columns = ["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"]
    print(f"Teste de Shapiro-Wilk para {specie_name}:\n")
    for column in columns:
        p_value = stats.shapiro(data[column]).pvalue

        if p_value > LIMIT:
            print(f"{column}: Distribuição Normal (p-value = {p_value:.4f})\n")
        else:
            print(f"{column}: Distribuição Não Normal (p-value = {p_value:.4f})\n")
    
test_normality(setosa,"Iris-Setosa")
print("-"*20)
test_normality(versicolor,"Iris-Versicolor")
print("-"*20)
test_normality(virginica,"Iris-Virginica")

print("-"*40)

# 4) Quais caracteristicas(Comprimento de peta+la,largura de petala,Comprimento de sepala,Largura de separa) 
# tem a maior variabilidade dentro de cada especie?

def test_variability(data, specie_name):
    columns = ["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"]
    print(f"Teste de variabilidade com desvio padrão para {specie_name}:\n")
    for column in columns:
        standard_deviation = data[column].std(ddof=0)
        print(f"{column}: Desvio padrão = {standard_deviation:.4f}\n")
        
test_variability(setosa,"Iris-setosa")
    