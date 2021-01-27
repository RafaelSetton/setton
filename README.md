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
	-> matematica.py
		+ primo(numero)
		+ primos_ate(numero)
		+ maior_primo_ate(numero)
		+ somatoria(inicio: int, fim: int, passo: int) -> float
		+ somatoria(inicio: int, fim: int) -> float
		+ somatoria(fim: int) -> float
		+ gera_funcao_quadratica(a: float, b: float, c: float) -> Callable[[float], float]
		+ resolve_funcao_quadratica(a: float, b: float, c: float) -> str
		+ limite(maximo: float, minimo: float, valor: float) -> float
		+ soma_pg(termo_1: float, razao: float, numero_de_termos: int) -> float
		+ simplify_polynomial(poly: str)
	-> music.py
		+ coffin_dance()
		+ toca_mp3(caminho)
		+ toca_musicas_mp3()
		+ do_re_mi_fa()
	-> Pygame/others.py
		+ grafico_de_linha(surface: pg.Surface, values: list[int, float], cor
		+ grafico_cheio(surface: pg.Surface, values: list[int, float], cor
	-> tones.py
		+ c(oitava=5, duracao=500)
		+ d(oitava=5, duracao=500)
		+ e(oitava=5, duracao=500)
		+ f(oitava=5, duracao=500)
		+ g(oitava=5, duracao=500)
		+ a(oitava=5, duracao=500)
		+ b(oitava=5, duracao=500)
		+ csh(oitava=5, duracao=500)
		+ dsh(oitava=5, duracao=500)
		+ fsh(oitava=5, duracao=500)
		+ gsh(oitava=5, duracao=500)
		+ ash(oitava=5, duracao=500)
		+ sil(mili=300)
		+ play(*args)

Classes: 
	-> manipulacao_de_arquivos.py
		+ File
	-> matematica.py
		+ Forma2D
		+ Triangulo(Forma2D)
		+ Quadrilatero(Forma2D)
		+ Trapezio(Quadrilatero)
		+ Paralelogramo(Quadrilatero)
		+ Retangulo(Quadrilatero)
		+ Quadrado(Retangulo)
		+ Circulo(Forma2D)
		+ Forma3D
		+ PrismaRetangular(Forma3D)
		+ AlgarismosRomanos
		+ CelsiusFahrenheit
		+ RadianosGraus
	-> Pygame/collisions.py
		+ CollisionDetector
	-> Pygame/hitboxes.py
		+ Rect
		+ Circle
	-> Pygame/__init__.py
		+ DefaultGame
	-> tones.py
		+ Sound

Constantes: 
	-> constantes.py
		+ A_ESPECIAL
		+ E_ESPECIAL
		+ I_ESPECIAL
		+ O_ESPECIAL
		+ U_ESPECIAL
		+ VOGAIS
		+ CONSOANTES
		+ BACKSLASH
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