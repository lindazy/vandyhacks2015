from Bio import Entrez
from Bio import Medline

def search_pub_med(term): 
	MAX_COUNT = 10
	TERM = term #'Tuberculosis'
	 
	print 'Getting %d publications containing %s' % (MAX_COUNT, TERM)
	Entrez.email = 'A.N.Other@example.com'
	h = Entrez.esearch(db='pubmed', retmax=MAX_COUNT, term=TERM)
	result = Entrez.read(h)
	print 'Total number of publications containing %s: %s' %(TERM, result['Count'])
	ids = result['IdList']
	h = Entrez.efetch(db='pubmed', id=ids, rettype='medline', retmode='text')
	records = Medline.parse(h)
	print records
	 
	data = []
	for record in records:
		title = record.get('TI','?')
		abstract = record.get('AB','No abstract given.')
		data.append((title,abstract))
	return data

if __name__=='__main__':
	query = raw_input('Enter query.\n')
	data = search_pub_med(query)
	for record in data:
		print record
