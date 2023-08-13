class Control:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        #del self.session["sumary"]
        self.carro = self.session.get("sumary")
        if not self.carro:
            self.session["sumary"] = {}
        if self.carro == None:
            self.carro = {}
        else:
            self.carro =self.carro

            
            
            
        
    def additems(self,**kwargs):
        __val= 0

        if  'id' not in self.carro.keys():
            self.carro['id'] = {
                'ids':0,
            }
            
            
         
        else:
            for key, value in self.carro.items():
                if key == 'id':
                    __val = value['ids']+1
                    value['ids'] = value['ids'] +1
                    
                
            if  __val not in self.carro.keys():
                self.carro[__val] = {
                    'controlfor':__val,
                    'control': str(__val)+ 'input'
                }
        
            
        self.save()
        
    def deleteseccion(self, **kwargs):
        del self.session["sumary"]
    
    def save(self):
        
        self.session["sumary"] = self.carro
        self.session.modified = True
        
        

