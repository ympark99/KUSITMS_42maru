## 큐시즘 26기 42MARU x KUSTIMS

### 개발과제 : 시스템 엔티티 구현

> 시스템에 등록된 개체명을 특정 문장에서 추출하는 python module 개발
> 

### Output 양식

| entity_name | 문장에서 찾아낸 개체명 |
| --- | --- |
| value | 문장에서 찾아낸 개체명의 value |
| start_idx | 문장에서 개체명이 시작하는 위치 |
| end_idx | 문장에서 개체명이 끝나는 위치 |
| tagged_sentence | 문장을 개체명으로 치환한 결과 |

### Input 예시

`"2018년 1월 15일에 보낸 메일 찾아줘"`

### Output 예시

`[[['@sys.date'], ['2018년 1월 15일'], [0], [12], '@sys.date에 보낸 메일 찾아줘']]`

### 구현

1. 예시 문장 data를 매개변수로 받는다.
2. 정규표현식을 반복해가며 finditer로 data에서 정규표현식과 일치하는 부분이 있는지 검사한다.
3. 예시의 output에 맞게 list를 제작해 append한다.

```python
def solution(data):
    entity_out = list()
    value = list()
    startIdx = list()
    endIdx = list()
    tagged_sentence = data
    output = list([])

    for i in range(len(patterns)):
        pattern = patterns[i]
        entity_name = entity_names[i]

        result = re.finditer(pattern, data)
        for matchObj in result:
            entity_out.append(entity_name)
            value.append(matchObj.group())
            startIdx.append(matchObj.start())
            endIdx.append(matchObj.end())
            tagged_sentence = re.sub(pattern, entity_name, tagged_sentence, 1)

    output.append([entity_out, value, startIdx, endIdx, tagged_sentence])
    return output

# - patterns : 정규표현식 list
# - entity_names : 엔티티 이름 list
```
