#!/usr/bin/python3
# Copyright (c) 2015 Davide Gessa
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.
from libcontractvm import Wallet, WalletNode, ConsensusManager
from studentreg import StudentRegManager
import sys
import config
import time

consMan = ConsensusManager.ConsensusManager ()
consMan.bootstrap ("http://127.0.0.1:8181")

#wallet=WalletChainSo.WalletChainSo (wallet_file='data/test_xltnode_a.wallet')
wallet=WalletNode.WalletNode (chain='XLT', url=config.WALLET_NODE_URL, wallet_file='data/test_xltnode_a.wallet')

srMan = StudentRegManager.StudentRegManager (consMan, wallet=wallet)

def check ():
	m = input ('Inser yout student id: ')
	v = srMan.getList ()
	for x in v:
		if x['studentid'] == str (m):
			print (x['studentid'],'\t',x['lecture'],'\t',x['comment'])
			break
	
def register ():
	sid = input ('Insert your student id: ')
	lec = input ('Insert the lecture title: ')
	com = input ('Insert a text comment: ')
	try:
		print ('Broadcasted:', srMan.register (sid, lec, com))
	except:
		print ('Error.')
	
def getlist ():
	while True:
		print ('List:')
		v = srMan.getList ()
		for x in v:
			print ('\t',x['studentid'],'\t',x['lecture'],'\t',x['comment'])
		time.sleep (5)

if __name__ == "__main__":
	if len (sys.argv) > 1:
		if sys.argv[1] == 'check':
			check ()
			sys.exit (0)

		elif sys.argv[1] == 'list':
			getlist ()
			sys.exit (0)
			
		elif sys.argv[1] == 'register':
			register ()
			sys.exit (0)

	print ('usage:', sys.argv[0], 'check|register|list')
