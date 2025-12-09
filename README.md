# ESP32-37-Sensor-Kit-MicroPython

**Migration and technical adaptation of the classic 37 Sensor Kit for the ESP32 platform.**

## Overview
This project documents the transition of the 37 Sensor Kit modules from their original Arduino (5V/C++) design to an ESP32 (3.3V/MicroPython) architecture. It serves as an Integrative Work for the Electromechanical Engineering degree at UTN Rafaela.

## Key Features
* **Language Migration:** All codes rewritten from C++ to **MicroPython**.
* **Hardware Adaptation:** Wiring diagrams modified for **3.3V logic levels** (including resistor adjustments for LEDs and sensors like KY-005, KY-009, etc.).
* **Code Optimization:** Algorithms improved for ESP32 capabilities (e.g., 12-bit ADC precision, PWM frequencies).

## Hardware Used
* Microcontroller: ESP32 (DevKit V1)
* Sensors: Standard 37 Sensor Kit (Keyes / generic)
