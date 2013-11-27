import re
import numpy
import Genes_proximos
arquivo = 'ap2a.txt.txt'
arquivo2 = 'sta3.txt.txt'
arquivo3 = 'tr4.txt.txt'
tfbp_main = open(arquivo, 'r').read()  # to save and real all lines in the same time
tfbp_query = open(arquivo2, 'r').read()  # to save and real all lines in the same time
tfbp_query2 = open(arquivo3, 'r').read()
saida = open("ap2a_sta3_tr4.txt",'w')
saida.write("chomossome \t position1 \t position2 \t position3 \t GenomeBrowser \t mean \t standart Devitation \t genes in window\n")

print("chromossome \t position1 \t position2 \t position3 \t GenomeBrowser \t mean \t standart Devitation \t genes in window")
for linha in re.split('\n', tfbp_main):
    linha = re.sub(r".$", "", linha)
    cordenada = re.search(r'^\d*\s*(\w*)\s*(\w*).*(\d*)$', linha)
    peak_main = re.search(r'(\d*)$', linha)
    cromossomo = cordenada.group(1)
    # print (peak_main.group(1))
    if cordenada and cordenada.group(2):
        posicao_main = cordenada.group(2)
        
        for query in re.split('\n', tfbp_query):
            query = re.sub(r".$", "", query)
          
            cordenada_query = re.search('^\d*\s*(\w*)\s*(\w*)\s*', query)
            
            if cordenada_query and cordenada_query.group(2):
                posicao_query = cordenada_query.group(2)
                peak_query = re.search(r'(\d*)$', query)
                if len(posicao_query) > 1 and len(posicao_main) > 1 : 
                    valor_final = abs(int(posicao_main) - int(posicao_query))  
                    if valor_final < 2000 and cromossomo == cordenada_query.group(1):
                      for query2 in re.split('\n', tfbp_query2):
                            query2 = re.sub(r".$", "", query2)
                            cordenada_query2 = re.search('^\d*\s*(\w*)\s*(\w*)\s*', query2)
                            if cordenada_query2 and cordenada_query2.group(2):
                              peak_query2 = re.search(r'(\d*)$', query2)
                              posicao_query2 = cordenada_query2.group(2)
                              if len(posicao_query2) > 1 and len(posicao_main) > 1 :
                                  valor_final2 = abs(int(posicao_main) - int(posicao_query2))
                                  if valor_final2 < 2000 and cromossomo == cordenada_query2.group(1):
                                    lista = sorted([posicao_main, posicao_query, posicao_query2])
                                    media = (int(peak_main.group(1)) + int(peak_query.group(1)) + int(peak_query2.group(1))) / 3
                                    stdr = numpy.round(numpy.std([int(peak_main.group(1)), int(peak_query.group(1)), int(peak_query2.group(1))], 0), 2) 
                                    genes = Genes_proximos.Genes_proximos('rfseq.txt',int(lista[0]),int(lista[02]),10000)
                                    print (cromossomo + ':\t' + posicao_main + '\t' + posicao_query + '\t' + posicao_query2 + '\t' + cromossomo + ':' + str(int(lista[0])) + "-" + str(int(lista[2])) + "\t" + str(media) + "\t" + str(stdr)+ '\t' +genes.procurar())
                                    saida.write(cromossomo + ':\t' + posicao_main + '\t' + posicao_query + '\t' + posicao_query2 + '\t' + cromossomo + ':' + str(int(lista[0])) + "-" + str(int(lista[2])) + "\t" + str(media) + "\t" + str(stdr)+ '\t' + genes.procurar()+"\n")
                                    

saida.close()		
			          
