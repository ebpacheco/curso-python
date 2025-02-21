""""
CONSTANTE = "Variaveis" que nao vao mudar
Muitas condicoes no mesmo if (ruim)
    <- Contagem de complixidade (ruim)
"""
velocidade = 61 # velocidade atual do carro
local_carro = 100   #local em que o carro esta na estrada

RADAR_1 = 60 # velocidade maxima do radar 1
LOCAL_1 = 100   # local onde o radar 1 esta
RADAR_RANGE = 1 # a distancia onde o radar pega

vel_carro_passou_radar = velocidade > RADAR_1
carro_multado_radar = local_carro >= (LOCAL_1 - RADAR_RANGE ) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)

if vel_carro_passou_radar:
    print('Passou da velocidade')
    
if  carro_multado_radar and velocidade > RADAR_1:
    print('Carro multado em radar 1')
