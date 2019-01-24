from Simulator import Simulator
import time

simulator = Simulator()
start_time = time.time()
simulator.run_simulation()
end_time = time.time()
simulator.print_winnings()

print(end_time - start_time)