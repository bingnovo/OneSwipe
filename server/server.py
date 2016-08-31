#
# OneSwipe is a solution using bluetooth beacon to
# facinate the instore mobile payment.
#
# The server will accpect query from clients and 
# return the payment code.
#
# Author: Bingnan Zhou
# Email: bingnovo@gmail.com
# Last Modified: Aug 30, 2016
#

import tornado.ioloop
import tornado.web

import os
import psycopg2
import urlparse

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("Welcome to use OneSwipe Server")
		
class QueryHandler(tornado.web.RequestHandler):
	def get(self):
		
		# get beacon id
		beacon_id = self.get_arguments("bid")
		
		# init the database connection
		urlparse.uses_netloc.append("postgres")
		url = urlparse.urlparse('postgres://vmkbaarpbqebjr:B3l2O-lo7QWdffVLN-Vv9LdFi-@ec2-54-243-235-107.compute-1.amazonaws.com:5432/dgsaji0dtgqop')
		conn = psycopg2.connect(
			database='dgsaji0dtgqop',
			user='vmkbaarpbqebjr',
			password='B3l2O-lo7QWdffVLN-Vv9LdFi-',
			host='ec2-54-243-235-107.compute-1.amazonaws.com',
			port='5432'
		)
		
		cursor = conn.cursor()
		
		# execute our Query
		cursor.execute("SELECT * FROM paycode WHERE bid = \'" + beacon_id[0] + "\'")
	 
		# retrieve the first record from the database
		records = cursor.fetchone()
		
		self.write("Welcome to use OneSwipe Server - Query")
		if records is not None:
			self.write(records[1])
		else:
			self.write("No record found")

class InsertHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("Welcome to use OneSwipe Server - Insert")

def main():
	app = tornado.web.Application ([
		(r"/", MainHandler),
		(r"/query", QueryHandler),
		(r"/insert", InsertHandler)
	])
	app.listen(8888)
	tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__" :
	main()
	
	