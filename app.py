
import streamlit as st
import pandas as pd
import psycopg2
import requests
import yfinance as yf

def descobrir_faixa_etaria_best_doctors(idade):
    if (idade>=0 and idade<=17):
        return '0-17'
    if idade == 18:
        return '18-18'
    elif idade == 19:
        return '19-19'
    elif idade == 20:
        return '20-20'
    elif idade == 21:
        return '21-21'
    elif idade == 22:
        return '22-22'
    elif idade == 23:
        return '23-23'
    elif idade == 24:
        return '24-24'
    elif idade == 25:
        return '25-25'
    elif idade == 26:
        return '26-26'
    elif idade == 27:
        return '27-27'
    elif idade == 28:
        return '28-28'
    elif idade == 29:
        return '29-29'
    elif idade == 30:
        return '30-30'
    elif idade == 31:
        return '31-31'
    elif idade == 32:
        return '32-32'
    elif idade == 33:
        return '33-33'
    elif idade == 34:
        return '34-34'
    elif idade == 35:
        return '35-35'
    elif idade == 36:
        return '36-36'
    elif idade == 37:
        return '37-37'
    elif idade == 38:
        return '38-38'
    elif idade == 39:
        return '39-39'
    elif idade == 40:
        return '40-40'
    elif idade == 41:
        return '41-41'
    elif idade == 42:
        return '42-42'
    elif idade == 43:
        return '43-43'
    elif idade == 44:
        return '44-44'
    elif idade == 45:
        return '45-45'
    elif idade == 46:
        return '46-46'
    elif idade == 47:
        return '47-47'
    elif idade == 48:
        return '48-48'
    elif idade == 49:
        return '49-49'
    elif idade == 50:
        return '50-50'
    elif idade == 51:
        return '51-51'
    elif idade == 52:
        return '52-52'
    elif idade == 53:
        return '53-53'
    elif idade == 54:
        return '54-54'
    elif idade == 55:
        return '55-55'
    elif idade == 56:
        return '56-56'
    elif idade == 57:
        return '57-57'
    elif idade == 58:
        return '58-58'
    elif idade == 59:
        return '59-59'
    elif idade == 60:
        return '60-60'
    elif idade == 61:
        return '61-61'
    elif idade == 62:
        return '62-62'
    elif idade == 63:
        return '63-63'
    elif idade == 64:
        return '64-64'
    elif idade == 65:
        return '65-65'
    elif idade == 66:
        return '66-66'
    elif idade == 67:
        return '67-67'
    elif idade == 68:
        return '68-68'
    elif idade == 69:
        return '69-69'
    elif idade == 70:
        return '70-70'
    elif idade == 71:
        return '71-71'
    elif idade == 72:
        return '72-72'
    elif idade == 73:
        return '73-73'
    elif idade == 74:
        return '74-74'
    elif idade == 75:
        return '75-75'
    elif idade == 76:
        return '76-76'
    elif idade == 77:
        return '77-77'
    elif idade == 78:
        return '78-78'
    elif idade == 79:
        return '79-79'
    else:
        return '80+'

def descobrir_faixa_etaria_vumi(idade):
    if (idade>=0 and idade<=17):
        return '0 - 17'
    if (idade>=18 and idade<=24):
        return '18 - 24'
    elif (idade>=25 and idade<=29):
        return '25 - 29'
    elif (idade>=30 and idade<=34):
        return '30 - 34'
    elif (idade>=35 and idade<=39):
        return '35 - 39'
    elif (idade>=40 and idade<=44):
        return '40 - 44'
    elif (idade>=45 and idade<=49):
        return '45 - 49'
    elif (idade>=50 and idade<=54):
        return '50 - 54'
    elif (idade>=55 and idade<=59):
        return '55 - 59'
    elif (idade>=60 and idade<=74):
        st = str(idade)
        return  st  
    elif (idade>=75 and idade<=79):
        return '75 - 79'
    else:
        return '80+'

def descobrir_faixa_etaria_vumi_hospitalar(idade):
    if (idade>=0 and idade<=17):
        return '0 - 17'
    if (idade>=18 and idade<=24):
        return '18 - 24'
    elif (idade>=25 and idade<=29):
        return '25 - 29'
    elif (idade>=30 and idade<=34):
        return '30 - 34'
    elif (idade>=35 and idade<=39):
        return '35 - 39'
    elif (idade>=40 and idade<=44):
        return '40 - 44'
    elif (idade>=45 and idade<=49):
        return '45 - 49'
    elif (idade>=50 and idade<=54):
        return '50 - 54'
    elif (idade>=55 and idade<=59):
        return '55 - 59'
    elif (idade>=60 and idade<=74):
        st = str(idade)
        return  st  
    elif (idade>=75):
        return '75+'
    else:
        return '80+'

def descobrir_faixa_etaria_ever(idade):
    if (idade>=0 and idade<=17):
        return '0 - 17'
    if (idade>=18 and idade<=24):
        return '18 - 24'
    elif (idade>=25 and idade<=29):
        return '25 - 29'
    elif (idade>=30 and idade<=34):
        return '30 - 34'
    elif (idade>=35 and idade<=39):
        return '35 - 39'
    elif (idade>=40 and idade<=44):
        return '40 - 44'
    elif (idade>=45 and idade<=49):
        return '45 - 49'
    elif (idade>=50 and idade<=54):
        return '50 - 54'
    elif (idade>=55 and idade<=59):
        return '55 - 59'
    elif (idade>=60 and idade<=74):
        var = str(idade)
        return  var  
    else:
        return '75+'

def descobrir_valor_ever_completo(idade, ever_completo):
    
    if idade >= 0 and idade <= 17:
        return 0,0,0,0,0,0,0,0

    elif idade >= 18:
        idade  = descobrir_faixa_etaria_ever(idade)
        var_0 = ever_completo.loc[ever_completo["Age"] == idade, 0].values[0]
        var_500 = ever_completo.loc[ever_completo["Age"] == idade, 500].values[0]
        var_1000 = ever_completo.loc[ever_completo["Age"] == idade, 1000].values[0]
        var_2000 = ever_completo.loc[ever_completo["Age"] == idade, 2000].values[0]
        var_5000 = ever_completo.loc[ever_completo["Age"] == idade, 5000].values[0]
        var_10000 = ever_completo.loc[ever_completo["Age"] == idade, 10000].values[0]
        var_20000 = ever_completo.loc[ever_completo["Age"] == idade, 20000].values[0]
        var_50000 = ever_completo.loc[ever_completo["Age"] == idade, 50000].values[0]
        
        return var_0, var_500, var_1000, var_2000, var_5000, var_10000, var_20000, var_50000

def descobrir_valor_ever_hospitalar(idade, ever_hospitalar):
    
    if idade >= 0 and idade <= 17:
        return 0,0,0,0,0,0,0,0

    elif idade >= 18:
        idade  = descobrir_faixa_etaria_ever(idade)
        var_0 = ever_hospitalar.loc[ever_hospitalar["Age"] == idade, 0].values[0]
        var_500 = ever_hospitalar.loc[ever_hospitalar["Age"] == idade, 500].values[0]
        var_1000 = ever_hospitalar.loc[ever_hospitalar["Age"] == idade, 1000].values[0]
        var_2000 = ever_hospitalar.loc[ever_hospitalar["Age"] == idade, 2000].values[0]
        var_5000 = ever_hospitalar.loc[ever_hospitalar["Age"] == idade, 5000].values[0]
        var_10000 = ever_hospitalar.loc[ever_hospitalar["Age"] == idade, 10000].values[0]
        var_20000 = ever_hospitalar.loc[ever_hospitalar["Age"] == idade, 20000].values[0]
        var_50000 = ever_hospitalar.loc[ever_hospitalar["Age"] == idade, 50000].values[0]
        
        return var_0, var_500, var_1000, var_2000, var_5000, var_10000, var_20000, var_50000

def descobrir_valor_vumi_completo(idade, vumi_completo):
    
    if idade >= 0 and idade <= 17:
        
        return 0,0

    elif idade >= 18:
        idade  = descobrir_faixa_etaria_vumi(idade)
        var_2000 = vumi_completo.loc[vumi_completo["Age"] == idade, 2000].values[0]
        var_5000 = vumi_completo.loc[vumi_completo["Age"] == idade, 5000].values[0]
       
        
        return var_2000, var_5000

def descobrir_valor_vumi_hospitalar(idade, vumi_hospitalar):
    
    if idade >= 0 and idade <= 17:
        
        return 0, 0

    elif idade >= 18:

        idade  = descobrir_faixa_etaria_vumi_hospitalar(idade)
        var_2000 = vumi_hospitalar.loc[vumi_hospitalar["Age"] == idade, 2000].values[0]
        var_5000 = vumi_hospitalar.loc[vumi_hospitalar["Age"] == idade, 5000].values[0]

        
        return var_2000, var_5000

def descobrir_valor_best_doctors_completo(idade, best_doctors_completo):
    
    if idade >= 0 and idade <= 17:
        
        return 0, 0

    elif idade >= 18:

        idade  = descobrir_faixa_etaria_best_doctors(idade)
        var_2000 = best_doctors_completo.loc[best_doctors_completo["Age"] == idade, 2000].values[0]
        var_5000 = best_doctors_completo.loc[best_doctors_completo["Age"] == idade, 5000].values[0]

        
        return var_2000, var_5000

def filhos(filhos):
    if (filhos == 0):
        return '0 Filho'
    if (filhos == 1):
        return '1 Filho'
    if (filhos == 2):
        return '2 Filhos'
    else:
        return '3+ Filhos'

def leitura_tabela():
    connection = psycopg2.connect(
    user="postgres.amebfcyidikmvzqcqqfz",
    password="SEGUROSDATABASE",
    host="aws-0-sa-east-1.pooler.supabase.com",
    port="5432",
    database="postgres"
)
    connection.autocommit = True
    cursor = connection.cursor()
    plan=cursor.execute(f""" 
        SELECT *
        FROM public.vumi_completo;
    """)
    plan=cursor.fetchall()

    vumi=pd.DataFrame(plan, columns=["id", "Age", 2000, 5000, 10000, 20000, 50000])

    plan=cursor.execute(f""" 
        SELECT *
        FROM public.vumi_hospitalar;
    """)
    plan=cursor.fetchall()

    vumi_hospitalar=pd.DataFrame(plan, columns=["id", "Age", 2000, 5000, 10000, 20000, 50000])


    plan=cursor.execute(f""" 
        SELECT *
        FROM public.ever_completo;
    """)
    plan=cursor.fetchall()

    ever_completo=pd.DataFrame(plan, columns=["id", "Age", 0, 500, 1000, 2000, 5000, 10000, 20000, 50000])

    plan=cursor.execute(f""" 
        SELECT *
        FROM public.ever_hospitalar;
    """)
    plan=cursor.fetchall()

    ever_hospitalar=pd.DataFrame(plan, columns=["id", "Age", 0,500,1000,2000, 5000, 10000, 20000, 50000])


    plan=cursor.execute(f""" 
        SELECT *
        FROM public.best_doctors_completo;
    """)
    plan=cursor.fetchall()
    cursor.close()

    best_doctors_completo=pd.DataFrame(plan, columns=["id", "Age",2000, 5000, 10000, 20000])
    cursor.close()


    vumi['Age'] = vumi['Age'].astype(str)
    vumi_hospitalar['Age'] = vumi_hospitalar['Age'].astype(str)
    ever_completo['Age'] = ever_completo['Age'].astype(str)
    ever_hospitalar['Age'] = ever_hospitalar['Age'].astype(str)
    best_doctors_completo['Age'] = best_doctors_completo['Age'].astype(str)

    return vumi, ever_completo, ever_hospitalar, vumi_hospitalar, best_doctors_completo

def cotar_vumi(idade, filhos, df, idade_2): #Estou cotando VUMI completo
    
    var_2000, var_5000 = descobrir_valor_vumi_completo(idade_2, df)
    
    novo_df = pd.DataFrame(columns=['Franquia', 'Prêmio Anual $'])

    
    #Criando as franquias::
    novo_df.loc[0,'Franquia'] = 0
    novo_df.loc[1,'Franquia'] = 500
    novo_df.loc[2,'Franquia'] = 1000
    novo_df.loc[3,'Franquia'] = 2000
    novo_df.loc[4,'Franquia'] = 5000
    
    #Criandos os valores
    novo_df.loc[0,'Prêmio Anual $'] = 0
    novo_df.loc[1,'Prêmio Anual $'] = 0
    novo_df.loc[2,'Prêmio Anual $'] = 0

    if (idade == '0 - 17'): # SEM VALOR

        novo_df.loc[3,'Prêmio Anual $'] = 0
        novo_df.loc[4,'Prêmio Anual $'] = 0
    
    elif (filhos == '0 Filho'):

        novo_df.loc[3,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 2000].values[0]  + var_2000 + 75
        novo_df.loc[4,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 5000].values[0]  + var_5000 + 75
   
   
    else:

        novo_df.loc[3,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 2000].values[0] + df.loc[df["Age"] == filhos, 2000].values[0] + var_2000 + 75
        novo_df.loc[4,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 5000].values[0] + df.loc[df["Age"] == filhos, 5000].values[0] + var_5000 + 75
   
    return novo_df
    
def cotar_vumi_hospitalar(idade, filhos, df, idade_2): #Estou cotando VUMI completo
    
    var_2000, var_5000 = descobrir_valor_vumi_hospitalar(idade_2,df)
   
    novo_df = pd.DataFrame(columns=['Franquia', 'Prêmio Anual $'])
    
    #Criando as franquias::
    novo_df.loc[0,'Franquia'] = 0
    novo_df.loc[1,'Franquia'] = 500
    novo_df.loc[2,'Franquia'] = 1000
    novo_df.loc[3,'Franquia'] = 2000
    novo_df.loc[4,'Franquia'] = 5000
    
    #Criandos os valores
    novo_df.loc[0,'Prêmio Anual $'] = 0
    novo_df.loc[1,'Prêmio Anual $'] = 0
    novo_df.loc[2,'Prêmio Anual $'] = 0

    if (idade == '0 - 17'): # SEM VALOR

        novo_df.loc[3,'Prêmio Anual $'] = 0
        novo_df.loc[4,'Prêmio Anual $'] = 0


    elif (filhos == '0 Filho'):

        novo_df.loc[3,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 2000].values[0] + var_2000 + 75
        novo_df.loc[4,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 5000].values[0] + var_5000 + 75
    

    else:

        novo_df.loc[3,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 2000].values[0] + df.loc[df["Age"] == filhos, 2000].values[0] + var_2000 + 75
        novo_df.loc[4,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 5000].values[0] + df.loc[df["Age"] == filhos, 5000].values[0] + var_5000 + 75
   
    
    return novo_df

def cotar_ever(idade, filhos, df, idade2): #Estou cotando VUMI completo


    var_0, var_500, var_1000, var_2000, var_5000, var_10000, var_20000, var_50000 = descobrir_valor_ever_completo(idade2,df)

    novo_df = pd.DataFrame(columns=['Franquia', 'Prêmio Anual $'])
    
    #Criando as franquias::
    novo_df.loc[0,'Franquia'] = 0
    novo_df.loc[1,'Franquia'] = 500
    novo_df.loc[2,'Franquia'] = 1000
    novo_df.loc[3,'Franquia'] = 2000
    novo_df.loc[4,'Franquia'] = 5000
    novo_df.loc[5,'Franquia'] = 10000
    novo_df.loc[6,'Franquia'] = 20000
    novo_df.loc[7,'Franquia'] = 50000



    if (idade == '0 - 17'): # SEM VALOR

        novo_df.loc[0,'Prêmio Anual $'] = 0
        novo_df.loc[1,'Prêmio Anual $'] = 0
        novo_df.loc[2,'Prêmio Anual $'] = 0
        novo_df.loc[3,'Prêmio Anual $'] = 0
        novo_df.loc[4,'Prêmio Anual $'] = 0
        novo_df.loc[5,'Prêmio Anual $'] = 0
        novo_df.loc[6,'Prêmio Anual $'] = 0
        novo_df.loc[7,'Prêmio Anual $'] = 0

    elif (filhos == '0 Filho'):

        novo_df.loc[0,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 0].values[0] + var_0 + 75
        novo_df.loc[1,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 500].values[0] + var_500 + 75
        novo_df.loc[2,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 1000].values[0] + var_1000 + 75
        novo_df.loc[3,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 2000].values[0] + var_2000 + 75
        novo_df.loc[4,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 5000].values[0] + var_5000 + 75
        novo_df.loc[5,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 10000].values[0] + var_10000 + 75
        novo_df.loc[6,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 20000].values[0] + var_20000 + 75
        novo_df.loc[7,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 50000].values[0] + var_50000 + 75

    else:

        novo_df.loc[0,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 0].values[0] + df.loc[df["Age"] == filhos, 0].values[0] +  var_0 + 75
        novo_df.loc[1,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 500].values[0] + df.loc[df["Age"] == filhos, 500].values[0] + var_500 + 75
        novo_df.loc[2,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 1000].values[0] + df.loc[df["Age"] == filhos, 1000].values[0] + var_1000 + 75
        novo_df.loc[3,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 2000].values[0] + df.loc[df["Age"] == filhos, 2000].values[0] + var_2000 + 75
        novo_df.loc[4,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 5000].values[0] + df.loc[df["Age"] == filhos, 5000].values[0] + var_5000 + 75
        novo_df.loc[5,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 10000].values[0] + df.loc[df["Age"] == filhos, 10000].values[0] + var_10000 + 75
        novo_df.loc[6,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 20000].values[0] + df.loc[df["Age"] == filhos, 20000].values[0] + var_20000 + 75
        novo_df.loc[7,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 50000].values[0] + df.loc[df["Age"] == filhos, 50000].values[0] + var_50000 + 75
   
    
    
    return novo_df

def cotar_ever_hospitalar(idade, filhos, df, idade2): #Estou cotando VUMI completo

    var_0, var_500, var_1000, var_2000, var_5000, var_10000, var_20000, var_50000 = descobrir_valor_ever_completo(idade2, df)


    novo_df = pd.DataFrame(columns=['Franquia', 'Prêmio Anual $'])
    
    #Criando as franquias::
    novo_df.loc[0,'Franquia'] = 0
    novo_df.loc[1,'Franquia'] = 500
    novo_df.loc[2,'Franquia'] = 1000
    novo_df.loc[3,'Franquia'] = 2000
    novo_df.loc[4,'Franquia'] = 5000
    novo_df.loc[5,'Franquia'] = 10000
    novo_df.loc[6,'Franquia'] = 20000
    novo_df.loc[7,'Franquia'] = 50000


    if (idade == '0 - 17'): # SEM VALOR

        novo_df.loc[0,'Prêmio Anual $'] = 0
        novo_df.loc[1,'Prêmio Anual $'] = 0
        novo_df.loc[2,'Prêmio Anual $'] = 0
        novo_df.loc[3,'Prêmio Anual $'] = 0
        novo_df.loc[4,'Prêmio Anual $'] = 0
        novo_df.loc[5,'Prêmio Anual $'] = 0
        novo_df.loc[6,'Prêmio Anual $'] = 0
        novo_df.loc[7,'Prêmio Anual $'] = 0

    elif (filhos == '0 Filho'):

        novo_df.loc[0,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 0].values[0]  + var_0 + 75
        novo_df.loc[1,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 500].values[0] + var_500 + 75
        novo_df.loc[2,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 1000].values[0] + var_1000 + 75
        novo_df.loc[3,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 2000].values[0] + var_2000 + 75
        novo_df.loc[4,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 5000].values[0] + var_5000 + 75 
        novo_df.loc[5,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 10000].values[0] + var_10000 + 75
        novo_df.loc[6,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 20000].values[0]  + var_20000 + 75
        novo_df.loc[7,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 50000].values[0]  + var_50000 + 75

    else:

        novo_df.loc[0,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 0].values[0] + df.loc[df["Age"] == filhos, 0].values[0] + var_0 + 75
        novo_df.loc[1,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 500].values[0] + df.loc[df["Age"] == filhos, 500].values[0] + var_500 + 75
        novo_df.loc[2,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 1000].values[0] + df.loc[df["Age"] == filhos, 1000].values[0] + var_1000 + 75
        novo_df.loc[3,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 2000].values[0] + df.loc[df["Age"] == filhos, 2000].values[0] + var_2000 + 75
        novo_df.loc[4,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 5000].values[0] + df.loc[df["Age"] == filhos, 5000].values[0] + var_5000 + 75
        novo_df.loc[5,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 10000].values[0] + df.loc[df["Age"] == filhos, 10000].values[0] + var_10000 + 75
        novo_df.loc[6,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 20000].values[0] + df.loc[df["Age"] == filhos, 20000].values[0] + var_20000 + 75
        novo_df.loc[7,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 50000].values[0] + df.loc[df["Age"] == filhos, 50000].values[0] + var_50000 + 75
   
        
    return novo_df

def cotar_best_doctors(idade, filhos, df, idade_2): #Estou cotando VUMI completo
    
    var_2000, var_5000 = descobrir_valor_best_doctors_completo(idade_2, df)
    
    novo_df = pd.DataFrame(columns=['Franquia', 'Prêmio Anual $'])
  
    #Criando as franquias::
    novo_df.loc[0,'Franquia'] = 0
    novo_df.loc[1,'Franquia'] = 500
    novo_df.loc[2,'Franquia'] = 1000
    novo_df.loc[3,'Franquia'] = 2000
    novo_df.loc[4,'Franquia'] = 5000
    
    #Criandos os valores
    novo_df.loc[0,'Prêmio Anual $'] = 0
    novo_df.loc[1,'Prêmio Anual $'] = 0
    novo_df.loc[2,'Prêmio Anual $'] = 0

    if (idade == '0 - 17'): # SEM VALOR

        novo_df.loc[3,'Prêmio Anual $'] = 0
        novo_df.loc[4,'Prêmio Anual $'] = 0
    
    elif (filhos == '0 Filho'):

        novo_df.loc[3,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 2000].values[0]  + var_2000 + 75
        novo_df.loc[4,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 5000].values[0]  + var_5000 + 75
   
   
    else:

        novo_df.loc[3,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 2000].values[0] + df.loc[df["Age"] == filhos, 2000].values[0] + var_2000 + 75
        novo_df.loc[4,'Prêmio Anual $'] = df.loc[df["Age"] == idade, 5000].values[0] + df.loc[df["Age"] == filhos, 5000].values[0] + var_5000 + 75

    return novo_df

def verificar_regra(param_list, df):
    if "Nenhuma" in param_list or not param_list:
        return df  # Nenhuma regra aplicada

    # Se as duas regras estão presentes, aplica 15% de desconto
    if "Sem Cobertura nos EUA" in param_list and "Mora fora do Eixo RJ-SP" in param_list:
        df['Prêmio Anual $'] = ((df['Prêmio Anual $']-75) * 0.85) + 75

    # Se só "Sem Cobertura nos EUA" foi selecionada
    elif "Sem Cobertura nos EUA" in param_list:
        df['Prêmio Anual $'] = (((df['Prêmio Anual $']-75)) * 0.9) + 75

    # Se só "Mora fora do Eixo RJ-SP" foi selecionada
    elif "Mora fora do Eixo RJ-SP" in param_list:
        df['Prêmio Anual $'] = ((df['Prêmio Anual $']-75) * 0.95) + 75

    return df

@st.cache_data(ttl=60)          # evita bater no limite chamando no máximo 1× por minuto
def pega_cotacao_dol():
    try:
        url = "https://economia.awesomeapi.com.br/last/USD-BRL"
        response = requests.get(url)
        x = response.json()
        return x['USDBRL']['bid']
    except:
        info = yf.Ticker("USDBRL=X").info
        return info['bid']

        

#Leitura das tabelas deparas
vumi, ever_completo, ever_hospitalar, vumi_hospitalar, best_doctors_completo = leitura_tabela()
dol = pega_cotacao_dol()
dol = float(dol)     # Convert string to float

dol = round(dol,2)
print(dol)

# --- Sidebar ---
st.sidebar.title("R.C Tech")
st.sidebar.title("Dolar: R$ " + str(dol))
st.sidebar.title("Parâmetros")
idade = st.sidebar.number_input("Idade", min_value=0, max_value=100, value=0)
idade_parceiro = st.sidebar.number_input("Idade Parceiro(a), caso nao tenha deixe 0.", min_value=0, max_value=100, value=0)

fil = st.sidebar.number_input("Quantos filhos", min_value=0, max_value=100, value=0)


regras = ["Nenhuma", "Sem Cobertura nos EUA", "Mora fora do Eixo RJ-SP"]
regra = st.sidebar.multiselect("Tem algumas dessas especificidades? (EVER)", regras)


profissoes = ["Nenhuma","Saúde", "Médico", "Advogado OAB", "Agro"]
profissao = st.sidebar.selectbox("Porfissão?", profissoes)

percentual_desconto = st.sidebar.number_input("Desconto VUMI?", min_value=0, max_value=100, value=0)

percentual_desconto = percentual_desconto/100

st.sidebar.markdown("<br>", unsafe_allow_html=True)

gerar_tabela = st.sidebar.button("🔍 Gerar Tabela")

                # --- Filtragem --- #
df_vumi_completo = pd.DataFrame(columns=['Franquia', 'Prêmio Anual $'])
df_ever_completo = pd.DataFrame(columns=['Franquia', 'Prêmio Anual $'])
df_ever_hospitalar = pd.DataFrame(columns=['Franquia', 'Prêmio Anual $'])
df_vumi_hospitalar = pd.DataFrame(columns=['Franquia', 'Prêmio Anual $'])
df_best_doctors_completo = pd.DataFrame(columns=['Franquia', 'Prêmio Anual $'])



if gerar_tabela:

    #gerando tabela da vumi 
    faixa_vumi  = descobrir_faixa_etaria_vumi(idade)
    faixa_vumi_hospitalar  = descobrir_faixa_etaria_vumi_hospitalar(idade)

    children  = filhos(fil)
    df_vumi_completo = cotar_vumi(faixa_vumi, children, vumi, idade_parceiro)

    #gerando tabela da EVER Completo::
    faixa_ever = descobrir_faixa_etaria_ever(idade)
    df_ever_completo = cotar_ever(faixa_ever, children, ever_completo, idade_parceiro)

    #gerando tabela da EVER hospitalar::
    df_ever_hospitalar = cotar_ever_hospitalar(faixa_ever, children, ever_hospitalar, idade_parceiro)

    #gerando tabela da VUMI hospitalar::
    df_vumi_hospitalar = cotar_vumi_hospitalar(faixa_vumi_hospitalar, children, vumi_hospitalar, idade_parceiro)
    #---------------------------------------------------------------------------------#
    #Especificidades da EVER
    df_ever_completo = verificar_regra(regra, df_ever_completo)
    df_ever_hospitalar = verificar_regra(regra, df_ever_hospitalar)

    #Gerando tabela da best doctors::
    faixa_best  = descobrir_faixa_etaria_best_doctors(idade)

    df_best_doctors_completo = cotar_best_doctors(faixa_best, children, best_doctors_completo, idade_parceiro)

    #----------------------------------------------------------------------------------#



    df_vumi_completo['Prêmio Anual $'] = pd.to_numeric(df_vumi_completo['Prêmio Anual $'], errors='coerce')
    df_vumi_hospitalar['Prêmio Anual $'] = pd.to_numeric(df_vumi_hospitalar['Prêmio Anual $'], errors='coerce')
    df_ever_completo['Prêmio Anual $'] = pd.to_numeric(df_ever_completo['Prêmio Anual $'], errors='coerce')
    df_ever_hospitalar['Prêmio Anual $'] = pd.to_numeric(df_ever_hospitalar['Prêmio Anual $'], errors='coerce')



    
    #Valores em Reais
    df_vumi_completo['Valor Mensal R$'] = ((df_vumi_completo['Prêmio Anual $']/12) * dol).round().astype(int)
    df_vumi_hospitalar['Valor Mensal R$'] = ((df_vumi_hospitalar['Prêmio Anual $']/12) * dol).round().astype(int)
    df_ever_completo['Valor Mensal R$'] = ((df_ever_completo['Prêmio Anual $']/12)*dol).round().astype(int)
    df_ever_hospitalar['Valor Mensal R$'] = ((df_ever_hospitalar['Prêmio Anual $']/12)*dol).round().astype(int)



    #Entrando nos descontos
    if(profissao == "Saúde"):
        
        if (percentual_desconto==0):

            df_vumi_completo['Prêmio Anual $ Desconto'] = "Sem Desconto"
            df_vumi_hospitalar['Prêmio Anual $ Desconto'] = "Sem Desconto"
            df_ever_completo['Prêmio Anual $ Desconto'] = (df_ever_completo['Prêmio Anual $']-75) * 0.8
            df_ever_hospitalar['Prêmio Anual $ Desconto'] = (df_ever_hospitalar['Prêmio Anual $']-75)* 0.8



            #Valores em Reais

            df_ever_completo['Valor Mensal R$ Desconto'] = ((df_ever_completo['Prêmio Anual $ Desconto']/12)*dol).round().astype(int)
            df_ever_hospitalar['Valor Mensal R$ Desconto'] = ((df_ever_hospitalar['Prêmio Anual $ Desconto']/12)*dol).round().astype(int)



        else:
            df_vumi_completo['Prêmio Anual $ Desconto'] = (df_vumi_completo['Prêmio Anual $']-75) * (1-percentual_desconto)
            df_vumi_hospitalar['Prêmio Anual $ Desconto'] = (df_vumi_hospitalar['Prêmio Anual $']-75)* (1 - percentual_desconto)
            df_ever_completo['Prêmio Anual $ Desconto'] = (df_ever_completo['Prêmio Anual $']-75) * 0.8
            df_ever_hospitalar['Prêmio Anual $ Desconto'] = (df_ever_hospitalar['Prêmio Anual $']-75)* 0.8
                        #ajustando coluna
            df_vumi_completo.loc[0,'Prêmio Anual $ Desconto'] = 0
            df_vumi_completo.loc[1,'Prêmio Anual $ Desconto'] = 0
            df_vumi_completo.loc[2,'Prêmio Anual $ Desconto'] = 0
            df_vumi_hospitalar.loc[0,'Prêmio Anual $ Desconto'] = 0
            df_vumi_hospitalar.loc[1,'Prêmio Anual $ Desconto'] = 0
            df_vumi_hospitalar.loc[2,'Prêmio Anual $ Desconto'] = 0



            df_ever_completo['Valor Mensal R$ Desconto'] = ((df_ever_completo['Prêmio Anual $ Desconto']/12)*dol).round().astype(int)
            df_ever_hospitalar['Valor Mensal R$ Desconto'] = ((df_ever_hospitalar['Prêmio Anual $ Desconto']/12)*dol).round().astype(int)
            df_vumi_completo['Valor Mensal R$ Desconto'] = ((df_vumi_completo['Prêmio Anual $ Desconto']/12)*dol).round().astype(int)
            df_vumi_hospitalar['Valor Mensal R$ Desconto'] = ((df_vumi_hospitalar['Prêmio Anual $ Desconto']/12)*dol).round().astype(int)

               
    if(profissao == "Médico"):

        df_vumi_completo['Prêmio Anual $ Desconto'] = (df_vumi_completo['Prêmio Anual $']-75) * 0.8
        df_vumi_hospitalar['Prêmio Anual $ Desconto'] = (df_vumi_hospitalar['Prêmio Anual $'] - 75)* 0.8
        df_ever_completo['Prêmio Anual $ Desconto'] = (df_ever_completo['Prêmio Anual $'] - 75)  * 0.8
        df_ever_hospitalar['Prêmio Anual $ Desconto'] = (df_ever_hospitalar['Prêmio Anual $'] - 75) * 0.8


        #com desconto
        df_ever_completo['Valor Mensal R$ Desconto'] = ((df_ever_completo['Prêmio Anual $ Desconto']/12)*dol).round().astype(int)
        df_ever_hospitalar['Valor Mensal R$ Desconto'] = ((df_ever_hospitalar['Prêmio Anual $ Desconto']/12)*dol).round().astype(int)
        df_vumi_completo['Valor Mensal R$ Desconto'] = ((df_vumi_completo['Prêmio Anual $ Desconto']/12)*dol).round().astype(int)
        df_vumi_hospitalar['Valor Mensal R$ Desconto'] = ((df_vumi_hospitalar['Prêmio Anual $ Desconto']/12)*dol).round().astype(int)








       
    if(profissao == "Advogado OAB"):

        if (percentual_desconto==0):
            df_vumi_completo['Prêmio Anual $ Desconto'] = "Sem Desconto"
            df_vumi_hospitalar['Prêmio Anual $ Desconto'] = "Sem Desconto"
            df_ever_completo['Prêmio Anual $ Desconto'] = (df_ever_completo['Prêmio Anual $'] - 75)* 0.875
            df_ever_hospitalar['Prêmio Anual $ Desconto'] = (df_ever_hospitalar['Prêmio Anual $'] - 75) * 0.875
        
        


            #Valores em Reais

            df_ever_completo['Valor Mensal R$ Desconto'] = ((df_ever_completo['Prêmio Anual $ Desconto']/12)*dol).round().astype(int)
            df_ever_hospitalar['Valor Mensal R$ Desconto'] = ((df_ever_hospitalar['Prêmio Anual $ Desconto']/12)*dol).round().astype(int)


        
        
        else:
            df_vumi_completo['Prêmio Anual $ Desconto'] = (df_vumi_completo['Prêmio Anual $']-75) * (1-percentual_desconto)
            df_vumi_hospitalar['Prêmio Anual $ Desconto'] = (df_vumi_hospitalar['Prêmio Anual $']-75)* (1 - percentual_desconto)
            df_ever_completo['Prêmio Anual $ Desconto'] = (df_ever_completo['Prêmio Anual $'] - 75)* 0.875
            df_ever_hospitalar['Prêmio Anual $ Desconto'] = (df_ever_hospitalar['Prêmio Anual $'] - 75) * 0.875
                        #ajustando coluna
            df_vumi_completo.loc[0,'Prêmio Anual $ Desconto'] = 0
            df_vumi_completo.loc[1,'Prêmio Anual $ Desconto'] = 0
            df_vumi_completo.loc[2,'Prêmio Anual $ Desconto'] = 0
            df_vumi_hospitalar.loc[0,'Prêmio Anual $ Desconto'] = 0
            df_vumi_hospitalar.loc[1,'Prêmio Anual $ Desconto'] = 0
            df_vumi_hospitalar.loc[2,'Prêmio Anual $ Desconto'] = 0



            #com desconto
            df_ever_completo['Valor Mensal R$ Desconto'] = ((df_ever_completo['Prêmio Anual $ Desconto']/12)*dol).round().astype(int)
            df_ever_hospitalar['Valor Mensal R$ Desconto'] = ((df_ever_hospitalar['Prêmio Anual $ Desconto']/12)*dol).round().astype(int)
            df_vumi_completo['Valor Mensal R$ Desconto'] = ((df_vumi_completo['Prêmio Anual $ Desconto']/12)*dol).round().astype(int)
            df_vumi_hospitalar['Valor Mensal R$ Desconto'] = ((df_vumi_hospitalar['Prêmio Anual $ Desconto']/12)*dol).round().astype(int)



   
    if(profissao == "Agro"):

        if (percentual_desconto==0):

            df_vumi_completo['Prêmio Anual $ Desconto'] = "Sem Desconto"
            df_vumi_hospitalar['Prêmio Anual $ Desconto'] = "Sem Desconto"
            df_ever_completo['Prêmio Anual $ Desconto'] = (df_ever_completo['Prêmio Anual $'] - 75) * 0.8
            df_ever_hospitalar['Prêmio Anual $ Desconto'] = (df_ever_hospitalar['Prêmio Anual $'] - 75) * 0.8
        
        
            #Valores em Reais

            df_ever_completo['Valor Mensal R$ Desconto'] = ((df_ever_completo['Prêmio Anual $ Desconto']/12)*dol).round().astype(int)
            df_ever_hospitalar['Valor Mensal R$ Desconto'] = ((df_ever_hospitalar['Prêmio Anual $ Desconto']/12)*dol).round().astype(int)        
        
        
        
        
        else:
            df_vumi_completo['Prêmio Anual $ Desconto'] = (df_vumi_completo['Prêmio Anual $']-75) * (1-percentual_desconto)
            df_vumi_hospitalar['Prêmio Anual $ Desconto'] = (df_vumi_hospitalar['Prêmio Anual $']-75)* (1 - percentual_desconto)
            df_ever_completo['Prêmio Anual $ Desconto'] = (df_ever_completo['Prêmio Anual $'] - 75) * 0.8
            df_ever_hospitalar['Prêmio Anual $ Desconto'] = (df_ever_hospitalar['Prêmio Anual $'] - 75) * 0.8

            #ajustando coluna
            df_vumi_completo.loc[0,'Prêmio Anual $ Desconto'] = 0
            df_vumi_completo.loc[1,'Prêmio Anual $ Desconto'] = 0
            df_vumi_completo.loc[2,'Prêmio Anual $ Desconto'] = 0
            df_vumi_hospitalar.loc[0,'Prêmio Anual $ Desconto'] = 0
            df_vumi_hospitalar.loc[1,'Prêmio Anual $ Desconto'] = 0
            df_vumi_hospitalar.loc[2,'Prêmio Anual $ Desconto'] = 0


            #com desconto
            df_ever_completo['Valor Mensal R$ Desconto'] = ((df_ever_completo['Prêmio Anual $ Desconto']/12)*dol).round().astype(int)
            df_ever_hospitalar['Valor Mensal R$ Desconto'] = ((df_ever_hospitalar['Prêmio Anual $ Desconto']/12)*dol).round().astype(int)
            df_vumi_completo['Valor Mensal R$ Desconto'] = ((df_vumi_completo['Prêmio Anual $ Desconto']/12)*dol).round().astype(int)
            df_vumi_hospitalar['Valor Mensal R$ Desconto'] = ((df_vumi_hospitalar['Prêmio Anual $ Desconto']/12)*dol).round().astype(int)





    if(profissao == "Nenhuma"):
        
        if (percentual_desconto==0):


            #df_vumi_completo['Prêmio Anual $ Desconto'] = "Sem Desconto"
            #df_vumi_hospitalar['Prêmio Anual $ Desconto'] = "Sem Desconto"
            #df_ever_completo['Prêmio Anual $ Desconto'] = df_ever_completo['Prêmio Anual $'] 
            #df_ever_hospitalar['Prêmio Anual $ Desconto'] = df_ever_hospitalar['Prêmio Anual $']
            do = 'nothing'
        else:
            df_vumi_completo['Prêmio Anual $ Desconto'] = (df_vumi_completo['Prêmio Anual $']-75) * (1-percentual_desconto)
            df_vumi_hospitalar['Prêmio Anual $ Desconto'] = (df_vumi_hospitalar['Prêmio Anual $']-75)* (1 - percentual_desconto)
            df_ever_completo['Prêmio Anual $ Desconto'] = df_ever_completo['Prêmio Anual $']
            df_ever_hospitalar['Prêmio Anual $ Desconto'] = df_ever_hospitalar['Prêmio Anual $']
                        #ajustando coluna
            df_vumi_completo.loc[0,'Prêmio Anual $ Desconto'] = 0
            df_vumi_completo.loc[1,'Prêmio Anual $ Desconto'] = 0
            df_vumi_completo.loc[2,'Prêmio Anual $ Desconto'] = 0
            df_vumi_hospitalar.loc[0,'Prêmio Anual $ Desconto'] = 0
            df_vumi_hospitalar.loc[1,'Prêmio Anual $ Desconto'] = 0
            df_vumi_hospitalar.loc[2,'Prêmio Anual $ Desconto'] = 0



            #com desconto
            df_ever_completo['Valor Mensal R$ Desconto'] = ((df_ever_completo['Prêmio Anual $ Desconto']/12)*dol).round().astype(int)
            df_ever_hospitalar['Valor Mensal R$ Desconto'] = ((df_ever_hospitalar['Prêmio Anual $ Desconto']/12)*dol).round().astype(int)
            df_vumi_completo['Valor Mensal R$ Desconto'] = ((df_vumi_completo['Prêmio Anual $ Desconto']/12)*dol).round().astype(int)
            df_vumi_hospitalar['Valor Mensal R$ Desconto'] = ((df_vumi_hospitalar['Prêmio Anual $ Desconto']/12)*dol).round().astype(int)






# --- Corpo principal ---
# CSS para alinhar tudo mais à esquerda
st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;   /* valor padrão é maior (~6rem) */
            padding-left: 6rem;
            padding-right: 1rem;
            max-width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho alinhado
st.markdown("<h1 style='text-align: left;'>Cotador Seguro Internacional</h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)




col1, col2 = st.columns([2, 3])  # col1 ocupa 2x o espaço da col2

# Primeira coluna: título e tabela
with col1:

    st.subheader("VUMI Completo")
    st.dataframe(df_vumi_completo)

# Segunda coluna: título e outra tabela
with col2:

    st.subheader("VUMI Hospitalar")
    st.dataframe(df_vumi_hospitalar)



col1, col2 = st.columns([2, 3])  # col1 ocupa 2x o espaço da col2

# Primeira coluna: título e tabela
with col1:

    st.subheader("EVER Completo")
    st.dataframe(df_ever_completo)

# Segunda coluna: título e outra tabela
with col2:

    st.subheader("EVER Hospitalar")
    st.dataframe(df_ever_hospitalar)

st.subheader("Best Doctors Completo")
st.dataframe(df_best_doctors_completo)
