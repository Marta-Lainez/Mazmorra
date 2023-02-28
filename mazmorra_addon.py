# Import necessary modules
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QMessageBox)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator
from mazmorra import Ui_MainWindow
from random import randint
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.initializeUI()
        self.show()
        self.createActions()

    def initializeUI(self):
        self.ui.textEdit_opcion3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ui.textEdit_opcion2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ui.textEdit_opcion1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.descolorearCajas()
        self.colorearSalasNoTerminadas()
        self.colorearBotones()
        self.desactivarRadioButtons()
        self.desactivarSalas()
        self.vaciarLabels()
        self.ui.pushSalir.setEnabled(False)
        self.ui.pushCentral.setEnabled(False)

        self.ui.pushNorte.clicked.connect(self.norte)
        self.ui.pushEste.clicked.connect(self.este)
        self.ui.pushSur.clicked.connect(self.sur)
        self.ui.pushOeste.clicked.connect(self.oeste)
        self.ui.pushJugar.clicked.connect(self.jugar)
        self.ui.pushSalir.clicked.connect(self.salirSala)
    
    def terminar(self):
        if(len(self.salas) == 0):
            self.juegoTerminado()

    def desactivarRadioButtons(self):
        self.ui.radioButton_1.hide()
        self.ui.radioButton_2.hide()
        self.ui.radioButton_3.hide()

    def activarRadioButtons(self):
        self.ui.radioButton_1.show()
        self.ui.radioButton_2.show()
        self.ui.radioButton_3.show()

    def activarSalas(self):
        if("Norte" in self.salas):
            self.ui.pushNorte.setEnabled(True)
        if("Sur" in self.salas):
            self.ui.pushSur.setEnabled(True)
        if("Este" in self.salas):
            self.ui.pushEste.setEnabled(True)
        if("Oeste" in self.salas):
            self.ui.pushOeste.setEnabled(True)
            
    
    #def colorearSalasRojo(self):
    #    style = ("QPushButton"
    #            "{"
    #            "background-color: #FFE9C1;"
    #            "font: 15pt \"Lucida Calligraphy\";"
    #            "}") 
    #    self.ui.pushNorte.setStyleSheet(style)                         
    #    self.ui.pushEste.setStyleSheet(style)                         
    #    self.ui.pushSur.setStyleSheet(style)                         
    #    self.ui.pushOeste.setStyleSheet(style)
    
    def colorearSalasNoTerminadas(self):
        style = ("QPushButton"
                "{"
                "background-color: #FCE4EC;"
                "font: 17pt \"Lucida Calligraphy\";"
                "}") 
        self.ui.pushNorte.setStyleSheet(style)                         
        self.ui.pushEste.setStyleSheet(style)                         
        self.ui.pushSur.setStyleSheet(style)                         
        self.ui.pushOeste.setStyleSheet(style)                        
        self.ui.pushCentral.setStyleSheet(style)                        
    def coloreadRadio(self):
        self.ui.radioButton_1.setStyleSheet("background: #E1BEE7;")
    def colorearBotones(self):
        style = ("QPushButton"
                "{"
                "font: 14pt \"Lucida Calligraphy\";"
                "background-color: #E1BEE7;"
                "}")
        self.ui.pushJugar.setStyleSheet(style)                        
        self.ui.pushSalir.setStyleSheet(style) 
        
    
    def colorearCajas(self):
        style = ("QLineEdit"
                "{"
                "font: 12pt \"Lucida Calligraphy\";"
                "background-color: #F3E5F5;"
                "}")
        self.ui.textEdit_opcion1.setStyleSheet(style)                        
        self.ui.textEdit_opcion2.setStyleSheet(style) 
        self.ui.textEdit_opcion3.setStyleSheet(style)

    def descolorearCajas(self):
        style = ("QLineEdit"
                "{"
                "font: 12pt \"Lucida Calligraphy\";"
                "background-color: #EAEAEA;"
                "}")
        self.ui.textEdit_opcion1.setStyleSheet(style)                        
        self.ui.textEdit_opcion2.setStyleSheet(style) 
        self.ui.textEdit_opcion3.setStyleSheet(style) 

    def desactivarSalas(self):
        self.ui.pushNorte.setEnabled(False)
        self.ui.pushOeste.setEnabled(False)
        self.ui.pushEste.setEnabled(False)
        self.ui.pushSur.setEnabled(False)

    def activarJugarYSalir(self):
        self.ui.pushSalir.setEnabled(True)
        self.ui.pushJugar.setEnabled(True)

    def vaciarLabels(self):
        self.ui.textEdit_texto.setText("")
        self.ui.textEdit_respuesta.setText("")
        self.ui.textEdit_opcion1.setText("")
        self.ui.textEdit_opcion2.setText("")
        self.ui.textEdit_opcion3.setText("")

    def vaciarRadios(self):
        self.ui.textEdit_opcion1.setText("")
        self.ui.textEdit_opcion2.setText("")
        self.ui.textEdit_opcion3.setText("")
    


    sala = "empieza"
    jugar = 0
    posicionAcertijo = 0
    victoria = 0
    salas = ["Norte","Sur","Este","Oeste"]

    def imprimirSalas(self):
        salasRestantes = "\nSalas restantes:"
        for x in self.salas:
            salasRestantes += ("\n" + x)
        return salasRestantes

    

    def norte(self):
        self.sala = "Norte"
        self.activarJugarYSalir()
        self.desactivarSalas()
        self.ui.textEdit_texto.setText("Al entrar en la sala ves una bestia. Debes acabar con ella para superar la sala. Cuidado, podría acabar contigo también.")
        self.jugar = "ataque"
        

    def este(self):
        self.sala = "Este"
        self.desactivarSalas()
        self.activarJugarYSalir()
        self.ui.textEdit_texto.setText("Delante de tí hay un cofre. Para superar esta sala debes usar tu paciencia y conseguir abrirlo. Dale a jugar para intentar abrir el cofre.")
    
    def sur(self):
        self.sala = "Sur"
        self.desactivarSalas()
        self.activarJugarYSalir()
        self.ui.textEdit_texto.setText("Para superar esta sala debes resolver un acertijo.")
        self.jugar = "acertijo"

    def oeste(self):
        self.sala = "Oeste"
        self.desactivarSalas()
        self.activarJugarYSalir()
        self.ui.textEdit_texto.setText("Para superar esta sala debes acertar la respuesta correcta.")
        self.jugar = "respuesta"


    # SECCION NORTE
    def norteAtaque(self):
        """
        descripcion: Juego de la sala norte en la que te enfrentas a un monstruo en una pelea.
        Si mueres hay que empezar el juego de cero. Hay que vencer al monstruo para superar la sala.
        output: String "S", "N" o "Muert" que indica si se sale de la sala o no o si has muerto.
        """
        self.activarJugarYSalir()
        ataque = randint(0,100)
        self.imprimeAtaque(int(ataque))
        if(ataque > 90):
            
            self.muerte()
        else:
            self.ui.textEdit_respuesta.setText("Si quieres defenderte dale a jugar. Si no quieres, puedes salir de la sala. ")
            self.jugar = "defensa"
            

    def norteDefensa(self):
        self.ui.textEdit_respuesta.setText("")
        defensa = randint(0,100)
        self.imprimeDefensa(int(defensa))
        if(defensa < 60):
            self.imprimeDefensa(int(defensa))
            self.ui.pushSalir.setEnabled(False)
            self.jugar = "ataque"
        else:
            self.ui.textEdit_respuesta.setText("Enhorabuena, has vencido al jefe. Sala Norte eliminada.")
            self.ui.pushJugar.setEnabled(False)
            self.salas.remove("Norte")
            self.ui.pushNorte.setStyleSheet("QPushButton"
                                            "{"
                                            "font: 15pt \"Lucida Calligraphy\";"
                                            "background-color : #FFCEDF;"
                                            "text-decoration:line-through"
                                            "}")
    def muerte(self):
        self.desactivarSalas()
        self.ui.pushCentral.setEnabled(False)
        self.ui.pushJugar.setEnabled(False)
        self.ui.pushSalir.setEnabled(False)
        self.ui.textEdit_respuesta.setText("Has muerto. Puedes reiniciar el juego si lo deseas.")
        self.ui.textEdit_texto.setText("")
    
    def jugar(self):
        if self.sala == "empieza":
            self.ui.textEdit_texto.setText("Estás en la sala central de una mazmorra, rodeado de otras 4 salas. Una al norte, otra al sur, otra al oeste y otra al este. Para lograr salir de la mazmorra debes superarlas todas con vida...\n" + self.imprimirSalas())
            #self.colorearSalasRojo()
            self.activarSalas()
            self.sala = "0"
        if self.sala == "Norte":
            if self.jugar == "defensa":
                self.norteDefensa()
            elif self.jugar == "ataque":
                self.norteAtaque()
        if self.sala == "Este":
            self.abrirCofre()
        if self.sala == "Sur":
            if self.jugar == "acertijo":
                self.acertijo()
            elif(self.jugar == "comprobar"):
                self.comprobarAcertijo()
        if self.sala == "Oeste":
            if self.jugar == "respuesta":
                self.pregunta()
            elif(self.jugar == "comprobar"):
                self.comprobarRespuesta()

    # SECCION ESTE
    def abrirCofre(self):
        """
        descripcion: Juego de la sala este en el que hay que conseguir abrir un cofre para superar la sala.
        """
        numero = randint(1,100)
        if(numero > 63):
            self.ui.textEdit_texto.setText("Enhorabuena, has conseguido abrir el cofre. Sala Este eliminada.")
            self.ui.pushJugar.setEnabled(False)
            self.salas.remove("Este")
            self.ui.pushEste.setStyleSheet("QPushButton"
                                            "{"
                                            "font: 15pt \"Lucida Calligraphy\";"
                                            "background-color : #FFCEDF;"
                                            "text-decoration:line-through"
                                            "}")
        else:
            self.ui.textEdit_texto.setText("No lo has conseguido. Vuelve a intentarlo dándole a jugar o sal de la sala.")
            self.ui.pushJugar.setEnabled(True)

    # SECCION SUR
    posiciones = [1,2,3]

    def acertijo(self):
        self.colorearCajas()
        self.activarRadioButtons()
        self.ui.textEdit_respuesta.setText("")
        numAcertijo = randint(0,9)
        self.ui.textEdit_texto.setText(self.acertijos[numAcertijo])
        

        respuesta1 = randint(0,9)
        while(respuesta1 == numAcertijo):
            respuesta1 = randint(0,9)

        respuesta2 = randint(0,9)
        while(respuesta2 == numAcertijo or respuesta2 == respuesta1):
            respuesta2 = randint(0,9)

        respuestaCorrecta = self.respuestasAcertijos[numAcertijo]
        respuestaMal1 = self.respuestasAcertijos[respuesta1]
        respuestaMal2 = self.respuestasAcertijos[respuesta2]    
        
        posicion1 = self.posiciones[randint(0,len(self.posiciones)-1)]
        self.posiciones.remove(posicion1)

        posicion2 = self.posiciones[randint(0,len(self.posiciones)-1)]
        self.posiciones.remove(posicion2)
        
        posicion3 = self.posiciones[randint(0,len(self.posiciones)-1)]


        #reseteo las posiciones para la próxima ronda
        self.posiciones = [0,1,2]
        # Posición de la respuesta correcta
        if(posicion1 == 1):
            self.ui.textEdit_opcion1.setText(respuestaCorrecta)
            self.posicionAcertijo = "radio1"
        elif(posicion1 == 2):
            self.ui.textEdit_opcion2.setText(respuestaCorrecta)
            self.posicionAcertijo = "radio2"
        else:
            self.ui.textEdit_opcion3.setText(respuestaCorrecta)
            self.posicionAcertijo = "radio3"
        # Posición de la respuesta incorrecta 1
        if(posicion2 == 1):
            self.ui.textEdit_opcion1.setText(respuestaMal1)
        elif(posicion2 == 2):
            self.ui.textEdit_opcion2.setText(respuestaMal1)
        else:
            self.ui.textEdit_opcion3.setText(respuestaMal1)
        # Posición de la respuesta incorrecta 2
        if(posicion3 == 1):
            self.ui.textEdit_opcion1.setText(respuestaMal2)
        elif(posicion3 == 2):
            self.ui.textEdit_opcion2.setText(respuestaMal2)
        else:
            self.ui.textEdit_opcion3.setText(respuestaMal2)
                
        self.jugar = "comprobar"
        
    
    def comprobarAcertijo(self):
        ganarAcertijo = False
        
        if(self.posicionAcertijo == "radio1"):
            if(self.ui.radioButton_1.isChecked()):
                ganarAcertijo = True
        elif(self.posicionAcertijo == "radio2"):
            if(self.ui.radioButton_2.isChecked()):
                ganarAcertijo = True
        else:
            if(self.ui.radioButton_3.isChecked()):
                ganarAcertijo = True

        if(ganarAcertijo == True):
            self.ui.textEdit_respuesta.setText("Has acertado. Sala sur eliminada.")
            self.salas.remove("Sur")
            self.ui.textEdit_texto.setText("")
            self.desactivarRadioButtons()
            self.vaciarRadios()
            self.ui.pushJugar.setEnabled(False)
            self.ui.pushSur.setStyleSheet("QPushButton"
                                            "{"
                                            "background-color : #FFCEDF;"
                                            "font: 15pt \"Lucida Calligraphy\";"
                                            "text-decoration:line-through"
                                            "}")
        else:
            self.ui.textEdit_respuesta.setText("Has fallado. Puedes volver a intentarlo dándole a jugar.")
            self.jugar = "acertijo"
    
    # SECCION OESTE

    def pregunta(self):
        self.colorearCajas()
        self.activarRadioButtons()
        self.ui.textEdit_respuesta.setText("")
        numPregunta = randint(0,7)
        self.ui.textEdit_texto.setText(self.preguntas[numPregunta])
        

        respuesta1 = randint(0,7)
        while(respuesta1 == numPregunta):
            respuesta1 = randint(0,7)

        respuesta2 = randint(0,7)
        while(respuesta2 == numPregunta or respuesta2 == respuesta1):
            respuesta2 = randint(0,7)

        respuestaCorrecta = self.respuestasPreguntas[numPregunta]
        respuestaMal1 = self.respuestasPreguntas[respuesta1]
        respuestaMal2 = self.respuestasPreguntas[respuesta2]    
        
        posicion1 = self.posiciones[randint(0,len(self.posiciones)-1)]
        self.posiciones.remove(posicion1)

        posicion2 = self.posiciones[randint(0,len(self.posiciones)-1)]
        self.posiciones.remove(posicion2)
        
        posicion3 = self.posiciones[randint(0,len(self.posiciones)-1)]


        #reseteo las posiciones para la próxima ronda
        self.posiciones = [0,1,2]
        # Posición de la respuesta correcta
        if(posicion1 == 1):
            self.ui.textEdit_opcion1.setText(respuestaCorrecta)
            self.posicionAcertijo = "radio1"
        elif(posicion1 == 2):
            self.ui.textEdit_opcion2.setText(respuestaCorrecta)
            self.posicionAcertijo = "radio2"
        else:
            self.ui.textEdit_opcion3.setText(respuestaCorrecta)
            self.posicionAcertijo = "radio3"
        # Posición de la respuesta incorrecta 1
        if(posicion2 == 1):
            self.ui.textEdit_opcion1.setText(respuestaMal1)
        elif(posicion2 == 2):
            self.ui.textEdit_opcion2.setText(respuestaMal1)
        else:
            self.ui.textEdit_opcion3.setText(respuestaMal1)
        # Posición de la respuesta incorrecta 2
        if(posicion3 == 1):
            self.ui.textEdit_opcion1.setText(respuestaMal2)
        elif(posicion3 == 2):
            self.ui.textEdit_opcion2.setText(respuestaMal2)
        else:
            self.ui.textEdit_opcion3.setText(respuestaMal2)
                
        self.jugar = "comprobar"
        
    
    def comprobarRespuesta(self):
        ganarRespuesta = False
        
        if(self.posicionAcertijo == "radio1"):
            if(self.ui.radioButton_1.isChecked()):
                ganarRespuesta = True
        elif(self.posicionAcertijo == "radio2"):
            if(self.ui.radioButton_2.isChecked()):
                ganarRespuesta = True
        else:
            if(self.ui.radioButton_3.isChecked()):
                ganarRespuesta = True

        if(ganarRespuesta == True):
            self.ui.textEdit_respuesta.setText("Has acertado. Sala oeste eliminada.")
            self.salas.remove("Oeste")
            self.ui.textEdit_texto.setText("")
            self.desactivarRadioButtons()
            self.vaciarRadios()
            self.ui.pushJugar.setEnabled(False)
            self.ui.pushOeste.setStyleSheet("QPushButton"
                                            "{"
                                            "font: 15pt \"Lucida Calligraphy\";"
                                            "background-color : #FFCEDF;"
                                            "text-decoration:line-through"
                                            "}")
        else:
            self.ui.textEdit_respuesta.setText("Has fallado. Puedes volver a intentarlo dándole a jugar.")
            self.jugar = "respuesta"
            


    def salirSala(self):
        if(self.sala == "Oeste" or self.sala == "Sur"):
            self.descolorearCajas()
            self.desactivarRadioButtons()
        self.ui.pushJugar.setEnabled(False)
        self.ui.pushSalir.setEnabled(False)
        self.activarSalas()
        self.vaciarLabels()
        self.sala = "centro"
        self.ui.textEdit_texto.setText("Has vuelto a la sala del centro. Continua hasta terminar todas las salas.\n" + self.imprimirSalas())
        if(len(self.salas) == 0):
            self.ui.pushSalir.setEnabled(True)
            self.juegoTerminado()

    ataques = ["El monstruo te intenta pinchar con su tridente de las delicias pero falla.",
            "De repente invoca 5 cabras satánicas que te escupen y patean sin parar, pero aguantas.",
            "La bestia te lanza un ataque mortal, pero Eric el delegado aparece en ultimo momento y te salva.",
            "El bicho se lanza hacia ti y sus garras casi te rozan, pero consigues evadirlas gracias a las clases de acrosport del cole.",
            "Oh no! Dibuja un pentagrama sobre el suelo, de ahi sale la play 5. Decides venderle tu alma por ella, lo que reduce tu durabilidad."]

    def imprimeAtaque(self, numAtaque):
        """
        Imprime el ataque correspondiente dependiendo del numero aleatorio de ataque que sale
        """
        if(numAtaque <= 25):
            self.ui.textEdit_texto.setText(str(self.ataques[0]))
        elif(numAtaque <= 45):
            self.ui.textEdit_texto.setText(str(self.ataques[1]))
        elif(numAtaque <= 60):
            self.ui.textEdit_texto.setText(str(self.ataques[2]))
        elif(numAtaque < 90):
            self.ui.textEdit_texto.setText(str(self.ataques[3]))
        elif(numAtaque <= 100):
            self.ui.textEdit_texto.setText(str(self.ataques[4]))

    defensas = ["Te lanzas a abofetear al temible monstruo pero resbalas con una cáscara de plátano y fallas.",
            "Le lanzas una piedra al jefe pero parece que no le ha afectado mucho.",
            "Le haces un calvo, se tapa los ojos un segundo. Parece muy enfadado.",
            "Agarras la espada para contraatacar pero se te cae.",
            "Coges un gran martillo y se lo lanzas, rozándole el pelo.",
            "Logras alcanzar una flecha, disparando y rozando a la bestia pero sobrevive.",
            "Sacas tus dagas y corres hasta la bestia, te tropiezas con una piedra que vuela hacia él y lo mata de un golpe.",
            "Aparece Eric el delegado y se lanza al monstruo. Para cuando acaba con él, el monstruo es irreconocible.",
            "Haces un triple salto mortal cayendo sobre los hombros del jefe y arrancandole la cabeza.",
            "Invoca a Jesucristo que abre un portal y devuelve al monstruo y le grita ATRÁS SATANÁS POR AQUÍ NO VUELVAS MÁS."]

    def imprimeDefensa(self, numDefensa):
        """
        Imprime la defensa correspondiente dependiendo del numero aleatorio de defensa que sale
        """
        if(numDefensa <= 10):
            self.ui.textEdit_texto.setText(str(self.defensas[0]))
        elif(numDefensa <= 20):
            self.ui.textEdit_texto.setText(str(self.defensas[1]))
        elif(numDefensa <= 30):
            self.ui.textEdit_texto.setText(str(self.defensas[2]))
        elif(numDefensa <= 40):
            self.ui.textEdit_texto.setText(str(self.defensas[3]))
        elif(numDefensa <= 50):
            self.ui.textEdit_texto.setText(str(self.defensas[4]))
        elif(numDefensa < 60):
            self.ui.textEdit_texto.setText(str(self.defensas[5]))
        elif(numDefensa <= 70):
            self.ui.textEdit_texto.setText(str(self.defensas[6]))
        elif(numDefensa <= 80):
            self.ui.textEdit_texto.setText(str(self.defensas[7]))
        elif(numDefensa <= 90):
            self.ui.textEdit_texto.setText(str(self.defensas[8]))
        elif(numDefensa <= 100):
            self.ui.textEdit_texto.setText(str(self.defensas[9]))

    acertijos = ["Hay algo que, aunque te pertenezca, la gente siempre lo utiliza más que tú. ¿Qué es?",
            "Crezco a pesar de no estar vivo. No tengo pulmones, pero para vivir necesito el aire. El agua, aunque no tenga boca, me mata. ¿Qué soy?",
            "Estando roto es más útil que sin romperse. ¿Qué es?",
            "Aparato que te metes en la boca unas 3 veces al día. ¿Qué es?",
            "Las personas siempre duermen menos en un mes del año. ¿Cuál es este mes?",
            "Estoy en todo pese a estar en nada. ¿Qué soy?",
            "Te paras cuando está verde y continúas cuando está rojo. ¿Qué es?",
            "¿Qué monte era el más alto del mundo antes de descubrir el Everest?",
            "La señora y el señor Sánchez tienen 6 hijos barones. Cada hijo baron tiene una hermana. ¿Cuántas personas hay en la familia Sánchez?",
            "Soy alto siendo joven y corto cuando soy viejo. Resplandezco con la vida y el viento es mi mayor enemigo. ¿Qué soy?"]
    respuestasAcertijos = ["Nombre","Fuego","Huevo","Cepillo","Febrero","D","Sandía","Everest","9","Vela"]

    preguntas = ["¿Cuál es el río más largo de España?",
            "¿Cuál es el río más largo de la península ibérica?",
            "¿Cuál es el río más largo del mundo?",
            "¿Cuál es la montaña más alta de España?",
            "¿Cuál es la montaña más alta del mundo?",
            "¿Cuál es el océano más grande?",
            "¿Cuál es el país con más extensión?",
            "¿Cuál es el país más poblado?"]
    respuestasPreguntas = ["Ebro","Tajo","Amazonas","Teide","Everest","Pacífico","Rusia","India"]

    def createActions(self):
        """Create the application's menu actions."""
        # Create actions for File menu
        self.ui.actionSalir.setShortcut("Ctrl+W")
        self.ui.actionSalir.triggered.connect(self.salir)
        self.ui.actionAyuda.setShortcut("Ctrl+H")
        self.ui.actionAyuda.triggered.connect(self.descripcionJuego)

    def salir(self):
        # clearing a single digit
        sys.exit() 
    
    def descripcionJuego(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Guia:")
        dlg.setText("Este juego trata de una mazmorra en la que hay que superar 4 salas para ganar.\n\n" +
                    "A continuación dele a \"Jugar\" para iniciar el juego.\n\n" +
                    "\tCómo jugar:\n\nAparecerá en la sala central. Haz click sobre las salas para jugar sus minijuegos.\n\n" +
                    "Cuando haya superado todas las salas habrá ganado. Puede salir y volver a iniciar el juego para volver a jugar.")
        dlg.setStyleSheet("background: pink;"
                        "font: 15pt \"Lucida Calligraphy\";")
        dlg.exec()

    def juegoTerminado(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Enhorabuena!!!")
        dlg.setText("Victoria!! Todas las salas han sido superadas.\nPuedes salir del juego y volver a empezar si quieres. Si eres Jorge puedes ponerme punto positivo c:")
        dlg.setStyleSheet("background: pink;"
                        "font: 15pt \"Lucida Calligraphy\";")
        dlg.exec()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Keypad = MainWindow()
    sys.exit(app.exec())

