class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros
        print(f"Hissi on alimmassa kerroksessa: {self.nykyinen_kerros}")

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi siirtyi kerrokseen: {self.nykyinen_kerros}")
        else:
            print("Hissi on jo ylimmässä kerroksessa.")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi siirtyi kerrokseen: {self.nykyinen_kerros}")
        else:
            print("Hissi on jo alimmassa kerroksessa.")

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros < self.alin_kerros or kohde_kerros > self.ylin_kerros:
            print("Virhe: Kohdekerros ei ole sallitulla alueella.")
            return

        while self.nykyinen_kerros < kohde_kerros:
            self.kerros_ylös()

        while self.nykyinen_kerros > kohde_kerros:
            self.kerros_alas()



if __name__ == "__main__":
    hissi = Hissi(1, 10)
    hissi.siirry_kerrokseen(5)
    hissi.siirry_kerrokseen(1)
