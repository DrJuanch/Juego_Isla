import re
import time
while True:
    contador = 0
    while True:
        main_Menu = input("Bienvenido al juego de la isla\n1) jugar \n2) Salir \n")
        x = re.search("[A-z03-9 ]",main_Menu)
        if x or not main_Menu:
            print("Opción incorrecta")
            input("Presione enter")
        else:
            break
    if "1" in main_Menu:
        while True:
            print("Acabas de naufragar por días y llegas a una isla desierta, llevas contigo un cuhillo y una cantimplora")
            time.sleep(2)
            print("Ves unas palmeras muy altas con cocos y una serpiente...\n")
            time.sleep(2)
            option1 = input("Piensa que debes comer cuando anochezca...\nElige\n1)Subir palmeras \n2)Cazar la serpiente\n")
            x = re.search("[A-z03-9 ]", option1)
            if x or not option1:
                print("Opc1ión incorrecta")
                input("Presione una tecla")
            else:
                break
        if "1" in option1:
            while True:
                print("...BORING...")
                time.sleep(2)
                print("Consigues unos cuantos cocos y pasa la noche...")
                time.sleep(2)
                print("La mañana siguiente decides caminar, das una vuelta por los alrededores y te das cuenta que hay una montaña bastante alta\nTe preguntas si puedes ver algo que sea de utilidad pero te ma miedo escalarla, se ve peligrosa")
                time.sleep(7)
                option2 = input("Tienes bastantes nervios pero crees que puede ser una oportunidad\n1)Decides escalarla\n2)Te quedas a salvo en tierra comiendo coquito :3\n")
                x = re.search("[A-z03-9 ]", option2)
                if x or not option1:
                    print("Opción incorrecta")
                    input("Presione enter")
                else:
                    break
            if "1" in option2:
                print("Decides escalar, llevas tu cuchullo y tu cantimplora, sabes que te espera una dura prueba")
                time.sleep(5)
                print("Duras horas subiendo, pero lo logras, ves pasar una avioneta muy cerca del mar")
                time.sleep(4)
                print("sacas tu cuchillo para que el reflejo del sol lo vea el piloto")
                time.sleep(4)
                print("No te ve... o eso es lo que crees")
                time.sleep(3)
                print("Bajas de la montaña, pasan los días y pierdes la esperanza que el piloto te haya visto\nDe repente ves como un barco de tamaño mediano con una cruz roja en su estandarte...\nSientes un gran alivio por que sabes que el piloto te vió y vienen a rescatarte")
                time.sleep(15)
                print("Felicidades ganaste el juego, el movimiento humanitario cruz roja ¡TE HA RESCATADO!")
            if "2" in option2:
                print("...BORING...")
                time.sleep(2)
                print("Decides no correr el riesgo de subir la montaña")
                time.sleep(3)
                print("...Eres un hombre que no toma riesgos, tal vez eso no pueda sacarte de está isla...")
                while contador <= 1:
                    option5_int = 0
                    while True:
                        time.sleep(5)
                        option3 = input("Encuentras un camino en una vegetación, lo recorres por una hora y el camino se divide en 2 ¿elige?\n1)Izquierda\n2)Derrecha\n")
                        x = re.search("[A-z03-9 ]", option3)
                        if x or not option3:
                            print("Opció n incorrecta")
                            input("Presione enter")
                        else:
                            break
                    if "1" in option3:
                        print("Elegiste la izquierda, caminas... un animal te asusta y sales cocrriendo, no te percatas y caes en hueco")
                        time.sleep(4)
                        print("Has muerto")
                        contador += 1
                    if "2" in option3:
                        while contador <= 1:
                            while True:
                                print("Elegiste la derecha, caminas...")
                                time.sleep(3)
                                option4 = input("ves una tribu... elige\n1)Hablarles\n2)Ignorarlos\n")
                                x = re.search("[A-z03-9 ]", option4)
                                if x or not option4:
                                    print("Opción incorrecta")
                                    input("Presione enter")
                                else:
                                    break
                            if "1" in option4:
                                print("Decides hablarles... Te acercas con cuidado y demostrando que no quieres problemas...\nEmpiezas a hablar pero notas que no hablan tu lengua, de repente sientes un frío metal penetrar tu cuerpo en el costado derecho de tu torso...\nEres usado en una cerominia\n")
                                time.sleep(15)
                                print("Te percartas de que estas personas quieren comerte, ¡son canivales!")
                                time.sleep(4)
                                print("Has muerto")
                                contador += 1
                            if "2" in option4:
                                while contador <= 1:
                                    while True:
                                        print("Decides retirarte ya que notas algo raro en estas personas")
                                        time.sleep(5)
                                        print("Caminas unas horas y ves una avioneta pasar volando bajo, piensas que hubiese sido bueno escalar aquella montaña...\n")
                                        time.sleep(7)
                                        option5 = input("Ves un monton de madera y se te ocurre que sería bueno hacer una balsa e intentar escapar de la isla, elige\n1)Hacer la balsa e intentar escapar\n2)Quedarte y esperar una mejor idea\n")
                                        x = re.search("[A-z03-9 ]", option5)
                                        if x or not option5:
                                            print("Opción incorrecta")
                                            input("Presione enter")
                                        else:
                                            option5_int = int(option5)
                                            break
                                    if option5_int == 1:
                                        time.sleep(1)
                                        print("Pasan los días y terminas tu balsa... Te embarcas en el sol naciente del siguiente día\n")
                                        time.sleep(5)
                                        print("Es una gran aventura donde luchas con un tiburon y te salvas dandole puños al rostro")
                                        time.sleep(7)
                                        print("Pasas tormentas que crees que te botaran de la balsa pero eres persistente y no lo hacen")
                                        time.sleep(7)
                                        print("Llegas a un puerto")
                                        time.sleep(2)
                                        print("Te has salvado, piensas que fué un camino largo, pero valió la pena la experiencia")
                                        break
                                    if option5_int == 2:
                                        print("...BORING...")
                                        time.sleep(2)
                                        print("Decides esperar que se te ocurra otra idea, llega la noche y prendes una fogata\n")
                                        time.sleep(5)
                                        print("empiezas a escuchar un montón de ruido viniendo hacia ti, te das cuenta que no te alejaste lo suficiente de aquella tribu y te descubrieron por el humo")
                                        time.sleep(8)
                                        print("Eres cazado y devorado por aquella tribu de canivales, has muerto!")
                                        contador += 1
                            if option5_int == 1:
                                break
                    if option5_int == 1:
                        break
        if "2" in option1:
            while True:
                print("Decides cazar la serpiente, casi sales herido, pero tienes un buen botín ya que la carne de la serpiente es rica en proteinas")
                time.sleep(4)
                print("La mañana siguiente decides caminar, das una vuelta por los alrededores y te das cuenta que hay una montaña bastante alta\nTe preguntas si puedes ver algo que sea de utilidad pero te ma miedo escalarla, se ve peligrosa")
                time.sleep(7)
                option2 = input("Tienes bastantes nervios pero crees que puede ser una oportunidad\n1)Decides escalarla\n2)Te quedas a salvo en tierra comiendo coquito :3\n")
                x = re.search("[A-z03-9 ]", option2)
                if x or not option1:
                    print("Opción incorrecta")
                    input("Presione enter")
                else:
                    break
            if "1" in option2:
                print("Decides escalar, llevas tu cuchullo y tu cantimplora, sabes que te espera una dura prueba")
                time.sleep(5)
                print("Duras horas subiendo, pero lo logras, ves pasar una avioneta muy cerca del mar")
                time.sleep(4)
                print("sacas tu cuchillo para que el reflejo del sol lo vea el piloto")
                time.sleep(4)
                print("No te ve... o eso es lo que crees")
                time.sleep(3)
                print("Bajas de la montaña, pasan los días y pierdes la esperanza que el piloto te haya visto\nDe repente ves como un barco de tamaño mediano con una cruz roja en su estandarte...\nSientes un gran alivio por que sabes que el piloto te vió y vienen a rescatarte")
                time.sleep(15)
                print("Felicidades ganaste el juego, el movimiento humanitario cruz roja ¡TE HA RESCATADO!")
            if "2" in option2:
                print("...BORING...")
                time.sleep(2)
                print("Decides no correr el riesgo de subir la montaña")
                time.sleep(3)
                print("...Eres un hombre que no toma riesgos, tal vez eso no pueda sacarte de está isla...")
                while contador <= 1:
                    option5_int = 0
                    while True:
                        time.sleep(5)
                        option3 = input("Encuentras un camino en una vegetación, lo recorres por una hora y el camino se divide en 2 ¿elige?\n1)Izquierda\n2)Derrecha\n")
                        x = re.search("[A-z03-9 ]", option3)
                        if x or not option3:
                            print("Opció n incorrecta")
                            input("Presione enter")
                        else:
                            break
                    if "1" in option3:
                        print("Elegiste la izquierda, caminas... un animal te asusta y sales cocrriendo, no te percatas y caes en hueco")
                        time.sleep(4)
                        print("Has muerto")
                        contador += 1
                    if "2" in option3:
                        while contador <= 1:
                            while True:
                                print("Elegiste la derecha, caminas...")
                                time.sleep(3)
                                option4 = input("ves una tribu... elige\n1)Hablarles\n2)Ignorarlos\n")
                                x = re.search("[A-z03-9 ]", option4)
                                if x or not option4:
                                    print("Opción incorrecta")
                                    input("Presione enter")
                                else:
                                    break
                            if "1" in option4:
                                print("Decides hablarles... Te acercas con cuidado y demostrando que no quieres problemas...\nEmpiezas a hablar pero notas que no hablan tu lengua, de repente sientes un frío metal penetrar tu cuerpo en el costado derecho de tu torso...\nEres usado en una cerominia\n")
                                time.sleep(15)
                                print("Te percartas de que estas personas quieren comerte, ¡son canivales!")
                                time.sleep(6)
                                print("Has muerto")
                                contador += 1
                            if "2" in option4:
                                while contador <= 1:
                                    while True:
                                        print("Decides retirarte ya que notas algo raro en estas personas")
                                        time.sleep(5)
                                        print("Caminas unas horas y ves una avioneta pasar volando bajo, piensas que hubiese sido bueno escalar aquella montaña...\n")
                                        time.sleep(7)
                                        option5 = input("Ves un monton de madera y se te ocurre que sería bueno hacer una balsa e intentar escapar de la isla, elige\n1)Hacer la balsa e intentar escapar\n2)Quedarte y esperar una mejor idea\n")
                                        x = re.search("[A-z03-9 ]", option5)
                                        if x or not option5:
                                            print("Opción incorrecta")
                                            input("Presione enter")
                                        else:
                                            option5_int = int(option5)
                                            break
                                    if option5_int == 1:
                                        time.sleep(1)
                                        print("Pasan los días y terminas tu balsa... Te embarcas en el sol naciente del siguiente día\n")
                                        time.sleep(5)
                                        print("Es una gran aventura donde luchas con un tiburon y te salvas dandole puños al rostro")
                                        time.sleep(7)
                                        print("Pasas tormentas que crees que te botaran de la balsa pero eres persistente y no lo hacen")
                                        time.sleep(7)
                                        print("Llegas a un puerto")
                                        time.sleep(2)
                                        print("Te has salvado, piensas que fué un camino largo, pero valió la pena la experiencia")
                                        break
                                    if option5_int == 2:
                                        print("...BORING...")
                                        time.sleep(2)
                                        print("Decides esperar que se te ocurra otra idea, llega la noche y prendes una fogata\n")
                                        time.sleep(5)
                                        print("empiezas a escuchar un montón de ruido viniendo hacia ti, te das cuenta que no te alejaste lo suficiente de aquella tribu y te descubrieron por el humo")
                                        time.sleep(8)
                                        print("Eres cazado y devorado por aquella tribu de canivales, has muerto!")
                                        contador += 1
                            if option5_int == 1:
                                break
                    if option5_int == 1:
                        break
    if "2" in main_Menu:
        print("Gracias por jugar, ¡vuelve pronto!")
        break
    if contador == 2:
        print("Has perdido tus posibles oportunidades, vuelve a intentarlo desde el inicio.")
        print('Quizá deberías ser más arriesgado\n"El que no arriesga no gana"')
        input("Presiona enter para volver al menú inicial")
    else:
        print("¡HAS GANADO!, tu valentía y coraje te han traido hasta acá")
        input("Presiona enter para volver al menú inicial")