import random


class Auto:
    def __init__(self, nimi, huippunopeus):
        self.nimi = nimi
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def muuta_nopeutta(self):
        nopeuden_muutos = random.randint(-10, 15)
        self.nopeus = max(0, min(self.nopeus + nopeuden_muutos, self.huippunopeus))

    def kulje(self):
        self.matka += self.nopeus


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.muuta_nopeutta()
            auto.kulje()

    def tulosta_tilanne(self):
        print(f"\n{'Auto':<20}{'Nopeus (km/h)':<15}{'Matka (km)':<15}")
        print("=" * 50)
        for auto in self.autot:
            print(f"{auto.nimi:<20}{auto.nopeus:<15}{auto.matka:<15}")

    def kilpailu_ohi(self):
        return any(auto.matka >= self.pituus for auto in self.autot)


autot = [
    Auto("Auto 1", 200),
    Auto("Auto 2", 200),
    Auto("Auto 3", 200),
    Auto("Auto 4", 200),
    Auto("Auto 5", 200),
    Auto("Auto 6", 200),
    Auto("Auto 7", 200),
    Auto("Auto 8", 200),
    Auto("Auto 9", 200),
    Auto("Auto 10", 200)
]

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunnit = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunnit += 1

    if tunnit % 10 == 0:
        print(f"\nTunti: {tunnit}")
        kilpailu.tulosta_tilanne()

print(f"\nKilpailu '{kilpailu.nimi}' päättyi. Kokonaisaika: {tunnit} tuntia.")
kilpailu.tulosta_tilanne()
