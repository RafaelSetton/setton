# setton

Minhas funções que podem ser extremamente úteis.
Algumas foram feitas somente para treino.

Lista de Funções:

```
constantes.py:
	None

jogos_de_sorte.py:
	pedra_papel_tesoura()
	par_impar()
	dado(lados)

manipulacao_de_arquivos.py:
	conta_linhas(arquivo)
	insere(arquivo, indice, texto)
	bkspc(arquivo, indice)
	busca_indices(arquivo, termo)
	conta_ocorrencias(arquivo, termo)

matematica.py:
	add(*args)
	subtr(num1, num2, absolute=False)
	times(*args)
	divide(dividendo, divisor, arredondar=False)
	mmc2(num1, num2)
	mmc(*args)
	primo(numero)
	primos_ate(numero)
	maior_primo_ate(numero)
	circunferencia(raio, arredondar=False)
	area_do_circulo(raio, arredondar=False)
	somatoria(inicio, fim, passo)
	somatoria(inicio, fim)
	somatoria(fim)
	gera_funcao_quadratica(a, b, c)
	resolve_funcao_quadratica(a, b, c)
	limite(maximo, minimo, valor)
	par(numero, mudar='')
	impar(numero, mudar='')
	soma_pg(termo_1, razao, numero_de_termos)
	celcius_fahrenheit(temperatura_celsius, arredondar=False)
	fahrenheit_celsius(temperatura_fahrenheit, arredondar=False)
	graus_radianos(graus, mostrar_como_decimal=False)
	radianos_graus(radianos)
	radianos_graus(radianos)
	calcular(string: str) -> float

MRU.py:
	None

Music.py:
	coffin_dance()
	toca_musica(caminho)
	toca_musicas_mp3()
	do_re_mi_fa()

Tones.py:
	c(oitava=5, duracao=500)
	d(oitava=5, duracao=500)
	e(oitava=5, duracao=500)
	f(oitava=5, duracao=500)
	g(oitava=5, duracao=500)
	a(oitava=5, duracao=500)
	b(oitava=5, duracao=500)
	csh(oitava=5, duracao=500)
	dsh(oitava=5, duracao=500)
	fsh(oitava=5, duracao=500)
	gsh(oitava=5, duracao=500)
	ash(oitava=5, duracao=500)
	sil(mili=300)
	play(*args)

utils.py:
	trata_texto(acentos: bool = True, pontos: bool = True) -> callable
	keyboard_listener(dic_funcs: dict) -> None
	valida_resposta(texto: str, respostas: iter, somente_maiusculas: bool = True) -> str
	trata_acento(*args) -> tuple
	trata_ponto(*args) -> tuple
	split_nth(iteravel: iter, n: int) -> list
	codifica(texto, repeticoes_maximas) -> str
	codifica(texto) -> str
	codifica(texto, modo, repetir) -> str
	decodifica(texto) -> str
	decodifica(texto, modo, repetir) -> str
	udir(objeto: object) -> list
	mais_repetidas(iterable: iter, quantidade_de_itens: int = 3, quantidade_minima: int = 0) -> list
	list_replace(lista: list, old, new) -> list
	inverte_dict(dicionario: dict) -> dict
	alphalen(iterable: iter) -> int
	get_all_files(directory: str, extension: str = '*', start_string: str = './') -> str
	dicionario_portugues() -> list
	desempacota_listas(lista: list) -> list
```

Constantes:

```
A_ESPECIAL
E_ESPECIAL
I_ESPECIAL
O_ESPECIAL
U_ESPECIAL
VOGAIS
CONSOANTES
ALFABETO_MINUSCULO
ALFABETO_MAIUSCULO
ALFABETO_COMPLETO
PONTUACAO
CODABLE
MORSE_MINUSCULO
MORSE_MAIUSCULO
MORSE_ESPECIAL
MORSE_COMPLETO
MESES
ADJACENTES_TECLADO
p
```