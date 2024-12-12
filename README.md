# ESP32-C6 RNG

![Link](https://github.com/MicroControleurMonde/ESP32_RNG/blob/main/Reports/ESP32download.jpg)

### !!! UNDER CONSTRUCTION !!!

A Micro-python library which provides an interface to generate a random number using the ESP32-C6's hardware RNG.

The code uses several hardware devices of the MCU to generate random noise values using additional entropy sources. The SAR ADC and Wi-Fi are exploited to provide quality inputs to the hardware random number generator integrated into the ESP32-C6.

- Library :
- Library test: 
- Example:

**Source**: ESP32-S3 Technical Reference Manual V. 1.6 - Chapter 26 Random Number Generator (RNG) - Pages 705/706 [Extract]

The ESP32-C6 RNG generates random integer numbers as 32-bit values.

## Performance:

- Time taken to generate xxxxxxxx values: xx seconds (avg)
- Throughput: xxxxx  Bytes/sec
- xxxxx random values / sec.

Testing tools used:

* Ent (28.01.2008)
* Dieharder version 3.31.1

# Ent Test Report 
  ([www.fourmilab.ch](https://www.fourmilab.ch/random/)) John Walker
- Sample size: **xx.xx MB**
- Total generated: **x'xxx'xxx values**

- [Ent Report -Raw]()
- [Ent Report Analyse]()

# Dieharder Test Report
(https://webhome.phy.duke.edu/~rgb/General/dieharder.php) Robert G. Brown

- Sample size: **xx.xx MB**
- Total generated: **x'xxx'xxx values**

- [Dieharder Report - Raw]()
- [Dieharder Report Analyses]()

  
  
# Special tribute:

## Passing of John Walker

We are deeply saddened to hear of the passing of John Walker, one of the founders of Autodesk. He died at home in Switzerland, on 2nd February 2024, aged 74.

[The announcement was shared here.](https://www.engineering.com/a-cad-legend-passes-autodesk-founder-john-walker-1949-to-2024/)
