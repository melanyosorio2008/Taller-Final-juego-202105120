import sys
import time

# --- PANTALLA DE BIENVENIDA ---
def mostrar_bienvenida():
    print("=" * 65)
    print("   ¡BIENVENIDO A MI VIDEOJUEGO: GUARDIANES DEL CÓDIGO!   ")
    print("=" * 65)
    print("Un mundo lleno de magia, misterios y grandes desafíos te espera.")
    print("Desarrollado para héroes y heroínas listos para salvar el reino.\n")
    time.sleep(1)

# --- MENÚ PRINCIPAL INTERACTIVO ---
def mostrar_menu_principal():
    while True:
        print("\n" + "-" * 40)
        print("         MENÚ PRINCIPAL         ")
        print("-" * 40)
        print("1. Iniciar Nueva Partida")
        print("2. Ajustes / Dificultad")
        print("3. Ver Inventario Inicial")
        print("4. Créditos")
        print("5. Salir")
        print("-" * 40)
        
        opcion = input("Selecciona una opción (1-5): ").strip()
        
        if opcion == "1":
            iniciar_nueva_partida()
            break
        elif opcion == "2":
            configurar_dificultad()
        elif opcion == "3":
            mostrar_inventario()
        elif opcion == "4":
            mostrar_creditos()
        elif opcion == "5":
            print("\n¡Gracias por jugar Guardianes del Código! Hasta pronto.")
            sys.exit()
        else:
            print("\nOpción no válida. Por favor, selecciona un número del 1 al 5.")

# --- OPCIÓN 1: NUEVA PARTIDA Y FLUJO DEL DIAGRAMA ---
def iniciar_nueva_partida():
    # Introducción a la historia
    print("\n" + "=" * 65)
    print("INTRODUCCIÓN A LA HISTORIA")
    print("=" * 65)
    print("¡ALERTA EN EL REINO!")
    print("El villano VirusX ha irrumpido y robado los 5 Cristales Mágicos.")
    print("Tu misión: Explorar los 5 mundos, derrotar a sus esbirros y")
    print("recuperar los Cristales Mágicos antes de que sea demasiado tarde.")
    print("=" * 65 + "\n")
    
    input("Presiona ENTER para iniciar la carga del mundo...")
    
    # Carga del Mundo 1
    print("\n--------------------------------------------------")
    print("Cargando Mundo 1: Bosque Encantado...")
    print("Iniciando Nivel 1...")
    print("--------------------------------------------------\n")
    print("¡Has ingresado al Bosque Encantado! Prepárate para la aventura...")

# --- OPCIÓN 2: DIFICULTAD ---
def configurar_dificultad():
    print("\n--- SELECCIÓN DE DIFICULTAD ---")
    print("1. Fácil (Para aprendices)")
    print("2. Normal (Para aventureros)")
    print("3. Difícil (Para verdaderos Guardianes)")
    dif = input("Elige la dificultad (1-3): ")
    if dif in ["1", "2", "3"]:
        print("¡Dificultad actualizada correctamente!\n")
    else:
        print("Opción no válida. Se mantendrá la dificultad Normal.\n")

# --- OPCIÓN 3: INVENTARIO INICIAL ---
def mostrar_inventario():
    print("\n" + "="*34)
    print("INVENTARIO INICIAL DEL JUGADOR")
    print("="*34)
    print("- Espada de Madera (Arma Básica)")
    print("- Escudo de Cuero")
    print("- 2x Pociones de Vida")
    print("- Mapa del Bosque Encantado")
    print("- 50 Monedas de Oro")
    print("="*34)
    input("\nPresiona ENTER para volver al menú...")

# --- OPCIÓN 4: CRÉDITOS ---
def mostrar_creditos():
    print("\n" + "="*40)
    print("CRÉDITOS DE GUARDIANES DEL CÓDIGO")
    print("="*40)
    print("- Desarrollo & Programación: Alan")
    print("- Público Objetivo: Niños de 8 a 12 años")
    print("- Motor: Python 3 / Visual Studio Code")
    print("="*40)
    input("\nPresiona ENTER para volver al menú...")

# --- PUNTO DE ENTRADA ---
if __name__ == "__main__":
    mostrar_bienvenida()
    mostrar_menu_principal()