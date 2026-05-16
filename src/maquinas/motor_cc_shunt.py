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

    def __init__(self, dados: Dict, verboso: bool = False):
        print(f"Objeto {self.__class__.__name__} criado...")
        if verboso:
            for chave, valor in dados.items():
                print(f"\t {chave:10} = {valor}")

        self.transforma_dados(dados)

    def transforma_dados(self, dados: Dict) -> None:
        """
        Recebe dicionário com dados de entrada e transforma em valores adequados para cálculos
        """
        self.ua            = float(dados['Uan'])
        # self.ia            = float(dados['Ian'])
        self.ia            = 10.2549
        self.ra            = float(dados['Ra'])
        self.rf            = float(dados['Rf'])
        self.r_reos        = 0 # float(dados['Rreos'])
        self.ke            = float(dados['Ke'])
        self.kt            = float(dados['Kt'])
        self.iner          = float(dados['J'])
        self.rpm           = float(dados['RPM'])
        self.pn            = float(dados['Pn']) * 1000
        self.n             = float(dados['n'])
        self.torque_carga  = 0 # float(dados['T_L'])
    
    def calcula_fem(self) -> float:
        return self.ua - (self.ra * self.ia)

    def calcula_w_rads(self) -> float:
        return self.rpm * (2 * np.pi / 60)

    def calcula_torque(self) -> float:
        return self.pn / self.calcula_w_rads()
        
    def calcula_corrente_campo(self) -> float:
        return self.ua / (self.rf + self.r_reos)

    def calcula_fluxo_tensao(self) -> float: 
        return self.calcula_fem() / (self.ke * self.calcula_w_rads())

    def calcula_torque_fluxo(self) -> float:
        return self.kt * self.calcula_fluxo_tensao() * self.ia

    def calcula_fluxo_torque(self) -> float:
       return self.calcula_torque() / (self.kt * self.ia)

    def calcula_const_magnetica(self) -> float:
        # O trabalho proposto adota a relação linear entre fluxo magnético e corrente de campo, 
        # if self.calcula_fluxo_tensao() == self.calcula_fluxo_torque():
        return self.calcula_fluxo_tensao() / self.calcula_corrente_campo()

    def calcula_corrente_armadura(self) -> float:
        if self.calcula_fluxo_tensao == 0: return 0
        if self.torque_carga == 0:
            self.torque_carga = self.calcula_torque_fluxo()
        return self.torque_carga / (self.kt * self.calcula_fluxo_tensao())

    def calcula_velocidade(self) -> float:
        if self.calcula_fluxo_tensao() == 0 or self.ke == 0:
            return 0, 0
        return self.calcula_fem() / (self.ke * self.calcula_fluxo_tensao())

    def calcula_potencias(self) -> Tuple[float, float, float]:
        if self.torque_carga == 0:
            self.torque_carga = self.calcula_torque_fluxo()
        p_mecanica = self.torque_carga * self.calcula_w_rads() # Potência de saída ou potência mecânica disponível no eixo
        p_eletrica = self.ua * (self.ia + self.calcula_corrente_campo()) # Potência de entrada ou potência elétrica fornecida à máquina.
        rendimento = (p_mecanica/p_eletrica) * 100
        return p_mecanica, p_eletrica, rendimento
    
    def calcular_resultados(self) -> Dict:
        """
        Chama todas as funções de cálculo e atribui resultados à um dicionário
        """
        resultados = {}

        resultados["fem"]               = self.calcula_fem()
        resultados["w_rads"]            = self.calcula_w_rads()
        resultados["torque"]            = self.calcula_torque()
        resultados["fluxo_tensao"]      = self.calcula_fluxo_tensao()
        resultados["fluxo_torque"]      = self.calcula_fluxo_torque()
        resultados["const_magnetica"]   = self.calcula_const_magnetica()
        resultados["corrente_campo"]    = self.calcula_corrente_campo()
        resultados["corrente_armadura"] = self.calcula_corrente_armadura() 
        resultados["velocidade"]        = self.calcula_velocidade()
        resultados["potencia_mecânica"] = self.calcula_potencias()[0]
        resultados["potencia_elétrica"] = self.calcula_potencias()[1]
        resultados["rendimento"]        = self.calcula_potencias()[2]

        return resultados

    def mostrar_resultados(self) -> None:
        """
        Mostra os parâmetros e os resultados resultados
        """
        print("====="*5, "Parâmetros", "====="*5)
        print(f"Uan   = {self.ua:20}")
        print(f"Ian   = {self.ia:20}")
        print(f"Ra    = {self.ra:20}")
        print(f"Rf    = {self.rf:20}")
        print(f"Rreos = {self.r_reos:20}")
        print(f"Ke    = {self.ke:20}")
        print(f"Kt    = {self.kt:20}")
        print(f"J     = {self.iner:20}")
        print(f"RPM   = {self.rpm:20}")
        print(f"Pn    = {self.pn:20}")
        print(f"n     = {self.n:20}")
        print(f"T_L   = {self.torque_carga:20}",   )
        
        print(f"====="*5, "Resultados", "====="*5)
        resultados = self.calcular_resultados()
        for chave, valor in resultados.items():
            print(f"{chave:20} = {valor:.4f}")



