import numpy as np
from typing import Tuple

class MotorCCShunt:
    """
    Classe para representar um motor CC Shunt.

    # Parâmetros Padrão:

        * Tensão de armadura nominal:           $240 V $
        * Corrente nominal de armadura:         $10 A $
        * Resistência de armadura (Ra):         $2 \Omega$ 
        * Resistência de campo (Rf ):           $120 \Omega $ 
        * Reostato de campo:                    $0 a 100 \Omega $ 
        * Constantes eletromecânicas (Ke, Kt):  $0.8 $
        * Momento de inércia total:             $0.02 kg \cdot m^2$
        * Velocidade nominal:                   $1800 rpm $ 
        * Potência nominal:                     $2,5 kW $
        * Rendimento:                           $85\% $
        * Torque de carga:                      $entre 8 e 15 N\cdot m $
    """

    dados: dict = {}
    """Dicionário com todos os dados do Motor CC Shunt"""

    def __init__(self, dados):
        print(f"Objeto {self.__class__.__name__} criado...")
        
        self.dados = dados
        print("Dados:\n", "\t", dados)

    def curva_tensao_velocidade(self):
        """Recebe limites de tensão e velocidade e retorna os vetores de Tensão e Velocidade""" 


    def calcular_tensao_velocidade(self, a, b) -> Tuple[int, int]:
        return 10*a, 20*b
