# octoprint-update-tuya-address
For Octoprints tuya plugin, updates the ip address of the plug based on MAC address.

# dependancies
Need to install nmap, and python's yam with 
> sudo apt-get install nmap python3-yaml

# configure
Edit update-tuya-address.py and change the settings

>MAC_ADDRESS = '84:f3:eb:32:e3:b4'
>NET_MASK = '192.168.1.1/24'
>OCTOPI_CONFIG = '/home/pi/.octoprint/config.yaml'

with values that will match your config.

# run
>./update-tuya-address.py


