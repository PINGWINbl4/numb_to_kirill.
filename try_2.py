numb = int(input())
final = str

first_numb = numb//1000

second_numb = numb//100
second_numb %= 10

third_numb = numb//10
third_numb %= 10

forth_numb = numb % 10
tisyaci =['', 'одна тысяча ','две тысячи ','три тысячи ','четыре тысячи ','пять тысяч ','шесть тысяч ','восемь тысяч ',
          'девять тысяч ']
sotny = ['','сто ','двести ','триста ','четыреста ','пятсот ','шесот ','семьсот ','весемьсот ','девятьсот ']
desyatki = ['', 'десять ','двадцать ','тридцать ','сорок ','пятьдесят ','шестьдесят ','семьдесят ','восемдесят ','девяноста ']
dodvadcati = ['', 'одиннадцать рублей','двенадцать рублей','тринадцать рублей','четырнадцать рублей','пятнадцать рублей',
              'шестнадцать рублей','восемнадцать рублей',
              'девятьнадцать рублей']
edinici = ['', 'один рубль ','два рубля ','три трубля ','четыре рубля ','пять рублей ','шесть рублей ','семь рублей ',
           'восемь рублей ','девять рублей ']

if (third_numb==1) and (forth_numb!=0):
    print(tisyaci[first_numb]+sotny[second_numb]+dodvadcati[forth_numb])
elif forth_numb == 0:
    print(tisyaci[first_numb] + sotny[second_numb] + desyatki[third_numb] +'рублей')
elif forth_numb == 0 and third_numb==0:
    print(tisyaci[first_numb] + sotny[second_numb] +'рублей')
elif forth_numb == 0 and third_numb==0 and second_numb == 0:
    print(tisyaci[first_numb] + 'рублей')
else:
    print(tisyaci[first_numb] + sotny[second_numb] + desyatki[third_numb]+ edinici[forth_numb])
