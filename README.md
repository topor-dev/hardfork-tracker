# hardfork-tracker

Monitors state of the blockchain, displays approximately  time to hardFork.
On hardfork - print `hardfork`, then exit.

---

usage: hardfork [-h] timestamp

positional arguments:  
  timestamp   hardfork unix time or -1 (then current time will be used)  

optional arguments:  
  -h, --help  show this help message and exit

---

### Build docker image:
    
    docker build -t hardfork-tracker:latest .

Run docker image:

    docker run --rm -it hardfork-tracker:latest -1
