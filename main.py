import datetime
import math
import lunarcalendar

decimals = ['', '一', '二', '三', '四', '五', '六', '七', '八', '九']
powers_of_ten = ['', '十', '百']

def to_jp_number(number:int):
    
    if number == 0 :
        return '〇'
    
    result = ''
    
    magnitude = math.floor(math.log10(number))
    
    for i in range(magnitude + 1):
        power = magnitude - i
        digit = (number // (10 ** power)) % 10
        if not (digit == 1 and power > 0):
            result += decimals[digit]
        result += powers_of_ten[power]
    
    return result

#https://www.ndl.go.jp/koyomi/chapter3/s8.html
months = ['睦月', '如月', '弥生', '卯月', '皐月', '水無月', '文月', '葉月', '長月', '神無月', '霜月', '師走']

def main():

    leap_month = ''
    lunardate = lunarcalendar.Lunar.from_date(datetime.date(2022, 6, 29))

    season = lunardate.year - 1885
    if lunardate.isleap :
        leap_month = '閏'

    print(f'第{to_jp_number(season)}季 {leap_month}{months[lunardate.month - 1]} {to_jp_number(lunardate.day)}日')

if __name__ == '__main__':
    main()