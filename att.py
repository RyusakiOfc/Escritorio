import pyautogui
import pandas as pd
import time

pyautogui.PAUSE = 0.5

pyautogui.click(x=605, y=1058)

tabela = pd.read_excel("Escritorio/aa.xlsx")
print(tabela)


for linha in tabela.index:
    pyautogui.click(x=770, y=846)
    codigo = str(tabela.loc[linha, "nome"])
    item1 = tabela.loc[linha, 'idade']
    item2 = tabela.loc[linha, 'resposavel com deficiencia']
    item3 = tabela.loc[linha, 'ocupacao do responsavel']
    item4 = tabela.loc[linha, 'grau de escola']
    item5 = tabela.loc[linha, 'renda']
    item6 = tabela.loc[linha, 'numero de membros']
    item7 = tabela.loc[linha, 'algum membro com deficiencia']
    item8 = tabela.loc[linha, 'tipo de deficiencia']
    item9 = tabela.loc[linha, 'quantos idosos acima de 60 anos']
    item10 = tabela.loc[linha, 'Nivel de escolaridade dos membros']
    item11 = tabela.loc[linha, 'renda familiar']
    item12 = tabela.loc[linha, 'quanto membros tem renda']
    item13 = tabela.loc[linha, 'quais beneficios']
    item14 = tabela.loc[linha, 'alguma atividade de renda extra']
    item15 = tabela.loc[linha, 'em qual area']
    item16 = tabela.loc[linha, 'quais servicos publicos utilizam']
    item17 = tabela.loc[linha, 'qual organizacao comunitaria usam']
    item18 = tabela.loc[linha, 'discurssoes que poderiam ser feita']

    # Nome da pessoa
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # Nis da pessoa
    pyautogui.write(str(tabela.loc[linha, "nis"]))
    pyautogui.press("tab")

    # 0 Sexo
    sexo = tabela.loc[linha, 'sexo']
    if sexo == 'm':
        pyautogui.press('space')
    elif sexo == 'h':
        pyautogui.press('down')
    pyautogui.press('tab', presses=2)

    # 1 Idade
    if 18 <= item1 < 31:
        pyautogui.press('space')
    elif 31 <= item1 < 41:
        pyautogui.press('down')
    elif 41 <= item1 < 51:
        pyautogui.press('down', presses=2)
    elif 51 <= item1 < 60:
        pyautogui.press('down', presses=3)
    elif 60 <= item1 < 70:
        pyautogui.press('down', presses=4)
    elif 70 <= item1 < 99:
        pyautogui.press('up')
    pyautogui.press('tab', presses=2)

    # 2 Resposavel com deficiencia?
    if item2 == 'n':
        pyautogui.press('space')
    elif item2 == 's':
        pyautogui.press('down', presses=3)
    pyautogui.press('tab', presses=2)
    # 3 Ocupação do Responsável
    pyautogui.press("up", presses=2)
    pyautogui.press('tab', presses=2)

    # 4 Grau de Escola
    if item4 == 'in':
        pyautogui.press('down')
    elif item4 == 'co':
        pyautogui.press('down', presses=2)
    elif item4 == 'ana':
        pyautogui.press('space')
    pyautogui.press('tab', presses=2)

    # 5 Renda
    if item5 == 'um':
        pyautogui.press('down')
    elif item5 == 'meio':
        pyautogui.press('space')
    pyautogui.press('tab', presses=2)

    # 6 Numero de Membros
    pyautogui.press('space')
    pyautogui.press('tab', presses=2)

    # 7 Algum membro com deficiencia?
    if item7 == 'n':
        pyautogui.press('down')
    elif item7 == 's':
        pyautogui.press('space')
    pyautogui.press('tab', presses=2)

    # 8 Tipo de deficiencia
    if item8 == 'n':
        pyautogui.press('space')
    elif item8 == 's':
        pyautogui.press('up', presses=2)
    pyautogui.press('tab', presses=2)

    # 9 quantos idosos acime de 60 anos
    if item9 == 'n':
        pyautogui.press('up')
    elif item9 == 's':
        pyautogui.press('space')
    pyautogui.press('tab', presses=2)

    # 10 Nivel de escolaridade dos membros
    if item10 == 'in':
        pyautogui.press('tab', presses=2)
        pyautogui.press('space')
        pyautogui.press('tab', presses=11)
    elif item10 == 'co':
        pyautogui.press('tab', presses=3)
        pyautogui.press('space')
        pyautogui.press('tab', presses=10)
    elif item10 == 'ana':
        pyautogui.press('tab', presses=12)
        pyautogui.press('space')
        pyautogui.press('tab')
    elif item10 == 'in e ana':
        pyautogui.press('tab', presses=2)
        pyautogui.press('space')
        pyautogui.press('tab', presses=10)
        pyautogui.press('space')
        pyautogui.press('tab')

    # 11 renda familiar
    if item11 == 'um':
        pyautogui.press('down')
    elif item11 == 'meio':
        pyautogui.press('space')
    pyautogui.press('tab', presses=2)

    # 12 quanto membros tem renda
    pyautogui.press('space')
    pyautogui.press('tab', presses=2)

    # 13 quais beneficios?
    if item13 == 'aux':
        pyautogui.press('tab', presses=2)
        pyautogui.press('space')
        pyautogui.press('tab', presses=4)
    elif item13 == 'bo':
        pyautogui.press('space')
        pyautogui.press('tab', presses=6)
    elif item13 == 'bpc':
        pyautogui.press('tab')
        pyautogui.press('space')
        pyautogui.press('tab', presses=5)

    # 14 alguma atividade de renda extra?
    if item14 == 'n':
        pyautogui.press('down')
    elif item14 == 's':
        pyautogui.press('space')
    pyautogui.press('tab', presses=2)

    # 15 em qual area
    if item15 == 'art':
        pyautogui.press('tab', presses=2)
        pyautogui.press('space')
        pyautogui.press('tab', presses=7)

    elif item15 == 'na':
        pyautogui.press('tab', presses=7)
        pyautogui.press('space')
        pyautogui.press('tab', presses=2)

    # 16 quais serviços publicos utilizam
    pyautogui.press('space')
    pyautogui.press('tab', presses=8)

    # 17 qual organização comunitaria usam?
    if item17 == "re":
        pyautogui.press('tab')
        pyautogui.press('space')
        pyautogui.press('tab', presses=6)
    elif item17 == "na":
        pyautogui.press('space')
        pyautogui.press('tab', presses=7)

    # 18 discurssões que poderiam ser feita
    if item18 == 'sa or':
        pyautogui.press('space')
        pyautogui.press('tab', presses=4)
        pyautogui.press('space')
        pyautogui.press('tab', presses=8)
    elif item18 == 'or se':
        pyautogui.press('tab', presses=3)
        pyautogui.press('space')
        pyautogui.press('tab')
        pyautogui.press('space')
        pyautogui.press('tab', presses=8)
    elif item18 == 'sa se':
        pyautogui.press('space')
        pyautogui.press('tab', presses=3)
        pyautogui.press('space')
        pyautogui.press('tab', presses=9)
    pyautogui.press("space")
    time.sleep(2)
    pyautogui.click(x=754, y=337)
    pyautogui.click(x=754, y=337)
    time.sleep(2)
