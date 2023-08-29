class TV:
    _canal: int=1
    _precio: int=500
    _estado: bool
    _volumen: int=1
    _numTV: int=0

    def __init__(self,marca,estado):
        self._marca=marca
        self._estado=estado
        TV._numTV+=1
    def getEstado(self):
        return self._estado   
    def turnOn(self):
        self._estado=True
    def turnOff(self):
        self._estado=False
    def canalUp(self):
        if(self._estado and self._canal<120):
            self._canal+=1
    def canalDown(self):
        if(self._estado and self._canal>1):
            self._canal -= 1
    def getVolumen(self):
        return self._volumen
    def setVolumen(self,volumen):
        if(self._estado and volumen>=0 and volumen<=7):
            self._volumen=volumen
    def volumenUp(self):
        if(self._estado and self._volumen<7):
            self._volumen+=1
    def volumenDown(self):
        if(self._estado and self._volumen>0):
            self._volumen-=1
    def getMarca(self):
        return self._marca   
    def setMarca(self,marca):
        self._marca=marca
    def getCanal(self):
        return self._canal
    def setCanal(self,canal):
        if(self._estado and canal>=1 and canal<=120):
            self._canal=canal
    def getPrecio(self):
        return self._precio
    def setPrecio(self,precio):
        self._precio=precio
    def setControl(self,control):
        self._control=control
    def getControl(self):
        return self._control
    def getNumTV():
        return TV._numTV  
    def setNumTV(numTV):
        TV._numTV=numTV