import wikipedia
wikipedia.set_lang('es')

x = str(input('Que quieres buscar? '))

print(wikipedia.summary(x))