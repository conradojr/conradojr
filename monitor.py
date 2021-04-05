import schedule
import time
import speedtest
from datetime import datetime
import pandas as pd
import numpy as np
from threading import Timer

def internet()
	df = pd.read_excel('dados.xlsx', sheet_name='base')
	s = speedtest.Speedtest()
	data_atual = datetime.now().strftime('%d/%m/%Y')
	hora_atual = datetime.now().strftime('%H:%M')
	velocidade_download = s.download(threads=None)*(10**-6)
	velocidade_upload = s.upload(threads=None)*(10**-6)
	df.loc[len(df)] = [data_atual, hora_atual, velocidade_download, velocidade_upload]
	df.to_excel('dados.xlsx'), sheet_name='base', index=False)
	Timer(1800, internet).start()

internet()
