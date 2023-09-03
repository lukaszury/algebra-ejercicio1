import regex 
from collections import defaultdict
import sys

tweets = [
    "a silvina la mataron en vida, y el responsable se tiene que hacer cargo. a donde vaya lo iremos a buscar",
    "En otro país Lotocki ya estaría preso de por vida por malapraxis.",
    "Si después de la muerte de Silvina, Lotoki no termina en la cárcel y con un palo de escoba incrustado en el esófago, yo ya no entiendo más nada.",
    "Y encima el asesino no está en cana. Porque eso es lo que es Este pais es una joda",
    "Que triste la puta madre, al hijo de puta de Lotocki lo tienen que colgar del obelisco",
    "Silla eléctrica y la peor de las torturas para el hijo de mil puta de lotocki.",
    "Lo triste que me puso esto😔😔😔 al hijo de remil puta de lotocki hay que mwordearlo entre todos",
    "y el cirujano que la mató a ella y a no sé cuántas personas más? libre, como siempre la justicia argentina dando cátedra en corrupción e ineficiencia, hijos de puta",
    "pobre mujer por favor,ojala lo maten al otro por hijo de mil puta",
    "pobre mujer, no puedo creer que lotocki siga libre dios mio",
    "Pobre la peleó bastante y el asesino libre",
    "Que triste esto realmente pobre chica",
    "silvina la estaba pasando mal hace años, denunció a lotocki y la justicia no hizo nada, el seguia operando. Ella soñaba con ser mamá y no pudo serlo por los tratamientos que tuvo que hacerse por culpa de lotocki, ella se estaba muriendo y a el no le prohibían operar",
    "A pesar de todas las circunstancias, Silvina Luna mantuvo hasta el final todas sus ganas de vivir y de recuperarse y la peleó como las mejores, que injusto que el culpable de quitarle la vida esté libre.",
    "Como la lucho esta mina, un ejemplo. Ojalá el hijo de mil puta de Lotocki sea encarcelado, violado y torturado.",
    "Che yo sé que nada que ver esto acá pero me da una pena la muerte de esta mina,de verdad. Ella quería vivir y se murió por culpa de un forro que sigue libre",
    "Pobre mujer, dios mío🥺en su última nota decía como quería tener una vida normal y poder tener hijos😢que sufrimiento vivió",
    "Qué tristeza y ojalá que el hijo de mil mierda responsable vaya preso",
    "Qué triste!! QEPD. Y mañana, con más tranquilidad, a ver qué se hace con el asesino éste. El Doctor.",
    "Tristísimo la verdad, era una bella y destacada mujer. Algunas decisiones personales pueden terminar mal, lamentablemente"
]

# Separador de palabras
def separar_palabras(texto):
    palabras_y_emojis = regex.findall(r'\w+|\p{P}|\p{So}', texto.lower())
    palabras = [palabra for palabra in palabras_y_emojis if not regex.match(r'\p{P}', palabra)]
    return palabras

def avg(w):
    return sum(w) / len(w)

def score(s):
    return s[0] - s[2]

palabras_por_tweet = []

for tweet in tweets:
    palabras = separar_palabras(tweet)
    palabras_por_tweet.append(palabras)

palabras_totales = {"vivir", "lucho","justicia", "doctor","asesino", "triste", "muerte", "puta"}
positivas = {"vivir", "lucho"}
neutras = {"justicia", "doctor"}
negativas = {"asesino", "triste", "muerte", "puta"}

vector_tweet = [0] * len(palabras_totales)
vector_sentimiento = [0,0,0]

for tweet in tweets:
    for palabra in separar_palabras(tweet):
        if palabra == "vivir":
            vector_tweet[0] += 1
            vector_sentimiento[0] += 1
        elif palabra == "normal":
            vector_tweet[1] += 1
            vector_sentimiento[0] += 1
        elif palabra == "justicia":
            vector_tweet[2] += 1
            vector_sentimiento[1] += 1
        elif palabra == "doctor":
            vector_tweet[3] += 1
            vector_sentimiento[1] += 1
        elif palabra == "asesino":
            vector_tweet[4] += 1
            vector_sentimiento[2] += 1
        elif palabra == "triste":
            vector_tweet[5] += 1
            vector_sentimiento[2] += 1
        elif palabra == "muerte":
            vector_tweet[6] += 1
            vector_sentimiento[2] += 1
        elif palabra == "puta":
            vector_tweet[7] += 1
            vector_sentimiento[2] += 1
print(f"Vector total palabras: {vector_tweet}")
print(f"Vector sentimiento: {vector_sentimiento}")
print(f'Calidad promedio de tweets {avg(vector_sentimiento)}')

    



print("----------------------------------------------------------------------")

cont = 0
max_score = -sys.maxsize - 1
min_score = sys.maxsize
max_score_tweet = ''
min_score_tweet = ''

for tweet in tweets:
    vector_tweet = [0] * len(palabras_totales)
    vector_sentimiento = [0,0,0]
    for palabra in separar_palabras(tweet):
        if palabra == "vivir":
            vector_tweet[0] += 1
            vector_sentimiento[0] += 1
        elif palabra == "normal":
            vector_tweet[1] += 1
            vector_sentimiento[0] += 1
        elif palabra == "justicia":
            vector_tweet[2] += 1
            vector_sentimiento[1] += 1
        elif palabra == "doctor":
            vector_tweet[3] += 1
            vector_sentimiento[1] += 1
        elif palabra == "asesino":
            vector_tweet[4] += 1
            vector_sentimiento[2] += 1
        elif palabra == "triste":
            vector_tweet[5] += 1
            vector_sentimiento[2] += 1
        elif palabra == "muerte":
            vector_tweet[6] += 1
            vector_sentimiento[2] += 1
        elif palabra == "puta":
            vector_tweet[7] += 1
            vector_sentimiento[2] += 1
    cont = cont +1
    print(f"Tweet {cont}\n")
    print(f"Vector total palabras: {vector_tweet}")
    print(f"Vector sentimiento: {vector_sentimiento}")
    print(f"El score del tweet es: {score(vector_sentimiento)}\n")
    if(score(vector_sentimiento) > max_score):
        max_score = score(vector_sentimiento)
        max_score_tweet = f'Tweet {cont}'
    if(score(vector_sentimiento) < min_score):
        min_score = score(vector_sentimiento)
        min_score_tweet = f'Tweet {cont}'

print(f'El tweet mas positivo fue {max_score_tweet} con {max_score} puntos')
print(f'El tweet mas negativo fue {min_score_tweet} con {min_score} puntos')












