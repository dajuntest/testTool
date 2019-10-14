import faker


f_cn = faker.Faker(locale='zh-CN') #需要指定国家，生成的数据是根据中国进行生成，比如电话号码等
f_en = faker.Faker()

print(dir(f_cn)) #打印对象可用的所有方法


# print(f_en.sentence())
# print(f_en.name()[:6])
print(f_cn.user_name()[:6])
print(f_cn.file_name()) #随机生成文件名称
print(f_cn.province()) #随机生成省份
print(f_cn.password()) #随机生成密码
print(f_cn.name()) #随机生成名字
print(f_cn.image_url()) #随机生成图片连接
print(f_cn.email()) #随机生成邮箱
print(f_cn.country()) #随机生成国家名称
print(f_cn.city()) #随机生成城市名称
print(f_cn.date()) #随机生成时间
print(f_cn.ssn()) #随机生成证件名称
print(f_cn.random.randint(1, 100000))



# number = (yield x for x in range(100))

# -*- coding:utf-8 -*-

# def create_counter():
#
#     def increase(): #定义一个还有自然数算法的生成器,企图使用next来完成不断调用的递增
#         n = 0
#         while True:
#             n = n+1
#             yield n
#     it = increase() #一定要将生成器转给一个(生成器)对象,才可以完成,笔者第一次做,这里一直出问题,
#
#     def counter(): #再定义一内函数
#         return next(it) #调用生成器的值,每次调用均自增
#     return counter
#
# counter_ = create_counter() #用变量来指向(闭包函数返回的函数)
#
# print(counter_(),counter_(),counter_())
