class TV:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True
    def aum_canal(self):
        if self.ligada:
            self.canal += 1
    def dim_canal(self):
        if self.ligada:
            self.canal -= 1

if __name__ == '__main__':
    tv = TV()
    print('Televisão está ligada: {}'.format(tv.ligada))
    tv.power()
    print('Televisão está ligada: {}'.format(tv.ligada))
    # tv.power()

    print(tv.canal)
    tv.aum_canal()
    tv.aum_canal()
    print(tv.canal)
    tv.dim_canal()
    print(tv.canal)
