# -*- coding: utf-8 -*-

import string

# Bảng mã chữ cái của Việt Nam
chars_map = {
    "à": "a", "á": "a", "ả": "a", "ã": "a", "ạ": "a", "ằ": "ă", "ắ": "ă",
    "ẳ": "ă", "ẵ": "ă", "ặ": "ă", "ầ": "â", "ấ": "â", "ẩ": "â", "ẫ": "â",
    "ậ": "â", "è": "e", "é": "e", "ẻ": "e", "ẽ": "e", "ẹ": "e", "ề": "ê",
    "ế": "ê", "ể": "ê", "ễ": "ê", "ệ": "ê", "ì": "i", "í": "i", "ỉ": "i",
    "ĩ": "i", "ị": "i",  "ò": "o", "ó": "o", "ỏ": "o", "õ": "o", "ọ": "o",
    "ồ": "ô", "ố": "ô", "ổ": "ô", "ỗ": "ô", "ộ": "ô", "ờ": "ơ", "ớ": "ơ",
    "ở": "ơ", "ỡ": "ơ", "ợ": "ơ", "ù": "u", "ú": "u", "ủ": "u", "ũ": "u",
    "ụ": "u", "ừ": "ư", "ứ": "ư", "ử": "ư", "ữ": "ư", "ự": "ư", "ỳ": "y",
    "ý": "y", "ỷ": "y", "ỹ": "y", "ỵ": "y"
}
# Lấy n ký tự từ điểm bắt đầu và điểm cuối.
def get_nchars(text, start=1, end=2):
    chars = text[start:end].strip()
    for ch in chars:
        nh = chars_map.get(ch, ch)
        if nh == ch:
            continue
        chars = chars.replace(ch, nh)
    return chars.lower()

# Hàm kiểm tra chuỗi là một số thực hoặc số nguyên
def is_number(s):
    v = s.lstrip('-')
    v = v.lstrip('+')
    v = v.replace(',','')
    v = v.replace('.','')
    return v.isdigit()

# Kiểm tra một từ có phải là chữ quốc ngữ hay không ?
def isVNESE(syllabel):
    ch = syllabel[0:1].lower() # Lấy chữ cái đầu tiên để kiểm tra
    if len(syllabel) == 1: # Nếu như chữ cho vào là một ký tự
        # Chữ quốc ngữ sẽ là chữ có một chữ cái hợp lệ trong bảng mã
        # hoặc là các ký tự latin, con số và các ký tự đặc biệt của latin
        if ch in chars_map.keys() or ch in chars_map.values():
            return True
        if ch in '0123456789abcdefghijklmnopqrstuvwxyz' + string.punctuation:
            return True
        return False
    # Nếu là một con số nào đó thì là đúng
    if is_number(syllabel):
        return True
    ch = chars_map.get(ch, ch)
    # Tiến hành kiểm tra tính hợp lệ của các nguyên âm
    # các nguyên âm sẽ tuân thủ theo luật tạo chữ quốc ngữ
    # nếu như thỏa mãn là chữ quốc ngữ thì cuối từ phải là một khoảng trắng
    # hoặc là không có ký tự nào sau hết. Đó là nguyên nhân vì sao phải kiểm
    # tra độ dài sau khi đã kiểm tra một thành phần xong
    if ch == 'a':
        chk = get_nchars(syllabel,0,3)
        if chk in ['ang', 'anh', 'ach']:
            if syllabel[3:4]:
                return False
            return True
        if len(chk) > 2:
            return False
        if get_nchars(syllabel,0,2) in ['ac', 'ai', 'am', 'an','ao', 'ap',
                                        'at', 'au', 'ay']:
            if syllabel[2:3]:
                return False
            return True
        return False
    if ch == 'ă':
        chk = get_nchars(syllabel,0,3)
        if chk in ['ăng']:
            if syllabel[3:4]:
                return False
            return True
        if len(chk) > 2:
            return False
        if get_nchars(syllabel,0,2) in ['ăc', 'ăm', 'ăn', 'ăp', 'ăt']:
            if syllabel[2:3]:
                return False
            return True
        return False
    if ch == 'â':
        chk = get_nchars(syllabel,0,3)
        if chk in ['âng']:
            if syllabel[3:4]:
                return False
            return True
        if len(chk) > 2:
            return False
        if get_nchars(syllabel,0,2) in ['âc', 'âm', 'ân', 'âp', 'ât', 'âu',
                                        'ây']:
            if syllabel[2:3]:
                return False
            return True
        return False
    if ch == 'e':
        chk = get_nchars(syllabel,0,3)
        if chk in ['eng']:
            if syllabel[3:4]:
                return False
            return True
        if len(chk) > 2:
            return False
        if get_nchars(syllabel,0,2) in ['ec', 'em', 'en', 'eo', 'ep', 'et']:
            if syllabel[2:3]:
                return False
            return True
        return False
    if ch == 'ê':
        chk = get_nchars(syllabel,0,3)
        if chk in ['êch', 'ênh','êng']:
            if syllabel[3:4]:
                return False
            return True
        if len(chk) > 2:
            return False
        if get_nchars(syllabel,0,2) in ['êm', 'ên', 'êp', 'êt', 'êu']:
            if syllabel[2:3]:
                return False
            return True
        return False
    if ch == 'i':
        chk = get_nchars(syllabel,0,4)
        if chk in ['iêng']:
            if syllabel[4:5]:
                return False
            return True
        if len(chk) > 3:
            return False
        chk = get_nchars(syllabel,0,3)
        if chk in ['ich', 'inh','iêc','iêm','iên','iêp','iêt','iêu']:
            if syllabel[3:4]:
                return False
            return True
        if len(chk) > 2:
            return False
        if get_nchars(syllabel,0,2) in ['im', 'in', 'ia', 'ip', 'it', 'iu']:
            if syllabel[2:3]:
                return False
            return True
        return False
    if ch == 'o':
        chk = get_nchars(syllabel,0,4)
        if chk in ['oong','oach','oang','oanh','oăng','oeng']:
            if syllabel[4:5]:
                return False
            return True
        if len(chk) > 3:
            return False
        chk = get_nchars(syllabel,0,3)
        if chk in ['ong', 'ooc','oac','oai','oam','oan','oap','oao','oat',
            'oay','oăc','oăm','oăn','oăt','oen', 'oeo', 'oet', 'oem']:
            if syllabel[3:4]:
                return False
            return True
        if len(chk) > 2:
            return False
        if get_nchars(syllabel,0,2) in ['oc', 'oi', 'om', 'on', 'op', 'ot',
                                        'oa','oe']:
            if syllabel[2:3]:
                return False
            return True
        return False
    if ch == 'ô':
        chk = get_nchars(syllabel,0,3)
        if chk in ['ông']:
            if syllabel[3:4]:
                return False
            return True
        if len(chk) > 2:
            return False
        if get_nchars(syllabel,0,2) in ['ôc', 'ôi', 'ôm', 'ôn', 'ôp', 'ôt']:
            if syllabel[2:3]:
                return False
            return True
        return False
    if ch == 'ơ':
        if get_nchars(syllabel,0,2) in ['ơi', 'ơm', 'ơn', 'ơp', 'ơt']:
            if syllabel[2:3]:
                return False
            return True
        return False
    if ch == 'u':
        chk = get_nchars(syllabel,0,4)
        if chk in ['uông','uênh', 'uêch','uych', 'uynh','uyên', 'uyêt']:
            if syllabel[4:5]:
                return False
            return True
        if len(chk) > 3:
            return False
        chk = get_nchars(syllabel,0,3)
        if chk in ['uya','ung','uôc', 'uôi', 'uôm', 'uôn', 'uôt','uây',
                                'uân','uât','uyt', 'uyu', 'uyn', 'uyp']:
            if syllabel[3:4]:
                return False
            return True
        if len(chk) > 2:
            return False
        if get_nchars(syllabel,0,2) in ['ua', 'uc', 'ui', 'um', 'un', 'up',
                                                      'uê','ut','uơ','uy']:
            if syllabel[2:3]:
                return False
            return True
        return False
    if ch == 'ư':
        chk = get_nchars(syllabel,0,4)
        if chk in ['ương']:
            if syllabel[4:5]:
                return False
            return True
        if len(chk) > 3:
            return False
        chk = get_nchars(syllabel,0,3)
        if chk in ['ưng', 'ươc', 'ươi', 'ươm', 'ươn', 'ươp', 'ươt',
                   'ươu']:
            if syllabel[3:4]:
                return False
            return True
        if len(chk) > 2:
            return False
        if get_nchars(syllabel,0,2) in ['ưc', 'ưi', 'ưu', 'ưt', 'ưm', 'ưa']:
            if syllabel[2:3]:
                return False
            return True
        return False
    if ch == 'y':
        chk = get_nchars(syllabel,0,4)
        if chk in ['yêng']:
            if syllabel[4:5]:
                return False
            return True
        if len(chk) > 3:
            return False
        chk = get_nchars(syllabel,0,3)
        if chk in ['yêm', 'yên', 'yêt', 'yêu', 'ynh']:
            if syllabel[3:4]:
                return False
            return True
        if len(chk) > 2:
            return False
        return False
    # Kiểm tra với các phụ âm
    if ch in 'bcdđghklmnpqrstvx':
        nc = chars_map.get(syllabel[1:2],syllabel[1:2])
        if nc == ch:
            return False
        if syllabel[0:3].lower() in ['ngh']:
            return isVNESE(syllabel[3:])
        if syllabel[0:2].lower() in ["ch", "gi", "kh", "ng", "nh", "ph",
                                        "qu", "th", "tr", "gh"]:
            return isVNESE(syllabel[2:])
        if ch == 'đ':
            if nc == 'y': # từ 'đy" không hợp lệ dùng từ "đi"
                return False
        if ch == 'c' or ch == 'q' or ch == 'g':
            # chữ "ê" và "e" không được đi liên sau.
            if nc in ['ê','e']:
                return False
        # "q" thì phải đi với "u" là "qu"
        if ch == 'q':
            if nc != 'u':
                return False
        return isVNESE(syllabel[1:]) # Cắt chuối từ phụ âm tiếp tục kiểm tra
    return False
