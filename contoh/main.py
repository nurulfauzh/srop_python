from persegi import Persegi
from persegi_controller import persegiController
from persegi_view import PersegiView

Persegi - Persegi(2)
perhitung_persegi = persegiController()
penampil_persegi = PersegiView()

penampil_persegi.show_luas(Persegi, perhitung_persegi)
penampil_persegi.show_keliling(Persegi, perhitung_persegi)