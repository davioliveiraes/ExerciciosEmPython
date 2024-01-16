import datetime

def feliz_natal():
    ano_atual = datetime.date.today().year
    dia_natal = datetime.date(ano_atual, 12, 25)
    return f'{dia_natal.day}/{dia_natal.month}/{dia_natal.year} - FELIZ NATAL!'


print(feliz_natal())
