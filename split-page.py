# Adapted from https://gist.github.com/tshrinivasan/23d8e4986cbae49b8a8c
# This program picks pdf pages and split each of them in 3 new same-size pages, with horizontal cuts on the original page. Its useful because you can read without scrolling, by just passing page-to-page

import copy
import sys
import math
import PyPDF2 as pyPdf

def split_pages(src, dst):
	src_f = open(src, 'r+b')
	dst_f = open(dst, 'w+b')

	input = pyPdf.PdfReader(src_f)
	output = pyPdf.PdfWriter()

	for i in range(len(input.pages)):
		p = input.pages[i]
		q = copy.copy(p)
		r = copy.copy(p)
		q.mediabox = copy.copy(p.mediabox)
		r.mediabox = copy.copy(p.mediabox)

		x1, x2 = p.mediabox.lower_left
		x3, x4 = p.mediabox.upper_right

		x1, x2 = math.floor(x1), math.floor(x2)
		x3, x4 = math.floor(x3), math.floor(x4)
		x5, x6 = math.floor(x3/3), math.floor(x4/3)
		x7, x8 = math.floor(2*x3/3), math.floor(2*x4/3)
		
		# vertical
		p.mediabox.upper_right = (x3, x6)
		p.mediabox.lower_left = (x1, x2)

		q.mediabox.upper_right = (x3, x8)
		q.mediabox.lower_left = (x1, x6)

		r.mediabox.upper_right = (x3, x4)
		r.mediabox.lower_left = (x1, x8)

		output.add_page(r)
		output.add_page(q)
		output.add_page(p)

	output.write(dst_f)
	src_f.close()
	dst_f.close()

input_file= input("Enter the original PDF file name :")
output_file=input_file.replace(".pdf","_cut.pdf")

split_pages(input_file,output_file)