# hardfork-tracker

Monitors state of the blockchain, displays approximately  time to hardFork.  
On hardfork - print `hardfork`, then exit.

---

usage: python3 -m hardfork [-h] timestamp

positional arguments:  
  timestamp   hardfork unix time or -1 (then current time will be used)  

optional arguments:  
  -h, --help  show this help message and exit


**Or** install
	
	$ python3 setup.py install

then call:
    
    $ hardfork-tracker timestamp

---

### Build docker image:
    
    $ docker build -t hardfork-tracker:latest .

Run docker image:

    $ docker run --rm -it hardfork-tracker:latest -1
