# ACT 1

print("Ingrese los datos del cliente")

while True:
    nombre = input("Cliente: ")
    if nombre == "":
        print("Error: el nombre no puede quedar vacío.")
    elif not nombre.replace(" ", "").isalpha():
        print("Error: el nombre debe contener solo letras.")
    else:
        break

while True:
    cantidad = input("Cantidad de productos: ")
    if not cantidad.isdigit():
        print("Error: ingrese un número entero positivo.")
    else:
        cantidad_int = int(cantidad)
        if cantidad_int <= 0:
            print("Error: la cantidad debe ser mayor a 0.")
        else:
            break

cantidad = cantidad_int

total_sin_descuentos = 0
total_con_descuentos = 0

for i in range(1, cantidad + 1):
    while True:
        precio = input(f"Producto {i} - Precio: ")
        if not precio.isdigit():
            print("Error: ingrese un precio entero válido.")
        else:
            precio_int = int(precio)
            break

    while True:
        respuesta = input(f"Producto {i} - Descuento (S/N): ").lower()
        if respuesta not in ("s", "n"):
            print("Error: responda S o N.")
        else:
            tiene_descuento = respuesta == "s"
            break

    total_sin_descuentos += precio_int
    if tiene_descuento:
        total_con_descuentos += precio_int * 0.9
    else:
        total_con_descuentos += precio_int

ahorro = total_sin_descuentos - total_con_descuentos
promedio = float(total_con_descuentos) / cantidad

print(f"Cliente: {nombre}")
print(f"Cantidad de productos: {cantidad}")
print(f"Total sin descuentos: ${total_sin_descuentos}")
print(f"Total con descuentos: ${total_con_descuentos:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

# ACT 2

usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso = False
while intentos < 3:
    intentos += 1
    print(f"Intento {intentos}/3 - Usuario: alumno")
    usuario = input("Usuario: ")
    clave = input("Clave: ")
    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.")
        acceso = True
        break
    print("Error: credenciales inválidas.")

if not acceso:
    print("Cuenta bloqueada")
else:
    while True:
        print("1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
        opcion = input("Opción: ")
        if not opcion.isdigit():
            print("Error: ingrese un número válido.")
            continue
        opcion_int = int(opcion)
        if opcion_int < 1 or opcion_int > 4:
            print("Error: opción fuera de rango.")
            continue

        if opcion_int == 1:
            print("Inscripto")
        elif opcion_int == 2:
            while True:
                nueva_clave = input("Nueva clave: ")
                if len(nueva_clave) < 6:
                    print("Error: mínimo 6 caracteres.")
                    continue
                confirmacion = input("Confirmar nueva clave: ")
                if nueva_clave != confirmacion:
                    print("Error: las claves no coinciden.")
                    continue
                clave_correcta = nueva_clave
                print("Clave cambiada con éxito.")
                break
        elif opcion_int == 3:
            print("Seguí aprendiendo, vas por buen camino.")
        else:
            break

# ACT 3

print("\nAgenda de Turnos con Nombres")

while True:
    operador = input("Nombre del operador: ")
    if operador == "":
        print("Error: el nombre no puede quedar vacío.")
    elif not operador.isalpha():
        print("Error: el nombre debe contener solo letras.")
    else:
        break

lunes1 = lunes2 = lunes3 = lunes4 = ""
martes1 = martes2 = martes3 = ""

while True:
    print("\nMenú de opciones:")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")
    opcion = input("Opción: ")

    if not opcion.isdigit():
        print("Error: ingrese un número válido.")
        continue

    opcion_int = int(opcion)
    if opcion_int < 1 or opcion_int > 5:
        print("Error: opción fuera de rango.")
        continue

    if opcion_int == 5:
        print("Cerrando el sistema...")
        break

    if opcion_int == 1:
        while True:
            dia = input("Elegir día (1=Lunes, 2=Martes): ")
            if not dia.isdigit():
                print("Error: ingrese 1 o 2.")
                continue
            dia_int = int(dia)
            if dia_int not in (1, 2):
                print("Error: ingrese 1 o 2.")
                continue
            break

        while True:
            paciente = input("Nombre del paciente: ")
            if paciente == "":
                print("Error: el nombre no puede quedar vacío.")
            elif not paciente.isalpha():
                print("Error: el nombre debe contener solo letras.")
            else:
                break

        if dia_int == 1:
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("Error: el paciente ya tiene turno el lunes.")
            elif lunes1 == "":
                lunes1 = paciente
                print("Turno reservado en Lunes - Turno 1.")
            elif lunes2 == "":
                lunes2 = paciente
                print("Turno reservado en Lunes - Turno 2.")
            elif lunes3 == "":
                lunes3 = paciente
                print("Turno reservado en Lunes - Turno 3.")
            elif lunes4 == "":
                lunes4 = paciente
                print("Turno reservado en Lunes - Turno 4.")
            else:
                print("Error: no hay turnos libres para el lunes.")
        else:
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("Error: el paciente ya tiene turno el martes.")
            elif martes1 == "":
                martes1 = paciente
                print("Turno reservado en Martes - Turno 1.")
            elif martes2 == "":
                martes2 = paciente
                print("Turno reservado en Martes - Turno 2.")
            elif martes3 == "":
                martes3 = paciente
                print("Turno reservado en Martes - Turno 3.")
            else:
                print("Error: no hay turnos libres para el martes.")

    elif opcion_int == 2:
        while True:
            dia = input("Elegir día para cancelar (1=Lunes, 2=Martes): ")
            if not dia.isdigit():
                print("Error: ingrese 1 o 2.")
                continue
            dia_int = int(dia)
            if dia_int != 1 and dia_int != 2:
                print("Error: ingrese 1 o 2.")
                continue
            break

        while True:
            paciente = input("Nombre del paciente a cancelar: ")
            if paciente == "":
                print("Error: el nombre no puede quedar vacío.")
            elif not paciente.isalpha():
                print("Error: el nombre debe contener solo letras.")
            else:
                break

        encontrado = False
        if dia_int == 1:
            if lunes1 == paciente:
                lunes1 = ""
                encontrado = True
            elif lunes2 == paciente:
                lunes2 = ""
                encontrado = True
            elif lunes3 == paciente:
                lunes3 = ""
                encontrado = True
            elif lunes4 == paciente:
                lunes4 = ""
                encontrado = True
        else:
            if martes1 == paciente:
                martes1 = ""
                encontrado = True
            elif martes2 == paciente:
                martes2 = ""
                encontrado = True
            elif martes3 == paciente:
                martes3 = ""
                encontrado = True

        if encontrado:
            print("Turno cancelado con éxito.")
        else:
            print("Error: nombre no encontrado en ese día.")

    elif opcion_int == 3:
        while True:
            dia = input("Elegir día para ver agenda (1=Lunes, 2=Martes): ")
            if not dia.isdigit():
                print("Error: ingrese 1 o 2.")
                continue
            dia_int = int(dia)
            if dia_int != 1 and dia_int != 2:
                print("Error: ingrese 1 o 2.")
                continue
            break

        if dia_int == 1:
            print("\nAgenda de Lunes:")
            print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
            print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
            print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
            print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
        else:
            print("\nAgenda de Martes:")
            print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
            print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
            print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")

    else:
        lunes_ocupados = 0
        if lunes1 != "":
            lunes_ocupados += 1
        if lunes2 != "":
            lunes_ocupados += 1
        if lunes3 != "":
            lunes_ocupados += 1
        if lunes4 != "":
            lunes_ocupados += 1

        martes_ocupados = 0
        if martes1 != "":
            martes_ocupados += 1
        if martes2 != "":
            martes_ocupados += 1
        if martes3 != "":
            martes_ocupados += 1

        lunes_disponibles = 4 - lunes_ocupados
        martes_disponibles = 3 - martes_ocupados

        print("\nResumen general:")
        print(f"Lunes - Ocupados: {lunes_ocupados}, Disponibles: {lunes_disponibles}")
        print(f"Martes - Ocupados: {martes_ocupados}, Disponibles: {martes_disponibles}")

        if lunes_ocupados > martes_ocupados:
            print("Día con más turnos: Lunes")
        elif martes_ocupados > lunes_ocupados:
            print("Día con más turnos: Martes")
        else:
            print("Días con más turnos: empate")

# ACT 4

print("\nEscape Room: La Bóveda")

while True:
    agente = input("Nombre del agente: ")
    if agente == "":
        print("Error: el nombre no puede quedar vacío.")
    elif not agente.isalpha():
        print("Error: el nombre debe contener solo letras.")
    else:
        break

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
consecutivos_forzar = 0

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:
    print("\nEstado de la misión:")
    print(f"Energía: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}")
    print(f"Alarma: {'ON' if alarma else 'OFF'}")
    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("Opción: ")
    if not opcion.isdigit():
        print("Error: ingrese un número válido.")
        continue

    opcion_int = int(opcion)
    if opcion_int < 1 or opcion_int > 3:
        print("Error: opción fuera de rango.")
        continue

    if opcion_int == 1:
        energia -= 20
        tiempo -= 2
        consecutivos_forzar += 1

        if consecutivos_forzar == 3:
            alarma = True
            print("La cerradura se trabó y se activó la alarma.")
        else:
            if energia < 40:
                while True:
                    numero = input("Riesgo de alarma: elija un número del 1 al 3: ")
                    if not numero.isdigit():
                        print("Error: ingrese un número válido.")
                        continue
                    numero_int = int(numero)
                    if numero_int < 1 or numero_int > 3:
                        print("Error: ingrese 1, 2 o 3.")
                        continue
                    break

                if numero_int == 3:
                    alarma = True
                    print("Se activó la alarma durante el intento de fuerza.")

            if not alarma:
                cerraduras_abiertas += 1
                print("Forzaste una cerradura con éxito.")

    elif opcion_int == 2:
        energia -= 10
        tiempo -= 3
        consecutivos_forzar = 0
        print("Hackeando el panel...")
        for paso in range(1, 5):
            print(f"Paso {paso}/4")
            codigo_parcial += "A"

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("El código parcial abrió una cerradura.")
        else:
            print(f"Código parcial: {codigo_parcial}")

    else:
        consecutivos_forzar = 0
        tiempo -= 1
        energia += 15
        if energia > 100:
            energia = 100
        if alarma:
            energia -= 10
            print("Alarma activa: costo extra de energía.")
        print("Descansaste y recuperaste energía.")

    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("El sistema se bloqueó por alarma y tiempo crítico.")
        break

print("\nFin de la misión")
if cerraduras_abiertas == 3:
    print("VICTORIA: abriste la bóveda.")
elif alarma and tiempo <= 3 and cerraduras_abiertas < 3:
    print("DERROTA: bloqueo por alarma.")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA: te quedaste sin energía o tiempo.")
elif alarma:
    print("DERROTA: la alarma se activó.")
else:
    print("DERROTA: no lograste abrir la bóveda.")


# ACT 5

print("\n--- BIENVENIDO A LA ARENA ---")

while True:
    nombre_gladiador = input("Nombre del Gladiador: ")
    if nombre_gladiador == "" or not nombre_gladiador.isalpha():
        print("Error: Solo se permiten letras.")
    else:
        break

vida_gladiador = 100
vida_enemigo = 100
pociones = 3
ataque_pesado = 15
danio_enemigo = 12
turno_gladiador = True
juego_activo = True

print("=== INICIO DEL COMBATE ===")

while juego_activo and vida_gladiador > 0 and vida_enemigo > 0:
    if turno_gladiador:
        print(f"{nombre_gladiador} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
        print("Elige acción:")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")

        while True:
            opcion = input("Opción: ")
            if not opcion.isdigit():
                print("Error: Ingrese un número válido.")
                continue
            opcion_int = int(opcion)
            if opcion_int < 1 or opcion_int > 3:
                print("Error: Ingrese un número válido.")
                continue
            break

        if opcion_int == 1:
            if vida_enemigo < 20:
                danio_final = ataque_pesado * 1.5
                print(f"¡Atacaste al enemigo por {danio_final} puntos de daño!")
            else:
                danio_final = float(ataque_pesado)
                print(f"¡Atacaste al enemigo por {int(danio_final)} puntos de daño!")
            vida_enemigo -= int(danio_final)

        elif opcion_int == 2:
            print(">> ¡Inicias una ráfaga de golpes!")
            for _ in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")

        else:
            if pociones > 0:
                vida_gladiador += 30
                if vida_gladiador > 100:
                    vida_gladiador = 100
                pociones -= 1
                print("¡Usaste una poción y recuperaste 30 puntos de vida!")
            else:
                print("¡No quedan pociones!")

        turno_gladiador = False

    if vida_enemigo <= 0:
        break

    if not turno_gladiador and vida_enemigo > 0:
        vida_gladiador -= danio_enemigo
        print(f"¡El enemigo te atacó por {danio_enemigo} puntos de daño!")
        turno_gladiador = True

    if vida_gladiador <= 0:
        break

    if vida_enemigo > 0 and vida_gladiador > 0:
        print("=== NUEVO TURNO ===")

print("\n=== FIN DEL COMBATE ===")
if vida_gladiador > 0:
    print(f"¡VICTORIA! {nombre_gladiador} ha ganado la batalla.")
elif vida_gladiador <= 0:
    print("DERROTA. Has caído en combate.")