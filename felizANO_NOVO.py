import datetime

def feliz_ano_novo():
    ano_atual = datetime.date.today().year
    data_ano_novo = datetime.date(ano_atual, 1, 1)
    return data_ano_novo.strftime('%d/%m/%Y' + ' - FELIZ ANO NOVO!')

print(feliz_ano_novo())