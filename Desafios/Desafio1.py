velocidade = 61
local_carro = 90

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

if velocidade > RADAR_1:
    print('Velocidade acima do radar 1')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE):
    print('MULTADO')