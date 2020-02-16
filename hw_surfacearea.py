import math
def surface_area(num1):
    return(4*math.pi*num1**2)
print(surface_area(5))
print(surface_area(3959))
def num_colorados(num1):
    return(num1/104185)
print(num_colorados(196961284.33723968))
print("Mercury:", surface_area(1516),"Number of Colorados:",num_colorados(28880736.662674654))
print("Venus:", surface_area(3760),"Number of Colorados:",num_colorados(177658321.19756424))
print("Earth:", surface_area(3959), "Number of Colorados:",num_colorados(196961284.33723968))
print("Mars:", surface_area(2110), "Number of Colorados:",num_colorados(55946738.61218847))
print("Jupiter:", surface_area(44423), "Number of Colorados:",num_colorados(55946738.61218847))
print("Saturn:", surface_area(37449), "Number of Colorados:",num_colorados(17623424993.97263))
print("Uranus:", surface_area(15882), "Number of Colorados:",num_colorados(3169715235.980562))
print("Neptune:", surface_area(15388), "Number of Colorados:",num_colorados(2975597733.8797226))
print("Pluto:", surface_area(743), "Number of Colorados:", num_colorados(6937252.331286367))
