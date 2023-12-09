#!/usr/bin/env python
# coding: utf-8

# # Analisando o engajamento do Instagram
# 
# ### O que queremos responder?
# - Qual tipo de conteúdo **mais engaja** no Instagram da minha empresa?
# <br><br>
# - Temos a base de dados do Instagram **desde que o usuário começou a postar na marca até o dia 27/março**
# <br><br>
# - Ele também dá alguns direcionamentos:
#     - Podem ignorar a coluna visualizações, queremos entender apenas curtidas, comentários e interações
#     - Tags vazias é que realmente não possuem tag (favor tratar como vazio)

# ### Como ele pediu para não considerar a coluna visualizações, vamos retirar essa coluna da base

# **O .drop() permite apagar uma coluna ou linha da base:** <br>
# base<font color="blue">**.drop(**</font>nome_coluna,axis=1<font color="blue">**)**</font>
# - O axis = 1 se refere a coluna, enquanto axis = 0 se refere a linha
# - Devemos passar o nome da coluna que queremos apagar da base
# - Em caso de mais de 1 coluna, passamos a lista entre colchetes

# ### Vamos importar e visualizar a nossa base

<<<<<<< HEAD
# In[1]:
=======
# In[37]:
>>>>>>> edfcf3b9572891a7a259fc23f77210ffa50e02aa


# Importando o pandas
import pandas as pd
import datetime
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go


<<<<<<< HEAD
# In[2]:
=======
# In[38]:
>>>>>>> edfcf3b9572891a7a259fc23f77210ffa50e02aa


# Para melhorar a visualização, vamos criar um padrão no formato dos valores
pd.options.display.float_format = '{:,.2f}'.format

# Importar a base em excel
# - Base: 08. Analisando o engajamento no Instagram.xlsx
<<<<<<< HEAD
df = pd.read_excel(r'C:\Users\Virtual Office\08. Analisando o engajamento no Instagram.xlsx')
display(df.head(10))


# In[3]:
=======
df = pd.read_excel(r'C:\Users\Grupo Condor\Desktop\teste\08. Analisando o engajamento no Instagram.xlsx')
display(df.head(10))


# In[39]:
>>>>>>> edfcf3b9572891a7a259fc23f77210ffa50e02aa


#Convertendo os dados para melhor tipo possível
df = df.convert_dtypes()
#Visualizando como as colunas estão dispostas
print(df.columns)
#Pegando as informações referente a data
df['Data'] = pd.to_datetime(df['Data'], format='%Y%m%d')
df['Dia'] = df['Data'].dt.day
df['Mes'] = df['Data'].dt.month
df['Ano'] = df['Data'].dt.year
#Removeendo colunas que já na primeira analise não úteis para o projeto e que poluirão os resultados
df = df.drop(columns = ['Data', 'Visualizações'], axis = 1)
# Remover espaços extras no nome da coluna 'Interações'
df = df.rename(columns={'Interacoes ': 'Interacoes'})

display(df.head(10))


<<<<<<< HEAD
# In[4]:
=======
# In[40]:
>>>>>>> edfcf3b9572891a7a259fc23f77210ffa50e02aa


#Visualizando e entendo com que tipo de dados e farmato estou trabalhando. Consigo compreender o tipo,
#quantas linhas, quantas colunas e quantidade de dados nulos ou vazios.
df.info()
df.shape
display(df.isnull().sum())
df.describe()


# ### Carrossel possui apenas 8 valores não nulos
# - Vamos entender os valores de carrossel

<<<<<<< HEAD
# In[5]:
=======
# In[41]:
>>>>>>> edfcf3b9572891a7a259fc23f77210ffa50e02aa


df.loc[df.Carrossel.isnull(),'Carrossel']


<<<<<<< HEAD
# In[6]:
=======
# In[42]:
>>>>>>> edfcf3b9572891a7a259fc23f77210ffa50e02aa


df.loc[df.Carrossel.notnull(),'Carrossel']


# - Na verdade, os valores nulos são de postagens que não são carrossel. Sendo assim o nulo deveria ser "N"

<<<<<<< HEAD
# In[7]:
=======
# In[43]:
>>>>>>> edfcf3b9572891a7a259fc23f77210ffa50e02aa


# Removendo a coluna devido 44 valores nulos
df.loc[df.Carrossel.isnull(),'Carrossel'] = 'N'


<<<<<<< HEAD
# In[8]:
=======
# In[44]:
>>>>>>> edfcf3b9572891a7a259fc23f77210ffa50e02aa


#Visualizando e entendo com que tipo de dados e farmato estou trabalhando. Consigo compreender o tipo,
#quantas linhas, quantas colunas e quantidade de dados nulos ou vazios.
df.info()
df.shape
display(df.isnull().sum())
df.describe()


<<<<<<< HEAD
# In[9]:
=======
# In[45]:
>>>>>>> edfcf3b9572891a7a259fc23f77210ffa50e02aa


# Visualizando as 5 primeiras linhas
df.head()


<<<<<<< HEAD
# In[10]:
=======
# In[46]:
>>>>>>> edfcf3b9572891a7a259fc23f77210ffa50e02aa


# Visualizando as 5 ultimas linhas
df.tail()


<<<<<<< HEAD
# In[11]:
=======
# In[47]:
>>>>>>> edfcf3b9572891a7a259fc23f77210ffa50e02aa


# Agrupando os dados por tipo 
df_tipo = df.drop(columns = ['Tags', 'Pessoas','Campanhas','Carrossel','Dia','Mes','Ano'], axis = 1)
df_tipo = df_tipo.groupby(by='Tipo').sum()
display(df_tipo)


# ### Visualizando essas informações de maneira gráfica

<<<<<<< HEAD
# In[12]:
=======
# In[48]:
>>>>>>> edfcf3b9572891a7a259fc23f77210ffa50e02aa


# Um gráfico de dispersão ajudaria a entender melhor curtidas e comentários
df.plot(kind="scatter",x="Dia",y="Curtidas",figsize=(14,8));


<<<<<<< HEAD
# In[13]:
=======
# In[49]:
>>>>>>> edfcf3b9572891a7a259fc23f77210ffa50e02aa


# Podemos colocar curtidas e comentários no mesmo gráfico
ax = df.plot(kind="scatter",x="Dia",y="Curtidas",color="blue",label="Curtidas",figsize=(14,8));
df.plot(kind="scatter",x="Dia",y="Comentários",color="red",label="Comentários",figsize=(14,8),ax=ax);


<<<<<<< HEAD
# In[14]:
=======
# In[50]:
>>>>>>> edfcf3b9572891a7a259fc23f77210ffa50e02aa


# A escala de curtidas pode estar atrapalhando a visualização, por isso vamos deixar comentários em um gráfico separado
df.plot(kind="scatter",x="Dia",y="Comentários",color="red",label="Comentários",figsize=(14,8));


# - O gráfico e as informações estatítiscas não estão dizendo muita coisa pois existe uma grande dispersão entre curtidas e comentários
# - Precisamos verificar se existe um padrão usando as outras colunas de informações

# ### A primeira coisa que podemos fazer é pegar os 5 primeiros registros com mais e menos curtidas

<<<<<<< HEAD
# In[15]:
=======
# In[51]:
>>>>>>> edfcf3b9572891a7a259fc23f77210ffa50e02aa


# Ordenando os valores por curtidas
df.sort_values(by="Curtidas",ascending=False).head(30)


<<<<<<< HEAD
# In[16]:
=======
# In[52]:
>>>>>>> edfcf3b9572891a7a259fc23f77210ffa50e02aa


# Selecionando os 5 últimos valores 
# Ordenando os valores
df.sort_values(by="Curtidas",ascending=False).tail(10)


# - Podemos observar que no top 5 todas as postagens tinham pessoas e eram fotos de campanha
# - Nas 5 piores postagens, não haviam pessoas e nem eram postagens de campanhas
# <br><br>
# - **Isso pode ser um indicador que pessoas e campanhas tem relação com as curtidas**

<<<<<<< HEAD
# In[17]:
=======
# In[53]:
>>>>>>> edfcf3b9572891a7a259fc23f77210ffa50e02aa


# Agrupando as informações por tipo e pessoas

df1 = df.groupby(["Tipo",'Pessoas'])["Comentários"].count()
df1_1 = df.groupby(["Tipo",'Pessoas'])["Comentários"].mean()

tipos = ['Foto', 'IGTV', 'Reels', 'Vídeo']
# Colunas para plotagem
colunas = ['Curtidas', 'Comentários', 'Interacoes']

pessoas_sim = df.loc[(df['Tipo'].isin(tipos)) & (df['Pessoas'] == 'S')]
pessoas_nao = df.loc[(df['Tipo'].isin(tipos)) & (df['Pessoas'] == 'N')]

display(df1)
display(df1_1)


# Criando figuras de subplots
fig = go.Figure()

# Plotando barras lado a lado
for coluna in colunas:
    fig.add_trace(go.Bar(
        x=['Pessoas Sim', 'Pessoas Não'],
        y=[pessoas_sim[coluna].mean(), pessoas_nao[coluna].mean()],
        text=[round(pessoas_sim[coluna].mean(), 2), round(pessoas_nao[coluna].mean(), 2)],
        textposition='auto',
        name=coluna,
    ))

# Atualizando layout do gráfico
fig.update_layout(
    barmode='group',
    xaxis_title='Grupos',
    yaxis_title='Valores',
    title='Comparação entre Pessoas Sim e Não para Curtidas, Comentários e Interacoes',
    title_x=0.5,  # Define a posição horizontal do título (0 a 1, sendo 0 à esquerda e 1 à direita)
    plot_bgcolor='#e5ecf6',  # Altere a cor de fundo para a cor desejada
    paper_bgcolor='#e5ecf6'  # Altera a cor de fundo do papel (background fora do gráfico)
)

fig.show()


# Agrupando as informações por tipo e pessoas
df2 = df.groupby(["Tipo",'Pessoas'])["Curtidas"].mean()
df2_1 = df.groupby(["Tipo",'Pessoas'])["Curtidas"].count()

tipos = ['Foto', 'IGTV', 'Reels', 'Vídeo']
# Colunas para plotagem
colunas = ['Curtidas', 'Comentários', 'Interacoes']

campanha_sim = df.loc[(df['Tipo'].isin(tipos)) & (df['Campanhas'] == 'S')]
campanha_nao = df.loc[(df['Tipo'].isin(tipos)) & (df['Campanhas'] == 'N')]

display(df2)
display(df2_1)

# Criando figuras de subplots
fig2 = go.Figure()

# Plotando barras lado a lado
for coluna in colunas:
    fig2.add_trace(go.Bar(
        x=['Capanha Sim', 'Campanha Não'],
        y=[campanha_sim[coluna].mean(), campanha_nao[coluna].mean()],
        text=[round(campanha_sim[coluna].mean(), 2), round(campanha_nao[coluna].mean(), 2)],
        textposition='auto',
        name=coluna
    ))

# Atualizando layout do gráfico
fig2.update_layout(
    barmode='group',
    xaxis_title='Grupos',
    yaxis_title='Valores',
    title='Comparação entre Campanha Sim e Não para Curtidas, Comentários e Interacoes',
    title_x=0.5,  # Define a posição horizontal do título (0 a 1, sendo 0 à esquerda e 1 à direita)
    plot_bgcolor='#e5ecf6' , # Altere a cor de fundo para a cor desejada
    paper_bgcolor='#e5ecf6'  # Altera a cor de fundo do papel (background fora do gráfico)
)

fig2.show()

# Agrupando as informações por tipo e pessoas
df3 = df.groupby(["Tipo",'Pessoas','Campanhas'])["Interacoes"].mean()
df3_1 = df.groupby(["Tipo",'Pessoas','Campanhas'])["Interacoes"].count()

display(df3)
display(df3_1)

pessoas_e_campanha_sim = df.loc[(df['Tipo'].isin(tipos)) & (df['Pessoas'] == 'S') & (df['Campanhas'] == 'S')]
pessoas_e_campanha_nao = df.loc[(df['Tipo'].isin(tipos)) & (df['Pessoas'] == 'N') & (df['Campanhas'] == 'N')]

# Criando figuras de subplots
fig3 = go.Figure()

# Plotando barras lado a lado
for coluna in colunas:
    fig3.add_trace(go.Bar(
        x=['Pessoas e Campanha Sim', 'Pessoas e Campanha Não'],
        y=[pessoas_e_campanha_sim[coluna].mean(),pessoas_e_campanha_nao[coluna].mean()],
        text=[round(pessoas_e_campanha_sim[coluna].mean(), 2), round(pessoas_e_campanha_nao[coluna].mean(), 2)],
        textposition='auto',
        name=coluna
    ))

# Atualizando layout do gráfico
fig3.update_layout(
    barmode='group',
    xaxis_title='Grupos',
    yaxis_title='Valores',
    title='Comparação entre Campanha Sim e Não para Curtidas, Comentários e Interacoes',
    title_x=0.5,  # Define a posição horizontal do título (0 a 1, sendo 0 à esquerda e 1 à direita)
    plot_bgcolor='#e5ecf6',  # Altere a cor de fundo para a cor desejada
    paper_bgcolor='#e5ecf6'  # Altera a cor de fundo do papel (background fora do gráfico)
)

fig3.show()


<<<<<<< HEAD
=======
# In[54]:


get_ipython().system('pip install dash')


>>>>>>> edfcf3b9572891a7a259fc23f77210ffa50e02aa
# # Conclusões

#  * Podemos inferir que conteúdos com pessoas performam melhor que conteúdos sem pessoas.
#  * Podemos inferir que conteúdos de campanha performam melhor que conteúdos não campanha.
#  * Podemos inferir que conteúdos de campanhas com pessoas performam muito melhor do que conteúdos de campanhas sem pessoas.
#      - Então na decisão de investir em uma campanha o melhor formato é a que contém pessoas;

# # Vamos analisar como os conteúdos criados performam por dia  e mês para 2021

<<<<<<< HEAD
# In[18]:
=======
# In[55]:
>>>>>>> edfcf3b9572891a7a259fc23f77210ffa50e02aa


# Criando uma lista com os anos que há no dataframe
print(df['Ano'].unique())
anos = ['2021', '2022']
# Convertendo a coluna 'Ano' para string e filtrando apenas os registros de 2021
df_2021 = df[df['Ano'].astype(str) == '2021']
df_2022 = df[df['Ano'].astype(str) == '2022']

display(df_2021.head(10))
display(df_2022.head(10))


<<<<<<< HEAD
# In[19]:
=======
# In[56]:
>>>>>>> edfcf3b9572891a7a259fc23f77210ffa50e02aa


df_2021_selecionado = df_2021.loc[:, ['Curtidas', 'Comentários', 'Interacoes', 'Pessoas', 'Campanhas', 'Dia','Mes','Ano']]

display(df_2021_selecionado.head(5))

# Reorganizando os dados para usar o 'Dia' como índice e as métricas como colunas
df_melted = df_2021_selecionado.melt(id_vars=['Dia'], value_vars=['Curtidas', 'Comentários', 'Interacoes'], var_name='Métrica', value_name='Valor')

# Criando um gráfico de barras agrupadas para cada métrica ao longo dos dias
fig4 = px.bar(df_melted, x='Dia', y='Valor', color='Métrica', barmode='group', title='Métricas de Curtidas, Comentários e Interacoes por Dia em 2021',
             labels={'Valor': 'Valor da Métrica', 'Dia': 'Dia'})

# Atualizando as configurações para adicionar rótulos fora das barras com tamanho maior
fig4.update_traces(text=fig4.data[0]['y'], textposition='outside', textfont=dict(size=40))  # Ajuste o tamanho da fonte conforme necessário

# Exibindo o gráfico
fig4.update_layout(
    plot_bgcolor='#e5ecf6',  # Altere a cor de fundo para a cor desejada
    paper_bgcolor='#e5ecf6',  # Altera a cor de fundo do papel (background fora do gráfico)
    title_x=0.5,  # Define a posição horizontal do título (0 a 1, sendo 0 à esquerda e 1 à direita)
)


# Exibindo o gráfico
fig4.show()

# Convertendo a coluna 'Mes' para nome do mês em formato de string
meses = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}
df_2021_selecionado['Mes'] = df_2021_selecionado['Mes'].map(meses)

# Reorganizando os dados para usar o 'Mês' como índice e as métricas como colunas
df_melted2 = df_2021_selecionado.melt(id_vars=['Mes'], value_vars=['Curtidas', 'Comentários', 'Interacoes'], var_name='Métrica', value_name='Valor')

# Criando um gráfico de barras agrupadas para cada métrica ao longo dos meses
fig5 = px.bar(df_melted2, x='Mes', y='Valor', color='Métrica', barmode='group', title='Métricas de Curtidas, Comentários e Interacoes por Mês em 2021',
             labels={'Valor': 'Valor da Métrica', 'Mes': 'Mês'})

# Atualizando as configurações para adicionar rótulos dentro das barras
fig5.update_traces(text=fig5.data[0]['y'], textposition='inside')

# Exibindo o gráfico
fig5.update_layout(
    plot_bgcolor='#e5ecf6' , # Altere a cor de fundo para a cor desejada
    paper_bgcolor='#e5ecf6',  # Altera a cor de fundo do papel (background fora do gráfico)
    title_x=0.5,  # Define a posição horizontal do título (0 a 1, sendo 0 à esquerda e 1 à direita)
)


# Exibindo o gráfico
fig5.show()


# # Vamos analisar como os conteúdos criados performam por dia  e mês para 2022

<<<<<<< HEAD
# In[20]:
=======
# In[57]:
>>>>>>> edfcf3b9572891a7a259fc23f77210ffa50e02aa


df_2022_selecionado = df_2022.loc[:, ['Curtidas', 'Comentários', 'Interacoes', 'Pessoas', 'Campanhas', 'Dia','Mes','Ano']]
display(df_2022_selecionado.head(5))

# Criando um gráfico de barras agrupadas para cada métrica ao longo dos dias
fig6 = px.bar(df_2022_selecionado, x='Dia', y=['Curtidas', 'Comentários', 'Interacoes'], barmode='group', 
              title='Métricas de Curtidas, Comentários e Interacoes por Dia em 2022',
              labels={'variable': 'Métrica','value': 'Valor da Métrica', 'Dia': 'Dia'})

# Atualizando as configurações para adicionar rótulos fora das barras com tamanho maior
fig6.update_traces(textposition='outside', textfont=dict(size=14))

# Personalizando o layout do gráfico
fig6.update_layout(
    plot_bgcolor='#e5ecf6',  # Cor de fundo do gráfico
    paper_bgcolor='#e5ecf6',  # Cor de fundo do papel (background fora do gráfico)
    title_x=0.5  # Posição horizontal do título (0 a 1, sendo 0 à esquerda e 1 à direita)
)

# Exibindo o gráfico
fig6.show()

# Convertendo a coluna 'Mes' para nome do mês em formato de string
meses = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}
df_2022_selecionado['Mes'] = df_2022_selecionado['Mes'].map(meses)

# Criando um gráfico de barras agrupadas para cada métrica ao longo dos meses
fig7 = px.bar(df_2022_selecionado, x='Mes', y=['Curtidas', 'Comentários', 'Interacoes'], barmode='group',
              title='Métricas de Curtidas, Comentários e Interacoes por Mês em 2022',
              labels={'variable': 'Métrica','value': 'Valor da Métrica', 'Mes': 'Mês'})

# Atualizando as configurações para adicionar rótulos dentro das barras
fig7.update_traces(text=fig7.data[0]['y'], textposition='inside', textfont=dict(size=14))

# Exibindo o gráfico
fig7.update_layout(
    plot_bgcolor='#e5ecf6' , # Altere a cor de fundo para a cor desejada
    paper_bgcolor='#e5ecf6',  # Altera a cor de fundo do papel (background fora do gráfico)
    title_x=0.5,  # Define a posição horizontal do título (0 a 1, sendo 0 à esquerda e 1 à direita)
)

# Exibindo o gráfico
fig7.show()


<<<<<<< HEAD
=======
# In[58]:


# Criando um gráfico de barras agrupadas para cada métrica ao longo dos dias
fig6 = px.bar(df_2022, x='Dia', y=['Curtidas', 'Comentários', 'Interacoes'], barmode='group', 
              title='Métricas de Curtidas, Comentários e Interacoes por Dia em 2022',
              labels={'value': 'Valor da Métrica', 'Dia': 'Dia'})

# Atualizando as configurações para adicionar rótulos fora das barras com tamanho maior
fig6.update_traces(textposition='outside', textfont=dict(size=14))

# Personalizando o layout do gráfico
fig6.update_layout(
    plot_bgcolor='#e5ecf6',  # Cor de fundo do gráfico
    paper_bgcolor='#e5ecf6',  # Cor de fundo do papel (background fora do gráfico)
    title_x=0.5  # Posição horizontal do título (0 a 1, sendo 0 à esquerda e 1 à direita)
)

# Exibindo o gráfico
fig6.show()


>>>>>>> edfcf3b9572891a7a259fc23f77210ffa50e02aa
# # Conslusões

# * Dias de maior engajamento do publico no ano de 2021:
#     * 10, 11, 19, 24, 26, 28, 29, 30
# * Dias de maior engajamento do publico no ano de 2022: 
#     * 4, 6, 8, 9, 15, 17, 20, 21, 22, 24, 26
# * Não temos dados o suficiente para traçar um padrão de comportamento do público. Mas continuar observando ao longo do tempo
#     as reações que o público tem aos conteúdos criados pode oferecer insights valiosos quanto ao momento ideal para postagem.

# # Vamos analisar os conteúdos com base nas tags 

<<<<<<< HEAD
# In[21]:
=======
# In[59]:
>>>>>>> edfcf3b9572891a7a259fc23f77210ffa50e02aa


df.Tags = df.Tags.str.split('/')
# Selecione os registros onde a coluna 'Tags' é nula e atribua um valor nulo
# Identificar os valores nulos
valores_nulos = df.isnull()
# Substituir os valores nulos por NaN
df[valores_nulos] = float('NaN')
df = df.explode('Tags')
display(df.head(10))


<<<<<<< HEAD
# In[22]:
=======
# In[60]:
>>>>>>> edfcf3b9572891a7a259fc23f77210ffa50e02aa


df_tags = df.groupby('Tags')[['Curtidas','Comentários','Interacoes']].mean()
df_tags.sort_values('Curtidas', ascending =False)


<<<<<<< HEAD
# In[23]:
=======
# In[61]:
>>>>>>> edfcf3b9572891a7a259fc23f77210ffa50e02aa


df_tags_campanhas = df.groupby(['Campanhas','Tags'])[['Curtidas','Comentários','Interacoes']].mean()
df_tags_campanhas.sort_values('Curtidas', ascending =False)
display(df_tags_campanhas)

# Redefinir o índice para tornar 'Campanhas' e 'Tags' colunas do DataFrame
df_tags_campanhas= df_tags_campanhas.reset_index()

# Ordenando os dados para facilitar a visualização
df_tags_campanhas = df_tags_campanhas.sort_values(by=['Curtidas'], ascending=False)

# Plotando gráfico de barras para cada métrica
fig9 = px.bar(df_tags_campanhas, x='Tags', y='Curtidas', color='Campanhas',
              title='Média de Curtidas por Combinação de Campanhas e Tags',
              labels={'Curtidas': 'Média de Curtidas', 'Tags': 'Tags', 'Campanhas': 'Campanhas'})

# Adicionando rótulos
for index, row in df_tags_campanhas.iterrows():
    fig9.add_annotation(
        x=row['Tags'],
        y=row['Curtidas'],
        text=f"{row['Curtidas']:.2f}",  # Formatação do valor com 2 casas decimais
        showarrow=True,
        arrowhead=1,
        yshift=10 if index % 2 == 0 else -30,  # Ajuste para posicionamento dos rótulos
        xshift=0.25 if row['Campanhas'] == 'N' else -0.25  # Ajuste para posicionar corretamente em cada barra
    )

# Exibindo o gráfico com rótulos
fig9.update_layout(
    barmode='group',
    yaxis_title='Média de Curtidas',
    title='Média de Curtidas por Combinação de Campanhas e Tags',
    title_x=0.5,  # Define a posição horizontal do título (0 a 1, sendo 0 à esquerda e 1 à direita)
    plot_bgcolor='#e5ecf6',  # Altere a cor de fundo para a cor desejada
    paper_bgcolor='#e5ecf6'  # Altera a cor de fundo do papel (background fora do gráfico)
)

print('''
Podemos inferir:
    Em geral as Tags performam quando estão em Campanha.
Ação:
    Consolidar mais insights sobre o mehor tipo, no momento apropriado e no formato mais adequado para investir em uma campanha
    para ter o maior engajamento do público.
''')

fig9.show()


<<<<<<< HEAD
# In[24]:
=======
# In[62]:
>>>>>>> edfcf3b9572891a7a259fc23f77210ffa50e02aa


df_tags_tipo = df.groupby(['Tipo','Tags'])[['Curtidas','Comentários','Interacoes']].mean()
df_tags_tipo.sort_values('Curtidas', ascending =False)
display(df_tags_tipo)

# Redefinir o índice para tornar 'Campanhas' e 'Tags' colunas do DataFrame
df_tags_tipo = df_tags_tipo.reset_index()

# Ordenando os dados para facilitar a visualização
df_tags_tipo = df_tags_tipo.sort_values(by=['Curtidas'], ascending=False)

# Plotando gráfico de barras para cada métrica
fig8 = px.bar(df_tags_tipo, x='Tipo', y='Curtidas', color='Tags',
              title='Média de Curtidas por Combinação de Campanhas e Tags',
              labels={'Curtidas': 'Média de Curtidas', 'Tags': 'Tags', 'Tipo': 'Tipo'})

# Adicionando rótulos
for index, row in df_tags_tipo.iterrows():
    fig8.add_annotation(
        x=row['Tipo'],
        y=row['Curtidas'],
        text=f"{row['Curtidas']:.2f}",  # Formatação do valor com 2 casas decimais
        showarrow=True,
        arrowhead=1,
        yshift=10 if index % 2 == 0 else -20,  # Ajuste para posicionamento dos rótulos
        xshift=5 if row['Tipo'] == 'N' else -15 # Ajuste para posicionar corretamente em cada barra
    )

# Exibindo o gráfico com rótulos
fig8.update_layout(
    barmode='group',
    yaxis_title='Média de Curtidas',
    title='Média de Curtidas por Combinação Tags por Tipo de Conteúdo',
    title_x=0.5,  # Define a posição horizontal do título (0 a 1, sendo 0 à esquerda e 1 à direita)
    plot_bgcolor='#e5ecf6',  # Altere a cor de fundo para a cor desejada
    paper_bgcolor='#e5ecf6'  # Altera a cor de fundo do papel (background fora do gráfico)
)

fig8.show()
print('''
Podemos inferir:
    Que as fotos em datas comemorativas, com influciadores e sobre promoções performaram muitos melhor que as demais tags.
    Não teve uma diferença relevante das trends postados no Reels e Videos, mas Reels se mostrou melhor.
    Postar somente os produtos não performaram bem em todos os tipos.
Ações:
    Testar as tags Promoções, Data Comemorativas, Influeciadores e Trends nos demais tipos de conteúdos.
        Observamos que Datas Comemorativas tiveram bons resultados no tipo Foto e Vídeo. Como também Trends obtiveram bons 
        resultados em Video e Reels;  
''')


<<<<<<< HEAD
# In[25]:
=======
# In[63]:
>>>>>>> edfcf3b9572891a7a259fc23f77210ffa50e02aa


import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Criação do aplicativo Dash
app = dash.Dash(__name__)

# Lista de figuras de exemplo (substitua essas variáveis pelas suas figuras)
figuras = [fig, fig2, fig3, fig4, fig5, fig6, fig7, fig9, fig8]

# Textos explicativos para cada gráfico
explicacoes = [
    "Obersamos que conteúdos com pessoas engajam muito mais o público comparado a conteúdos sem pessoas.",
    "Postagem em Campanhas tem maior alcance.",
    "Campanhas com pessoas performan melhro que conteúdos que não estão em campanhas ou que estão em campanhas, mas não contém pessoas.",
    "A distribuição nos dias dos conteúdos criados, mostram um inconstância no trabalho.\nO público ainda não foi alcançado",
    '''Os meses Setembro, Outubro e Dezembro mostram o padrão de engamento do público.\nMas em Novembro fizemos algo de errado, 
    encontrar a causa raiz para não cometermos o mesmo erro em conteúdos futuros.''',
    '''Conseguimos observar melhores resultados, o público se identifica mais com o conteúdo, porém ainda erramos em alguns pontos,
    pois hora o público está bastante engajado, outrora não.''',
    '''Os meses de Janeiro e Março, apresentam o padrão de engajamento do público. Mas em fevereiro algo engajou mais, 
    necessário investigar as ações tomadas para escalar nos demais conteúdos.''',
    '''Observamos insights valiosos no gráfico 8, confirmando o que já vimos no gráfico 2, 
    entretanto com adicional de informações. Conteúdos em campanha engajam mais do que quando não estão em campanhas e quando
    são sobre promoções, em trends, datas comemorativas e com influenciadores tem uma melhor performance.''',
    '''Podemos tirar ótimos insights com esse gráfico! Observamos que tivemos conteúdos que performaram muito bem,
    porém não testamos nos demais tipos. As fotos em datas comemorativas, com influciadores e sobre promoções performaram muitos melhor que as demais tags.
    Não teve uma diferença relevante das trends postados no Reels e Videos, mas Reels se mostrou melhor.
    Postar somente os produtos não performam bem em todos os tipos'''
]

# Índice inicial
current_index = 0

# Estilos personalizados
app_colors = {
<<<<<<< HEAD
    'background': '#334B48',  
=======
    'background': '#334B48',  # Alteração da cor de fundo para um tom de cinza escuro
>>>>>>> edfcf3b9572891a7a259fc23f77210ffa50e02aa
    'text': '#f2f2f2'  # Cor do texto para um tom claro
}

# Layout do painel com os gráficos existentes e controles de navegação
app.layout = html.Div(style={'textAlign': 'center', 'backgroundColor': app_colors['background'], 'fontFamily': 'Arial, sans-serif', 'color': app_colors['text']}, children=[
    html.H1('Dashboard - Engajamento do Público', style={'marginBottom': '20px', 'fontSize': '2.5em'}),  # Título estilizado
    
    html.Div([
        dcc.Graph(id='carousel-graph', config={'displayModeBar': False}),  # Oculta a barra de ferramentas dos gráficos
        html.Div(id='graph-explanation', style={'marginTop': '20px', 'fontSize': '1.2em'}),  # Div para o texto explicativo
        html.Div([
            html.Button('Anterior', id='previous-button', n_clicks=0, style={'marginRight': '10px'}),
            html.Button('Próximo', id='next-button', n_clicks=0)
        ], style={'marginTop': '20px'})
    ], style={'columnCount': 1, 'width': '80%', 'margin': 'auto', 'marginTop': '20px'}),
    
<<<<<<< HEAD
=======
    # Adicione mais dcc.Graph conforme necessário para mais gráficos existentes
>>>>>>> edfcf3b9572891a7a259fc23f77210ffa50e02aa
])

# Função para atualizar o gráfico e o texto explicativo com base no índice
@app.callback(
    [Output('carousel-graph', 'figure'),
     Output('graph-explanation', 'children')],
    [Input('previous-button', 'n_clicks'),
     Input('next-button', 'n_clicks')]
)
def update_graph(previous_clicks, next_clicks):
    global current_index
    
    # Verifica qual botão foi clicado
    ctx = dash.callback_context
    if ctx.triggered_id == 'previous-button' and current_index > 0:
        current_index -= 1
    elif ctx.triggered_id == 'next-button' and current_index < len(figuras) - 1:
        current_index += 1

    # Obtém a figura e a explicação para o gráfico atual
    figura_atual = figuras[current_index]
    explicacao_atual = explicacoes[current_index]

    return figura_atual, explicacao_atual

# Executa o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)

