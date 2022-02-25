from cgitb import text
import pickle
from textwrap import fill
import tkinter as tk
import pandas as pd


def app(modelo):

    def classifica():
        elemento = {'abnormal_short_term_variability':[entry01.get()],
                    'prolongued_decelerations':[entry02.get()],
                    'accelerations':[entry03.get()],
                    'histogram_mode':[entry04.get()],
                    'histogram_mean':[entry05.get()],
                    'histogram_median':[entry06.get()],
                    'mean_value_of_long_term_variability':[entry07.get()],
                    'percentage_of_time_with_abnormal_long_term_variability':[entry08.get()],
                    'histogram_variance':[entry09.get()],
                    'histogram_tendency':[entry10.get()],
                    'light_decelerations':[entry11.get()]}

        result = modelo.predict(pd.DataFrame(elemento))[0]
        proba_result = modelo.predict_proba(pd.DataFrame(elemento))[0]

        print('Resultado: ', result)
        print('Probabilidades: ', proba_result)

        if result == 1:
            label12.config(text='Classificação:\nCondições normais')
            label13.config(text=f'Probabilidade: {proba_result[0]*100}%')
        elif result == 2:
            label12.config(text='Classificação:\nCondições suspeitas')
            label13.config(text=f'Probabilidade: {proba_result[1]*100}%')
        elif result == 3:
            label12.config(text='Classificação:\nCondições patológicas')
            label13.config(text=f'Probabilidade: {proba_result[2]*100}%')
        else:
            label12.config(text='Classificação: Erro')
            label13.config(text='Probabilidade: 0%')
    #-------------------------------------------------------------------------------------------

    try:
        root = tk.Tk()

        root.title('Análise Saúde Fetal')
        root.geometry('500x400')

        frame01 = tk.LabelFrame(root, text='Dados de entrada do indivíduo', padx=10, pady=10)
        frame01.pack(fill=tk.BOTH)

        #Entrada 01 -------------------------------------------------------------
        label01 = tk.Label(frame01, text='abnormal_short_term_variability')
        label01.grid(row=1, column=1)
        entry01 = tk.Entry(frame01)
        entry01.grid(row=2, column=1)
        #------------------------------------------------------------------------
        #Entrada 02 -------------------------------------------------------------
        label02 = tk.Label(frame01, text='prolongued_decelerations')
        label02.grid(row=1, column=2)
        entry02 = tk.Entry(frame01)
        entry02.grid(row=2, column=2)
        #------------------------------------------------------------------------
        #Entrada 03 -------------------------------------------------------------
        label03 = tk.Label(frame01, text='accelerations')
        label03.grid(row=3, column=1)
        entry03 = tk.Entry(frame01)
        entry03.grid(row=4, column=1)
        #------------------------------------------------------------------------
        #Entrada 04 -------------------------------------------------------------
        label04 = tk.Label(frame01, text='histogram_mode')
        label04.grid(row=3, column=2)
        entry04 = tk.Entry(frame01)
        entry04.grid(row=4, column=2)
        #------------------------------------------------------------------------
        #Entrada 05 -------------------------------------------------------------
        label05 = tk.Label(frame01, text='histogram_mean')
        label05.grid(row=5, column=1)
        entry05 = tk.Entry(frame01)
        entry05.grid(row=6, column=1)
        #------------------------------------------------------------------------
        #Entrada 06 -------------------------------------------------------------
        label06 = tk.Label(frame01, text='histogram_median')
        label06.grid(row=5, column=2)
        entry06 = tk.Entry(frame01)
        entry06.grid(row=6, column=2)
        #------------------------------------------------------------------------
        #Entrada 07 -------------------------------------------------------------
        label07 = tk.Label(frame01, text='mean_value_of_long_term_variability')
        label07.grid(row=7, column=1)
        entry07 = tk.Entry(frame01)
        entry07.grid(row=8, column=1)
        #------------------------------------------------------------------------
        #Entrada 08 -------------------------------------------------------------
        label08 = tk.Label(frame01, text='percentage_of_time_with_abnormal_long_term_variability')
        label08.grid(row=7, column=2)
        entry08 = tk.Entry(frame01)
        entry08.grid(row=8, column=2)
        #------------------------------------------------------------------------
        #Entrada 09 -------------------------------------------------------------
        label09 = tk.Label(frame01, text='histogram_variance')
        label09.grid(row=9, column=1)
        entry09 = tk.Entry(frame01)
        entry09.grid(row=10, column=1)
        #------------------------------------------------------------------------
        #Entrada 10 -------------------------------------------------------------
        label10 = tk.Label(frame01, text='histogram_tendency')
        label10.grid(row=9, column=2)
        entry10 = tk.Entry(frame01)
        entry10.grid(row=10, column=2)
        #------------------------------------------------------------------------
        #Entrada 11 -------------------------------------------------------------
        label11 = tk.Label(frame01, text='light_decelerations')
        label11.grid(row=11, column=1)
        entry11 = tk.Entry(frame01)
        entry11.grid(row=12, column=1)
        #------------------------------------------------------------------------
        
        frame02 = tk.LabelFrame(root, text='Resultado', padx=10, pady=10, width=500)
        frame02.pack(fill=tk.BOTH)

        frame03 = tk.Frame(frame02)
        frame03.pack(side=tk.LEFT)

        label12 = tk.Label(frame03, text='Classe: ')
        label12.grid(row=1, column=1)
        
        label13 = tk.Label(frame03, text='Probabilidade: ')
        label13.grid(row=2, column=1)
        
        button01 = tk.Button(frame02, text='Classificar', command=classifica, height=5, padx=16)
        button01.pack(side=tk.RIGHT)

        print('App aberto com sucesso!')

        root.resizable(width=False, height=False)
        root.mainloop()

    except:
        print('Falha ao abrir o app...')


if __name__ == '__main__':
    try:
        arquivo = open('modelo.pk', 'rb')
        modelo = pickle.load(arquivo)
        print('Modelo carregado com sucesso!')
    except:
        print('Falha ao carregar o modelo de aprendizado de máquina...')

    app(modelo)