#!/usr/bin/env python

def main():
	print('In Main')
	pwd = input('What is the password?')
	if pwd == 'apple':
		print('Logging on ...')
	else:
		print('Incorrect password.')
		print('All done!')
