# henrietta.kathryn.main.py
from _spy.vitollino.main import Cena, STYLE, NADA, NoEv, Popup
from _spy.vitollino.main import Texto as Text
from browser import html, doc, window, alert

PR = chr(172)
MU = chr(181)
DEBUG = False

OCEANO = "https://i.imgur.com/NRi5i6d.jpg"
STYLE["width"] = 600
STYLE["height"] = "400px"
CNV = 400
MX = 400//4 - 10
STK = 2


class Plotter:
    def __init__(self, cena, tit=""):
        self.color = "blue"
        canvas = html.CANVAS(width=CNV, height=200)
        cena.html = ""
        cena <= canvas
        self.prt = html.DIV()
        self.prt.html = ""
        cena <= self.prt
        self.ctx = canvas.getContext("2d")
        self.tit = tit

        self.dataset = []
        self.figure_title()
        self.axis()

        ## After doing this I saw that this could be achieved using
        ## translate(0,canvas.height); scale(1,-1);
        ## https://developer.mozilla.org/en-US/docs/HTML/Canvas/Tutorial/Transformations

    @staticmethod
    def change_ref_system(_x, _y):
        return 20 + _x * 4, 180 - _y * 1

    def draw_line(self, x1, y1, x2, y2, linethick=3, color="black"):
        self.ctx.beginPath()
        self.ctx.lineWidth = linethick
        self.ctx.moveTo(x1, y1)
        self.ctx.lineTo(x2, y2)
        self.ctx.strokeStyle = color
        self.ctx.stroke()

    def axis(self, color="black", linethick=3):
        # Draw of x axis
        self.draw_line(20, 180, 380, 180, linethick=linethick, color=color)
        # Draw of y axis
        self.draw_line(20, 20, 20, 180, linethick=linethick, color=color)

    def figure_title(self):
        self.ctx.fillStyle = "gray"
        self.ctx.fillRect(0, 0, 400, 300)

        self.ctx.clearRect(410, 0, 400, 30)
        self.ctx.fillStyle = "white"
        self.ctx.font = "bold 16px Arial"
        self.ctx.fillText(self.tit, 15, 15)

    def title_update(self, _):
        self.figure_title()

    def graph(self, absiss, data):
        color = self.color
        self.dataset.append((absiss, data))
        if len(self.dataset) == 1:
            _x, _y = self.change_ref_system(absiss, data)
            self.draw_line(_x, _y, _x, _y, linethick=STK, color=color)
        else:
            cur, prev = self.dataset[-1], self.dataset[-2]
            x1, y1 = self.change_ref_system(*prev)
            x2, y2 = self.change_ref_system(*cur)
            self.draw_line(x1, y1, x2, y2, linethick=STK, color=color)
            # self.prt <= '{}\n'.format((x1, y1, x2, y2))

    @staticmethod
    def pack(dataset):
        return PR.join(MU.join([str(ab) for ab in pair]) for pair in dataset)

    @staticmethod
    def unpack(datapack):
        return [pair.split(MU) for pair in datapack.split(PR)]

    def display(self, text):
        self.prt <= html.P(text)

    def plot(self, x_, y_, color="blue"):
        self.color = color
        self.dataset = []
        [self.graph(_x, _y) for _x, _y in zip(x_[:MX], y_[:MX])]
        self.display(self.pack(self.dataset)) if DEBUG else False


class Texto(Text):
    def __init__(self, cena=NADA, tit="", txt="", texto=None, foi=None, indo=None, **kwargs):
        super().__init__(cena=cena, tit=tit, txt=txt, foi=foi, **kwargs)
        # self.elt = Popup.POP.popup
        self.t = []
        self.cena, self.area = cena, html.DIV()
        if texto is not None:
            self.area = html.TEXTAREA(texto, Id="_TEXT_POPUP_", rows=4,
                                      style=dict(width='100%', resize=None))
            self.area.bind('keypress', self.indo)
        self._esconde = foi if foi else lambda: None
        self.indo = indo if indo else self.indo
        # cena <= self

    def _esconde(self, ev=NoEv()):
        ev.preventDefault()
        ev.stopPropagation()
        self._esconde()
        return False

    @classmethod
    def put_area(cls):
        if "_TEXT_POPUP_" in doc:
            return
        Popup.POP.area = html.DIV()
        Popup.POP.div <= Popup.POP.area
        Texto.put_area = lambda *_: None

    def vai(self, ev=NoEv()):
        # self.elt = Popup.POP.popup
        ev.stopPropagation()
        self.cena.elt <= Popup.POP.popup
        Texto.put_area()
        Popup.POP.area.html = ''
        Popup.POP.area <= self.area
        Popup.POP.mostra(lambda *_: None, self.tit, self.txt)
        Popup.POP.esconde = self.esconde
        return False

    def sai(self, _=NoEv()):
        j = '{}'.format(PR)
        t = self.area.value if self.area else ''
        return t, j.join(self.t)

    def indo(self, ev=NoEv()):
        char = ev.keyCode if ev.keyCode else ev.which
        # self.t.append('{}{}{}'.format(chr(char), MU, str(window.Date.now())[-6:]))
        t = str(window.Date.now())[-7:]
        self.t.append('{}{}{}'.format(chr(char), MU, t))


class Game:
    def __init__(self):
        # self.elt = Popup.POP.popup
        self.cena = self.grafico = Cena(OCEANO)
        self.t = []
        foi = lambda *_: Texto(cena=self.cena, tit="score", txt="\n".join(self.texto.sai())).vai() or self.pontua(self.texto.sai())
        # foi=lambda *_: alert("\n".join(self.texto.sai()))
        self.texto = Texto(cena=self.cena, tit="diga, com quantos paus se faz a canoa?", texto="",
                           foi=foi)  # lambda *_:alert(self.texto.sai()[0])) #"\n".join(self.texto.sai())))
        self.cena.meio.vai = self.texto.vai
        # self.cena.vai = self.texto.vai
        self.cena.vai()
        
        # self.texto.vai()
        
    def pontua(self, pontos):
        resposta, grafo = pontos
        grafo_ = Plotter.unpack(grafo)
        t0 = int(grafo_[0][1])
        grafo = [(int(t)-t0) // 10 for _, t in grafo_]
        _grafo = [(x, b - a) for x, (b, a) in enumerate(zip(grafo[1:], grafo))]
        _grafp = [(x, b - a + 80) for x, ((_,b), (_,a)) in enumerate(zip(_grafo[1:], _grafo))]
        datapack = Plotter.pack([[c, '{0:0>6}'.format((int(t)-t0)//1)] for c, t in grafo_])
        alert("grafo: {}, pack: {}".format(grafo_, datapack))
        plt = Plotter(self.grafico.elt, "game")
        x, y = zip(*_grafo)
        plt.plot(x, y)
        x, y = zip(*_grafp)
        plt.plot(x, y, "magenta")
        plt.display("grafo: {}, pack: {}".format(_grafp, datapack))

    def indo(self, *_):
        self.t.append(self.texto.area.value)

if __name__ == '__main__':
    DEBUG = True
    Game()
    # x, y = [2, 4, 6, 8, 10, 12], [50, 100, 40, -80, 140, -10]
    # Plotter(doc["pydiv"], "imaginário").plot(x, y)
