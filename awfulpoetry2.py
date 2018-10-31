#!/usr/bin/env python3
# Поэма без героя
import random
import sys

articles = ['a','an','the','mine','yours','his','hers','its','ours','theirs', "one's"]
nouns = ['history','way','art','world','information','map','two','family','government']
verbs = ['abash','abate','abide','absorb','accept','accompany','ache','achieve','acquire','act','add','address','adjust','admire']
adverbs = ['accidentally','always','angrily','anxiously','awkwardly','badly','blindly','boastfully','boldly',
           'bravely','brightly','cheerfully','coyly','crazily','defiantly','deftly','deliberately','devotedly','doubtfully','dramatically',
           'dutifully','eagerly','elegantly','enormously','evenly','eventually','exactly','faithfully','finally','foolishly','fortunately','frequently',
           'gleefully','gracefully','happily','hastily','honestly','hopelessly','hourly','hungrily','innocently','inquisitively','irritably','jealously',
           'justly','kindly','lazily','loosely','madly','merrily','mortally','mysteriously','nervously','never','obediently','obnoxiously','occasionally','often',
           'only','perfectly','politely','poorly','powerfully','promptly','quickly','rapidly','rarely','regularly','rudely','safely','seldom','selfishly','seriously',
           'shakily','sharply','silently','slowly','solemnly','sometimes','speedily','sternly','technically','tediously','unexpectedly','usually','victoriously','vivaciously',
           'warmly','wearily','weekly','wildly','yearly']
lines = 5
if len(sys.argv) > 1:
    try:
        temp = int(sys.argv[1])
        if 1<= temp <=10:
            lines = temp
        else:
            print("Количество строк в поэме от 1 до 10")
    except ValueError as err:
        print(err, 'Пожалуйста, введите программу в следующем формате',sys.argv[0],' <количество строк от 1 до 10>')
                      
while lines:
           article = random.choice(articles)
           noun = random.choice(nouns)
           verb = random.choice(verbs)
           if random.randint(0,1) ==0:
               adverb = random.choice(adverbs)
               print(article + ' ' + noun + ' '+ verb + ' ' + adverb)
           else:
               print(article +' ' + noun + ' ' + verb)
           lines -= 1
           
           
