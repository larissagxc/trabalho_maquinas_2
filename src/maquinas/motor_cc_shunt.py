import numpy as np
from typing import Tuple, Dict

class MotorCCShunt:
    """
    Classe para representar um motor CC Shunt.
    """

    ua = 0 
    "Tensão de armadura nominal:           $240 V $"
    ia = 0 
    "Corrente nominal de armadura:         $10 A $"
    ra = 0
    "Resistência de armadura (Ra):         $2 \Omega$ "
    rf = 0
    "Resistência de campo (Rf ):           $120 \Omega $ "
    r_reos = 0
    "Reostato de campo:                    $0 a 100 \Omega $"
    ke = 0
    "Constantes eletromecânica (Ke):       $0.8 $"
    kt = 0
    "Constantes eletromecânica (Kt):       $0.8 $"
    iner = 0
    "Momento de inércia total:             $0.02 kg \cdot m^2$"
    rpm = 0
    "Velocidade nominal:                   $1800 rpm $ "
    pn = 0
    "Potência nominal:                     $2,5 kW $"
    n = 0
    "Rendimento:                           $85\% $"
    torque_carga = 0
    "Torque de carga:                      $entre 8 e 15 N\cdot m $"

    def __init__(self, dados):
        print(f"Objeto {self.__class__.__name__} criado... Parâmetros:")
        for chave, valor in dados.items():
            print(f"\t {chave} : \t {valor}")
        self.transforma_dados(dados)

    def transforma_dados(self, dados: Dict) -> None:
        """
        Recebe dicionário com dados de entrada e transforma em valores adequados para cálculos
        """
        self.ua            = float(dados['Uan'])
        self.ia            = float(dados['Ian'])
        self.ra            = float(dados['Ra'])
        self.rf            = float(dados['Rf'])
        self.r_reos        = 0 # float(dados['Rreos'])
        self.ke            = float(dados['Ke'])
        self.kt            = float(dados['Kt'])
        self.iner          = float(dados['J'])
        self.rpm           = float(dados['RPM'])
        self.pn            = float(dados['Pn'])
        self.n             = float(dados['n'])
        self.torque_carga  = 0 # float(dados['T_L'])
    
    def calcula_fem(self) -> float:
        return self.ua - (self.ra * self.ia)

    def calcula_w_rads(self) -> float:
        return self.rpm * (2 * np.pi / 60)

    def calcula_torque(self) -> float:
        return (self.calcula_fem() * self.ia) / self.calcula_w_rads()
        
    def calcula_corrente_campo(self) -> float:
        return self.ua / (self.rf + self.r_reos)

    def calcula_fluxo_tensao(self) -> float: 
        return self.calcula_fem() / (self.ke * self.calcula_w_rads())

    def calcula_fluxo_torque(self) -> float:
        return self.calcula_torque() / (self.kt * self.ia)

    def calcula_const_magnetica(self) -> float:
        # O trabalho proposto adota a relação linear entre fluxo magnético e corrente de campo, 
        # if self.calcula_fluxo_tensao() == self.calcula_fluxo_torque():
        return self.calcula_fluxo_tensao() / self.calcula_corrente_campo()

    def calcula_corrente_armadura(self) -> float:
        if self.calcula_fluxo_tensao == 0: return 0
        if self.torque_carga == 0:
            self.torque_carga == self.calcula_torque()
        return self.torque_carga / (self.kt * self.calcula_fluxo_tensao())

    # def calcula_velocidade(self) -> Tuple[float, float]:
    #     if self.calcula_fluxo_tensao() == 0 or self.ke == 0:
    #         return 0, 0
    #     omega_rad_s = fem / (Ke * fluxo)
    #     return omega_rad_s, velocidade_rpm

    # def calcula_potencias(self) -> Tuple[float, float, float]:
    #     p_mecanica = self.tl * w # Potência de saída ou potência mecânica disponível no eixo
    #     p_eletrica = self.ua * (self.ia + If) # Potência de entrada ou potência elétrica fornecida à máquina.
    #     rendimento = (p_mecanica/p_eletrica) * 100
    #     return p_mecanica, p_eletrica, rendimento

