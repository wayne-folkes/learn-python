name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"

hours = dict()

for hour in filter(lambda line: line.startswith('From '), open(name)):
    h = hour.split()[5].split(':')[0]
    hours[h] = hours.get(h, 0) + 1

for h in sorted(hours):
    print '%s %s' % (h,hours[h])