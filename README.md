## Trabalho de Máquinas 2: Simulação de um motor CC shunt e análise de comportamento em regime permanente

O presente trabalho contempla:
* a leitura e manipulação de dados de um arquivo externo;
* cálculos em regime permanente;
* gráficos de velocidade, torque e potência.

### Codagem colaborativa via Github

#### Setup Inicial: ambiente virtual Python + Jupyter Notebook no VSCode
_Instruções por: https://github.com/pesadaum_

1. Instalar o ambiente virtual python (`sudo apt update && sudo apt install python3-venv`)
2. Criar um ambiente virtual no terminal Linux: `python3 -m venv <nome do ambiente>` 
    1. Exemplo: `python3 -m venv virtualenv` 
3. Ativar o ambiente virtual: `source virtualenv/bin/activate`
4. Agora com o ambiente ativo, é possível instalar os pacotes com pip: `pip install matplotlib numpy <...>`
5. Pra rodar o Jupyter, é necessário o ipykernel: `pip install ipykernel`
Extensão Jupyter → https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter

Com o Kernel instalado, agora basta selecionar no VSCode o Kernel em questão:

1. Ctrl+Shift+P
2. Procurar por “Notebook: Select notebook kernel”
3. Usar o `virtualenv` criado
    1. Se não aparecer, escolher “Select Another Kernel” → Python Environments → Virtualenv com o Python em questão

Com isso já deve ser possível rodar o Python + Jupyter localmente com o WSL e o VSCode.

1. Quando usar o Git+Github, criar imediatamente um arquivo `.gitignore` com o nome do ambiente virtual. Essa pasta não deve ser commitada!
    1. também adicionar uma linha com `**/__pycache__` 
    2. também adicionar uma linha com `<nome do virtualenv>` 
2. Congelar as versões dos pacotes instalados no virtualenv:
    1. Criar lista:`pip freeze > requirements.txt`
    2. Instalar a partir da lista já criada: `pip install -r requirements.txt`
