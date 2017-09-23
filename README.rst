dht22 to mqtt for Raspberry Pi
=============================

Reads the temperature and humidity from a dht22 sensors and sends it to a mqtt broker.


Installation:
-------------------

    pip install rpi-dht22-mqtt

Configuration:
-------------------

Needs a json configuration file as follows (don't forget to change ip and credentials ;-)):

.. code:: json

    {
      "mqtt_client_id": "rpi-dht22",
      "mqtt_host": "192.168.0.210",
      "mqtt_port": "1883",
      "verbose": "true",
      "topics": {
        "temperature": "halti/datacenter/temperature",
        "humidity": "halti/datacenter/humidity",
      }
    }

Start:
-------------------

    rpi-dht22-mqtt config.json
