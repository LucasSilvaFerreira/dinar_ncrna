import re
def orf_prediction(seq_in):
      sequencias_verso=[seq_in,
                        seq_in[1:len(seq_in)],
                        seq_in[2:len(seq_in)]]
      print sequencias_verso
      sequencias_reverso=[seq_in[::-1],
                        seq_in[0:len(seq_in)-1][::-1],
                        seq_in[0:len(seq_in)-2][::-1]]
      #print sequencias_reverso
      for sequencia_entrada in sequencias_verso:
            sequencia_vetor_3 = sequencia_entrada.find_all('...')
            position=0
            for seq in sequencia_vetor_3: 
                  if seq.find('TAC'):
                        print position
                        start= seq.find('TAC')
                        
                        if seq.find('ACT|ATT|ATC'):
                                    padrao = 'ACT|ATT|ATC'
                                    first_stop= re.search(padrao,seq[start+3:len(seq)]).group(0)
                                    stop =start+(seq[start+3:len(seq)].find(first_stop))
                                    print "start",start,"stop",stop
            position+=1



print orf_prediction("abcAAAAAAAAATACCAAATTAAAAAAAAAAAAAAAAAAAAACATabc")

