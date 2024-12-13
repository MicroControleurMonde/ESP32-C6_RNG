# esp32_c6_rng.py
'''
Library for generating random numbers using the RNG hardware on the ESP32-C6.
Author: [MicroControleurMonde]
Date: [13.12.2024]
Version: 1.0
'''

import machine
import network

# Address of the LPPERI_RNG_DATA_REG register
LPPERI_RNG_DATA_REG = 0x600B2808

# Global variable to store the Wi-Fi object
wifi = None

# Function to read the RNG data from LPPERI_RNG_DATA_REG register.
def read_rng_data():
    return machine.mem32[LPPERI_RNG_DATA_REG]

# Function to initialize the ADC SAR
def init_adc_sar():   
    adc_pin = machine.Pin(4)  # GPIO 4 is mapped to ADC1_CH4
    adc = machine.ADC(adc_pin)
    adc.atten(machine.ADC.ATTN_6DB)  # 0-2V range
    adc.width(machine.ADC.WIDTH_12BIT)  # 12-bit resolution (range: 0-4095)
    
# Function to initialize the Wi-Fi
def init_wifi():
    global wifi 
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)

# Function to generate a random number by reading from the RNG register.
def generate_random_number():
    rng_value = read_rng_data()  # Read RNG value from the hardware register
    return rng_value

# Function to deinitialize the Wi-Fi connection
def deinit_wifi():
    global wifi
    if wifi is not None:
        wifi.active(False)

