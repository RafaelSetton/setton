# setton

Minhas funções, classes e constantes que podem ser extremamente úteis.
Algumas foram feitas somente para treino.

_Lista_:

```
Funções: 
	-> jogos_de_sorte.py
		+ pedra_papel_tesoura()
		+ par_impar()
		+ dado(lados)
	-> manipulacao_de_arquivos.py
		+ conta_linhas(arquivo)
		+ insere(arquivo, indice, texto)
		+ bkspc(arquivo, indice)
		+ busca_indices(arquivo, termo)
		+ conta_ocorrencias(arquivo, termo)
	-> matematica.py
		+ add(*args)
		+ subtr(num1, num2, absolute=False)
		+ times(*args)
		+ divide(dividendo, divisor, arredondar=False)
		+ mmc2(num1, num2)
		+ mmc(*args)
		+ primo(numero)
		+ primos_ate(numero)
		+ maior_primo_ate(numero)
		+ somatoria(inicio: int, fim: int, passo: int) -> float
		+ somatoria(inicio: int, fim: int) -> float
		+ somatoria(fim: int) -> float
		+ gera_funcao_quadratica(a: float, b: float, c: float) -> Callable[[float], float]
		+ resolve_funcao_quadratica(a: float, b: float, c: float) -> str
		+ limite(maximo: float, minimo: float, valor: float) -> float
		+ par(numero: int, mudar: str = '') -> (bool, int)
		+ impar(numero: int, mudar: str = '') -> (bool, int)
		+ soma_pg(termo_1: float, razao: float, numero_de_termos: int) -> float
		+ calcular(string: str) -> float
		+ simplify_polynomial(poly: str)
	-> Music.py
		+ coffin_dance()
		+ toca_mp3(caminho)
		+ toca_musicas_mp3()
		+ do_re_mi_fa()
	-> Pygame/others.py
		+ grafico_de_linha(surface: pg.Surface, values: list[int, float], cor
		+ grafico_cheio(surface: pg.Surface, values: list[int, float], cor
	-> utils.py
		+ trata_texto(acentos: bool = True, pontos: bool = True) -> callable
		+ keyboard_listener(dic_funcs: Dict[Any, Callable[[], None]]) -> None
		+ valida_resposta(texto: str, respostas: Iterable[Any], somente_maiusculas: bool = True) -> str
		+ trata_acento(*args) -> Tuple[Any]
		+ trata_ponto(*args) -> Tuple[Any]
		+ split_nth(iteravel: Iterable[Any], n: int) -> List[Any]
		+ codifica(texto, repeticoes_maximas) -> str
		+ codifica(texto) -> str
		+ codifica(texto, modo, repetir) -> str
		+ decodifica(texto) -> str
		+ decodifica(texto, modo, repetir) -> str
		+ udir(objeto: object) -> List[str]
		+ mais_repetidas(iterable: Iterable[Any], quantidade_de_itens: int = 3, quantidade_minima: int = 0) -> List[Any]
		+ list_replace(lista: List[Any], old, new) -> List[Any]
		+ inverte_dict(dicionario: Dict[Any, Any]) -> Dict[Any, Any]
		+ alphalen(iterable: Iterable[Any]) -> int
		+ max_2_keys(__iter: iter, primary: callable, secondary: callable) -> Any
		+ get_all_files(directory: str, extension: str = '*', start_string: str = './', ignore_file='') -> str
		+ dicionario_portugues() -> List[str]
		+ desempacota_listas(lista: List[Any]) -> List[Any]
		+ get_pixels(img_path: str, cor: Tuple[int]) -> Tuple[int]
		+ esteganografia(texto: str, file_name: str = 'esteganografia.png', override: bool = False) -> Any
		+ all_key(_iterable: iter, key: Callable)
		+ any_key(_iterable: iter, key: Callable)

Classes: 
	-> matematica.py
		+ Forma2D
		+ Triangulo(Forma2D)
		+ Quadrilatero(Forma2D)
		+ Trapezio(Quadrilatero)
		+ Paralelogramo(Quadrilatero)
		+ Retangulo(Quadrilatero)
		+ Quadrado(Retangulo)
		+ Circulo(Forma2D)
		+ PrismaRetangular
		+ AlgarismosRomanos
		+ CelsiusFahrenheit
		+ RadianosGraus
	-> MRU.py
		+ MRU
	-> Pygame/collisions.py
		+ CollisionDetector
	-> Pygame/hitboxes.py
		+ Rect
		+ Circle
	-> Pygame/__init__.py
		+ DefaultGame
	-> utils.py
		+ MyList(list)

Constantes: 
	-> constantes.py
		+ A_ESPECIAL
		+ E_ESPECIAL
		+ I_ESPECIAL
		+ O_ESPECIAL
		+ U_ESPECIAL
		+ VOGAIS
		+ CONSOANTES
		+ ALFABETO_MINUSCULO
		+ ALFABETO_MAIUSCULO
		+ ALFABETO_COMPLETO
		+ PONTUACAO
		+ CODABLE
		+ MORSE_MINUSCULO
		+ MORSE_MAIUSCULO
		+ MORSE_ESPECIAL
		+ MORSE_COMPLETO
		+ MESES
		+ ADJACENTES_TECLADO
	-> matematica.py
		+ GUGOL
```