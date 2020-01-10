import Infineon_DPS310

from time import sleep


dps310 = Infineon_DPS310.DPS310()
try:

     

        while True:

            scaled_p = dps310.calcScaledPressure()

            scaled_t = dps310.calcScaledTemperature()

            p = dps310.calcCompPressure(scaled_p, scaled_t)

            t = dps310.calcCompTemperature(scaled_t)

            print(f'{p:8.1f} Pa {t:4.1f} C')

           

            sleep(1)

except KeyboardInterrupt:

        pass
