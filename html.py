import pyautogui as pya
import time

e = 'enter';	t = 'tab';	l = 'left';	d = 'down';

#SIMPLIFICA TEMPO

def tm(temp):
	time.sleep(temp)

#SIMPLIFICA ENTRADA DE TEXTO

def write(text):
	pya.write(text)

#SIMPLIFICA ENTRADA DE TECLADO

def press(button):
	pya.press(button)

#GERA TABULAÇÃO E RETORNA A LINHA 1, SIMPLIFICA DOWN

downs = 0; tabs = 0;

def dt(downs,tabs):
	i = 1;
	for i in range(downs):
		pya.press(d)
	for i in range(tabs):
		pya.press(t)
	for i in range(tabs):
		pya.press(l)
	tm(1)

#SALVA ARQUIVO .HTML
	
def save():
	tm(1)
	pya.hotkey('ctrl','s')
	tm(5)
	write("index.html")
	pya.click(635,370)
	press(['t',e,e])
	tm(3)

#INICIO DO PROGRAMA

dicas = int(input("Desejar receber instruções sobre html?(1 = sim/2 = não)\n-> "))

if(dicas==0 and dicas<2):
	print("ERROR 504")
	pya.hotkey('ctrl','c')


#ACESSAR PROMPT E ABRIR NOTEPAD

pya.hotkey('win', 'r')
tm(1)
write('cmd')
press(e)
tm(1)
write("start /max notepad")
press(e)
tm(1)


#ESCRITA DO CODÍGO-FONTE EM HTML 

write("<!DOCTYPE html>")
press(e)
write("<html lang='pt_br'>")
press([e,e])
write("<head>")
press(e)
write("<meta http-equiv='content-type' content='text/html' charset='UFT-8'>")
press(e)
write("<meta http-equiv='X-UA-Compatible' content='IE=edge'>")
press(e)
write("<meta http-equiv='refresh' content=''>")
press([e,e])
write("<meta name='keywords' content=''>")
press(e)
write("<meta name='author' content=''>")
press(e)
write("<meta name='description' content=''>")
press(e)
write("<meta name='viemport' content='width=device-width, initial-scale=1.0'>")
press([e,e])
write("<title></title>")
press([e,e])
write("<link rel='stylesheet' href=''>")
press([e,e])
write("</head>")
press([e,e])
write("<body>")
press(e)
write("<header>")
press(e)
write("</header>")
press(e)
write("<main>")
press(e)
write("</main>")
press(e)
write("<footer>")
press(e)
write("</footer>")
press(e)
write("</body>")
press(e)
press(e)
write("</html>")

if(dicas==1):
	press([e,e])
	write("<!-----------------------------------------")
	press([e,t])
	write("Esse ambiente tem o nome de comentario, triste eu nao poder usar acentos mas enfim")
	press([e,t])
	write("Dentro do <head> temos as tags <meta> que guarda informacoes do seu website")
	press([e,t])
	write("Capriche e com certeza ele aparecera no topo das buscar")
	press([e,t])
	write("Segue agora as informacoes que devem ser adicionas entre as aspas do content de cada tag")
	press([e,e])
	write("refresh -> adicione um tempo em segundos para que o seu website atualize")
	press(e)
	write("keywords -> adicone palavras-chaves, bom, PALAVRAS, que tenham a ver com o tema do seu website, nada de frases")
	press(e)
	write("author -> o ser-humanos por traz do codigo-fonte, espero que seja voce :)")
	press(e)
	write("description -> Agrora sim um resumo do seu website, afinal de contas, por que ele existe...")
	press([e,e,t])
	write("Entre as tags title -> Titulo que aparecera na aba que fica ao topo do navegador")
	press([e,t])
	write("Entre as tags body -> Corpo do website, onde fica imagens, textos, videos, afins")
	press([e,e,t])
	write("Se bem que <body> deve ser subdividida em:")
	press([e,t,t])
	write("<header> -> cabecario/cabecalho")
	press([e,t,t])
	write("<main> -> conteudo principal")
	press([e,t,t])
	write("<footer> -> rodape, contendo contatos, copyright, logo do website, etc")
	press([e,e])
	write("por fim a tag html, bom, serve mesmo somente para avisar que se trata de um documento em html :D")
	press(e)
	write("-------------------------------------------->")
save()
pya.press('up', presses=60)
tm(1)
press([e,"up"])
write("Ao fim do processo será aberto uma caixa, mostrando o local do seu arquivo")
press(e)
dt(4,1) #head
dt(1,2)
dt(1,2)
dt(1,2) #3meta
dt(2,2)
dt(1,2)
dt(1,2)
dt(1,2) #4names
dt(2,2)
dt(2,2)
dt(2,1) #/head
dt(2,1) #body
dt(1,2)
press(e)
dt(1,2)
press(e)
dt(1,2)
press(e)
dt(1,2)
press(e)
dt(1,2)
press(e)
dt(1,2)
press(e)
dt(1,1) #/body
pya.click(1332,0)
tm(3)
press(e)
