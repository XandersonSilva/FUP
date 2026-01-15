dicis = []

compr = int(input())

def compararData(d):
    tm = len(d) - 1
    for z in range(tm):
        for n in range(tm):
            cmp_at = d[n]
            cmp_px = d[n+1]

            ano_at = d[n]['data']['ano']
            ano_px = d[n+1]['data']['ano']
            if ano_at > ano_px:
                d[n] = cmp_px
                d[n+1] = cmp_at

        for n in range(tm):
            cmp_at = d[n]
            cmp_px = d[n+1]

            ano_at = d[n]['data']['ano']
            ano_px = d[n+1]['data']['ano']
            if ano_at == ano_px:
                mes_at = d[n]['data']['mes']
                mes_px = d[n+1]['data']['mes']
                if mes_at > mes_px:
                    d[n] = cmp_px
                    d[n+1] = cmp_at
        
        for n in range(tm):
            cmp_at = d[n]
            cmp_px = d[n+1]

            mes_at = d[n]['data']['mes']
            mes_px = d[n+1]['data']['mes']
            if mes_at == mes_px:
                dia_at = d[n]['data']['dia'] 
                dia_px = d[n+1]['data']['dia']

                if dia_at > dia_px:
                    d[n] = cmp_px
                    d[n+1] = cmp_at
    return d


def compararHora(d):
    tm = len(d) - 1
    for _ in range(tm):
        for n in range(tm):
            cmp_at = d[n]
            cmp_px = d[n+1]

            dcmp_at = d[n]['data']
            dcmp_px = d[n+1]['data']

            if dcmp_at == dcmp_px:
                hrr_at = d[n]['horario']
                hrr_px = d[n+1]['horario']

                if (hrr_at['hora'] == hrr_px['hora'] and 
                    hrr_at['minuto'] == hrr_px['minuto'] and
                    hrr_at['segundo'] > hrr_px['segundo']
                    ):
                    d[n] = cmp_px
                    d[n+1] = cmp_at

            if dcmp_at == dcmp_px:
                hrr_at = d[n]['horario']
                hrr_px = d[n+1]['horario']

                if (hrr_at['hora'] == hrr_px['hora'] and 
                    hrr_at['minuto'] > hrr_px['minuto']
                    ):
                    d[n] = cmp_px
                    d[n+1] = cmp_at

            if dcmp_at == dcmp_px:
                hrr_at = d[n]['horario']
                hrr_px = d[n+1]['horario']

                if (hrr_at['hora'] > hrr_px['hora']):
                    d[n] = cmp_px
                    d[n+1] = cmp_at
    return d
        
                          


for c in range(compr):
    dia = int(input("Dia: "))
    mes = int(input("Mes: "))
    ano = int(input("Ano: "))
    hora = int(input("Hora: "))
    minuto = int(input("Minuto: "))
    segundo = int(input("Segundo: "))
    descricao = input("Descricao: ")

    dicis.append({'data': {'dia': dia, 'mes': mes, 'ano': ano}, 'horario': {'hora': hora, 'minuto': minuto, 'segundo': segundo}, 'descricao': descricao})


ord_comp = compararHora(compararData(dicis))

for _ in range(compr):
    print(ord_comp[_])







