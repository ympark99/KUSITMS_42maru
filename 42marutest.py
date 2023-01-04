import re

patterns = [
            r'\d+년 \d+월 \d+일|\d+일|\d+월 \d+일|오늘|어제|내일|모레|그저께|글피|저번주|이번주|다음주|다다음주|이번달|저번달|다음달|지난해|작년|내년',
            r'음력 \d+월|음력\d+월|음력에서 \d+번째',
            r'오전|아침|정오|점심|저녁|새벽|\d+시부터|\d+시까지',
            r'\d+부|\d+회|\d+편|\d+차|\d+회차|\d+화',
            r'\d+%|\d+퍼센트|\d+프로',
            r'\d+번|\d+ 번째|첫 번째|두 번째|세 번째|네 번째|다섯 번째|여섯 번째|일곱 번째|여덟 번째|아홉 번째',
            r'\d+살',
            #민서
            r'\d{1,4}년생',
            r'\d{1,4}년대',
            r'\d*위|\d*등|\d*순위',
            r'\b\d*m\b|\b\d*cm\b|\b\d*mm\b|\b\d*km\b|\b\d*센티미터\b|\b\d*미터\b|\b\d*밀리미터\b|\b\d*킬로미터\b|\b\d*야드\b|\b\d*피트\b|\b\d*인치\b|\b\d*마일\b',
            r'\d*.\d{1,3}km²| \d{1,3}.\d{1,3}m² | \d{1,3}.\d{1,3}yd² | \d{1,3}.\d{1,3}km² | \d{1,3}.\d{1,3}ft² | \d{1,3}.\d{1,3}제곱미터 | \d{1,3}.\d{1,3}제곱킬로미터 | \d{1,3}.\d{1,3}헥타아르 | \d{1,3}.\d{1,3}평 | \d{1,3}.\d{1,3}에이커'
            r'\b\d*kg\b|\b\d*g\b|\b\d*mg\b|\b\d*톤\b|\b\d*파운드\b|\b\d*온스\b|\b\d*그레인\b|\b\d*돈\b|\b\d*근\b|\b\d*냥\b|\b\d*관\b',
            r'\d*.\d{1,3}cc|\d*.\d{1,3}ml|\d*.\d{1,3}L|\d*.\d{1,3}톤|\d*.\d{1,3}데시리터|\d*.\d{1,3}밀리리터|\d*.\d{1,3}리터|\d*.\d{1,3}갤론|\d*.\d{1,3}cc|\d*.\d{1,3}cm³|\d*.\d{1,3}m³|\d*.\d{1,3}in³|\d*.\d{1,3}ft³|\d*.\d{1,3}yd³|\d*.\d{1,3}홉|\d*.\d{1,3}되|\d*.\d{1,3}말',
            r'\d*기압|\d*프사이|\d*파스칼|\d*헥토파스칼|\d*메가파스칼|\d*밀리바|\d*바|\d*수은주밀리미터|\d*mmH₂O|\d*inHg|\d*inchH₂O',
            r'\d*.\d*도|\d*.\d*°c|\d*.\d*°f',
            r'\d.\dm/[smh]|\d.\dkm/[smh]|\d.\d마하|\d.\dknot',
            r'\d*.\d*비트|\d*.\d*바이트|\d*.\d*킬로바이트|\d*.\d*메가바이트|\d*.\d*기가바이트|\d*.\d*테라바이트|\d*.\d*bit|\d*.\d*byte|\d*.\d*KB|\d*.\d*MB|\d*.\d*GB|\d*.\d*TB',
            r'\d*.\d*헤르츠|\d*.\d*킬로헤르츠|\d*.\d*메가헤르츠|\d*.\d*Mhz|\d*.\d*kHz|\d*.\d*기가헤르츠|\d*.\d*데시벨|\d*.\d*ampre|\d*.\d*암페어|\d*.\d*마',
            r'[0-9]{2,3}\s[가-힣]{1}\s[0-9]{4}',
            r'[가-힣]+[띠]',
            r'[가-힣]+[광역시|특별시|도|시|읍|면|동|가|리|군|구|로|길]',
            r'\d{3}-\d{4}-\d{4}',
            r'[가-힣]+[자리]',
            r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+',
            r'^(\d{3,3})+[-]+(\d{2,2})+[-]+(\d{5,5})',
            r'^(\d{6,6})+[-]+(\d{7,7})'
            ]

entity_names = [
                '@sys.date',
                '@sys.date.lunar',
                '@sys.time',
                '@sys.number.times',
                '@sys.number.percent',
                '@sys.number.ordinal',
                '@sys.number.age',
                '@sys.number.birthyear',
                '@sys.number.decade',
                '@sys.number.rank',
                '@sys.unit.length',
                '@sys.unit.area',
                '@sys.unit.weight',
                '@sys.unit.volume',
                '@sys.unit.pressure',
                '@sys.unit.temperature',
                '@sys.unit.speed',
                '@sys.unit.data',
                '@sys.unit.energy',
                '@sys.licenseplate.number',
                '@sys.fortune.zodiac',
                '@sys.location',
                '@sys.phone.number',
                '@sys.fortune.starsign',
                '@sys.url',
                '@sys.business.number',
                '@sys.corporate.number'
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

    assert solution("1996년생 운세 알려줘") ==\
           [[['@sys.number.birthyear'], ['1996년생'], [0], [6], '@sys.number.birthyear 운세 알려줘']]

    assert solution("1990년대 발라드 틀어줘") ==\
           [[['@sys.number.decade'], ['1990년대'], [0], [6], '@sys.number.decade 발라드 틀어줘']]

    assert solution("멜론 차트 10위부터 틀어줘") ==\
           [[['@sys.number.rank'], ['10위'], [6], [9], '멜론 차트 @sys.number.rank부터 틀어줘']]

    assert solution("서울의 면적은 605.2km²입니다") ==\
           [[['@sys.unit.area'], ['605.2km²'], [8], [16], '서울의 면적은 @sys.unit.area입니다']]

    assert solution("나는 뱀띠야") ==\
           [[['@sys.fortune.zodiac'], ['뱀띠'], [3], [5], '나는 @sys.fortune.zodiac야']]
            
     assert solution("내 전화번호는 010-1111-1111 이고 나는 서울특별시에 살아") == \
           [[['@sys.location', '@sys.phone.number'], ['서울특별시', '010-1111-1111'], [28, 8], [33, 21], '내 전화번호는 @sys.phone.number 이고 나는 @sys.location에 살아']]

