import pyperclip



text = pyperclip.paste()
lines = text.split('#')
for i in range(len(lines)):
    lines[i] = '* '+lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)
# 'Canelo#Galletitas#Chumbolita#Piloncita#Cafecita#Vaquita#Mochi#Atole'