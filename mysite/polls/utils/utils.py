from ..models import Question, Choice, Major
import IPython as ipy
def get_medians_unsorted(num = 5):
	median = Major.objects.all().values_list('median')
	medianlst = query2list(median, func = int)
	return query2list(median, func = int)[:num]

def get_majors_unsorted(num = 5):
	major = list(Major.objects.all().values_list('major'))
	majorlst = query2list(major, func = str)
	print len(majorlst)
	return majorlst[:num]

def get25_unsorted(num = 5):
	firstQ = list(Major.objects.all().values_list('p25th'))
	return query2list(firstQ, func = int)[:num]

def get75_unsorted(num = 5):
	thirdQ = list(Major.objects.all().values_list('p75th'))
	return query2list(thirdQ, func = int)[:num]

def get_majors_sorted(num = 10):
	major = list(Major.objects.all().order_by('-median').values_list('major'))
	return query2list(major, func = str)[:num]

def get_salaries_sorted(num = 10):
	"""Returns three lists (firstQ, median, third)"""
	sortedQset = Major.objects.all().order_by('-median')
	first = query2list(list(sortedQset.values_list('p25th')),func=int)[:num]
	median = query2list(list(sortedQset.values_list('median')),func=int)[:num]
	third = query2list(list(sortedQset.values_list('p75th')),func=int)[:num]
	return (first, median, third)

def query2list(queryset, func):
	old = zip(*queryset)
	lst = list(old[0])
	return map(func, lst)
