# ESP32 + TTP223 en Caminadora (Control VR)

Este proyecto utiliza una ESP32 y dos sensores táctiles TTP223 montados en una caminadora para controlar un escenario en Unreal Engine mediante emulación de teclado.

# Funcionamiento

El usuario toca los sensores capacitivos para enviar señales binarias:
 00 → No se mueve
 01 → Mover a la derecha
 10 → Mover a la izquierda
 11 → No se mueve

La ESP32 envía las señales a la PC y se mapean como teclas (ejemplo: A = izquierda, D = derecha).

Compatible con testers de teclado online (ej: keyboard-test.space
) para verificar.
La **ESP32** envía los datos por **UDP** a la PC.  
- Un programa receptor en Python (usando `pynput`) traduce las señales en **entradas de teclado**.  
- Compatible con testers de teclado online como [keyboard-test.space](https://keyboard-test.space/es/).  

# Hardware usado

ESP32

2× TTP223 (sensores capacitivos)

Fuente de 5V (powerbank o batería LiPo con regulador)


