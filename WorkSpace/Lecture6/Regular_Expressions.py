'''
Regular Expressions Module,
Bilgi işlemde, "regex" veya "regexp" olarak da adlandırılan bir düzenli ifade, belirli karakterler,
kelimeler veya karakter kalıpları gibi metin dizelerini eşleştirmek için kısa ve esnek bir araç sağlar.
'''
import re

# düzenli ifadeleri test etmek için bir dize tanımlama
test_string = "The quick brown fox jumps over the lazy dog."

# match() fonksiyonunu kullanarak dizenin "The" ile başlayıp başlamadığını kontrol etmek
match_result = re.match(r"The", test_string)
if match_result:
    print("The string starts with 'The'.")
else:
    print("The string does not start with 'The'.")

# "brown" sözcüğünün ilk geçtiği yeri bulmak için search() işlevini kullanmak
search_result = re.search(r"brown", test_string)
if search_result:
    print("The string contains 'brown' at index", search_result.start(), ".")
else:
    print("The string does not contain 'brown'.")

# findall() işlevini kullanarak "o" sözcüğünün tüm geçtiği yerleri bulmak
findall_result = re.findall(r"o", test_string)
print("The string contains the letter 'o' ", len(findall_result), " times.")

# sub() fonksiyonunu kullanarak "the" kelimesinin tüm geçtiği yerleri "THE" ile değiştirmek
sub_result = re.sub(r"the", "THE", test_string)
print("The modified string is:", sub_result)

print("\n ------------------- \n ")

handle = open('sample.txt')
for line in handle:
    line = line.rstrip()
    if line.find('bal') >= 0:
        print(line)

print("\n ------------------- \n ")

#import re 'yukarıda zaten import edildi.'

handle = open('sample.txt')
for line in handle:
    line = line.rstrip()
    if re.search('bal', line):
        print(line)
