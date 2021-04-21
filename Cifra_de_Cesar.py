#CIFRA DE CESAR RENÊ ANDRADE!!!
class Cesar:
   
   def __init__(self):
    self.letras= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
  
   def crip(self,texto_normal,chave=4):
      texto_cifrado= '  '
      texto_normal=texto_normal.upper()       
      for i in texto_normal:
         if i in self.letras:
            pos=self.letras.find(i)+chave                
            if pos >= 26:
               pos -= 26
            texto_cifrado += self.letras[pos]      
      return texto_cifrado

   
   def decrip(self, texto_cifrado, chave=-4):
      texto_normal= '  '
      texto_cifrado=texto_cifrado.upper()
      
      for i in texto_cifrado:
         if i in self.letras:
            pos=self.letras.find(i)+chave
            texto_normal += self.letras[pos]
      return texto_normal



print("------------------------------------------------------------------------------------")



continuar="s"
while continuar=="s":
   
   print ("você deseja criptagrafar 'c' ou deseja descriptografar 'd'")
   n1=input ()

   

   if (n1=="c"):   
      texto=Cesar()
      
      teste1=texto.crip(input('Digite alguma palavra : '))
      teste2=texto.decrip(teste1)
      print ('Cifrando o texto: ',teste1 )
      print ("você deseja continuar s/N")
      continuar=input ()


      

   if (n1=="d"):   
      texto=Cesar()

      teste1=texto.decrip(input('Digite alguma  palavra : '))

      print ('decifrando : ',teste1 )
      print ("você deseja continuar s/N")
      continuar=input ()
      
print("------------------------------------------------------------------------------------")



  
      
