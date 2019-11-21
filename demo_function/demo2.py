import jieba
import jieba.analyse
import re



file = './UntitledTestCase.py'

local_data = {}
number = 0

# with open(file, 'r', encoding='utf-8') as f:
#     lines = f.readline()
#
# for i in lines:

for line in open(file, 'r', encoding='utf-8'):
    # print(line)
    data_number = 'data' + str(number)
    if re.match('driver.get', line.strip()):
        # print(re.match('driver.get', line.strip()))
        p1 = re.compile(r'''(?<=["]).+?(?=["])''', re.S)
        local_data[data_number] = dict(url=re.findall(p1, line)[0])
        # print(local_data)
        number += 1
    if re.match('driver.find', line.strip()):
        p1 = re.compile(r'(?<=[y]).+?(?=[(])', re.S)
        local_data[data_number] = dict(
            local_type=str(re.findall(p1, line.split('"')[0])[0])[1:],
            local_value=line.split('"')[1]
        )
        number += 1

print(local_data)
