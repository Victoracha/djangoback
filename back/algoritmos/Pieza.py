class Pieza:
    def __init__(self,  maquinas, tiempos, pieza, valor, tiempoEsperado):
        q=0
        self._nPieza=pieza
        self._fases = []
        self._tiempoTotal = 0
        self._asignatiempo = True
        self._libreMaquina=True
        self._tiempoOperacionalTotal=0
        self._valor = valor
        self._tiempoEsperado = tiempoEsperado

        self._Ad = 0
        self._Ret = 0



        for i in range ( len (tiempos)):
            max=len(tiempos)-1
            if i < max:
                fase=Fase(self._nPieza, tiempos[i], maquinas[i], i, self._valor, self._tiempoEsperado, tiempos[i+1])
            else:
                fase = Fase(self._nPieza, tiempos[i], maquinas[i], i, self._valor, self._tiempoEsperado, 0)
            self._tiempoOperacionalTotal+= fase.get_tiempoRequerido()
            self._fases.append(fase)
        self._tiempoOperacionalTotalRestante = self._tiempoOperacionalTotal

        for fase in self._fases:

            fase.set_tiempoOperacionalRestante(self._tiempoOperacionalTotalRestante)
            self._tiempoOperacionalTotalRestante -= fase.get_tiempoRequerido()
    def getNpieza(self):
        return self._nPieza

    def getValor(self):
        return self._valor

    def getTiempoEsperado(self):
        return self._tiempoEsperado



    def getAdelanto(self):
        return self._Ad
    def setAdelanto(self, adelanto):
        self._Ad=adelanto
    def getRetroceso(self):
        return self._Ret
    def setRetroceso(self, retroceso):
        self._Ret=retroceso
    def getFases(self):
        return self._fases

    def setTiempoTotal(self, tiempo):
        self._tiempoTotal = tiempo
        self._asignatiempo=False

    def getTiempoTotal(self):
        return self._tiempoTotal

    def get_modificartiempo(self):
        return self._asignatiempo

    def set_LibreMaquina(self, libre):
        self._libreMaquina=libre

    def get_LibreMaquina(self, libre):
        return self._libreMaquina

    def get_tiempoOperacionalRestante(self):
        return self._tiempoOperacionalTotalRestante

    def set_tiempoOperacionalRestante(self, tiempo):
        self._tiempoOperacionalTotalRestante = tiempo

class Fase:
    def __init__(self, nPieza, tiempoRequerido, maquinaNecesaria, nFase, valor, tiempoEsperado, tiempoSig):
        self._nPieza=nPieza
        self._tiempoRequerido=tiempoRequerido
        self._maquinaNecesaria=maquinaNecesaria
        self._nFase=nFase
        self._tiempoSig=tiempoSig
        self._tiempoFaseEntrada = 0
        self._tiempoFaseSalida = 0
        self._tiempoOperacionalTotalRestante=0
        self._valor = valor
        self._tiempoEsperado = tiempoEsperado
    def getValor(self):
        return self._valor
    def getTiempoEsperado(self):
        return self._tiempoEsperado
    def get_nPieza(self):
        return self._nPieza
    def get_tiempoRequerido(self):
        return self._tiempoRequerido
    def get_maquinaNecesaria(self):
        return self._maquinaNecesaria
    def get_nSubpieza(self):
        return self._nFase
    def getTiempoSig(self):
        return self._tiempoSig
    def get_tiempoFaseEntrada(self):
        return self._tiempoFaseEntrada
    def get_tiempoFaseSalida(self):
        return self._tiempoFaseSalida
    def get_TiempoEntrada(self):
        return self._tiempoFaseEntrada

    def get_TiempoSalida(self):
        return self._tiempoFaseSalida

    def set_TiempoEntrada(self, tiempo):
        self._tiempoFaseEntrada=tiempo

    def set_TiempoSalida(self, tiempo):
        self._tiempoFaseSalida=tiempo

    def get_tiempoOperacionalRestante(self):
        return self._tiempoOperacionalTotalRestante

    def set_tiempoOperacionalRestante(self, tiempo):
        self._tiempoOperacionalTotalRestante = tiempo