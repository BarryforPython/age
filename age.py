driving = input('請問你有沒有開過車?')
if driving != 'yes' and driving != 'no':
    print('Just answer yes/no')
    raise SystemExit()

age = input('請問你的年齡?')
age = int(age)
# 記得要型別轉換
if driving == 'yes':
    if age >= 18:
        print('pass')
    else:
        print('good luck!')
elif driving == 'no':
    if age < 18:
        print('wait for years~')
    else:
        print('get your own lisense!')
else:
    print('Just answer yes/no')
