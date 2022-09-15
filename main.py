dias = int(input("Digite o numero de dias que você passou no hospital: "))

quarto = (input("Digite o quarto que você ficou hospedado(particular, semi particular \n ou coletivo? \n"))

usouwifi = (input("Você usou wifi?(sim ou não)"))

usoutv = (input("Você usou a TV?"))

particular = 360.00
semi =  210.00
coletivo = 185.00
wifi = 3.00
tv = 4.00
total = 0

if quarto == str("particular"):
    
    print("Tipo de quarto:..... Particular \n"
    "Diárias:............", str(particular * dias))
    
    total = total + (particular * dias)

elif quarto == str("semi particular"):
          
    print("Tipo de quarto:..... Semi Particular \n"
    "Diárias:............", str(semi * dias))

    total = total + (semi * dias)

elif quarto == str("coletivo"):
              
    print("Tipo de quarto:..... Coletivo \n"
    "Diárias:............", str(coletivo * dias))
    
    total = (coletivo * dias)

if usouwifi == str("sim"):
    print ("WIFI:............... 3,00")

    total = total + 3

if usoutv == str("sim"):
    print ("TV a cabo:.......... 4,00")

    total = total + 4

if total > 0:
    print ("Total: ", total)





    





          
