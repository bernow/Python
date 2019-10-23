'''
# class Person:
#     name = '설똥재'

#     def say_hello(self):
#         print(f'hello! {self.name}')

# # 클래스 -> 인스턴스
# wtf = Person()
# # 인스턴스를 통해 메서드를 호출
# wtf.say_hello()
# # 인스턴스를 통해 속성에 접근
# print(wtf.name)
# # 클래스를 통해 속성에 접근
# print(Person.name)
# # 클래스를 통해 메서드 호출
# Person.say_hello(wtf)

# wtf.name = '찬또빡'
# print(wtf.name)
# print(Person.name)

# class Person:
#     name = '밍균'
#     age = 27

#     def greeting(self):
#         print(f'{self.name} : {self.age}세')

# wtf = Person()
# wtf.greeting()

# print(wtf.name)
# print(wtf.age)

# name = '???'
# class Person:
#     name = '밍균'

#     def greeting(self):
#         print(f'{name}')

# wtf = Person()
# wtf.greeting()

# print(wtf.name)
# print(Person.name)

# wtf.name = '증휴니'
# print(wtf.name)
# print(Person.name)

# wtf.greeting()
# Person.greeting(wtf)

# word = "Not class member"

# class Something:
#     word = "Class member"

#     def Set(self,msg):
#         self.word = msg
#     def Print(self):
#         print(word)

# g = Something()
# g.Set('First Message')
# g.Print()

class Person:
    def __init__(self, name):
        print(f'하이 {name}')
    def __del__(self):
        print('바이')
hong = Person('hong')

class Myclass:
    name = '홍길동'
    def __init__(self, value): #4. self = d, value = 10
        self.value = value #5. self.value -> d.value = 10
        print(f'{self.value}가 생성되었습니다.') #6. self.value -> 
    def __del__(self):
        print('소멸되었습니다.') #7. 소멸

def foo(): #2. foo 함수 실행
    d = Myclass(10) #3. d라는 인스턴스
foo() #1. 함수 호출

# p1 = Person()
# p2 = Person()

# print(p1.name)
# print(p2.name)
# print(Person.name)
# p1.name = 'eric'
# print(p1.name)
# print(p2.name)
# print(Person.name)
# Person.title = 'Welcome'
# print(p1.title)
# print(p2.title)
# print(Person.title)
# p1.water = '삼다수'
# print(p1.water)
# print(p2.water)
# print(Person.water)

class Person:
    population = 0 # 클래스 변수 -> 모든 인스턴스를 공유

    def __init__(self,name): #생성자 함수(매직 메서드) -> 인스턴스 생성시에 호출이 된다.
        self.name = name # me.name = name(juan) -> 인스턴스
        Person.population += 1

    def greeting(self):
        print(f'{self.name}입니다. 만나서 반갑습니다.')

me = Person('juan')
print(me.name)

friend = Person('bob')
print(friend.name)

print(Person.population)
print(me.population)
print(friend.population)
'''

# class Person:
#     def __init__(self, name):
#         self.name = name
        
#     def greeting(self):
#         print(f'안녕하세요, 저는 {self.name}입니다.')

# class Student(Person):
#     def __init__(self, name , student_id):
#         self.name = name
#         self.student_id = student_id
#     def greeting(self):
#         print(f'안녕하세요. 저는 {self.name}입니다. 제 학번은 {self.student_id}입니다.')

# s1 = Person('juan')
# s1.greeting()
# s2 = Student('justin', 12345)
# s2.greeting()

class Person:
    name = '홍길동'
    age = 19
    hometown = 'Seoul'
    def __init__(self, name , age, hometown):
        self.name = name
        self.age = age
        self.hometown = hometown
    def greeting(self):
        print(f'제 이름은 {self.name}이고 나이는 {self.age}살 입니다. 고향은{self.hometown}입니다.')

s1 = Person('홍길동', 19, 'Seoul')
s1.greeting()