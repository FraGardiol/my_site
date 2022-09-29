# come posso mettere un'icona che stia in alto nel titolo della pagina?
# questa si chiama "favicon" (favourite icon)
# se vado su questo sito posso crearne una: https://www.favicon.cc/?
# quando la scarichiamo sarà in un formato speciale: favicon.ico
# dopo averla scaricata andiamo a metterla nel folder dove abbiamo il sito

# per incorporarla dobbiamo creare un nuovo link in questo modo:
<link rel="icon" href="favicon.ico">

############################################################################################

# possiamo anche mettere diverse sezioni o divisioni nel sito

# per fare ciò si usa il comando <div class=""> </div>
# div crea una divisione nel body

# per togliere i margine da destra e sinistra dobbiamo cambiare il margine del div
# se dentro al dv c'è un h1 dobbiamo anche cambiare il margine dell'h1

##########################################################################################

# ricordiamoci che tutto in css è un rettangolo
# posso specificare le dimensioni di questi rettangoli sia in pixels sia in oercentuali

# oltre a width e height posso anche specificare se ci sarà o meno un "border"

# se aumentiamo le dimensioni del bordo aumenterà la dimensione del rettangolo di conseguenza

# possiamo anche specificare quanto spazio deve esserci tra ciò che c'è dentro al rettangolo
# dal rettangolo stesso -> "padding"

# possiamo inoltre anche specificare il "margin", cioè la distanza dal resto
# di ciò che c'è sullo schermo

################################################################################################

# DISPLAY PROPERTY

# display property ha 4 value differenti:
# 1: Block
# 2: Inline
# 3: Inline-Block
# 4: None

# i rettangoli attorno alle immagini sono di default larghi solo quanto l'immagine stessa
# per quanto riguarda le scritte, i rettangoli si espandono fino a fine schermo a destra e a sinistra

# questa tipologia di rettangolo che va fino in fondo si chiama "BLOCK ELEMENT"


# esiste un comando chiamato <span> </span>

# lo span mette qualcosa dentro a questo block element senza andare a capo in un nuovo rettangolo

# lo span è un "Inline Display Element", cioè è grande solo quanto basta per contenere ciò che ha dentro

# <img>, <span>, <a>: sono tutti inline elements


# attenzione: in un block element posso specificare la WIDTH, in uno span NO

# quello che posso fare è cambiare le DISPLAY PROPERTY di un elemento
# ad esempio:

# p {
#   display: inline;
#   }

# ora il paragrafo <p> diventa un inline element
# tuttavia ho perso l'abilità di modificarne le dimensioni

# per ovviare a questo problema posso usare "inline-block", che mantiene questa caratteristica

# p {
#   display: inline-block;
#   }

# le <img> è come se fossero inline-block

# display: none -> questo comando fa sparire l'elemento


# esiste anche una property chiamata "visibility"

# visibility: hidden; -> questo comando nasconde l'elemento
# ma ne mantiene la posizione (resta un rettangolo vuoto)


#############################################################################

# CSS Positioning

# gli elementi di html hanno già di loro delle regole di default di positioning:
# 1: il contenuto è importante, la height è predefinita dall'altezza del contenuto
# 2: l'ordine in quale appaiono gli oggetti dipende dal codice html
# 3: "children sit on top of parents", cioè se metto
#     qualcosa dentro a un div, il div resta dietro e il contenuto resta sopra
#     anche uno span sopra dentro a un h1 risulta stare sopra all'h1 stesso


# esiste una proprietà chiamata "Position"
# Position ha 4 attributi:
# 1: Static
# 2: Relative
# 3: Absolute
# 4: Fixed


# Static position significa che mantengo le regole di html


# Relative Positioning ci permette di posizionare un elemento relativamente
# a come sarebbe stato posizionato se l'elemento fosse stato Static

# esempio:
# img {
#   position: relative;
#   left: 30px;
#   }

# in questo caso l'immagine avrà 30 pixel di spazio a sinistra
# rispetto a dove si sarebbe trovato se fosse stato static

# per muovere l'oggetto in questo modo i sono 4 coordinate:
# top, bottom, left, right

# OSS: se muoviamo un elemento in questo modo non modifichiamo la posizione di nessun altro oggetto
# se ad esempio sotto c'è un'altra immagine e spostiamo la prima immagine in basso, e due immagini
# si ritroveranno una sopra l'altra



# attenzione: con questo metodo possiamo spostare gli elementi anche fuori dallo schermo


#############################################################################################

# Absolute Positioning

# esiste anche un altro modo per spostare un oggetto

# con la absolute positioning sposteremo l'oggetto relativamente al suo "Parent"
# non è davvero assoluto, ma semplicemente indichiamo lo spazio che
# deve avere dal parent (che può essere anche il body)

# es:

# img {
#   position: absolute;
#   left: 200px;
#   }

# in questo caso spostiamo l'immagine in modo da avere solo 20px di margine dal lato destro dello schermo


# se usiamo la absolute position viene influenzata anche la posizione di tutto il resto degli oggetti

########################################################################################################

# FIXED POSITION

# fixed position significa che anche se scrollo
# la pagina l'oggetto resterà comunque fissato dove l'ho messo sullo schermo


#####################################################################################################


# per centrare gli elementi in mezzo allo schermo possiamo usare una proprietà:

# text-align: center;


# un altro modo potrebbe essere quello di usare il "MARGIN"

# margin: 0 auto 0 auto;

# così facendo ho messo un margine a destra e a sinistra per centrare l'oggetto


#############################################################################################

# FONT

# vediamo come cambiare il font dei testi in CSS

# posso andare nel body dello styles.css e scrivere:
# font-family: serif;

# così facendo cambio tutte le scritte nel body


# le font-family possono essere:
# serif
# sans-serif
# monospace
# cursive
# fantasy
# inherit


# di default c'è il serif


# dopo aver messo la famiglia posso specificare il font specifico
# es:

# font-family: verdana, sans-serif


# verdana è un font specifico della famiglia sans-serif
# scriverlo in questo modo vuol dire che se il computer riesce renderizzerà i
# testi in verdana, se non riesce passerà a un font sans-serif che riesce a renderizzare

# posso anche "embed" dei font nel programma per far si che tutti riescano a rendereizzarlo

# posso cercare font su: https://fonts.google.com/


####################################################################################

# font size

# cambio il font size:

h1 {
    font-size: 90px;
}




###################################################################################################

float: left;

# questo comando fa in modo che due cose siano una a sinistra dell'altra



clear: left;

# questo elimina il float