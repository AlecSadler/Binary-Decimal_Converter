import guizero

# DECIMAL -> BINARY PROCEDURE
def dec_bin():
    n=text_box1.get()
    q=int(n)
    binary=str()
    while q>1:
        mod_n=int(q%2)
        q=q/2
        binary=str(mod_n)+binary
    output_box1.value=binary
    return None

# BINARY -> DECIMAL PROCEDURE
def bin_dec():
    n = text_box2.get()
    n_str=str(n)
    # CHECKS IF INPUT NUMBER IS BINARY
    for w in n_str:
        if w!="0" and w!="1":
            guizero.warn("Error 01","NUMERO NON BINARIO!") #ALERT WINDOW
            text_box2.clear()
            break
        else:
            decimal=int(0)
            i=len(n_str)-1
            k=0
            while i>=0:
                decimal=decimal+(int(n_str[k])*(2**i))
                i=i-1
                k=k+1
            output_box2.value=decimal
    return None

# CLEAR ALL APPLET FIELDS (CLEAR BUTTON)
def clear():
    text_box1.clear()
    text_box2.clear()
    output_box2.clear()
    output_box1.clear()
    return None

# MAIN WINDOW
applet=guizero.App(title='Binary Converter',bg='#dffce8')
title_box=guizero.Box(applet,width='fill',align='top')
title= guizero.Text(title_box,color='red',text='CONVERTITORE BINARIO/DECIMALE',size=18)
space1=guizero.Text(title_box)
clear_btn = guizero.PushButton(applet,align='bottom',width='fill',text='Azzera Campi',command=clear)

# DECIMAL TO BINARY FRAME
binary_box=guizero.Box(applet,width='fill',layout='grid',align='top')
intr1= guizero.Text(binary_box,text='Inserire cifra decimale da convertire:',color='blue',grid=[0,0],size=14)
text_box1= guizero.TextBox(binary_box,grid=[1,0],width='fill')
output_txt2= guizero.Text(binary_box,text='Cifra binaria:',color='blue',grid=[0,1],size=14)
output_box1= guizero.TextBox(binary_box,grid=[1,1],width='fill',align='top')
button1= guizero.PushButton(binary_box,text='Converti',command=dec_bin,grid=[1,2])

# BINARY TO DECIMAL FRAME
decimal_box=guizero.Box(applet,width='fill',layout='grid',align='top')
space2=guizero.Text(decimal_box,grid=[0,0])
intr2= guizero.Text(decimal_box,text='Inserire cifra binaria da convertire:   ',color='blue',grid=[0,2],size=14)
text_box2= guizero.TextBox(decimal_box,grid=[1,2],width='fill')
output_txt2= guizero.Text(decimal_box,text='Cifra decimale:   ',color='blue',grid=[0,3],size=14)
button2= guizero.PushButton(decimal_box,text='Converti',command=bin_dec,grid=[1,4])
output_box2= guizero.TextBox(decimal_box,grid=[1,3],width='fill',align='top')

applet.display()


