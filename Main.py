from Simulator import Simulator
import time

"""
Entrypoint into the Blackjack simulator
"""

print("Starting")

simulator = Simulator()
start_time = time.time()
simulator.run_simulation()
end_time = time.time()
simulator.print_winnings()

print("Seconds:  " + str(end_time - start_time))