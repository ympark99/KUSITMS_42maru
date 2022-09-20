import re

patterns = [r'\d+년 \d+월 \d+일|\d+일|\d+월 \d+일|오늘|어제|내일|모레|그저께|글피|저번주|이번주|다음주|다다음주|이번달|저번달|다음달|지난해|작년|내년',
            r'\d+부|\d+회|\d+편|\d+차|\d+회차|\d+화',
            r'\d+%|\d+퍼센트|\d+프로'
            ]

entity_names = ['@sys.date',
                '@sys.number.times',
                '@sys.number.percent'
                ]


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

# 테스트 함수
def test():
    assert solution("2018년 1월 15일에 보낸 메일 찾아줘") ==\
           [[['@sys.date'], ['2018년 1월 15일'], [0], [12], '@sys.date에 보낸 메일 찾아줘']]
