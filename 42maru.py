import re

patterns = [r'\d+년 \d+월 \d+일|\d+일|\d+월 \d+일|오늘|어제|내일|모레|그저께|글피|저번주|이번주|다음주|다다음주|이번달|저번달|다음달|지난해|작년|내년',
            r'\d+부|\d+회|\d+편|\d+차|\d+회차|\d+화',
            r'\d+%|\d+퍼센트|\d+프로',
            r'\d{1,4}년생',
            r'\d{1,4}년대',
            r'\d*위|\d*등|\d*순위',
            r'\b\d*분\s\d{1,2}초\b|\b\d{1,2}초\b|\b\d*분\b|\b\d*시간\s반\b|\b\d*시간\b|\b\d*시간\s\d{1,2}분\s\d{1,2}초\b|\b\d*시간\s\d{1,2}분\b|\d*일|\d*주|\d*주일|[가-힣]주일|\d*개월\s\d{1,2}일|\d*개월|\d*년\s\d{1,2}개월|\d*년',
            r'\b\d*m\b|\b\d*cm\b|\b\d*mm\b|\b\d*km\b|\b\d*센티미터\b|\b\d*미터\b|\b\d*밀리미터\b|\b\d*킬로미터\b|\b\d*야드\b|\b\d*피트\b|\b\d*인치\b|\b\d*마일\b',
            r'\d*.\d{1,3}km²| \d{1,3}.\d{1,3}m² | \d{1,3}.\d{1,3}yd² | \d{1,3}.\d{1,3}km² | \d{1,3}.\d{1,3}ft² | \d{1,3}.\d{1,3}제곱미터 | \d{1,3}.\d{1,3}제곱킬로미터 | \d{1,3}.\d{1,3}헥타아르 | \d{1,3}.\d{1,3}평 | \d{1,3}.\d{1,3}에이커'
            r'\b\d*kg\b|\b\d*g\b|\b\d*mg\b|\b\d*톤\b|\b\d*파운드\b|\b\d*온스\b|\b\d*그레인\b|\b\d*돈\b|\b\d*근\b|\b\d*냥\b|\b\d*관\b',
            r'\d*.\d{1,3}cc|\d*.\d{1,3}ml|\d*.\d{1,3}L|\d*.\d{1,3}톤|\d*.\d{1,3}데시리터|\d*.\d{1,3}밀리리터|\d*.\d{1,3}리터|\d*.\d{1,3}갤론|\d*.\d{1,3}cc|\d*.\d{1,3}cm³|\d*.\d{1,3}m³|\d*.\d{1,3}in³|\d*.\d{1,3}ft³|\d*.\d{1,3}yd³|\d*.\d{1,3}홉|\d*.\d{1,3}되|\d*.\d{1,3}말',
            r'\d*기압|\d*프사이|\d*파스칼|\d*헥토파스칼|\d*메가파스칼|\d*밀리바|\d*바|\d*수은주밀리미터|\d*mmH₂O|\d*inHg|\d*inchH₂O',
            r'\d*.\d*도|\d*.\d*°c|\d*.\d*°f',
            r'\d.\dm/[smh]|\d.\dkm/[smh]|\d.\d마하|\d.\dknot',
            r'\d*.\d*비트|\d*.\d*바이트|\d*.\d*킬로바이트|\d*.\d*메가바이트|\d*.\d*기가바이트|\d*.\d*테라바이트|\d*.\d*bit|\d*.\d*byte|\d*.\d*KB|\d*.\d*MB|\d*.\d*GB|\d*.\d*TB',
            r'\d*.\d*헤르츠|\d*.\d*킬로헤르츠|\d*.\d*메가헤르츠|\d*.\d*Mhz|\d*.\d*kHz|\d*.\d*기가헤르츠|\d*.\d*데시벨|\d*.\d*ampre|\d*.\d*암페어|\d*.\d*마',
            ]

entity_names = ['@sys.date',
                '@sys.number.times',
                '@sys.number.percent',
                '@sys.number.birthyear',
                '@sys.number.decade',
                '@sys.number.rank',
                '@sys.unit.duration',
                '@sys.unit.length',
                '@sys.unit.area',
                '@sys.unit.weight',
                '@sys.unit.volume',
                '@sys.unit.pressure',
                '@sys.unit.temperature',
                '@sys.unit.speed',
                '@sys.unit.data',
                '@sys.unit.energy'
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


print(solution("1996년생 운세 알려줘, 1990년대 발라드 틀어줘, 멜론 차트 10위부터 틀어줘, 1시간 타이머 맞춰줘, 1m 간격으로 앉으세요, 서울의 면적은 605.2km²입니다, 1돈은 3.75그램입니다, 1.0cc는 0.001리터를 의미한다, 1기압은 몇 파스칼입니까?, 거실 난방 20도로 맞춰줘, 100m/s는 0.1km/s 입니다, 1비트는 8비트 입니다, 12Mhz는 1000kHz 입니다"))