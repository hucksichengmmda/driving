country = input('请问你的国家:')
age = input('你的年龄:')
age = int(age)
if country == '台湾':
	if age >= 18:
		print('你可以考驾照！')
	else:
		print('你还不可以考驾照哦！')
elif country == '美国':
	if age >= 16:
		print('你可以考驾照了！')
	else:
		print('你还不可以考驾照哦')
else:
	print('妳只能输入台湾或者美国！')