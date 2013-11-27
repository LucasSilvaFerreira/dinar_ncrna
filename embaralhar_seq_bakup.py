import re
import random
from matplotlib.pyplot import hist
def embaralhar (sequencia,size_nucleotideo):
            """
            Retorna um vetor 'V' e uma string  'S' com o a sequencia embaralhada, por uma quantidade 'X' de nucleotideos
            definidas pelo usuario 
            """
            sequencia=sequencia
            size_nucleotideo = size_nucleotideo
            #vetor =re.split('.{'+str(size_nucleotideo)+'}',sequencia )
            vetor = re.findall('.{'+str(size_nucleotideo)+'}',sequencia )
            vetor_result_orf_size=[]
            
            random.shuffle(vetor)
            #print vetor
            contador=1
            encontrado=False
            #print ('entrando')
            vetor_ATG=[]
            encontrar_ATG=0
            for trinca in vetor:
                if re.match('ATG',trinca):
                    vetor_ATG.append(encontrar_ATG)
                encontrar_ATG+=1

            print 'atgs->',vetor_ATG

            for atg_diferente in vetor_ATG:
                
            for start in vetor:
                if re.match('ATG',start) and encontrado==False:
                    print(re.findall('ATG',start))
                    print ('primeiro')
                    print contador
                    position_start=contador
                    #print contador,start
                    end_contador=1
                    for end in vetor[position_start:len(vetor)]:
                          if re.match('(TAA|TAG|TGA)',end):
                                #print 'size:',end_contador
                                vetor_result_orf_size.append(end_contador)
                                saida.write(str(end_contador)+'\n')
                                #print position_start,end_contador,end
                                encontrado=True
                                break

                          end_contador+=1


                contador+=1
            string_conct = ''.join(vetor)
            #print string_conct
            return string_conct

        #return vetor
saida=open ('dinar_ncrna_1000_embaralhado_1_so.txt','w')

def orf_prediction(seq_in):
      sequencias_verso=[seq_in,
                        seq_in[1:len(seq_in)],
                        seq_in[2:len(seq_in)],
                        seq_in[::-1],
                        seq_in[0:len(seq_in)-1][::-1],
                        seq_in[0:len(seq_in)-2][::-1]]
      return sequencias_verso
### nao esta funcionando
vetor_result_orf_size=[]
dinar_rna=open('ncrna_dinar.txt','r').read()

for provaveis_orfs in  orf_prediction(dinar_rna):
      #print provaveis_orfs
      for teste in range(1,2):

            s =embaralhar(provaveis_orfs,3)
            print s
            
            saida.write(s+'\n')

saida.close()



