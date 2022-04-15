# EPython -> Micropython Backend

In order to target micropython as a backend, we set a subset of devices as a target.

The most elusive target of these is the [ESP-32](https://en.wikipedia.org/wiki/ESP32) Embedded  Microprocessor. This is a popular Microcontroller amongst the electronicscommunity used for many projects.

Currently, micropython implements stdlib from Python 3.4, alongside additional features.

## Target Devices

* ESP-32
  * [Heltec-ESP32](https://www.amazon.com/HiLetgo-Display-Bluetooth-Internet-Development/dp/B07DKD79Y9/ref=sr_1_2_sspa?crid=3M2QKT5Z9XUWR&keywords=ESP32&qid=1650041968&sprefix=esp32%2Caps%2C141&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzOFI2T081UTkwSTBBJmVuY3J5cHRlZElkPUEwNjM2MjI5RkFIWUVEUU1DRjMyJmVuY3J5cHRlZEFkSWQ9QTAzMDc5NDEyOFJZN08wTEw5SVpHJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==)

  This specific iteration of the chip deviates from the original design by integrating an OlED board. A target a little  bit to hard to compile to, even using the normal  Arduino/PlatformIO IDEs. 

  * [ESP-32](https://www.amazon.com/HiLetgo-ESP-WROOM-32-Development-Microcontroller-Integrated/dp/B0718T232Z/ref=sr_1_3?crid=3M2QKT5Z9XUWR&keywords=ESP32&qid=1650044084&sprefix=esp32%2Caps%2C141&sr=8-3)

  *RECOMMENDED*  This is a fairly normal build of the  ESP32 DevKit, and  the recommended way to test  this. 
* Raspberry Pi Pico
* x86 Machine
