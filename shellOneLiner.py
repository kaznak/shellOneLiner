

import subprocess, tempfile, threading


class ShellOneLiner:

# oneliner	: one liner script of shell
# input		: input object
# outfile	: output file
# reader	: reader python function reads output from one liner
# writer	: writer python function writes input to one liner


	def fieldReader(self, line):
		return line[0:-1].split(' ')

	def fieldWriter(self, line):
		return ' '.join([str(x) for x in line]) + '\n'


	def doinput(self, input, inport, writer):
		for line in input:
			inport.write(writer(line))
		inport.close()

	def __init__(self, oneliner, input=False, outfile=False, reader=False, writer=False):
		if reader:
			self.reader = reader
		else:
			self.reader = self.fieldReader

		if writer:
			self.writer = writer
		else:
			self.writer = self.fieldWriter

		# subprocess
                if outfile:
			# output to file
                        self.outff = True
			self.outfn = outfile
                        self.outfd0 = open(self.outfn, 'w+b')
			soutf = self.outfd0
		else:
			# output to pipe
                        self.outff = False
			soutf = subprocess.PIPE

		if input:
			sinf = subprocess.PIPE
		else:
			sinf = None


		self.p = subprocess.Popen(oneliner + '| self 1/NF',
					shell=True,
					stdin=sinf,
					stdout=soutf)

		# input thread
		if input:
			self.int = threading.Thread(target=self.doinput,
							name="input",
							args=(input, self.p.stdin, self.writer) )
			self.int.start()


	def __iter__(self):
		if self.outff:
			# wait for processing is done
			# and designate the output file descripter as the output
			self.p.wait()
			self.outfd0.close()
			self.outfd = open(self.outfn, 'r+b')
		else:
			# and designate the output pipe descripter as the output
			self.outfd = self.p.stdout

		return self

	def next(self):
		return self.reader(self.outfd.next())



