import pygame
import random


# classe: Configurações
class Configuracoes:
	# tela (dimensão)
	largura_da_tela = 800
	altura_da_tela = 600
	largura_centro = largura_da_tela / 2
	altura_centro = altura_da_tela / 2
	superficie_centro = (largura_centro, altura_centro)

	# cores (google: rgb color picker)
	cor_de_fundo = (255, 255, 255)  # branco
	cor_do_texto = (15, 64, 142)  # azul
	cor_do_botao = (66, 244, 128)  # verde
	amarelo = (234, 242, 2)
	verde = (0, 200, 0)

	# outras 
	fonte_do_texto = 'freesansbold.ttf'
	largura_imagem_jogador = 130
	altura_imagem_jogador = 100
	largura_objeto = 150
	altura_objeto = 200

	# imagens
	plano_de_fundo = pygame.image.load('espaco.jpg')
	imagem_do_personagem = pygame.transform.scale(pygame.image.load('nave_et.png'), (largura_imagem_jogador, altura_imagem_jogador))
	imagem_derrota = pygame.transform.scale(pygame.image.load('et.png'), (largura_imagem_jogador * 2, altura_imagem_jogador * 2))
	imagem_do_asteroide = pygame.transform.scale(pygame.image.load('cometa.png'), (largura_objeto, altura_objeto))

# objeto da classe Configurações
jogo = Configuracoes()

# inicializa pygame
pygame.init()

# configurações da tela do jogo (exibição.modo de ajuste)
janela_do_jogo = pygame.display.set_mode((jogo.largura_da_tela, jogo.altura_da_tela))

# legenda inicial do jogo (definir legenda)
pygame.display.set_caption('Desvie do Cometa!')

relogio = pygame.time.Clock()

# define um ícone para o jogo (mesma imagem do personagem)
pygame.display.set_icon(jogo.imagem_do_personagem)

# função que exibe o número de objetos desviados (pontuação do jogo)
def contador_objetos_desviados(count):
	fonte = pygame.font.SysFont(0, 45)
	texto = fonte.render('Pontuação: {:d}'. format(count), True, jogo.amarelo)
	# exibe a pontuação no canto superior esquerdo
	janela_do_jogo.blit(texto, (0, 0))

# adiciona a imagem do jogador
def personagem(posicao_x, posicao_y):
  janela_do_jogo.blit(jogo.imagem_do_personagem, (posicao_x, posicao_y))

# função para exibir algum texto na tela do jogo
def exibe_texto(texto, fonte, centro):
	# obtem superfície da tela
	superficie_tela = fonte.render(texto, True, jogo.cor_do_texto)
	# centraliza o texto
	superficie_rec = superficie_tela.get_rect()
	superficie_rec.center = centro
	# atualiza
	janela_do_jogo.blit(superficie_tela, superficie_rec)


# função para exibir mensagem de colisão
def colisao(pontuacao):
	# música
	pygame.mixer.music.stop()
	pygame.mixer.music.load('colisao.mp3')
	pygame.mixer.music.play()
	# atualiza tela
	janela_do_jogo.fill(jogo.cor_de_fundo)
	# exibe mensagem
	texto_grande = pygame.font.SysFont(jogo.fonte_do_texto, 115)
	exibe_texto("Colisão Detectada!", texto_grande, jogo.superficie_centro)
	texto_medio = pygame.font.SysFont(jogo.fonte_do_texto, 40)
	exibe_texto("Pontuação: {:d}". format(pontuacao), texto_medio, (jogo.superficie_centro[0], jogo.superficie_centro[1]+50))

	# atualiza imagem com alien da derrota
	janela_do_jogo.blit(jogo.imagem_derrota, (jogo.largura_centro-jogo.largura_imagem_jogador, 30))

	# exibe menu inicial
	while True:
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				pygame.quit()
				quit()
		# botões do menu inicial
		menu_inicial()
		pygame.display.update()
		relogio.tick(15)


# exibe botões do menu inicial
def botao(msg, pos_x, pos_y, largura, altura, ic, ac, action=0):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	# verifica posição dos botões na tela
	if pos_x + largura > mouse[0] > pos_x and pos_y + altura > mouse[1] > pos_y:
		pygame.draw.rect(janela_do_jogo, ac, (pos_x, pos_y, largura, altura))
		if click[0] == 1 and action != 0:
			# seleciona opção de começar ou terminar o jogo
			action()
	else:
		pygame.draw.rect(janela_do_jogo, ic, (pos_x, pos_y, largura, altura))

	# texto para ser colocado no botão
	texto_pequeno = pygame.font.Font(jogo.fonte_do_texto, 20)
	exibe_texto(msg, texto_pequeno, ((pos_x + (largura / 2)), (pos_y + (altura / 2))))


# função desenha os botões do menu inicial
def menu_inicial():
	botao("INICIAR", 150, 450, 100, 50, jogo.cor_do_botao, jogo.verde, jogar)
	botao("SAIR", 550, 450, 100, 50, jogo.cor_do_botao, jogo.amarelo, sair_do_jogo)


# função para finalizar o jogo
def sair_do_jogo():
	pygame.quit()
	quit()


primeiro_jogada = True

# função do menu inicial
def game_intro():
	intro = True
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		if primeiro_jogada == True:
			mensagem = "Desvie do Cometa!"
		else:
			mensagem = "Colisão Detectada"

		# desenha tela do menu inicial
		janela_do_jogo.fill(jogo.cor_de_fundo)  # cria a janela em branco
		texto_grande = pygame.font.SysFont(jogo.fonte_do_texto, 115)
		exibe_texto(mensagem, texto_grande, jogo.superficie_centro)
		menu_inicial()
		pygame.display.update()
		relogio.tick(15)


# função do jogo
def jogar():
	# carrega música de fundo
	pygame.mixer.music.load("musica.mp3")
	pygame.mixer.music.play(-1)

	# define altura, largura e posição iniciais
	x =  (jogo.largura_da_tela * 0.45)
	y = (jogo.altura_da_tela * 0.8)
	posicao = 0

	# construção dos objetos que caem
	objeto_pos_x = random.randrange(0, 73)
	objeto_pos_y =- 600
	velocidade_objeto = 5

	# pontuação do jogo é contada através do número de objetos
	desviados = 0

	# flag com condiçao pra sair
	continuar = True
	while continuar == True:
		# detecta eventos do jogo
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				pygame.quit()
				quit()

			# verifica movimentação caso tecla seja pressionada
			if evento.type == pygame.KEYDOWN:  # se pressionada a tecla, movimenta o jogador
				if evento.key == pygame.K_LEFT: 	 # seta para esquerda
					posicao = -15
				elif evento.key == pygame.K_RIGHT:   # seta para direita
					posicao = 15
			if evento.type == pygame.KEYUP:  # quando termina o clique na tecla, para a movimentação
				if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
					posicao = 0

		# não permite que jogador saia da tela
		if x + posicao > 0 and x + posicao + jogo.largura_imagem_jogador < jogo.largura_da_tela:
			x += posicao

		# mantém plano de fundo
		janela_do_jogo.blit(jogo.plano_de_fundo, (0, 0))
		# movimenta o asteróide
		janela_do_jogo.blit(jogo.imagem_do_asteroide, (objeto_pos_x, objeto_pos_y))

		# aumenta a velocidade dos objetos a após a passagem de cada um
		objeto_pos_y += velocidade_objeto
		# desloca o personagem na tela
		personagem(x, y)
		# conta pontos
		contador_objetos_desviados(desviados)

		# direcionamento dos objetos
		if objeto_pos_y > jogo.altura_da_tela:
			objeto_pos_y = 0 - jogo.altura_objeto
			objeto_pos_x = random.randrange(0, jogo.largura_da_tela)
			desviados += 1
			velocidade_objeto += 1

		# detecta colisão dos objetos
		if y < objeto_pos_y + jogo.altura_objeto:  # verifica se objeto está próximo na altura
			if x > objeto_pos_x and x < objeto_pos_x + jogo.largura_objeto or x + jogo.largura_imagem_jogador > objeto_pos_x and x + jogo.largura_imagem_jogador < objeto_pos_x + jogo.largura_objeto:
				colisao(desviados)

		primeira_jogada = False
		pygame.display.update()
		relogio.tick(60)


# início da execução do jogo
game_intro()
jogar()


pygame.quit()
quit()
