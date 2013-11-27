import re
class gene:
      def __init__(self,id,sequencia):
            self.id=id
      
            self.sequencia=sequencia
            
      
      
      
      
      def size_s(self,fala):
            '''
            mostra o tamanho da sequencia
            '''
            print str(len(self.sequencia)) + fala


gene1= gene(23, 'atcgatcgatcgatcga')   
print gene1.id  
print gene1.sequencia 
gene1.size_s('      olaaa')

vetor_genes=[]
vetor_genes.append(gene1)
vetor_genes[0].size_s('      oii')
vetor_genes.append(gene(2, 'ccccccccc'))
genes = open('dinar_ncrna_1000_embaralhado.txt','r').read()
for linha in genes.split('\n'):
      if re.match('ACTG',linha):
            print linha