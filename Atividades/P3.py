velocidade = 61 #Veclodidade do carro
local_carro = 90 #Local onde esta o carro

RADAR_1 = 60 #Velocidade permitida do radar
LOCAL_1 = 100 #Local onde esta o radar
RADAR_RANGE = 1 #Range onde o radar pega a velocidade permitida

#Aqui é feita uma variavel onde é pego o local onde o carro esta e verifica se é maior/menor/igual ao local onde esta o radar +/- o Range  
carrol_multado = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

#Primeira verificação se a velocidade do carro esta acima do permitido pelo radar
if velocidade > RADAR_1:
    print('Velocidade acima do radar')

#Segunda verificação se esta dentro do range do radar e se esta acima da velocidade no range do radar
if carrol_multado and velocidade > RADAR_1:
    print('Carro multado')
