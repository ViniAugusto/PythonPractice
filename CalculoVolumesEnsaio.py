def testa_consistencia(vol_amostra, maior_vol_ac_prim, diferenca_ac_prim, maior_vol_ac_sec, diferenca_ac_sec):
    vp = maior_vol_ac_prim
    vs = maior_vol_ac_sec
    if 5 <= vol_amostra and vol_amostra <= 100 and 1 <= maior_vol_ac_prim and maior_vol_ac_prim <= 60 and 1.2 <= maior_vol_ac_sec and maior_vol_ac_sec <= 65:
        for i in range(1,9):
            vp = vp - diferenca_ac_prim
            if vp < 1:
                entradas_consistentes = False
                return(entradas_consistentes)
        for j in range(1,13):
            vs = vs - diferenca_ac_sec
            if vs < 1.2:
                entradas_consistentes = False
                return(entradas_consistentes)  
        entradas_consistentes = True
    else:
        entradas_consistentes = False  
    return(entradas_consistentes)

def faz_combinacoes(vol_amostra, maior_vol_ac_prim, diferenca_ac_prim, maior_vol_ac_sec, diferenca_ac_sec):
    lista_impressoes = []
    for i in range(1,9):
      for j in range(1,13):
        if i == 1 and j == 1:
           volume_necessario_pocinho = vol_amostra + determina_tampao(vol_amostra) + determina_vol_prim(maior_vol_ac_prim,diferenca_ac_prim,i) + determina_vol_sec(maior_vol_ac_sec,diferenca_ac_sec,j) + calcula_estabilizador(determina_vol_sec(maior_vol_ac_sec,diferenca_ac_sec,j)) 
        linha_impressa = f"({identifica_pocinho(i,j)}) Amostra: {vol_amostra:.01f} ul | Tampão: {determina_tampao(vol_amostra):.01f} ul | Anticorpo primário: {determina_vol_prim(maior_vol_ac_prim,diferenca_ac_prim,i):.01f} ul | Anticorpo secundário: {determina_vol_sec(maior_vol_ac_sec,diferenca_ac_sec,j):.01f} ul | Estabilizador: {calcula_estabilizador(determina_vol_sec(maior_vol_ac_sec,diferenca_ac_sec,j)):.01f} ul | Água: {calcula_agua(vol_amostra, determina_tampao(vol_amostra), determina_vol_prim(maior_vol_ac_prim,diferenca_ac_prim,i), determina_vol_sec(maior_vol_ac_sec,diferenca_ac_sec,j), calcula_estabilizador(determina_vol_sec(maior_vol_ac_sec,diferenca_ac_sec,j)), volume_necessario_pocinho):.01f} ul"
        lista_impressoes.append(linha_impressa)
        print(linha_impressa, end="\n") 
      print()
  
    return (lista_impressoes) 

def determina_vol_prim(maior_vol_ac_prim,diferenca_ac_prim,linha):
  if linha == 1:
    vol_ac_prim = maior_vol_ac_prim
  if linha == 2:
    vol_ac_prim = maior_vol_ac_prim-(diferenca_ac_prim)
  if linha == 3:
    vol_ac_prim = maior_vol_ac_prim-(2*diferenca_ac_prim)
  if linha == 4:
    vol_ac_prim = maior_vol_ac_prim-(3*diferenca_ac_prim)
  if linha == 5:
    vol_ac_prim = maior_vol_ac_prim-(4*diferenca_ac_prim)
  if linha == 6:
    vol_ac_prim = maior_vol_ac_prim-(5*diferenca_ac_prim)
  if linha == 7:
    vol_ac_prim = maior_vol_ac_prim-(6*diferenca_ac_prim)
  if linha == 8:
    vol_ac_prim = maior_vol_ac_prim-(7*diferenca_ac_prim)     
  return(vol_ac_prim)

def determina_vol_sec(maior_vol_ac_sec,diferenca_ac_sec,coluna):
  if coluna == 1:
    vol_ac_sec = maior_vol_ac_sec
  else:
    vol_ac_sec = maior_vol_ac_sec - ((coluna-1)*diferenca_ac_sec)   
  return(vol_ac_sec)

def determina_tampao(vol_amostra):
    if 5 <= vol_amostra <= 10:
       vol_tampao = 1
    elif 10 < vol_amostra <= 40:
     vol_tampao = 1.5
    elif 40 < vol_amostra <= 75:
      vol_tampao = 2
    elif 75 < vol_amostra <= 100:
      vol_tampao = 2.5         
    return(vol_tampao)

def calcula_estabilizador(vol_ac_sec):
    if vol_ac_sec <= 3:
      vol_estab = 0.7 
    else: vol_estab = 0.23*vol_ac_sec
    return(vol_estab)

def calcula_agua(vol_amostra, vol_tampao, vol_ac_prim, vol_ac_sec, vol_estab, volume_necessario_pocinho):
    vt = vol_amostra + vol_tampao + vol_ac_prim + vol_ac_sec + vol_estab
    vol_agua = -vt + volume_necessario_pocinho
    return(vol_agua)

def identifica_pocinho(linha, coluna):
    if linha == 1:
      letra = "A"
    if linha == 2:
      letra = "B"
    if linha == 3:
      letra = "C"
    if linha == 4:
      letra = "D"
    if linha == 5:
      letra = "E"
    if linha == 6:
      letra = "F"
    if linha == 7:
      letra = "G"
    if linha == 8:
      letra = "H" 
    identifica_pocinho = letra + str(coluna)        
    return(identifica_pocinho)


def main():
    vol_amostra = float(input("Insira o volume de amostra, em microlitros, a ser inserido em cada poço: "))

    maior_vol_ac_prim = float(input("Insira o maior volume de anticorpo primário (quantidade a ser adicionada nos poços da linha A): "))
    diferenca_ac_prim = float(input("Insira a diferença do volume de anticorpo primário entre poços de uma linha e os da linha seguinte: "))
    
    maior_vol_ac_sec = float(input("Insira o maior volume de anticorpo secundário (quantidade a ser adicionada nos poços da coluna 1): "))
    diferenca_ac_sec = float(input("Insira a diferença do volume de anticorpo secundário entre poços de uma coluna e os da coluna seguinte: "))

    entradas_consistentes = testa_consistencia(vol_amostra, maior_vol_ac_prim, diferenca_ac_prim, maior_vol_ac_sec, diferenca_ac_sec)
    if entradas_consistentes == True: 
        lista_impressoes = faz_combinacoes(vol_amostra, maior_vol_ac_prim, diferenca_ac_prim, maior_vol_ac_sec, diferenca_ac_sec)
    elif entradas_consistentes == False: 
        print("Detectou-se problema com as entradas. Verifique-as e execute o programa novamente.")

if __name__ == "__main__": 
    main()