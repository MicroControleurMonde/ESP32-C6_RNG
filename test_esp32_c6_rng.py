# test_esp32_c6_rng.py
# Example usage script

import esp32_c6_rng

# Generate and print 10 random numbers
for _ in range(10):
    random_number = esp32_c6_rng.generate_random_number()
    print("Random Number:", random_number)

