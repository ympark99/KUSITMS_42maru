import re

patterns = [r'[0-9]{2,3}\s[가-힣]{1}\s[0-9]{4}',
            r'[가-힣]+[띠]',
            r'[A-Z]{3}',
            r'[가-힣]+[광역시|특별시|도|시|읍|면|동|가|리|군|구|로|길]',
            r'\d{3}-\d{4}-\d{4}',
            r'[가-힣]+[자리]',
            r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+',
            r'^(\d{3,3})+[-]+(\d{2,2})+[-]+(\d{5,5})',
            r'^(\d{1,})(-(\d{1,})){1,}',
            r'^(\d{6,6})+[-]+(\d{7,7})']

entity_names = ['@sys.licenseplate.number',
                '@sys.fortune.zodiac',
                '@sys.currency.code',
                '@sys.location',
                '@sys.phone.number',
                '@sys.fortune.starsign',
                '@sys.url',
                '@sys.business.number',
                '@sys.account.number',
                '@sys.corporate.number']

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

print(solution("서울특별시에서 왔어"))

