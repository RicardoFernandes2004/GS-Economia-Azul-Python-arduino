import serial
import time
import pandas as pd
import os
from log import *

class Reader:
    def startRead():
        # Configura a conexão serial 
        ser = serial.Serial('COM5', 9600, timeout=1)

        time.sleep(2)  # Aguarda a conexão ser estabelecida

        # Função para armazenar dados de níveis de petróleo em CSV
        def store_nivel_data(nivel_petroleo, timestamp):
            data = {
                'timestamp': [timestamp],
                'nivel_petroleo': [nivel_petroleo]
            }
            # Converter o dicionário em um DataFrame do pandas
            df = pd.DataFrame(data)
            # Verificar se o arquivo já existe
            file_exists = os.path.isfile('nivel_petroleo.csv')
            
            if not file_exists or os.path.getsize('nivel_petroleo.csv') == 0:
                df.to_csv('nivel_petroleo.csv', mode='a', header=True, index=False)
            else:
                df.to_csv('nivel_petroleo.csv', mode='a', header=False, index=False)
        # Loop de monitoramento
        contador_leitura = 0
        while contador_leitura <= 100:
            if ser.in_waiting > 0: # Verifica se tem dados na serial
                try:
                    # Converte o valor lido para um inteiro e obtém o timestamp atual.
                    raw_data = ser.readline().decode('utf-8').rstrip()
                    nivel_petroleo = int(raw_data)
                    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
                    
                    store_nivel_data(nivel_petroleo, timestamp)
                    
                    print(f"Nível de petróleo: {nivel_petroleo}% - Timestamp: {timestamp}")
                    if nivel_petroleo > 50 and nivel_petroleo <= 70:
                        print("Nível de petróleo acima de 50%! Acione a empresa responsavel!")
                    elif nivel_petroleo > 80:
                        print("Nivel de petróleo acima de 80%! Contate as autoridades!")
                    contador_leitura += 1
                        
                except Exception as e:
                    print(f'Erro ao ler os dados: {e}')
            
            time.sleep(1)
        Log.logger(timestamp)
        

