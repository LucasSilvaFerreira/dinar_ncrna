import re
import numpy
class Tfbp:
  def __init__ (self,arquivo1,arquivo2,saida):
    self.tfbp_main = open(arquivo1, 'r').read()  # to save and real all lines in the same time
    self.tfbp_query = open(arquivo2, 'r').read()  # to save and real all lines in the same time
    self.saida = open(saida,'w')
    self.saida.write("chomossome \t position1 \t position2 \t GenomeBrowser \t mean \t standart Devitation\n")
  def find(self):
      
      
      for linha in re.split('\n', self.tfbp_main):
        linha=re.sub(r".$", "", linha)
        #print ("<"+linha+">")
        cordenada = re.search(r'^\d*\s*(\w*)\s*(\w*)', linha)
        peak_main = re.search(r'([0-9]*)$',linha)
        
        #print ("<"+   re.search(r'(\d*)$',linha).group(1)  +">")
        cromossomo = cordenada.group(1)
        if cordenada and cordenada.group(2):
            posicao_main = cordenada.group(2)
            for query in re.split('\n',self.tfbp_query):
                cordenada_query = re.search('^\d*\s*(\w*)\s*(\w*)\s*',query) 
                if cordenada_query and cordenada_query.group(2):
                    query=re.sub(r".$", "", query)
                    posicao_query = cordenada_query.group(2)
                    peak_query = re.search(r'(\d*)$', query)
                    if len(posicao_query) > 1 and len(posicao_main) > 1 : 
                        valor_final = abs(int(posicao_main) - int(posicao_query))  
                        if valor_final < 2000 and cromossomo == cordenada_query.group(1):
                          lista = sorted([posicao_main, posicao_query])
                          if len(peak_main.group(1))>0:
                            #print ("--"+peak_query.group(1)+"--")
                            media = (int(peak_main.group(1)) + int(peak_query.group(1)))/2
                            stdr = numpy.std([int(peak_main.group(1)) , int(peak_query.group(1))], 0)
                            print (cromossomo + ':\t' + posicao_main + '\t' + posicao_query + '\t' + cromossomo + ':' + str(int(lista[0])) + "-" + str(int(lista[1])) + "\t" + str(media)+"\t"+ str(stdr))
                            self.saida.write(cromossomo + ':\t' + posicao_main + '\t' + posicao_query + '\t' + cromossomo + ':' + str(int(lista[0])) + "-" + str(int(lista[1])) + "\t" + str(media)+"\t"+ str(stdr)+"\n")
      self.saida.close()
      


testando =Tfbp('sta3.txt.txt','tr4.txt.txt','stat3_tr4.txt')
testando2 =Tfbp('ap2a.txt.txt','tr4.txt.txt','ap2a_tr4.txt')
testando3 =Tfbp('ap2g.txt.txt','tr4.txt.txt','ap2g_tr4.txt')
testando.find()
testando2.find()
testando3.find()

     
                     
