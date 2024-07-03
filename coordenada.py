import pyautogui
import pandas
import time
pyautogui.pause = 1
pyautogui.click(x=605, y=1058)
pyautogui.click(x=770, y=846)

tabela = pandas.read_csv('Escritorio/teste1.csv')
print(tabela)


for linha in tabela.index:
    codigo = str(tabela.loc[linha, "nome"])
    # Nome da pessoa
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # Nis da pessoa
    pyautogui.write(str(tabela.loc[linha, "nis"]))
    pyautogui.press("tab")
    # 0 Sexo
    pyautogui.press("down")
    pyautogui.press("tab")
    pyautogui.press("tab")
    # 1 Idade
    pyautogui.press("down")
    pyautogui.press("tab")
    pyautogui.press("tab")
    # 2 Resposavel com deficiencia?
    pyautogui.press("space")
    pyautogui.press("tab")
    pyautogui.press("tab")
    # 3 Ocupação do Responsável
    pyautogui.press("up")
    pyautogui.press("up")
    pyautogui.press("tab")
    pyautogui.press("tab")
    # 4 Grau de Escola
    pyautogui.press("down")
    pyautogui.press("down")
    pyautogui.press("tab")
    pyautogui.press("tab")
    # 5 Renda
    pyautogui.press("space")
    pyautogui.press("tab")
    pyautogui.press("tab")
    # 6 Numero de Membros
    pyautogui.press("space")
    pyautogui.press("tab")
    pyautogui.press("tab")
    # 7 Algum membro com deficiencia?
    pyautogui.press("down")
    pyautogui.press("tab")
    pyautogui.press("tab")
    # 8 Tipo de deficiencia
    pyautogui.press("space")
    pyautogui.press("tab")
    pyautogui.press("tab")
    # 9 quantos idosos acime de 60 anos
    pyautogui.press("up")
    pyautogui.press("tab")
    pyautogui.press("tab")
    # 10 Nivel de escolaridade dos membros
    pyautogui.press("down")
    pyautogui.press("down")
    pyautogui.press("tab")
    pyautogui.press("tab")
    # 11 renda familiar
    pyautogui.press("space")
    pyautogui.press("tab")
    pyautogui.press("tab")
    # 12 quanto membros tem renda
    pyautogui.press("space")
    pyautogui.press("tab")
    pyautogui.press("tab")
    # 13 quais beneficios?
    pyautogui.press("space")
    pyautogui.press("tab")
    pyautogui.press("tab")
    # 14 alguma atividade de renda extra?
    pyautogui.press("down")
    pyautogui.press("tab")
    pyautogui.press("tab")
    # 15 em qual area
    pyautogui.press("down")
    pyautogui.press("down")
    pyautogui.press("tab")
    pyautogui.press("tab")
    # 16 quais serviços publicos utilizam
    pyautogui.press("down")
    pyautogui.press("down")
    pyautogui.press("tab")
    pyautogui.press("tab")
    # 17 qual organização comunitaria usam?
    pyautogui.press("down")
    pyautogui.press("tab")
    pyautogui.press("tab")
    # 18 discurssões que poderiam ser feita
    pyautogui.press("space")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("space")
    pyautogui.click(x=791, y=275)
    time.sleep(3)
