from django.core.management.base import BaseCommand, CommandError
from polls.models import Major
import urllib2, csv

rawURL = "https://raw.githubusercontent.com/fivethirtyeight/data/master/college-majors/all-ages.csv"


def populateMajors():
	Major.objects.all().delete()
	response = urllib2.urlopen(rawURL)
	cr = csv.reader(response)
	cr.next()
	for row in cr:
		addSingleMajor(row)

def addSingleMajor(row):
	new_major = Major(major_code = row[0],
	major = row[1],
	major_category = row[2],
	total = row[3],
	employed = row[4],
	employed_full_time_year_round = row[5],
	unemployed = row[6],
	unemployment_rate = row[7],
	median = row[8],
	p25th= int(float(row[9])),
	p75th = int(float(row[10])))
	new_major.save()

class Command(BaseCommand):
	help = 'Does some magical work'

	def handle(self, *args, **options):
		print('There are {} majors'.format(Major.objects.count()))
		populateMajors()
		print('There are now {} majors'.format(Major.objects.count()))

