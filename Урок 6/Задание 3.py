article1 = 'Недавно проходил обучение в Academy.'
article2 = 'Недавно проходил обучениею'
article3 = 'Недавно проходил обучение в Academy. Все очень круто.'
art1 = len(article1)
art2 = len(article2)
art3 = len(article3)
m_len = max(art1, art2, art3)
if m_len == art1:
    print(article1)
elif m_len == art2:
    print(article2)
else:
    print(article3)