from persegi import persegi

class persegiController:

    def hitung_luas(self, persegi: Persegi) -> float:
        return persegi.get_sisi() * persegi.get_sisi()

    def hitung_keliling(self, persegi: Persegi) -> float:
        return 4 * persegi.get_sisi()