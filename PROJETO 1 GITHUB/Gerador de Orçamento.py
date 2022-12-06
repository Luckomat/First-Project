#!/usr/bin/env python
# coding: utf-8

# # Meu primeiro código Python

# In[6]:


print("Orçamento Gerado Com Sucesso!")
print("Semana do Python na Prática")
print("Eu quero muito aprender Python!")

## Este é meu primeiro código Python, realizado com o apoio do Curso da Empowerdata: Semana do Python na Prática
# 
# # Entrada de Dados

# In[7]:


input("Digite a descrição do projeto: ")
input("Digite o total de horas estimadas: ")
input("Digite o valor da hora trabalhada: ")
input("Digite o prazo estimado: ")


# # Guardando informações do Usuário

# In[18]:


projeto = input("Digite a descrição do projeto: ")
horas_estimadas = input("Digite o total de horas estimadas: ")
valor_hora = input("Digite o valor da hora trabalhada: ")
prazo = input("Digite o prazo estimado: ")


# In[20]:


print(prazo)


# # Realizando cálculos

# In[49]:


valor_total = int(horas_estimadas) * int(valor_hora)


# In[32]:


type("Lucas")


# In[38]:


print(valor_total)


# # Gerando o PDF

# In[40]:


get_ipython().system('pip install fpdf')


# In[50]:


from fpdf import FPDF


# In[56]:


pdf = FPDF()

pdf.add_page()
pdf.set_font("Arial")

pdf.image("template.png", x=0, y=0)
###### Nesta parte se usa um Template já criado anteriormente para o fundo do PDF. ######

pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_estimadas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo)
pdf.text(115, 205, str(valor_total))

pdf.output("Orçamento.pdf")
print("Orçamento Gerado com sucesso!")

