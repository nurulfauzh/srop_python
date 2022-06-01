from typing_extensions import Self


class Balok:
    
    def __init__(self,panjang,lebar,tinggi:float):
        self.__panjang=panjang 
        self.__lebar= lebar
        self.__tinggi=tinggi  
        
        
    def get_panjang(self)-> float:
        return self.__panjang
    
    def set_panjang(panjang:float):
        Self.__panjang=panjang
    
    def get_lebar(self)-> float:
        return self.__lebar
    
    def set_lebar(lebar:float):
        Self.__lebar=lebar
    
    def get_tinggi(self)-> float:
        return self.__tinggi
    
    
    def set_tinggi(tinggi:float): 
        Self.__tinggi=tinggi
            