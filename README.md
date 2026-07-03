# Raspberry Pi Distance Sensor

HC-SR04 ultrasonic distance sensor project built with a Raspberry Pi 3B.

## Hardware
- Raspberry Pi 3B
- HC-SR04 ultrasonic distance sensor
- 1kΩ and 2kΩ resistors (voltage divider)

## Features
- Real-time distance measurement in cm
- Voltage divider to protect GPIO from 5V ECHO signal
- Speed of sound calculation

## Wiring
| HC-SR04 | Pi Pin |
|---------|--------|
| VCC | Pin 2 (5V) |
| GND | Pin 6 |
| TRIG | Pin 16 (GPIO 23) |
| ECHO | Pin 18 via voltage divider |

## Setup
```bash
source ~/pienv/bin/activate
pip install RPi.GPIO
python hcsr04.py
```

## Roadmap
- [ ] Speed of sound experiment using temperature data from BME280
- [ ] Parking sensor with LED distance indicator
- [ ] Intruder alert triggering buzzer
- [ ] Data logging distance over time

## Author
Zakariyah — London, 2026
