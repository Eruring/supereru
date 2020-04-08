#chap11 3번 문제
import os
from tkinter import *
aa = {}
txt = input("파일 이름을 입력하시오 : ") #파일 경로와 파일 이름 C:\Users\Supereru\Desktop\aa\HumptyDumpty.txt
infile = open(txt, "r") #infilename의 파일 이름을 파일을 여는 모드중에 r(파일을 처음부터 읽는모드)로 연다
rfile = infile.read() #infile에서 글자를 다 읽어서 rfile에 저장
infile.close() #infile을 닫음
for line in rfile: #각 줄을 읽는 반복문
    for ch in line: #각 줄안의 문자를 읽는 반복문
        if ch in aa: #각줄에 문자를 세는 반복문 
            aa[ch] += 1
        else:
            aa[ch] = 1
print(aa) 						# 딕셔너리를 호출 
os.system("pause")	

#chap11 5번 문제
from tkinter import *
file = input("입력 파일 이름: ")	# 파일이름 C:\Users\Supereru\Desktop\aa\numbers.txt
infile = open(file, "r")
rfile = infile.readlines()
infile.close()
file = input("출력 파일 이름: ")	#파일이름 C:\Users\Supereru\Desktop\aa\output.txt
outfile = open(file,"w")
total = 0 #변수값 초기화
avg = 0
count = 0
for s in rfile: 
    total += float(s) # 총 값을 더하고
    count += 1 # 각 값이 몇개인지를 구한다
avg = total / count # 평균을 구하고
print("합계="+str(total), file = outfile, end ="\n") #합계 
print("평균="+str(avg), file = outfile, end ="") # 평균 
outfile.close()
os.system("pause")	

#chap13 1번 문제
class Circle: # Circle객체 생성 
    def __init__(self, radius): #Circle()에 값을 받음 밑에 두 인자들은 매개변수와 일치를 해야한다. 
        self.radius = radius
    def calcPerimeter(self):
        self.calcperimeter = 3.14 * 2 * self.radius
    def calcArea(self):
        self.calcarea = 3.14 * self.radius**2
    def __str__(self):
        msg = "반지름: "+str(self.radius) +" 원의 면적: "+str(self.calcperimeter) +" 원의 둘레: "+str(self.calcarea)
        return msg
myCircle = Circle(100) #radius에 100이 들어감
myCircle.calcPerimeter()
myCircle.calcArea()
print(myCircle)
os.system("pause")	
from turtle import *

#chap13 4번 문제
class MyTurtle(Turtle):  #MyTurtle(Turtle) 객체를 만든다.
    def drawSquare(self): #사각형을 그리는 함수
        for i in range(4):
            self.right(90)
            self.forward(100)
t = MyTurtle()
t.forward(100) # 100을 전진
t.drawSquare() # 사각형을 그리는 함수를 호출해 사각형을 그린다.
os.system("pause")	



