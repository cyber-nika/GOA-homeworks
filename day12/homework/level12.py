# პირველ მაგალითში ორივე ბულეანით გამოვიყენებთ 'and' ოპერატორს
bool1 = True
bool2 = False

# ლოგიკური 'and' ოპერატორი: ორივე ცვლადი უნდა იყოს True, რათა შედეგი იყოს True
print(bool1 and bool2)  # False, რადგან bool2 არის False

# მეორე მაგალითი 'or' ოპერატორით
bool3 = True
bool4 = False

# ლოგიკური 'or' ოპერატორი: ერთი ცვლადი მაინც True უნდა იყოს, რომ შედეგი იყოს True
print(bool3 or bool4)  # True, რადგან bool3 არის True

# მესამე მაგალითი სამი ბულეანით
bool5 = True
bool6 = False
bool7 = True

# 'and' ოპერატორი: ყველა ცვლადი უნდა იყოს True, რომ შედეგი იყოს True
print(bool5 and bool6 and bool7)  # False, რადგან bool6 არის False

# 'or' ოპერატორი: ერთი მაინც True უნდა იყოს
print(bool5 or bool6 or bool7)  # True, რადგან bool5 და bool7 ორივე Trueა
