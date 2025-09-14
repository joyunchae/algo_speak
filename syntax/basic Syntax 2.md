# basic Syntax 2

## 🌟list 리스트

- 리스트 : 여러 개의 값을 순서대로 저장하는, 변경 가능한(mutable) 시퀀스 자료형
- 표현
    
    ```python
    my_list_1 = [ ]
    my_list_2 = [1,'a',3,'b',5] # 대괄호 안에 쉼표
    my_list_3 = [1,2,3, 'python',['hello','world','!!!']] # 문자열, 숫자, 다른 리스트 담을 수 ㅇ
    # 값 추가, 수정, 삭제 등 자유롭게 변경 가능
    ```
    
    - 대괄호 안에 값들을 쉼표로 구분

### 시퀀스로서의 리스트

- 리스트 시퀀스 특징 : 문자열처럼 인덱싱, 슬라이싱, 길이 확인, 반복 등 공통 기능 모두 사용 가능
    
    ```python
    my_list = [1, 'a', 3, 'b', 5]
    
    # 인덱싱
    print(my_list[1])  # a
    
    # 슬라이싱
    print(my_list[2:4])  # [3, 'b']
    print(my_list[:3])  # [1, 'a', 3]
    print(my_list[3:])  # ['b', 5]
    print(my_list[::2])  # [1, 3, 5]
    print(my_list[::-1])  # [5, 'b', 3, 'a', 1]
    
    # 길이
    print(len(my_list))  # 5
    ```
    

### 중첩 리스트(Nested List)

- 다른 리스트를 값으로 가진 리스트
- 인덱스를 연달아 사용하여 안쪽 리스트의 값에 접근할 수 있음
    
    ```python
    # 중첩된 리스트 접근
    my_list = [1, 2, 3, 'Python', ['hello', 'world', '!!!']] 
    -> world에 접근하려면 my_list[4][1]로 가야함
    
    print(len(my_list))  # 5
    print(my_list[4][-1])  # !!!
    print(my_list[-1][1][0])  # w   -> 문자열도 시퀀스라는 사실을 잊으면 안 됨
    
    ```
    

### 리스트 가변성(Mutability)

- 여러 개의 값을 순서대로 저장하는, 변경 가능한(mutable) 시퀀스 자료형

<aside>
✨

한번 생성된 리스트는 “그 내용을 자유롭게 수정, 추가, 삭제할 수 있다”는 뜻

이는 문자열의 불변성(Immutability)과 정반대되는 매우 중요한 특징

</aside>

- 리스트는 시퀀스 이므로, 문자열처럼 인덱싱, 슬라이싱, 길이 확인, 반복 등 공통 기능을 모두 사용 가능
- 리스트의 가변성
    - 한 번 생성된 리스트는 “그 내용을 자유롭게 수정, 추가, 삭제할 수 있다는 뜻입니다.”
    - 이는 문자열의 불변성과 정반대되는 매우 중요한 특징입니다.

```python
# 리스트는 가변
# 1. 인덱싱으로 값 수정
my_list = [1, 2, 3, 4, 5]
my_list[1] = 'two'
print(my_list)  # [1, 'two', 3, 4, 5]

# 2. 슬라이싱으로 값 수정
my_list = [1, 2, 3, 4, 5]
my_list[2:4] = ['three', 'four']
print(my_list)  # [1, 2, 'three', 'four', 5]

>>> [1, 2, 'three', 'four', 5]

# 2. 슬라이싱으로 값 수정
my_list = [1, 2, 3, 4, 5]
my_list[2:4] = ['three', 'four', 'ssafy']
print(my_list)  # [1, 2, 'three', 'four', 5]

>>> [1, 2, 'three', 'four', 'ssafy', 5]
```

</aside>

---

## tuple 튜플

- 여러 개의 값을 순서대로 저장하는 변경 불가능한 시퀀스 자료형
- 한번 만들어지면 절대 수정 불가(리스트와 차이)

```python
# 튜플 표현 : 소괄호 안에 쉼표
my_tuple_1 = ()
my_tuple_2 = (1)  => 1 # 이건 튜플이 아님, ()과 벗겨짐
my_tuple_2 = (1, )  # 이것이 요소가 하나의 튜플일 때임
my_tuple_3 = (1, 'a', 3, 'b', 5)
my_tuple_4 = 1, 'hello', 3.14, True # 모든 종류의 데이터를 담을 수 ㅇ
# 소괄호 없어도 생성 가능
```

### 시퀀스로서의 튜플

```python
my_tuple = (1, 'a', 3, 'b', 5)

# 인덱싱
print(my_tuple[1])  # a

# 슬라이싱
print(my_tuple[2:4])  # (3, 'b')
print(my_tuple[:3])  # (1, 'a', 3)
print(my_tuple[3:])  # ('b', 5)
print(my_tuple[::2])  # (1, 3, 5)
print(my_tuple[::-1])  # (5, 'b', 3, 'a', 1)

# 길이
print(len(my_tuple))  # 5
```

### 튜플의 불변성

- 튜플은 파이썬이 내부 동작(안전한 데이터 전달)을 할 때 사용됨
    - 다중 할당, 값 교환, 함수 다중 반환 값 등

```python
# 튜플은 불변
# TypeError: 'tuple' object does not support item assignment
# my_tuple[1] = 'z'

# 다중 할당
x, y = 10, 20
print(x)  # 10
print(y)  # 20

# 실제 내부 동작
# (x, y) = (10, 20)

# 값 교환
x, y = 1, 2   # 이것도 알고보면 튜플이었음
x, y = y, x

# 실제 내부 동작
temp = (y, x)  # 튜플 생성
x, y = temp  # 튜플 언패킹
print(x, y)  # 2 1

*내부 동작에 활용이 됨, 이처럼 튜플은 데이터의 "안정성과 무결성"을 보장합니다.
*파이썬에서 여러개의 값을 묶어서 활용하고 싶을 때 튜플을 사용함
```

## range

- 연속된 정수 시퀀스를 생성하는, 변경 불가능한(immutable) 자료형
- 주로 반복문과 함께 사용되어 특정 횟수만큼 코드를 반복 실행할 때 매우 유용
- 실제로 모든 숫자를 메모리에 저장하는 대신, 시작 값, 끝 값, 간격이라는 ‘규칙’만 기억하여 메모리를 매우 효율적으로 사용함

### range 기본 구문

- range( )는 1개, 2개, 또는 3개의 매개변수(인자) 를  가질 수 있음
    
    ```python
    range(start, stop, step)
    ```
    
- **range 매개변수별 특징**
    
    ```python
    # range 표현
    my_range_1 = range(5) # 매개변수 1개면 stop으로 인식
    my_range_2 = range(1, 10) # start는 0이, step은 1이 기본값으로 자동 설정
    my_range_3 = range(5, 0, -1) # 0,1,2,3,4
    
    print(my_range_1)  # range(0, 5) # 매개변수 2개면 start와 stop으로 인식
    print(my_range_2)  # range(1, 10) # step은 1이 기본값
    print(my_range_3)  # range(5, 0, -1)
    
    # 리스트로 형 변환 시 데이터 확인 가능 / 이건 거의 사용하지 않음
    print(list(my_range_1))  # [0, 1, 2, 3, 4]
    print(list(my_range_2))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(list(my_range_3))  # [5, 4, 3, 2, 1]
    
    그냥 변환없이 출력하면 덩어리가 나옴
    my_range_1 = range(5)
    
    print(my_range_1) #range(0, 5)
    ```
    

### range의 규칙

1. 값의 범위 규칙
    1. stop 값은 생성되는 시퀀스에 절대 포함되지 않음
    2. range(1, 5)는 1부터 5 ‘전’까지의 숫자를 의미 = 1, 2, 3, 4가 생성
2. 증가/감소 값(step)규칙
    1. step 값은 숫자 시퀀스의 간격과 방향을 결정
    
    ```python
    # 증가/감소 값(step) 규칙
    
    # step이 양수일 때 (기본값 1)
    # 시작 값이 끝 값보다 작은 경우 (정상)
    print(list(range(1, 5)))  # [1, 2, 3, 4]
    # 시작 값이 끝 값보다 큰 경우
    print(list(range(5, 1)))  # []
    
    # step이 음수일 때
    # 시작 값이 끝 값보다 큰 경우 (정상)
    print(list(range(5, 1, -1)))  # [5, 4, 3, 2]
    # 시작 값이 끝 값보다 작은 경우
    print(list(range(1, 5, -1)))  # []
    ```
    
- range 활용 예시
    
    ```python
    # 주로 반복문과 함께 활용 예정
    for i in range(1, 10):
        print(i)  # 1 2 3 4 5 6 7 8 9
    
    for i in range(1, 10, 2):
        print(i)  # 1 3 5 7 9
    ```
    

## dict(딕셔너리)

### 딕셔너리 값 접근

- `key-value 쌍`으로 이루어진 `순서`와 `중복`이 없는 `변경 가능한` 자료형 ⇒ 비시퀀스임

```python
# 딕셔너리 표현
my_dict_1 = {}
my_dict_2 = {'key':'value'}
my_dict_3 = {'apple':12, 'list':[1, 2, 3]}

print(my_dict_1)  # {}
print(my_dict_2)  # {'key': 'value'}
print(my_dict_3)  # {'apple': 12, 'list': [1, 2, 3]}
```

<aside>
💡

딕셔너리 순서?

- 딕셔너리는 순서가 없는 자료형이지만 파이썬 3.7이상에서는 입력한 순서는 출력 시 그대로 유지됩니다.
- 하지만 여전히 딕셔너리의 핵심은 `순서가 없는 자료형`이라는 점과 `key를 통한 접근`이라는 점을 기억합니다.
</aside>

### 딕셔너리 규칙

- key의 규칙
    - 고유해야 함: key는 중복될 수 없음
    - 변경 불가능한 자료형만 사용 가능
        - 가능: str, int, float, tuple
        - 불가능: list, dict
- value의 규칙
    - 어떤 자료형이든 자유롭게 사용할 수 있음

### 딕셔너리 값 접근 방법

- key를 사용하여 해당 value를 꺼내 올 수 있음
- key에 접근 시 대괄호 [ ] 사용
    
    ```python
    # 딕셔너리는 키에 접근해 값을 얻어냄
    my_dict = {'name': '홍길동', 'age': 25}
    print(my_dict['name'])  # '홍길동'
    print(my_dict['test'])  # KeyError: 'test'
    ```
    
    ```python
    # 딕셔너리 값 추가 및 변경
    my_dict = {'apple': 12, 'list': [1, 2, 3]}
    
    # 추가
    my_dict['banana'] = 50
    print(my_dict)  # {'apple': 12, 'list': [1, 2, 3], 'banana': 50}
    
    # 변경
    my_dict['apple'] = 100
    print(my_dict)  # {'apple': 100, 'list': [1, 2, 3], 'banana': 50} 
    
    # 값만 변경!!key는 변경 x
    ```
    

## Set 세트

- 순서와 중복이 없는 변경 가능한 자료형
- 수학에서의 집합과 동일한 연산 처리 가능
- **세트의 두 가지 핵심 특징**
    1. 중복을 허용하지 않음
        1. 똑같은 값은 단 하나만 존재할 수 있음
    2. 순서가 없음
        1. 인덱싱(set[0])이나 슬라이싱(set[0:2])을 사용할 수 없음

```python
# 세트 표현 {  , } 
my_set_1 = set()  # 빈 괄호일 때는 중괄호를 쓰지 않음 dict와 유사하게 생김
my_set_2 = {1, 2, 3}
my_set_3 = {1, 1, 1}

print(my_set_1)  # set()
print(my_set_2)  # {1, 2, 3}
print(my_set_3)  # {1}

```

### 세트의 집합 연산

- 세트의 집합 연산
    - 세트는 수학의 ‘집합’ 개념을 그대로 가져와, 두 데이터 그룹 간의 관계를 파악하는 데 매우 효과적
    - 튜플과 세트는 아주 중요한 것은 아니지만 세트는 튜플보다 많이 쓰이기는 함

```python
# 세트의 집합 연산산
my_set_1 = {1, 2, 3}
my_set_2 = {3, 6, 9}

# 합집합
print(my_set_1 | my_set_2)  # {1, 2, 3, 6, 9}

# 차집합
print(my_set_1 - my_set_2)  # {1, 2}

# 교집합
print(my_set_1 & my_set_2)  # {3}
```

## other type

### none

- 파이썬에서 ‘`값이 없음’`을 표현하는 특별한 데이터 타입
- 내용물이 없는 ‘빈 상자’와 같음(아직 무는 아님)
- 숫자 0이나 빈 문자열(’ ‘)과는 다른, ‘값이 존재하지 않음’ 또는 ‘아직 정해지지 않음’이라는 상태를 나타내기 위해 사용됨

```python
# None
# my_variable에는 아직 아무 값도 할당하고 싶지 않을 때 사용함

my_variable = None # 반드시 대문자로 작성하기
print(my_variable)  # None
```

### boolean

- 참(True)과 거짓(False) 단 두 가지 값만 가지는 데이터 타입
- 비교/ 논리 연산의 평가 결과로 사용됨
- *주로 조건/반목문과 함께 사용할 예정임(이래야 **프로그램 흐름 제어**가 가능해짐)

```python
# Boolean
is_active = True
is_logged_in = False

print(is_active)  # True
print(is_logged_in)  # False
print(10 > 5)  # True  === 이 표현식의 결과로 불리언이 나옴
print(10 == 5)  # False 

```

## collection

- 여러 개의 값을 하나로 묶어 관리하는 자료형을 통칭하는 말
- 여러 물건을 담는 ‘보관함’과 같으며, 파이썬은 목적에 따라 다양한 종류의 컬렉션을 제공합니다
- str, list, tuple, range, set, dict 데이터 타입이 모두 Collection에 분류됩니다
    
    
    | 컬렉션명 | 변경 가능 여부 | 순서 존재 여부 |
    | --- | --- | --- |
    | str | x | o(시퀀스) |
    | list | o | o |
    | tuple | x | o |
    | dict | o | x(비시퀀스) |
    | set | o | x |

### 불변과 가변

- 컬렉션 타입은 생성 후 내용을 변경할 수 있는지 없는지에 따라 ‘불변’과 ‘가변’ 두 그룹으로 나뉨
    
    
    | 구분 | 불변(Immutable) | 가변(Mutable) |
    | --- | --- | --- |
    | 특징 | 변경불가, 안전성, 예측가능 | 변경 가능, 유연성, 효율성 |
    | 종류 | str, tuple, range | list, dict, set |

```python
# immutable (불변)
my_str = 'hello'
my_str[0] = 'z'  # TypeError: 'str' object does not support item assignment

# mutable (가변)
my_list = [1, 2, 3]
my_list[0] = 100
print(my_list)  # [100, 2, 3]
```

## 형변환(type Conversion)

- 한 데이터 타입을 `다른 데이터 타입으로 변환`하는 과정

### 1. 암시적 형변환(Implict Conversion)

- 파이썬이 연산 중에 자동으로 데이터 타입을 변환하는 것
- 암시적 형변환은 파이썬이 데이터 손실을 막기 위해 더 정밀한 타입으로 자동 변환

```python
# 암시적 형변환
# 정수(int)와 실수(float)의 덧셈
print(3 + 5.0)  # 8.0
# 불리언(bool)과 정수(int)의 덧셈
print(True + 3)  # 4
# 불리언간의 덧셈
print(True + False)  # 1
```

### 2. 명시적 형변환: 거의 암시적 이외 전부

- 개발자가 변환하고 싶은 타입을 직접 함수로 지정하여 변환하는 것

```python
# 명시적 형변환
# str -> int
print(int('1'))  # 1
# ValueError: invalid literal for int() with base 10: '3.5'
# print(int('3.5'))
print(int(3.5))  # 3
print(float('3.5'))  # 3.5

# int -> str
print(str(1) + '등')  # 1등
```

![image.png](image.png)

### 형변환 함수 표

| 함수 | 설명 | 예시 | 결과 |
| --- | --- | --- | --- |
| int() | 정수로 변환 | int("123") | 123 |
| float() | 실수로 변환 | float("3.14") | 3.14 |
| str() | 문자열로 변환 | str(100) | "100" |
| list() | 리스트로 변환 | list("abc") | ['a','b','c'] |
| tuple() | 튜플로 변환 | tuple([1,2]) | (1, 2) |
| set() | 세트로 변환 | set([1,2,2]) | {1, 2} |

b. str → int 형식에 맞는 숫자만 가능

```python
print(int('1')) #1

# ValueError
print(int('3.5'))
```

c. int → str : 모두 가능

```python
print(str(1) + '등') # 1등
```

## 연산자

### 산술연산자

- 수학적 계산을 위해 사용되는 연산자
    
    ### 산술 연산자 표
    
    | 기호 | 연산자 |
    | --- | --- |
    | - | 음수 부호 |
    | + | 덧셈 |
    | - | 뺄셈 |
    | * | 곱셈 |
    | / | 나눗셈 |
    | // | 정수 나눗셈(몫) |
    | % | 나머지 |
    | ** | 지수(거듭제곱) |

### 복합연산자

- 연산과 할당이 함께 이뤄짐
    
    
    | 기호 | 예시 | 의미 |
    | --- | --- | --- |
    | += | a += b | a = a + b |
    | -= | a -= b | a =a - b |
    | *= | a *= b | a = a * b |
    | /= | a /= b | a = a / b |
    | //= | a //= b | a = a // b |
    | %= | a %= b | a = a % b |
    | **= | a **= b | a = a ** b |
    
    ```python
    # 복합 연산자
    y = 10
    y -= 4 # y = y - 4
    print(y)  # 6  
    
    z = 7
    z *= 2
    print(z)  # 14
    
    w = 15
    w /= 4
    print(w)  # 3.75
    
    q = 20
    q //= 3
    print(q)  # 6
    ```
    

### 비교연산자

- 두 값을 비교하여 그 관계가 맞는지 틀린지를 True 또는 False로 반환
    
    
    | 기호 | 내용 |
    | --- | --- |
    | < | 미만 |
    | < = | 이하 |
    | > | 초과 |
    | > = | 이상 |
    | == | 같음 |
    | ! = | 같지 않음 |
    | is | 같음 |
    | is not | 같지 않음 |
    
    ```python
    # 비교 연산자 예시 
    print(3 > 6)  # False
    print(3 < 6)  # True
    print(3 >= 3)  # True
    print(3 <= 6)  # True
    ```
    
- == 연산자
    - 값(데이터)이 같은지를 비교
    - 동등성(equality)
    - 예를 들어, 1 == True의 경우 파이썬이 내부적으로 True를 1로 간주할 수 있으므로 True 결과가 나옴
    
    ```python
    print(2 is 2.0) #False
    
    # == 연산자
    print(2 == 2.0)  # True
    print(2 != 2)  # False
    print('HI' == 'hi')  # False
    print(1 == True)  # True
    ```
    
- is 연산자
    - 객체 자체가 같은지를 비교
    - 식별성(identity)
    - 두 변수가 완전히 동일한 객체를 가리키는지, 즉 메모리 주소가 같은지를 확인할 때 사용
    
    ```python
    # is 연산자
    # SyntaxWarning: "is" with a literal. Did you mean "=="?
    print(1 is True)  # False
    print(2 is 2.0)  # False
    ```
    
- is 대신 ==를 사용해야 하는 이유
    - **is는 ‘정체성’, ==를 ‘가치’ 비교**
    - 두 연산자는 “같다”를 확인하는 목적이 근본적으로 다름
    - is(Identity Operator):
        - 두 변수가 완전히 동일한 메모리 주소의 객체를 가리키는지, 즉 ‘정체성’이 같은지를 확인
    - ==(Equality Operator)
        - 두 변수가 가리키는 객체의 내용, 즉 ‘값(value)’이 같은지를 확인
- is를 값 비교에 사용하면 안 되는 이유 - “의도와 다른 결과를 낳습니다.”
    
    ```python
    # 왜 is 대신 ==를 사용해야 하나?
    # 1(정수)과 True(불리언)는 다른 객체이다.
    print(1 is True)  # False
    # 1과 True의 '값'은 논리적으로 같다.
    print(1 == True)  # True
    
    # 2(정수)와 2.0(실수)은 다른 객체이다.
    print(2 is 2.0)  # False
    # 2와 2.0의 '값'은 논리적으로 같다.
    print(2 == 2.0)  # True
    ```
    
- is 연산자는 언제 사용하는가?
    - 주로 싱글턴 객체를 비교할 때 사용함
- 싱글턴(Singleton) 객체란?
    - 특정 값에 대해 파이썬 전체에서 단 하나의 객체만 생성되어 재사용되는 특별한 객체
    - 여러 변수가 이 값을 가지더라도, 모두 미리 만들어진 하나의 객체를 함께 가리키게 되므로 항상 같은 메모리 주소를 가짐
    - 파이썬의 대표적인 싱글턴 객체: None, True, False
- 싱글턴 객체를 비교할 때
    - is 연산자는 두 변수가 완전히 동일한 객체를 가리키는지, 즉 메모리 주소가 같은지를 확인할 때 사용
    - 파이썬 전체에서 단 하나의 객체만 생성되어 재사용되는 싱글턴 객체 비교에 적합함
    
    ```python
    # is 연산자는 언제 사용하는가?
    # 싱글턴 객체 비교할 때
    x = None
    # 권장
    if x is None:
        print('x는 None입니다.')
    # 비권장
    if x == None:
        print('x는 None입니다.')
    
    x = True
    y = True
    print(x is y)  # True
    print(True is True)  # True
    print(False is False)  # True
    print(None is None)  # True
    ```
    
- 추가 예시: 리스트나 객체 비교 시 주의사항
    - 리스트 또는 다른 가변 객체(mutable)를 비교할 때, 값 자체가 같은 지 확인하려면 ==를 사용
    - 두 변수가 완전히 동일한 객체를 가리키는지 확인해야 한다면 is를 사용
    
    ```python
    a = [1, 2, 3]
    b = [1, 2, 3]
    
    print(a == b) # True (두 리스트의 값은 동일)
    print(a is b) # False (서로 다른 리스트 객체)
    
    # b가 a를 그대로 참조하도록 할 경우
    b = a
    print(a is b) #true(같은 객체를 가리키므로 Ture)
    ```
    

### 논리 연산자

- 여러 개의 조건을 조합하거나, True/False 값을 반대로 뒤집을 때 사용(and, or, not이 대표적)
    
    
    | 기호 | 연산자 | 내용 |
    | --- | --- | --- |
    | and | 논리곱 | 두 피연산자 모두 True인 경우에만 전체 표현식을 True로 평가 |
    | or | 논리합 | 두 피연산자 중 하나라도 True인 경우 전체 표현식을 True로 평가 |
    | not | 논리부정 | 단일 피연산자를 부정 |
    
    ```python
    # 논리 연산자
    print(True and False)  # False
    print(True or False)  # True
    print(not True)  # False
    print(not 0)  # True
    
    # 논리 연산자 & 비교 연산자
    num = 15
    result = (num > 10) and (num % 2 == 0)
    print(result)  # False
    
    name = 'Alice'
    age = 25
    result = (name == 'Alice') or (age == 30)  # 앞이 참이면 뒤는 보지 않고 평가를 내버림
    print(result)  # True
    
    ```
    

### 단축평가

- 논리 연산에서 두 번째 피연산자를 평가하지 않고 결과를 결정하는 동작
- 단축평가 하는 이유: 코드 실행을 최적화하고, 불필요한 연산을 줄이기 위함
    - 거짓으로 취급되는 값들
        - False, 숫자 0, 빈 문자열 “”, 빈리스트 [ ], None 등, ‘비어있거나 없다’는 느낌의 값들
    - 참으로 취급되는 값들
        - True 그리고 ‘거짓’이 아닌 모든 값
        - 1, -10, “hello”,[1,2] 등 내용이 있는 값
    - and 연산자
        - 하나라도 ‘거짓’이면 바로 ‘거짓’
        - and는 연산을 왼쪽에서 오른쪽으로 진행하다가, 처음 만나는 ‘거짓’값을 바로 반환
        - 만약 끝까지 갔는데 모든 값이 ‘참’이면, 맨 마지막 ‘참’값을 반환
    - or 연산자
        - 하나라도 ‘참’이면 바로 ‘참’
        - or는 연산을 왼쪽에서 오른쪽으로 진행하다가, 처음 만나는 ‘참’값을 바로 반환
        - 만약 끝까지 갔는데 모든 값이 ‘거짓’이면, 맨 마지막 ‘거짓’ 값을 반환
    
    ```python
    # 단축 평가
    
    # 1
    # 준비물 1: 내용이 있는 문자열
    item1 = '지도'
    # 준비물 2: 내용이 있는 문자열
    item2 = '나침반'
    result = item1 and item2
    print(f'최종적으로 챙긴 물건: {result}')
    # >> 최종적으로 챙긴 물건: 나침반
    
    # 2
    item1 = '지도'
    # 준비물 2: 내용이 없는 빈 문자열
    item2 = ''
    result = item1 and item2
    print(f'최종적으로 챙긴 물건: "{result}"')
    # >> 최종적으로 챙긴 물건: ' '
    
    # 3
    # 준비물 1: 내용이 없는 빈 문자열
    item1 = ''
    item2 = '나침반'
    result = item1 and item2
    print(f'최종적으로 챙긴 물건: "{result}"')
    # >> 최종적으로 챙긴 물건: ' '
    
    ```
    

### 멤버십 연산자

- 특정 값이 시퀀스나 다른 컬렉션 안에 포함되어 있는지 확인하는 연산자
    - in : 왼쪽 피연산자가 오른쪽 피연산자의 시퀀스에 속하는지를 확인
    - not in : 왼쪽 피연산자가 오른쪽 피연산자의 시퀀스에 속하지 않는지를 확인

```python
# 멤버십 연산자

word = 'hello'
numbers = [1, 2, 3, 4, 5]

print('h' in word)  # True
print('z' in word)  # False

print(4 not in numbers)  # False
print(6 not in numbers)  # True
```

### 시퀀스 연산자

- 시퀀스 자료형(문자열, 리스트, 튜플)에 특별한 의미로 사용되는 연산자
- + : 결합 연산자(시퀀스 연결)
- * : 반복 연산자(시퀀스 반복)
    
    ```python
    # 시퀀스형 연산자
    
    print('Gildong' + ' Hong')  # Gildong Hong
    print('hi' * 5)  # hihihihihi
    
    print([1, 2] + ['a', 'b'])  # [1, 2, 'a', 'b']
    print([1, 2] * 2)  # [1, 2, 1, 2]
    ```
    

### 연산자 우선순위

- 외우기 보다는 가장 자주 쓰이는 걸 알아두기
    
    
    | 우선순위 | 연산자 | 내용 |
    | --- | --- | --- |
    | 높음 | () | 소괄호 grouping |
    |  | [] | 인덱싱, 슬라이싱 |
    |  | ** | 거듭제곱 |
    |  | +, - | 단항 연산자 양수/음수 |
    |  | *, /, //, % | 산술 연산자 |
    |  | +, - | 산술 연산자 |
    |  | <, <=, >, >=, ==, != | 비교 연산자 |
    |  | is, is not | 객체 비교 |
    |  | in, not in | 멤버십 연산자 |
    |  | not | 논리 부정 |
    |  | and | 논리 AND |
    | 낮음 | or | 논리 OR |

## 참고 | Trailing Comma

- 컬렉션의 마지막 요소 뒤에 붙는 쉼표
- 선택사항이지만, 단 하나의 요소로 구성된 튜플을 만들 때는 필수임
- 각 요소를 별도의 줄에 작성, 마지막 요소에 Trailing Comma 추가, 닫는 괄호는 새로운 줄에 배치
- 장점
    1. 가독성 향상
        1. 각 줄이 동일한 패턴을 가짐
        2. 코드 리뷰가 용이함
    2. 유지보수 용이성
        1. 항목추가/제거가 간단
        2. 실수로 인한 구문 오류 방지
    
    ```python
    items = [
    	'item1',
    	'item2',
    	'item3',
    ]
    
    config = {
    	'host' : 'localhost',
    	'port': 8080,
    	'debug':True,
    }
    ```
    
    ```python
    나쁜예시
    items = ['item1','item2',]
    # 한줄작성 시 불필요
    items = ['item1','item2']
    ```
