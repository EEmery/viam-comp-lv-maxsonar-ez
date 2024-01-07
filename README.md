# Sensor LV MAXSONAR EZ - VIAM Component

This repository describes the sensor LV MAXSONAR EZ as a modular VIAM sensor component to be used in order to aquire distance readings from the repsective ultrasonic sensor.

## Prerequisites

```
sudo apt update && sudo apt upgrade -y
sudo apt-get install python3
sudo apt install python3-pip
sudo apt-get install python3-venv
```

## API

The `lv-maxsonar-ez` resource fulfills the Viam sensor interface.

### `get_readings()`
The `get_readings()` method takes no arguments and returns the detected distance in centimeters (with the key 'distance').

## Viam Component Configuration

This component should be configured as type sensor, model `emery:sensor:lv-maxsonar-ez`.

The following attributes may be configured as `lv-maxsonar-ez` component config attributes.

Example:

```
{
  "pw_pin": 36,
  "rx_pin": 37
}
```

### `pw_pin: integer (required)`
This pin outputs a pulse width (PW) representation of range.

### `rx_pin: integer (required)`
This pin commands a range reading (RX) of the sensor.
