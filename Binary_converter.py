#DECIMAL-BINARY CONVERTER
repeat='Y'
print("CONVERTITORE DECIMALE/BINARIO\n")
while repeat == 'Y':
    conv_type=input("SELEZIONARE TIPO DI CONVERSIONE\nDECIMALE -> BINARIO (1) - BINARIO -> DECIMALE (2)\n")
    n=int(input("INSERIRE NUMERO DA CONVERTIRE: \n"))

    #DECIMAL -> BINARY
    if conv_type == "1":
        q=n
        binary=str()
        while q > 1:
            mod_n=int(q%2)
            q=q/2
            binary=str(mod_n) + binary
        print("IL NUMERO", n, "CONVERTITO IN BINARIO E': ", binary)
    #BINARY -> DECIMAL
    elif conv_type == "2":
        n_str=str(n)
        for w in n_str:
            if w != "0" and w != "1":
                print("NUMERO NON BINARIO!")
                exit()
        decimal=int(0)
        i=len(n_str)-1
        k=0
        while i>=0:
            decimal=decimal+(int(n_str[k])*(2**i))
            i=i-1
            k=k+1
        print("IL NUMERO",n,"CONVERTITO IN DECIMALE E': ",decimal)
    else:
        print("SCELTA NON VALIDA")
    repeat=input("VUOI ESEGUIRE UN'ALTRA CONVERSIONE? Y/N\n")
      
      
      
      
      
      
      

