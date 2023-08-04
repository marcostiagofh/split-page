# Adapted from https://gist.github.com/tshrinivasan/23d8e4986cbae49b8a8c
# This program picks pdf pages and split each of them in 3 new same-size pages, with horizontal cuts on the original page. Its useful because you can read without scrolling, by just passing page-to-page

import copy
import sys
import math
import pyPdf

def split_pages(src, dst):
	src_f = file(src, 'r+b')
	dst_f = file(dst, 'w+b')

	input = pyPdf.PdfFileReader(src_f)
	output = pyPdf.PdfFileWriter()

	for i in range(input.getNumPages()):
		p = input.getPage(i)
		q = copy.copy(p)
		r = copy.copy(p)
		q.mediaBox = copy.copy(p.mediaBox)
		r.mediaBox = copy.copy(p.mediaBox)

		x1, x2 = p.mediaBox.lowerLeft
		x3, x4 = p.mediaBox.upperRight

		x1, x2 = math.floor(x1), math.floor(x2)
		x3, x4 = math.floor(x3), math.floor(x4)
		x5, x6 = math.floor(x3/3), math.floor(x4/3)
		x7, x8 = math.floor(2*x3/3), math.floor(2*x4/3)
		
		# vertical
		p.mediaBox.upperRight = (x3, x6)
		p.mediaBox.lowerLeft = (x1, x2)

		q.mediaBox.upperRight = (x3, x8)
		q.mediaBox.lowerLeft = (x1, x6)

		r.mediaBox.upperRight = (x3, x4)
		r.mediaBox.lowerLeft = (x1, x8)

		output.addPage(r)
		output.addPage(q)
	output.addPage(p)

	output.write(dst_f)
	src_f.close()
	dst_f.close()

input_file=raw_input("Enter the original PDF file name :")
output_file=raw_input("Enter the splitted PDF file name :")

split_pages(input_file,output_file)
