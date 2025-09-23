# ESP32 + TTP223 en Caminadora (Control VR)

Este proyecto utiliza una ESP32 y dos sensores táctiles TTP223 montados en una caminadora para controlar un escenario en Unreal Engine mediante emulación de teclado.

# Funcionamiento

El usuario toca los sensores capacitivos para enviar señales binarias:
 00 → No se mueve
  
  01 → Mover a la derecha
  
  10 → Mover a la izquierda

La ESP32 envía las señales a la PC y se mapean como teclas (ejemplo: A = izquierda, D = derecha).

Compatible con testers de teclado online (ej: keyboard-test.space
) para verificar.

# Integración en caminadora

Alimentación: batería externa (powerbank) o toma de 5V de la caminadora.

Montaje de sensores:

En los pasamanos (control táctil con las manos).

En la consola frontal (junto a botones).

En el piso o costados (control con los pies).

Opcional: integrar sensor de velocidad de la banda (óptico o Hall) para sincronizar con el avatar.

# Hardware usado

ESP32

2× TTP223 (sensores capacitivos)

Fuente de 5V (powerbank o batería LiPo con regulador)

# Ideas futuras

Añadir acelerómetro/giroscopio para más control en VR.

Pantalla OLED de estado en la caminadora.

Botón físico de emergencia conectado a la ESP32.
