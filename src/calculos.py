# calculos.py
import numpy as np

def calcula_fem(Ua, Ra, Ia):
    return Ua - (Ra * Ia)

def calcula_w_rads(velocidade_rpm):
    return velocidade_rpm * (2 * np.pi / 60)

def calcula_torque(fem, Ia, w):
    return (fem * Ia)/w

def calcula_fluxo_tensao(fem, Ke, w): 
    return fem/ (Ke * w)

def calcula_fluxo_torque(Te, Kt, Ia):
    return Te/(Kt * Ia)

def calcula_const_magnetica(fluxo, If):
    # O trabalho proposto adota a relação linear entre fluxo magnético e corrente de campo, 
    return fluxo/If

def calcula_corrente_campo(Ua, Rf, R_reostato):
    return Ua / (Rf + R_reostato)

def calcula_corrente_armadura(TL, Kt, fluxo):
    if fluxo == 0: return 0
    return TL / (Kt * fluxo)

def calcula_velocidade(fem, Ke, fluxo):
    if fluxo == 0 or Ke == 0:
        return 0, 0
    omega_rad_s = fem / (Ke * fluxo)
    velocidade_rpm = omega_rad_s * (60 / (2 * np.pi))
    return omega_rad_s, velocidade_rpm

def calcula_potencias(TL, w, Ua, Ia, If):
    P_mecanica = TL * w # Potência de saída ou potência mecânica disponível no eixo
    P_eletrica = Ua * (Ia + If) # Potência de entrada ou potência elétrica fornecida à máquina.
    rendimento = (P_mecanica/P_eletrica) * 100
    return P_mecanica, P_eletrica, rendimento

