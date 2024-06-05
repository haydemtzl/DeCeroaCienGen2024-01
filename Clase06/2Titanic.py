
# coding: utf-8

# In[25]:

import pandas as pd

#importemos (carguemos en memoria) la data
#pandas carga la data como un dataframe o matriz, tal como si tuvieramos un spreadsheet

data = pd.read_csv('2titanic.csv')

#previsualicemos la data
data.head()


# In[26]:

#cual es la dimension (filas, columnas) de mi dataframe?
print(data.shape)


# In[6]:

print(data.count())


# In[9]:

col_names = data.columns.tolist()
for column in col_names:
    print("Valores nulos en "+ str(column) +": " +str(data[column].isnull().sum()))


# In[11]:

d = {'male': 'M', 'female':'F'}
data['Sex'] = data['Sex'].apply(lambda x:d[x])
data['Sex'].head()


# In[12]:

data.Age


# In[13]:

data.describe()


# In[14]:

data[data.Fare==0]


# In[16]:

pd.crosstab(data.Survived, data.Sex)


# In[17]:

#Como fue la sobreviviencia por clase, sexo
pclass_gender_survival_count_df = data.groupby( ['Pclass', 'Sex'] )['Survived'].sum()
pclass_gender_survival_count_df


# In[18]:


import matplotlib.pyplot as plt


fig = plt.figure(figsize=(30,10)) #creamos un canvas o figura de 30x10 pixeles

# queremos ver un plot al costado del otro, para esto pensemos en una grilla (celdas)
plt.subplot2grid((2,3),(0,0))
data.Survived.value_counts().plot(kind='bar', alpha=0.5)
plt.title('Sobrevivieron - cuenta total -')

# Hay manera un poco mas amigable de interpretar datos....con porcentajes!
plt.subplot2grid((2,3),(0,1))
data.Survived.value_counts(normalize = True).plot(kind='bar', alpha=0.5)
plt.title('Sobrevivieron - porcentaje total -')

plt.show()


# In[19]:

#Sobrevivieron mas hombres o mas mujeres?
fig = plt.figure(figsize=(30,10))
data.Sex[data.Survived == 1].value_counts(normalize = True).plot(kind='barh', alpha=0.5)
plt.title('Sobrevivieron - Male vs Female -')
plt.show()


# In[22]:

# La clase del ticket fue un factor de sobrevivencia (si viste Titanic, ya lo sabes!)
fig = plt.figure(figsize=(10,5))
#colors bgrcmykw
data.Pclass[data.Survived == 1 ].value_counts(normalize = True).plot(kind='bar', alpha=0.5)
plt.title('Sobrevivientes por Clase de Ticket')
plt.show()


# In[23]:


# Habra alguna relacion entre tipo de ticket y edad? (Poder Adquisitivo)
fig = plt.figure(figsize=(20,10))

for t_class in [1,2,3]:
    data.Age[data.Pclass == t_class].plot(kind='kde')

plt.legend(("1ra. Clase", "2da. Clase", "3ra.Clase"))
plt.show()

# La linea de la 1ra clase, nos muestra que el promedio de edad del comprador es de 40 annios
# La linea de la 3ra clase, tiene un promedio mucho mas joven

# Podriamos hacer una inferencia temprana y decir que los hombres que salvaron fueron
# en su mayoria ricos y > 30 annios


# In[24]:

data[data.Age < 1]


# In[ ]:
