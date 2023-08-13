class Register:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        
        cuentasxC = self.session.get("cuentas")
        if not cuentasxC:
            self.session["cuentas"] = {}
            print(self.session["cuentas"])
        
        if cuentasxC == None:
            self.cuentasxC = {}
        else:
            self.cuentasxC =cuentasxC
            
    def agregar(self, producto,**kwargs):
        print()
        id = str(producto.id)
       
        if  str(producto.id) not in self.cuentasxC.keys():
            self.cuentasxC[producto.id] = {
                'producto_id': producto.id,
                'nombre':producto.Titulo,
                'Moneda': producto. Moneda,
                'precio': producto.Precio,
                'acumulado': producto.Precio,
                'cantidad': 1, 
                'imagen': producto.Img.url,
            }
        else:
            for key, value in self.cuentasxC.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"]+1
                    value["acumulado"] = value["acumulado"]+producto.Precio
                    break

        
