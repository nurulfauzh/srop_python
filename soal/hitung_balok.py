from balok import Balok

class HitungBalok:

    def hitung_luas(self,balok:Balok) -> float:
        return ((balok.get_panjang()*balok.get_lebar()) +(balok.get_panjang()*balok.get_tinggi()) + (balok.get_lebar()*balok.get_tinggi())) *2


    def hitung_volume(self,balok:Balok) -> float:
        return balok.get_panjang()*balok.get_lebar() * balok.get_tinggi()

    def hitung_keliling(self,balok: Balok) -> float:
        return (balok.get_panjang() + balok.get_lebar() + balok.get_tinggi()) *4