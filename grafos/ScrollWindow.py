import matplotlib

# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from controller.Preenchimento import Preenchimento as preenchimento


class ScrollableWindow(QtWidgets.QMainWindow):

    # listaFormatadaDePosicoes = []

    # numeroDeCasasDecimais = 2

    # numeroDoGrafo = None

    '''
    def mostrarScores(self):
        print(self.listaDeScores)
        for i in self.listaDeScores:
            numeroDoGrafo = i

            plt.annotate(self.listaDeScores[numeroDoGrafo], xy=self.pos[numeroDoGrafo], xytext=(10, 10),
            textcoords="offset points", bbox=dict(boxstyle="round", fc="red")).get_bbox_patch().set_alpha(0.7)

    '''
    '''
    def formatarListaDePosicoes(self):
        for i in range(len(self.pos)):
            listaFormatada = (round(self.pos[i][0], self.numeroDeCasasDecimais)), (
                round(self.pos[i][1], self.numeroDeCasasDecimais))
            self.listaFormatadaDePosicoes.append(listaFormatada)
    

    def equacaoReduzidaDaCircunferencia(self, x, y, raio):
        isToShow = False
        for i in range(len(self.pos)):
            resultado = (x-self.pos[i][0]) * (x-self.pos[i][0]) + (y-self.pos[i][1]) * (y-self.pos[i][1])
            if resultado<=(raio*raio):
                isToShow = True
                self.numeroDoGrafo = i
                break

        return isToShow


    def isClosed(self):
        def fechar(event):
            print("...")

        self.fig.canvas.mpl_connect('motion_notify_event', fechar)




    def setMousePosition(self):
        def hover(event):
            #mousePosition = (round(event.xdata, self.numeroDeCasasDecimais), round(event.ydata, self.numeroDeCasasDecimais))

            if self.equacaoReduzidaDaCircunferencia(event.xdata, event.ydata, 0.01):
                #numeroDoGrafo = self.listaFormatadaDePosicoes.index(mousePosition)
                print(self.numeroDoGrafo)
                plt.annotate(self.listaDeScores[self.numeroDoGrafo], xy=self.pos[self.numeroDoGrafo], bbox=dict(boxstyle="round", fc="red")).get_bbox_patch().set_alpha(0.9)
                self.fig.canvas.draw_idle()

            else:
                print("entrou")
                for child in plt.gca().get_children():
                    if isinstance(child, matplotlib.text.Annotation):
                        child.remove()
                self.fig.canvas.draw_idle()

        self.fig.canvas.mpl_connect('button_press_event', hover)
    '''

    def __init__(self, fig, pos, listaDeScores):
        self.pos = pos
        self.listaDeScores = listaDeScores
        # self.formatarListaDePosicoes()

        self.qapp = QtWidgets.QApplication([])

        QtWidgets.QMainWindow.__init__(self)
        self.widget = QtWidgets.QWidget()
        self.setCentralWidget(self.widget)
        self.widget.setLayout(QtWidgets.QVBoxLayout())
        self.widget.layout().setContentsMargins(0, 0, 0, 0)
        self.widget.layout().setSpacing(0)

        self.fig = fig
        self.canvas = FigureCanvas(self.fig)
        self.canvas.draw()
        self.scroll = QtWidgets.QScrollArea(self.widget)
        self.scroll.setWidget(self.canvas)

        self.nav = NavigationToolbar(self.canvas, self.widget)
        self.widget.layout().addWidget(self.nav)
        self.widget.layout().addWidget(self.scroll)

        plt.xlim([-0.001, 1.008])    #1.042361111111111

        # self.setMousePosition()

        preenchimento.mostrarScores(self, plt, pos)

        self.show()

        exit(self.qapp.exec_())
