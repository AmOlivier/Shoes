import psycopg2

def connect():
	return psycopg2.connect(database='learning', user='postgres', password='2908', host='localhost')