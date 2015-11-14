# Copyright (c) 2015 Davide Gessa
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

from libcontractvm import Wallet, ConsensusManager, DappManager

class StudentRegManager (DappManager.DappManager):
	def __init__ (self, consensusManager, wallet = None):
		super (StudentRegManager, self).__init__(consensusManager, wallet)

	def register (self, studentid, lecture, comment):
		cid = self.produceTransaction ('studentreg.register', [studentid, lecture, comment])
		return cid

	def getList (self):
		return self.consensusManager.jsonConsensusCall ('studentreg.getlist', [])['result']
