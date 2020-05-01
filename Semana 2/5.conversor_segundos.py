print('----- Conversor de Segundos -----')
segundos_str = input('Digite os segundos para conversão: ')

segundos = int(segundos_str)

dias = segundos // 86400
horas = (segundos % 86400) // 3600
minutos = (segundos % 3600) // 60 
segundos = segundos % 60

print(dias, 'dias,', horas, 'horas,', minutos, 'minutos e', segundos, 'segundos.')

