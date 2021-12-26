
from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()

porco1 = [1, 1, 0]
porco2 = [1, 1, 0]
porco3 = [1, 1, 0]
cachorro1 = [1, 1, 1]
cachorro2 = [0, 1, 1]
cachorro3 = [0, 1, 1]

dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
#gordinho/perna curta/auau
# 1: PORCO
# -1: CACHORRO 

marcacoes = [1, 1, 1, -1, -1, -1]

misterioso1 = [1, 1, 1] #CACHORRO
misterioso2 = [1, 0, 0] #PORCO
misterioso3 = [0, 0, 1] #CACHORRO

testes = [misterioso1, misterioso2, misterioso3]

modelo.fit(dados, marcacoes) #Adequando o modelo aos meus dados
resultado = modelo.predict(testes)

print(resultado)

#Criando uma marcamção de teste para os elementos misteriosos utilziando o array "marcacoes_teste" indicando o que é
#cada elemento misterioso

marcacoes_teste = [-1, 1, -1] #CACHORRO, PORCO, CACHORRO

#Calculando a diferença entre as variaveis "resultado" e as "marcacoes_teste" e atribuindo uma variavel
#chamada diferenças
diferencas = resultado - marcacoes_teste
print(f"Diferenças: {diferencas}")

#Percorrendo o array "diferenças" e devolvendo todos os seus elementos que forem iguais a 0 e atribuindo
#a uma variavel chamada "acertos"

acertos = [d for d in diferencas if d==0]
print(f"Acertos: {acertos}")

#Calculando o total de acertos pegando o tamanho do array "acertos" com o método len() e atribuindo
#uma variável "total_de_acertos"
total_de_acertos = len(acertos)
print(f"Total de acertos: {total_de_acertos}")

#Calculando o total de elementos pegando o tamanho do array "teste" com o método len() e atribuindo
#uma variável "total_de_elementos"
total_elementos = len(testes)
print(f"Total de elementos: {total_elementos}")

#Calculando a taxa de acerto multiplicando por 100.0 pela divisão das variáveis "total_de_acertos"
#e "total_de_elementos" e atribuindo a variavel "taxa_de_acerto"

taxa_de_acertos = 100.0 * total_de_acertos / total_elementos
print(f"Taxa de acerto: {taxa_de_acertos}")

print(f"Resultado: {resultado}")
print(f"Diferenças: {diferencas}")
print(f"Taxa de Acerto: {taxa_de_acertos}")
