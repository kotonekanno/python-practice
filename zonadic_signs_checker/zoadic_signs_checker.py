month = int(input('何月：'))
day = int(input('何日：'))

while (month<1 or 12<month
	or day<1 or 31<day):
	print('有効な数字を入力してください')
	month = int(input('何月：'))
	day = int(input('何日：'))

match month:
	case 1:
		if day<=19: print('山羊座')
		else: print('水瓶座')
	case 2:
		if day<=18: print('水瓶座')
		else: print('魚座')
	case 3:
		if day<=20: print('魚座')
		else: print('牡羊座')
	case 4:
		if day<=19: print('牡羊座')
		else: print('牡牛座')
	case 5:
		if day<=20: print('牡牛座')
		else: print('双子座')
	case 6:
		if day<=21: print('双子座')
		else: print('蟹座')
	case 7:
		if day<=22: print('蟹座')
		else: print('獅子座')
	case 8:
		if day<=22: print('獅子座')
		else: print('乙女座')
	case 9:
		if day<=22: print('乙女座')
		else: print('天秤座')
	case 10:
		if day<=23: print('天秤座')
		else: print('蠍座')
	case 11:
		if day<=21: print('蠍座')
		else: print('射手座')
	case 12:
		if day<=21: print('射手座')
		else: print('山羊座')
