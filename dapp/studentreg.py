# Copyright (c) 2015 Davide Gessa
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import logging

from contractvmd import dapp, config, proto
from contractvmd.chain import message

logger = logging.getLogger(config.APP_NAME)


class StudentRegProto:
	DAPP_CODE = [ 0x57, 0x58 ]
	METHOD_REG = 0x01
	METHOD_LIST = [METHOD_REG]

	
class StudentRegMessage (message.Message):
	def register (sid, lecture, comment):
		m = StudentRegMessage ()
		m.StudentID = sid
		m.Lecture = lecture
		m.Comment = comment
		m.DappCode = StudentRegProto.DAPP_CODE
		m.Method = StudentRegProto.METHOD_REG
		return m

	def toJSON (self):
		data = super (StudentRegMessage, self).toJSON ()

		if self.Method == StudentRegProto.METHOD_REG:
			data['studentid'] = self.StudentID
			data['comment'] = self.Comment
			data['lecture'] = self.Lecture
		else:
			return None

		return data


class StudentRegCore (dapp.Core):
	def __init__ (self, chain, database):
		database.init ('students', [])
		super (StudentRegCore, self).__init__ (chain, database)
		
	def register (self, studentid, lecture, comment):
		self.database.listappend ('students', {'studentid': studentid, 'lecture': lecture, 'comment': comment})
			
	def getlist (self):
		return self.database.get ('students')


class StudentRegAPI (dapp.API):
	def __init__ (self, core, dht, api):
		self.api = api
		rpcmethods = {}

		rpcmethods["getlist"] = {
			"call": self.method_getlist,
			"help": {"args": [], "return": {}}
		}

		rpcmethods["register"] = {
			"call": self.method_register,
			"help": {"args": ["studentid", "lecture", "comment"], "return": {}}
		}

		errors = { }

		super (StudentRegAPI, self).__init__(core, dht, rpcmethods, errors)


	def method_getlist (self):
		return self.core.getlist ()

	def method_register (self, studentid, lecture, comment):
		msg = StudentRegMessage.register (studentid, lecture, comment)
		return self.createTransactionResponse (msg)


class studentreg (dapp.Dapp):
	def __init__ (self, chain, db, dht, apiMaster):
		self.core = StudentRegCore (chain, db)
		apiprov = StudentRegAPI (self.core, dht, apiMaster)
		super (studentreg, self).__init__(StudentRegProto.DAPP_CODE, StudentRegProto.METHOD_LIST, chain, db, dht, apiprov)

	def handleMessage (self, m):
		if m.Method == StudentRegProto.METHOD_REG:
			logger.pluginfo ('Found new message %s: registration of %s', m.Hash, m.Data['studentid'])
			self.core.register (m.Data['studentid'], m.Data['lecture'], m.Data['comment'])
