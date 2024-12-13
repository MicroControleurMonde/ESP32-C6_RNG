# ESP32-C6 RNG

![Link](https://github.com/MicroControleurMonde/ESP32_RNG/blob/main/Reports/ESP32download.jpg)

A Micro-python library which provides an interface to generate a random number using the ESP32-C6's hardware RNG.

The code uses several hardware devices of the MCU to generate random noise values using additional entropy sources. The SAR ADC and Wi-Fi are exploited to provide quality inputs to the hardware random number generator integrated into the ESP32-C6 (FH4). It reads a random value from the **`LPPERI_RNG_DATA_REG`** register.

- Library : **esp32_c6_rng.py**
- Library test: **test_esp32_c6_rng.py**
- Example: **Test_ESP32-C6_RNG.py**

**Source**: *`ESP32-C6 Technical Reference Manual V.1.0 - Chapter 26 Random Number Generator (RNG) - Pages 705/706`* [Doc. Extract](https://github.com/MicroControleurMonde/ESP32-C6_RNG/blob/main/26%20Random%20Number%20Generator%20(RNG).pdf)

The ESP32-C6 RNG generates random integer numbers as **32-bit values**.

                865254577
                418491403
                -1447893272
                1205348786
                -871015593
                637462341
                -725121184
                -959320840
                -2018839333
                996041137

## Platform

The code was implemented specifically for an Espressif ESP32-C6 microcontroller on a DFRobot Beetle ESP32-C6 development board [Link](https://www.dfrobot.com/product-2778.html?srsltid=AfmBOoobkIgBWxWnYV6HINjyG3PasT4rkkWpRrTADPIq6GYcCzJKCEQT)
- The flash indicates ESP32-C6FH4 chip revision v0.1
- Quad Flat No-lead 32 pins (QFN32).

        MicroPython v1.25.0-preview.114.gbdda91fe7 on 2024-12-11; ESP32C6 module with ESP32C6
  
Due to some difficulties to flash the card, the tested version is in "*preview*". By dint of playing with the registers, I generated several crash dumps...


## Performance:

- Time taken to generate 186'000 values: **67 seconds** (avg)
- Throughput: **11031.11 bytes/sec**
- **2757** random values / sec.

                Note: Performance without saving date on file !
                8000 values (beyond you will crash: "MemoryError: memory allocation failed")
                Total time : 0.15 secondes
                Throughput : 214765.09 bytes/sec
                Random values : 53691.27 valeurs/sec

Testing tools used:

* Ent (28.01.2008)
* Dieharder version 3.31.1

## Ent Test Report 
  ([www.fourmilab.ch](https://www.fourmilab.ch/random/)) John Walker
- Sample size: **2,0 MB**
- Total generated: **186'000 values**

- [Ent Report - Raw](https://github.com/MicroControleurMonde/ESP32-C6_RNG/blob/main/Reports/Ent_ESP32C6_RNG_186k.txt)
- [Ent Report Analyse](https://github.com/MicroControleurMonde/ESP32-C6_RNG/blob/main/Reports/Ent_report_analyses.md)

## Dieharder Test Report
(https://webhome.phy.duke.edu/~rgb/General/dieharder.php) Robert G. Brown

- Sample size: **2,0 MB**
- Total generated: **186'000 values**

- [Dieharder Report - Raw](https://github.com/MicroControleurMonde/ESP32-C6_RNG/blob/main/Reports/Dieharder_ESP32-C6_RNG_186k.txt)
- [Dieharder Report Analyses](https://github.com/MicroControleurMonde/ESP32-C6_RNG/blob/main/Reports/Dieharder_Report_ESP32-C6_RNG_186k.md)
---
## Espressif statement:

Page 705, at the bottom of the page:

    "A data sample of 2 GB, which is read from the random number generator at a rate of 5 MHz with only the
    high-speed ADC being enabled, has been tested using the Dieharder Random Number Testsuite (version
    3.31.1). The sample passed all tests."

I admit that C code may offer better performance than micro-python... OK. 

But physics is physics. And the mathematics associated with physical random phenomena is changeless.

I am quite doubtful (_considering my own tests_)!

# Special tribute:

## Passing of John Walker

We are deeply saddened to hear of the passing of John Walker, one of the founders of Autodesk. He died at home in Switzerland, on 2nd February 2024, aged 74.

[The announcement was shared here.](https://www.engineering.com/a-cad-legend-passes-autodesk-founder-john-walker-1949-to-2024/)
