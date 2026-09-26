# Taller-Final-juego-202105120
En este proyecto quiero crear un videojuego para la consola dirigido a niños y niñas de 8 a 12 años. Mi idea es que el jugador viva una aventura donde tenga que superar niveles, derrotar enemigos, conseguir premios y recoger objetos para completar el juego.
#FASE 1: REQUERIMIENTOS
Funcionales: Son las funciones que el videojuego debe realizar. 
El juego debe permitir iniciar una nueva partida. 
El jugador debe controlar un personaje principal. 
El juego debe contar con 25 niveles distribuidos en 5 mundos. 
El jugador debe enfrentarse a diferentes enemigos en cada mundo, incluyendo un jefe final llamado VirusX. 
El juego debe permitir recoger monedas, armas, pociones, llaves, armaduras e insignias como recompensas. 
No funcionales:Son las características de calidad que debe cumplir el videojuego. 
El juego debe tener una interfaz sencilla y fácil de usar para niños de 8 a 12 años. 
El tiempo de carga de cada nivel no debe superar los 5 segundos. 
El juego debe funcionar sin errores o bloqueos durante la partida. 
Los gráficos deben ser coloridos y atractivos. 
Los controles deben responder de forma rápida y precisa.
#FASE 2: ANÁLISIS
Hacer un juego divertido y fácil de entender, donde el jugador pueda aprender a pensar, tomar decisiones y resolver pequeños desafíos.
"FASE 3: DISEÑO (diagrama de flujo)
[ INICIO]
    │
    ▼
[ Menú Principal] ──► (Iniciar Nueva Partida)
    │
    ▼
[ Introducción a la Historia] (El villano VirusX roba los 5 Cristales Mágicos)
    │
    ▼
[ Carga del Mundo Actual] (Empieza en Mundo 1: Bosque Encantado)
    │
    ▼
[ Inicio del Nivel X] (Nivel 1 al 25)
    │
    ├──────────────────────────────────────────────────────┐
    ▼                                                      ▼
[ Exploración del Mapa]                           [ Ruta Secreta / Atajo ]
 (Buscar mapas y cofres escondidos)                (Acceso rápido / mejores premios)
    │                                                      │
    └──────────────────────────┬───────────────────────────┘
                               │
                               ▼
                    [ Encuentro con Enemigo ]
                               │
                               ▼
               ¿Tomar Estrategia de Combate?[cite: 1]
             ├── Seleccionar arma/armadura adecuada[cite: 1]
             └── Usar poción de vida si es necesario[cite: 1]
                               │
                               ▼
                     ¿Enemigo Derrotado?
                   /                     \
            ( NO ) /                       \ ( SÍ )
                  /                         \
                 ▼                           ▼
       [ El jugador pierde ]         [ Obtener Recompensa ][cite: 1]
                 │                   (Monedas, Experiencia, Llaves)[cite: 1]
                 ▼                           │
       ¿Reintentar Nivel?                    ▼
            /        \             ¿Es el Nivel Final del Mundo? (Nivel 5, 10, 15, 20, 25)
     (SÍ)  /          \ (NO)                /                                     \
          /            \             (NO)  /                                       \ (SÍ)
         ▼              ▼                 /                                         ▼
   [Reiniciar]     [Menú Principal]      ▼                                [ Batalla contra Jefe / VirusX ][cite: 1]
                                 [ Avanzar al siguiente ]                           │
                                   [ Nivel del Mundo ]                              ▼
                                                                           ¿Jefe Final Derrotado?
                                                                               /          \
                                                                        (NO)  /            \ (SÍ)
                                                                             /              ▼
                                                                            ▼       [ Recuperar Cristal Mágico ][cite: 1]
                                                                        [Reiniciar            │
                                                                         Nivel]               ▼
                                                                                   ¿Se recuperaron los 5 Cristales?[cite: 1]
                                                                                      /                       \
                                                                               (NO)  /                         \ (SÍ)
                                                                                    /                           ▼
                                                                                   ▼                     [ FINAL DEL JUEGO ]
                                                                       [ Desbloquear Siguiente ]         (¡VirusX derrotado y
                                                                       [   Mundo y Avanzar     ]          el mundo salvado!)[cite: 1]
#FASE 4: DESARROLLO SEGUN DIGRAMA DE FLUJO
El código constituye una excelente base arquitectónica para un prototipo de juego educativo o RPG de consola en Python. Aporta una estructura lógica modular que puede expandirse fácilmente agregando un sistema de combate turnado o integrando el inventario dinámico utilizando las clases ya definidas.
#FASE 5: CÓDIGO
El programa pasa de ser un borrador conceptual a un RPG de consola funcional en Python, adecuadamente estructurado mediante programación orientada a objetos y preparado para ser jugado de principio a fin.
#FASE 6: CREACION DE GITHUB
creamos nuestra cuenta y nuestro repositorio donde subimos todos los documentos
