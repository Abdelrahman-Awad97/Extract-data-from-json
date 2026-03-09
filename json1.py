import json
import urllib.request, urllib.parse, urllib.error
import ssl

sum = 0
lst_names = []
name_count = {}

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter url here: ').strip()

# fetch the data
fetch_data_b = urllib.request.urlopen(url, context=ctx)
fetch_data_s = fetch_data_b.read().decode()

# error handling
try:
    fetch_data_d = json.loads(fetch_data_s)
except:
    fetch_data_d = None

if not fetch_data_d or 'comments' not in fetch_data_d:
    print('Download Error')
    quit()

comments_lst = fetch_data_d['comments']

if len(comments_lst) == 0:
    print('object not found')
    quit()

# calculating the sum
for count in comments_lst:
    count = count['count']
    count = int(count)
    sum += count

print(f'the total value of count is: {sum}')

# counting names
for name in comments_lst:
    name = name['name']
    lst_names.append(name)

for key in lst_names:
    name_count[key] = name_count.get(key, 0) + 1

print(name_count)