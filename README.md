# 📊 Estudo e Aplicação de Técnicas para Modelar e Prever Padrões em Séries Temporais em Dados Econômicos de Mercado

Este repositório contém os códigos, análises e modelos desenvolvidos no âmbito do **Projeto de Iniciação Científica** realizado por **Gabriel Andrade do Nascimento** no curso de **Ciência de Dados** (FATEC Baixada Santista – Rubens Lara), com orientação da **Profª. Ms. Márcia Roberta dos Santos Pires da Silva**.

O projeto tem como foco a **análise e previsão de preços de derivados de petróleo no Brasil** a partir da integração de variáveis macroeconômicas e financeiras, utilizando técnicas de **Séries Temporais**, **Aprendizado de Máquina** e **Análise Exploratória de Dados (EDA)**.

---

## 🎯 Objetivos do Projeto

### Objetivo Geral

Investigar as relações econômicas entre:

* Preços dos combustíveis (Gasolina, Etanol, Diesel e GLP);
* Taxas de câmbio (Dólar e Riyal);
* Ações de petrolíferas globais (Petrobras, Aramco, Chevron e Exxon).

E aplicar modelos preditivos para previsão de preços dos derivados de petróleo.

### Objetivos Específicos

* Realizar **análise exploratória detalhada** dos dados históricos;
* Identificar **tendências, sazonalidades e outliers**;
* Avaliar modelos por meio das métricas **MAE, RMSE e MAPE**;
* Integrar variáveis macroeconômicas ao processo preditivo;
* Criar **visualizações informativas e interpretáveis**;
* Documentar todo o processo analítico de ponta a ponta.

---

## 🧠 Metodologia

O projeto foi estruturado seguindo boas práticas de ciência de dados, com inspiração no **CRISP-DM**, contemplando:

1. Levantamento bibliográfico;
2. Coleta e tratamento de dados;
3. Análise Exploratória dos Dados (EDA);
4. Modelagem Preditiva;
5. Avaliação dos Modelos;
6. Discussão dos Resultados.

### Tratamento de Dados

Foram criadas variáveis auxiliares para melhorar a qualidade das análises:

* **intervalo_de_corte_outliers**: utilizada para suavização da série temporal e detecção de valores discrepantes;
* **intervalo_de_agrupamento**: utilizada para reduzir a densidade de pontos nos gráficos e melhorar a interpretação visual.

---

## 📈 Análise Exploratória

Durante a EDA, foram observados:

* Forte correlação entre os preços dos combustíveis;
* Aumento expressivo dos preços a partir de 2020 (pandemia de COVID-19);
* Relações fracas entre câmbio (Dólar e Riyal) e os derivados;
* Correlações mais relevantes entre os preços do Diesel/GLP e ações de petrolíferas internacionais (Aramco, Chevron e Exxon);
* Alta interdependência entre Gasolina e Etanol, e entre Diesel e GLP.

As análises evidenciaram que variáveis globais impactam mais os preços dos derivados do que o câmbio isoladamente.

---

## 🤖 Modelagem Preditiva

Os modelos foram treinados individualmente para cada derivado utilizando **LightGBM (LGBMRegressor)**, um algoritmo baseado em **Gradient Boosting** altamente eficiente para regressão.

### Variáveis Utilizadas por Derivado

* **Gasolina**: Data, Volume EXXON, Fechamento ARAMCO e CHEVRON;
* **Etanol**: Data, Volume EXXON, Fechamento ARAMCO;
* **Diesel**: Data, Volume EXXON, Fechamento ARAMCO, CHEVRON e EXXON;
* **GLP**: Data, Volume EXXON, Fechamento ARAMCO, CHEVRON e EXXON.

### Métricas de Avaliação

| Derivado | MAE  | RMSE | MAPE  |
| -------- | ---- | ---- | ----- |
| Gasolina | 0.03 | 0.04 | 0.49% |
| Etanol   | 0.04 | 0.05 | 0.99% |
| Diesel   | 0.03 | 0.05 | 0.60% |
| GLP      | 0.53 | 0.69 | 0.58% |

Todos os modelos apresentaram **MAPE inferior a 1%**, indicando **altíssima precisão preditiva**.

---

## 🛠 Linguagem, Ferramentas e Bibliotecas

### Linguagem

* **Python**

### Bibliotecas Principais

* **Pandas** – Manipulação de dados
* **NumPy** – Operações numéricas
* **Scikit-learn** – Pré-processamento, métricas e modelagem
* **Statsmodels** – Estatística e séries temporais
* **Matplotlib** – Visualização de dados
* **Seaborn** – Visualização estatística
* **LightGBM** – Modelos de gradient boosting

### Desenvolvimento e Versionamento

* **Visual Studio Code**
* **Git & GitHub** para controle de versão

---

## ✅ Principais Contribuições

* Framework completo de análise de séries temporais aplicado ao setor energético;
* Identificação de relações globais entre mercado acionário e combustíveis no Brasil;
* Modelos preditivos com alta precisão;
* Base replicável para novos estudos em economia e ciência de dados.

---

## 📌 Considerações Finais

O estudo mostrou que a integração de variáveis internacionais (ações de petrolíferas globais) é mais relevante para a previsão dos preços dos combustíveis do que apenas o câmbio. A abordagem com **Machine Learning superou modelos tradicionais**, entregando previsões altamente precisas.

Como continuidade, recomenda-se:

* Inclusão de novas variáveis macroeconômicas (juros, inflação, política fiscal);
* Uso de modelos híbridos;
* Exploração de **Redes Neurais Profundas (LSTM, CNN para séries temporais)**.

---

## 👨‍💻 Autor

**Gabriel Andrade do Nascimento**
Graduando em Ciência de Dados – FATEC Baixada Santista

---

## 📄 Licença

Este projeto é de uso acadêmico e educacional. Sinta-se à vontade para estudar, reutilizar e expandir o trabalho, citando a fonte.
