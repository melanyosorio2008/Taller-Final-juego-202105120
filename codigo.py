import sys
import time
import random

# ==========================================
# ESTRUCTURA DE CLASES (POO)
# ==========================================

class Objeto:
    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor

class Arma(Objeto):
    def __init__(self, nombre, valor, puntos_ataque):
        super().__init__(nombre, valor)
        self.puntos_ataque = puntos_ataque

class Pocion(Objeto):
    def __init__(self, nombre, valor, curacion):
        super().__init__(nombre, valor)
        self.curacion = curacion

class Enemigo:
    def __init__(self, nombre, salud, ataque):
        self.nombre = nombre
        self.salud = salud
        self.ataque = ataque

    def atacar(self):
        return self.ataque

class Lobo(Enemigo):
    def __init__(self, salud=50, ataque=10):
        super().__init__("Lobo", salud, ataque)

class Esqueleto(Enemigo):
    def __init__(self, salud=80, ataque=15):
        super().__init__("Esqueleto", salud, ataque)

class JefeFinal(Enemigo):
    def __init__(self, salud=300, ataque=40):
        super().__init__("VirusX", salud, ataque)
        self.cristales_robados = 5

class Jugador:
    def __init__(self, nombre="Héroe"):
        self.nombre = nombre
        self.salud_max = 100
        self.salud = 100
        self.monedas = 50
        self.experiencia = 0
        self.inventario = [
            Arma("Espada de Madera", 10, 15),
            Pocion("Poción de Vida", 15, 30),
            Pocion("Poción de Vida", 15, 30)
        ]
        self.cristales_recuperados = 0

    def mostrar_inventario(self):
        print("\n" + "=" * 34)
        print("INVENTARIO INICIAL DEL JUGADOR")
        print("=" * 34)
        for idx, item in enumerate(self.inventario, 1):
            if isinstance(item, Arma):
                print(f"{idx}. {item.nombre} (Ataque: +{item.puntos_ataque})")
            elif isinstance(item, Pocion):
                print(f"{idx}. {item.nombre} (Curación: +{item.curacion})")
            else:
                print(f"{idx}. {item.nombre}")
        print(f"- Monedas de Oro: {self.monedas}")
        print("=" * 34)

# ==========================================
# MENÚ Y PANTALLA DE BIENVENIDA
# ==========================================

def mostrar_bienvenida():
    print("=" * 65)
    print("   ¡BIENVENIDO A MI VIDEOJUEGO: GUARDIANES DEL CÓDIGO!   ")
    print("=" * 65)
    print("Un mundo lleno de magia, misterios y grandes desafíos te espera.")
    print("Desarrollado para héroes y heroínas listos para salvar el reino.\n")
    time.sleep(1)

def configurar_dificultad():
    print("\n--- SELECCIÓN DE DIFICULTAD ---")
    print("1. Fácil (Para aprendices)")
    print("2. Normal (Para aventureros)")
    print("3. Difícil (Para verdaderos Guardianes)")
    dif = input("Elige la dificultad (1-3): ").strip()
    if dif in ["1", "2", "3"]:
        print("¡Dificultad actualizada correctamente!\n")
    else:
        print("Opción no válida. Se mantendrá la dificultad Normal.\n")

def mostrar_creditos():
    print("\n" + "=" * 40)
    print("CRÉDITOS DE GUARDIANES DEL CÓDIGO")
    print("=" * 40)
    print("- Desarrollo & Programación: Alan")
    print("- Público Objetivo: Niños de 8 a 12 años")
    print("- Motor: Python 3 / Visual Studio Code")
    print("=" * 40)
    input("\nPresiona ENTER para volver al menú...")

def mostrar_menu_principal(jugador):
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
            iniciar_nueva_partida(jugador)
            break
        elif opcion == "2":
            configurar_dificultad()
        elif opcion == "3":
            jugador.mostrar_inventario()
            input("\nPresiona ENTER para volver al menú...")
        elif opcion == "4":
            mostrar_creditos()
        elif opcion == "5":
            print("\n¡Gracias por jugar Guardianes del Código! Hasta pronto.")
            sys.exit()
        else:
            print("\nOpción no válida. Por favor, selecciona un número del 1 al 5.")

# ==========================================
# LÓGICA DE JUEGO (SEGÚN DIAGRAMA DE FLUJO)
# ==========================================

def combates_estrategia(jugador, enemigo):
    print(f"\n¡Un {enemigo.nombre} ha aparecido!")
    while enemigo.salud > 0 and jugador.salud > 0:
        print(f"\n--- TUS HP: {jugador.salud}/{jugador.salud_max} | HP {enemigo.nombre}: {enemigo.salud} ---")
        print("¿Tomar Estrategia de Combate?")
        print("1. Atacar con Arma")
        print("2. Usar Poción de Vida")
        
        eleccion = input("Selecciona tu acción (1-2): ").strip()
        
        if eleccion == "1":
            # Seleccionar arma adecuada
            armas = [item for item in jugador.inventario if isinstance(item, Arma)]
            arma_actual = armas[0] if armas else Arma("Puños", 0, 5)
            dano = arma_actual.puntos_ataque + random.randint(1, 5)
            enemigo.salud -= dano
            print(f"\n-> Atacas con {arma_actual.nombre} causando {dano} de daño.")
        elif eleccion == "2":
            # Usar poción de vida
            pociones = [item for item in jugador.inventario if isinstance(item, Pocion)]
            if pociones:
                pocion = pociones.pop(0)
                jugador.inventario.remove(pocion)
                jugador.salud = min(jugador.salud_max, jugador.salud + pocion.curacion)
                print(f"\n-> Te has curado {pocion.curacion} HP. HP actual: {jugador.salud}")
            else:
                print("\n-> ¡No tienes pociones disponibles!")
                continue
        else:
            print("\nOpción no válida, pierdes el turno.")

        if enemigo.salud > 0:
            dano_enemigo = enemigo.atacar()
            jugador.salud -= dano_enemigo
            print(f"-> El {enemigo.nombre} te ataca causando {dano_enemigo} de daño.")

    return jugador.salud > 0

def iniciar_nueva_partida(jugador):
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

    mundos = [
        "Mundo 1: Bosque Encantado",
        "Mundo 2: Cueva Misteriosa",
        "Mundo 3: Desierto Perdido",
        "Mundo 4: Ciudad Mecánica",
        "Mundo 5: Castillo Oscuro"
    ]

    nivel_global = 1
    for i, mundo in enumerate(mundos, 1):
        print(f"\n--------------------------------------------------")
        print(f"Cargando {mundo}...")
        print(f"--------------------------------------------------\n")
        time.sleep(1)

        for nivel in range(1, 6):
            while True:
                print(f"\n==========================================")
                print(f"   [ INICIO DEL NIVEL {nivel_global} (Nivel {nivel} del {mundo}) ]")
                print(f"==========================================")
                
                # Exploración / Ruta Secreta
                print("\nExplorando el mapa...")
                if random.choice([True, False]):
                    print("¡Encontraste una RUTA SECRETA / ATAJO! Acceso rápido y mejores premios.")
                    jugador.monedas += 20
                    print("¡Obtienes +20 monedas extra en la ruta secreta!")
                else:
                    print("Exploración regular del mapa completada.")

                # Encuentro con enemigo según el nivel
                if nivel < 5:
                    enemigo = Lobo() if i == 1 else Esqueleto()
                    derrotado = combates_estrategia(jugador, enemigo)
                else:
                    # Nivel Final del Mundo (Nivel 5, 10, 15, 20, 25) -> Batalla contra Jefe
                    print(f"\n¡ATENCIÓN! ¡Llegaste al nivel final del {mundo}!")
                    if i == 5:
                        print("¡BATALLA FINAL CONTRA VIRUSX!")
                        enemigo = JefeFinal()
                    else:
                        print("¡Batalla contra el Jefe del Mundo!")
                        enemigo = Esqueleto(salud=120, ataque=20)
                    derrotado = combates_estrategia(jugador, enemigo)

                if derrotado:
                    print("\n¡Enemigo Derrotado!")
                    # Obtener Recompensa
                    recompensa_monedas = random.randint(15, 30)
                    jugador.monedas += recompensa_monedas
                    jugador.experiencia += 50
                    print(f"-> Obtienes Recompensa: +{recompensa_monedas} Monedas, +50 Experiencia.")

                    if nivel == 5:
                        # Recuperar Cristal Mágico
                        jugador.cristales_recuperados += 1
                        print(f"\n¡RECUPERASTE UN CRISTAL MÁGICO! ({jugador.cristales_recuperados}/5)")
                        
                        if jugador.cristales_recuperados == 5:
                            print("\n" + "=" * 65)
                            print("           FINAL DEL JUEGO           ")
                            print("=" * 65)
                            print("¡VirusX ha sido derrotado y el mundo está a salvo!")
                            print("¡Has recuperado los 5 Cristales Mágicos!")
                            print("==========================================\n")
                            return
                        else:
                            print("¡Desbloqueando Siguiente Mundo y Avanzando!")

                    nivel_global += 1
                    break
                else:
                    print("\n[ El jugador pierde ]")
                    reintentar = input("¿Reintentar Nivel? (S/N): ").strip().upper()
                    if reintentar == "S":
                        jugador.salud = jugador.salud_max  # Restaurar salud para reintentar
                        print("\nReiniciando Nivel...")
                    else:
                        print("\nRegresando al Menú Principal...")
                        mostrar_menu_principal(jugador)
                        return

# ==========================================
# PUNTO DE ENTRADA
# ==========================================

if __name__ == "__main__":
    jugador_principal = Jugador()
    mostrar_bienvenida()
    mostrar_menu_principal(jugador_principal)