# Baekjun_Programming

# Title : A+B
# C:\Users\Kimmingyu\PycharmProjects\BAEKJOON\step1
# 1000.py
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------------------------------------
#  Author       : Mingyu Kim
#  E-mail       : mgkim@naver.com
#  Version      : 0.1
#  Rev. Date    : July. 28, 2020
#
#  First, I used to program name is PyCham
#   - Python 3.0
#   - Site url : Refer to https://www.acmicpc.net/step/1
#
#  요구 사항 : 시간 제한 (2 초), 메모리 제한 (128 MB), 정답 비율 (44.422 %)
#  문제 : 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
#
#  입력 : 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
#  출력 : 첫째 줄에 A+B를 출력한다.
#  예제 입력 : 1 2
#  예제 출력 : 3
#
# -----------------------------------------------------------------------------------------------------------
c = input().split()
a = int(c[0])
b = int(c[1])

print(a+b)