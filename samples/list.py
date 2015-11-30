#!/usr/bin/python3
# Copyright (c) 2015 Davide Gessa
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.
from libcontractvm import Wallet, WalletExplorer, ConsensusManager
from studentreg import StudentRegManager
import sys
import time
import os

consMan = ConsensusManager.ConsensusManager ()
consMan.bootstrap ("http://127.0.0.1:8181")

wallet = WalletExplorer.WalletExplorer (wallet_file='test.wallet')
srMan = StudentRegManager.StudentRegManager (consMan, wallet=wallet)

while True:
	os.system ('clear')
	print ('List:')
	v = srMan.getList ()
	for x in v:
		print ('\t',x['studentid'],'\t',x['lecture'],'\t',x['comment'])
	time.sleep (5)
