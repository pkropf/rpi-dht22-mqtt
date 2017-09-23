# -*- coding: utf-8 -*-
from setuptools import setup


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='rpi-dht22-mqtt',
    version='0.0.2',
    description='Send temperature and humidity from DHT22 sensor to mqtt broker',
    long_description=readme,
    author='David Uebelacker',
    author_email='david@uebelacker.ch',
    url='https://github.com/goodfield/rpi-dht22-mqtt.git',
    license=license,
    packages=['rpi_dht22_mqtt'],
    install_requires=['paho-mqtt', 'Adafruit_Python_DHT'],
    scripts=['bin/rpi-dht22-mqtt']
)
