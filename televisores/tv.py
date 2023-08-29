class TV:
    numTV = 0
    def __init__(self, marca, estado):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        self._control = None
        TV.numTV += 1
    @classmethod
    #def get_numTV(cls):
    #    return cls.numTV
    def get_marca(self):
        return self._marca
    def set_marca(self,marca):
        self._marca=marca
    def get_canal(self):
        return self._canal
    def set_canal(self,canal):
        if(self._estado and 1<=canal<=120):
            self._canal=canal
    def get_precio(self):
        return self._precio
    def set_precio(self,precio):
        self._precio=precio
    def get_estado(self):
        return self._estado
    def set_estado(self,estado):
        self._estado=estado
    def get_volumen(self):
        return self._volumen
    def set_volumen(self,volumen):
        if(self._estado and 0<=volumen<=7):
            self._volumen=volumen
    def get_control(self):
        return self._control
    def set_control(self,control):
        self._control=control
    def turnOn(self):
        self._estado=True
    def turnOff(self):
        self._estado=False
    def canalUp(self):
        if(self._estado and self._canal<120):
            self._canal+=1
    def canalDown(self):
        if(self._estado and self._canal>1):
            self._canal-=1
    def volumenUp(self):
        if(self._estado and self._volumen<7):
            self._volumen+=1
    def volumenDown(self):
        if(self._estado and self._volumen>0):
            self._volumen-=1