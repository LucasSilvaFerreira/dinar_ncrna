arquivo=read.delim('Dinar_embaralhado_1_so.txt')
arquivo<-as.numeric(as.matrix(arquivo))
hist((arquivo)*3,density=20)