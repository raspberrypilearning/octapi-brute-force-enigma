# This code is the original example provided with the Py-enigma
# Python3 library and utilities. It is included here to confirm
# correct operation of Py-enigma on your system before proceeding
# with the brute force attack code.
#

# Py-enigma:
# Brian Neal
# http://py-enigmareadthedocs.org/
# License: MIT License

# All other original code: Crown Copyright 2016, 2017 

# Assumes message was encrypted as follows:
#
# STEP 1: Choose a start position and message key
# where: 	UYT is initial rotor position (chosen 'randomly')
#		SCC is unencrypted message key (chosen 'randomly')
#	
# STEP 2: Encrypyt the message key
#	pyenigma.py -r II V III -i 1 1 1 -p AV BS CG DL FU HZ IN KM OW RX -u B --start=UYT --text='SCC'
#	PWE
# where: 	PWE is encrypted message key
#
# Note: We use a one-to-one relation for the rotor ring for compatability with Cryptoy 
#
# STEP 3: Encrypt the message using the unencrypted message key 
#	pyenigma.py --key-file=keys.txt --start='SCC' --text='THISXISXWORKING'
#	YJPYITREDSYUPIU
# where:
#	SCC is the unencrypted message key
#	YJPYITREDSYUPIU is the cypher text produced
#	
# STEP 4: Operator sends (usually in Morse):
#	STNA DE STNB 1104 = 15 = UYT PWE = BNUGZ YJPYI TREDS YUPIU
# where:
#	STNA is callsign of destination station
#	DE means 'from' in Morse abreviation
#	STNB is callsign of originating station
#	= is the 'break' Morse character, which is used as a delimiter
#	1104 is time message is sent (presumably UTC)
# 	BNUGZ contains UGZ 'Kenngruppen' (day indicator for confirmation of correct key sheet entry on decrypt)
#
#

from enigma.machine import EnigmaMachine

################################
# Decrypt
################################

# setup machine to be the same as that used for encrypt

machine = EnigmaMachine.from_key_sheet(
       rotors='II V III',
       reflector='B',
       ring_settings='1 1 1',
       plugboard_settings='AV BS CG DL FU HZ IN KM OW RX')

# set machine initial starting position
machine.set_display('UYT')

# decrypt the message key
msg_key = machine.process_text('PWE')

# decrypt the cipher text with the unencrypted message key
machine.set_display(msg_key)

ciphertext = 'YJPYITREDSYUPIU'
plaintext = machine.process_text(ciphertext)

print(plaintext)
