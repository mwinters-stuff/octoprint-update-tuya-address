#!/usr/bin/python3

import subprocess
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

#MAC address of the smart plug
MAC_ADDRESS = '84:f3:eb:32:e3:b4'
# netmask of your network
NET_MASK = '192.168.1.1/24'
#octopi config
OCTOPI_CONFIG = '/home/pi/.octoprint/config.yaml'

if __name__ == "__main__":
  subprocess.check_call(['/usr/bin/nmap','-sP','-T4',NET_MASK])

  p = subprocess.Popen(['/usr/sbin/arp','-n'], stdout=subprocess.PIPE)
  for line in iter(p.stdout.readline, b''):
    str = line.decode('utf-8')
    if(MAC_ADDRESS in str):
      ipaddress = str.split(' ')[0]
      print('Found Plug with address %s' % ipaddress)

      config = open(OCTOPI_CONFIG)
      configy = yaml.load(config, Loader=Loader)
      config.close()

      # print(configy)
      print(configy['plugins']['tuyasmartplug']['arrSmartplugs'][0]['ip'])
      if configy['plugins']['tuyasmartplug']['arrSmartplugs'][0]['ip'] != ipaddress:
        configy['plugins']['tuyasmartplug']['arrSmartplugs'][0]['ip'] = ipaddress
        config = open(OCTOPI_CONFIG, mode='w')
        config.write(yaml.safe_dump(configy, allow_unicode=False))
        config.close()
      break
