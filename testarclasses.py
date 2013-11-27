import Genes_proximos
import Multithread_find_tfbp
#teste = Genes_proximos.Genes_proximos('rfseq.txt',9827398,9827818,10000)
teste = Multithread_find_tfbp('rfseq.txt',9827398,9827818,10000)
saida=teste.procurar()
print(saida)


