''' - Escreva um programa que leia um arquivo `texto12.txt` e conte quantas vezes cada palavra
aparece no arquivo.
 - Exiba as palavras e suas contagens no console.'''
 
with open('arquivos criados/texto12.txt', 'w') as arquivo:
    arquivo.write('o futebol, mais do que um esporte, é uma paixão que une milhões de pessoas ao redor do mundo. No Brasil, essa paixão é ainda mais intensa, transformando o esporte em parte da nossa cultura e identidade. Desde os campos de várzea até os grandes estádios, o futebol é sinônimo de alegria, emoção e união. A cada jogo, a torcida vibra a cada gol, sofre com cada derrota e celebra os títulos com grande entusiasmo. A bola rolando é capaz de gerar momentos inesquecíveis e marcar gerações.')
    

with open('arquivos criados/texto12.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    conteudo = conteudo.replace(',','')
    palavras = conteudo.split()
    contagem = []
    dicio = {}
    for i, palavra in enumerate(palavras):
        contagem.append(palavras.count(palavra))
        dicio[palavra] = contagem[i]
        
    for c, v in dicio.items():
        print(f'A palavra: ({c}) apareceu {v} vez(es) no texto.')
        




