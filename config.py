##Log path
syslogpath="/var/log/lora/lorasys.log" #system messages
logpath='/var/log/lora/lora.log' #rf messages

## KISS Settings
# Where to listen?
#		TCP_HOST can be "localhost", "0.0.0.0" or a specific interface address
#		TCP_PORT as configured in aprx.conf <interface> section
TCP_HOST = "0.0.0.0"
TCP_PORT = 10001

## AXUDP Settings
# USE_AXUDP Switch from KISS to AXUDP if True
# AXUDP_REMOTE_IP IP to wich udp packets are sent
# AXUDP_REMOTE_PORT UDP Port to wich udp packets are sent
# AXUDP_LOCAL_IP IP of Interface to listen on, 0.0.0.0 for all interfaces
# AXUDP_LOCAL_PORT Port to listen for incoming AXUDP packets

USE_AXUDP = False
AXUDP_REMOTE_IP = "192.168.0.185"
AXUDP_REMOTE_PORT = 20000
AXUDP_LOCAL_IP = "0.0.0.0"
AXUDP_LOCAL_PORT = 20000

## LoRa Settings
frequency=433.775
preamble=8
spreadingFactor=12
bandwidth="BW.BW125"
#Possible BW values: BW7_8,BW10_4,BW15_6,BW20_8,BW31_25,BW41_7,BW62_5,BW125,BW250,BW500
codingrate="CODING_RATE.CR4_5"
#Possible CODING_RATE values: CR4_5,CR4_6,CR4_7,CR4_8,
APPEND_SIGNAL_REPORT = True
paSelect = 1
outputPower = 0
TX_OE_Style = False # if true, tx RF packets are in OE Style, otherwise in standard AX25
sync_word = 0x12
