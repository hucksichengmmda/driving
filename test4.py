country = input('请问你的国家:')
age = input('你的年龄:')
age = int(age)
if country == '台湾':
	if age >= 18:
		print('你可以考驾照！')
	else:
		print('你还不可以考驾照哦！')