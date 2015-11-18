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

sid = input ('Insert your student id: ')
lec = input ('Insert the lecture title: ')
com = input ('Insert a text comment: ')

try:
	print ('Broadcasted:', srMan.register (sid, lec, com))
except:
	print ('Error.')
	
