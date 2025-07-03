import requests
import PySimpleGUI as sg

def obter_taxas(moeda_base):
    url = f"https://open.er-api.com/v6/latest/{moeda_base}"
    try:
        resposta = requests.get(url)
        dados = resposta.json()
        if dados["result"] == "success":
            return dados["rates"]
        else:
            sg.popup_error("Erro na API:", dados.get("error-type", "Erro desconhecido"))
            return None
    except Exception as e:
        sg.popup_error("Erro de conexão com a API:", e)
        return None

def atualizar_moedas(taxas):
    moedas = sorted(taxas.keys())
    return moedas

def converter_moeda(taxas, destino, valor):
    try:
        taxa = taxas[destino]
        return valor * taxa
    except KeyError:
        sg.popup_error("Moeda de destino inválida.")
        return None

def main():
    sg.theme('DarkBlue3')

    moeda_base_inicial = "USD"
    taxas = obter_taxas(moeda_base_inicial)
    if not taxas:
        sg.popup_error("Não foi possível obter as taxas. Encerrando.")
        return

    moedas = atualizar_moedas(taxas)
    historico = []

    layout = [
        [sg.Text("Moeda Base:"), sg.Combo(moedas, default_value=moeda_base_inicial, key="-MOEDA_BASE-", readonly=True, size=(10,1)), 
         sg.Button("Atualizar Taxas")],
        [sg.Text("Moeda Destino:"), sg.Combo(moedas, key="-MOEDA_DESTINO-", readonly=True, size=(10,1))],
        [sg.Text("Valor:"), sg.Input(key="-VALOR-", size=(15,1))],
        [sg.Button("Converter"), sg.Button("Limpar")],
        [sg.Text("Resultado:", size=(40,1), key="-RESULTADO-")],
        [sg.Text("Histórico de Conversões:")],
        [sg.Table(values=[], headings=["Valor", "De", "Convertido", "Para"], 
                  key="-HISTORICO-", auto_size_columns=False,
                  col_widths=[10, 6, 12, 6], 
                  justification='center',
                  num_rows=10, enable_events=False)],
        [sg.Button("Sair")]
    ]

    window = sg.Window("Conversor de Moedas", layout, finalize=True)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Sair":
            break

        if event == "Atualizar Taxas":
            nova_base = values["-MOEDA_BASE-"]
            novas_taxas = obter_taxas(nova_base)
            if novas_taxas:
                taxas = novas_taxas
                moedas = atualizar_moedas(taxas)
                window["-MOEDA_BASE-"].update(value=nova_base, values=moedas)
                window["-MOEDA_DESTINO-"].update(values=moedas, value=moedas[0])
                sg.popup("Taxas atualizadas com sucesso!")
            else:
                sg.popup_error("Falha ao atualizar taxas.")

        if event == "Converter":
            moeda_base = values["-MOEDA_BASE-"]
            moeda_destino = values["-MOEDA_DESTINO-"]
            valor_str = values["-VALOR-"]

            if not moeda_destino:
                sg.popup_error("Selecione a moeda destino.")
                continue

            try:
                valor = float(valor_str)
            except ValueError:
                sg.popup_error("Digite um valor numérico válido.")
                continue

            convertido = converter_moeda(taxas, moeda_destino, valor)
            if convertido is not None:
                resultado_str = f"{valor:.2f} {moeda_base} = {convertido:.2f} {moeda_destino}"
                window["-RESULTADO-"].update(resultado_str)
                historico.append([f"{valor:.2f}", moeda_base, f"{convertido:.2f}", moeda_destino])
                window["-HISTORICO-"].update(values=historico)

        if event == "Limpar":
            window["-VALOR-"].update("")
            window["-RESULTADO-"].update("")

    window.close()

if __name__ == "__main__":
    main()
