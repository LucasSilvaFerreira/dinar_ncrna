import re
class Genes_proximos:
    def __init__(self,file,start,end,window):
      self.abrir_arquivo=open(file,'r').read()
      self.start=start-window
      self.end=end+window
      self.window=window
      self.contador=1
      self.minha_hash={}
      self.concactenar=""
    def procurar(self):
      
      for leitura in re.split('\n',self.abrir_arquivo):
        if (len(leitura)>0):
          procura = re.search(r'\d*\t+\w*\t+\w*\t+.\t*(\w*)\t(\w*)\t.*$', leitura)
          int_converter1 = re.search(r'(\d*)', procura.group(1))
          int_converter2 = re.search(r'(\d*)', procura.group(2))
          if int_converter1.group(1) and int_converter2.group(1) :
          # print ("<"+procura.group(1)+">")
            inicio = int(int_converter1.group(1)) 
            fim = int(int_converter2.group(1)) 
          # print (inicio+fim)
          
            if(inicio >= int(self.start) and inicio <= int(self.end)):
            # print('ok')
            
              refseq = re.search(r'([\w,+-]*\t){13}([\w,+-]*)', leitura)
            # refseq=re.search(r'[\w,+-]*\t[\w,+-]*\t[\w,+-]*\t[\w,+-]*\t[\w,+-]*\t[\w,+-]*\t[\w,+-]*\t[\w,+-]*\t[\w,+-]*\t[\w,+]*\t[\w,+-]*\t[\w,+-]*\t([\w,+-]*)',leitura)
            
            # print (refseq.group(1))
              self.minha_hash[refseq.group(1)] = str(inicio) +"-" + str(fim)
              
            if(fim >= int(self.start) and fim <= int(self.end)):
            # print('ok')
            
              refseq = re.search(r'([\w,+-]*\t){13}([\w,+-]*)', leitura)
            # refseq=re.search(r'[\w,+-]*\t[\w,+-]*\t[\w,+-]*\t[\w,+-]*\t[\w,+-]*\t[\w,+-]*\t[\w,+-]*\t[\w,+-]*\t[\w,+-]*\t[\w,+]*\t[\w,+-]*\t[\w,+-]*\t([\w,+-]*)',leitura)
            
            # print (refseq.group(1))
              self.minha_hash[refseq.group(1)] = str(inicio) +"-" + str(fim)       
      for chave in self.minha_hash:
          #print(chave + "  " + str(self.minha_hash[chave]))  
          self.concactenar=self.concactenar+","+chave
          
      return(re.sub('(^,|\s)', "",self.concactenar))


#felipe= Genes_proximos('rfseq.txt', 1000, 2000, 10000)
#print felipe.procurar()