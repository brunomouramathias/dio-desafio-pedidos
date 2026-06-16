import sys

def agrupar_pedidos():
    # Lê o número de pedidos utilizando sys.stdin.readline conforme a recomendação técnica
    linha_n = sys.stdin.readline().strip()
    if not linha_n:
        return
    N = int(linha_n)
    
    # Dicionário para armazenar totais por tipo de embalagem
    totais = {}
    
    # Processa cada pedido
    for _ in range(N):
        linha = sys.stdin.readline().strip()
        if not linha:
            continue
            
        cliente, embalagem, quantidade = linha.split(", ")
        quantidade = float(quantidade)
        
        # Lógica implementada: Soma a quantidade ao tipo de embalagem correspondente
        totais[embalagem] = totais.get(embalagem, 0) + quantidade
    
    # Imprime o resultado no formato solicitado, mantendo a ordem exata via STDOUT (print)
    for tipo in ["saco", "papelao ondulado", "papel kraft"]:
        print(f"{tipo}: {int(totais[tipo]) if tipo in totais and totais[tipo].is_integer() else totais.get(tipo, 0)}")

if __name__ == "__main__":
    agrupar_pedidos()
