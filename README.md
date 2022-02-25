## Planejamento

1. Uso de alguma técnica de aprendizado de máquina para resolver certo problema
2. Vídeo (máximo de 15 min) demonstrando o uso do sistema proposto
3. Relatório explicativo sobre o que foi realizado. 

Esse trabalho também deverá ser enviado ao Vinicius (email: viniciuscmgo@gmail.com)

**Uso da técnica de Regressão Logística para classificação de fetos em três possíveis classes:** normal, com condições suspeitas e com condições patológicas.

### Sobre os dados

*Dados:* Data set [Fetal Health Classification](https://www.kaggle.com/andrewmvd/fetal-health-classification), disponível no site Kaggle.

O conjnto de dados conta com 22 colunas e 2126 linhas da tabela no total, sendo que todos eles foram extraídos de exames cardiológicos e classificados por médicos obstétras experientes. As classificações são de três níveis diferentes, indicando para o feto:
1. Condições normais
2. Condições suspeitas
3. Condições patológicas (doença)


Coluna | Conteúdo
-------|-------
baseline value | Baseline Fetal Heart Rate (FHR)
accelerations | Number of accelerations per second 
fetal_movement | Number of fetal movements per second
uterine_contractions | Number of uterine contractions per second
light_decelerations | Number of LDs per second
severe_decelerations | Number of SDs per second
prolongued_decelerations | Number of PDs per second
abnormal_short_term_variability | Percentage of time with abnormal short term variability
mean_value_of_short_term_variability | Mean value of short term variability
percentage_of_time_with_abnormal_long_term_variability | Percentage of time with abnormal long term variability
mean_value_of_long_term_variability | Mean value of long term variability
histogram_width | Width of the histogram made using all values from a record
histogram_min | Histogram minimum value
histogram_max | Histogram maximum value
histogram_number_of_peaks | Number of peaks in the exam histogram
histogram_number_of_zeroes | Number of zeroes in the exam histogram
histogram_mode | Hist mode
histogram_mean | Hist mean
histogram_median | Hist Median
histogram_variance | Hist variance
histogram_tendency | Histogram trend
fetal_health (target) | Fetal health: 1 - Normal 2 - Suspect 3 - Pathological

Como forma de reduzir o alto número de colunas, foram selecionadas as colunas com mais influência na variável target da classificação (fetal_health). Essa seleção será abordada no arquivo Data_mining e as colunas selecionadas também serão explicitadas no arquivo.

### Estrutura do trabalho
O projeto foi dividido em 04 partes:
1. Data mining
    1. Pré processamento dos dados
        - Limpeza e correções
        - Balanceamento

    2. Processamento
        - Identificando a correlação das características (features)
        - Filtrando o conjunto de dados
        
        
2. Modeling        
    - Separação e normalização dos dados
    - Treinamento do modelo
    - Avaliação do desempenho do modelo criado com relação a dados desconhecidos (Evaluation)
        - Precision e Recall
        - F1 Score
        - Confusion Matrix
    - Salvando o modelo para uso na aplicação
    
    
3. Aplicação
