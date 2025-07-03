# Conversor de Moedas com Interface Gráfica (PySimpleGUI)

Este projeto é um conversor de moedas simples, que utiliza a API pública [ExchangeRate-API](https://open.er-api.com) para obter taxas de câmbio atualizadas em tempo real, e uma interface gráfica amigável construída com [PySimpleGUI](https://pysimplegui.readthedocs.io/).

---

## Funcionalidades

- Seleção da moeda base e moeda destino via menus suspensos (combo boxes)
- Entrada de valor a ser convertido com validação
- Conversão instantânea e exibição do resultado na interface
- Atualização das taxas de câmbio a qualquer momento
- Histórico das conversões realizadas durante a sessão exibido em tabela
- Interface intuitiva e leve, baseada em PySimpleGUI
- Tratamento de erros com mensagens claras para o usuário

---

## Requisitos

- Python 3.x
- Biblioteca `requests`
- Biblioteca `PySimpleGUI`

Para instalar as bibliotecas necessárias, execute:

```bash
pip install requests
pip install PySimpleGUI


Como usar
1. Baixe o arquivo conversor_gui.py com o código do projeto.

2. Execute o programa via terminal:
python conversor_gui.py

3. Na janela do programa:

Escolha a moeda base (padrão USD).

Clique em "Atualizar Taxas" para garantir que as últimas cotações estejam carregadas.

Selecione a moeda destino.

Digite o valor a ser convertido.

Clique em "Converter" para ver o resultado.

O histórico das conversões fica listado na tabela.

Clique em "Limpar" para limpar o campo de valor e resultado.

Clique em "Sair" para fechar o programa.



