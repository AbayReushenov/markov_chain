# Поэма без героя
import random

articles = ['a','an','the','mine','yours','his','hers','its','ours','theirs', "one's"]
nouns = ['history','way','art','world','information','map','two','family','government']
verbs = ['abash','abate','abide','absorb','accept','accompany','ache','achieve','acquire','act','add','address','adjust','admire']
adverbs = ['accidentally','always','angrily','anxiously','awkwardly','badly','blindly','boastfully','boldly','bravely','brightly','cheerfully','coyly','crazily','defiantly','deftly','deliberately','devotedly','doubtfully','dramatically','dutifully','eagerly','elegantly','enormously','evenly','eventually','exactly','faithfully','finally','foolishly','fortunately','frequently','gleefully','gracefully','happily','hastily','honestly','hopelessly','hourly','hungrily','innocently','inquisitively','irritably','jealously','justly','kindly','lazily','loosely','madly','merrily','mortally','mysteriously','nervously','never','obediently','obnoxiously','occasionally','often','only','perfectly','politely','poorly','powerfully','promptly','quickly','rapidly','rarely','regularly','rudely','safely','seldom','selfishly','seriously','shakily','sharply','silently','slowly','solemnly','sometimes','speedily','sternly','technically','tediously','unexpectedly','usually','victoriously','vivaciously','warmly','wearily','weekly','wildly','yearly']
n=0
a=1
b=2
line = []
while n<5:
           article = random.choice(articles[:])
           noun = random.choice(nouns[:])
           verb = random.choice(verbs[:])
           adverb = random.choice(adverbs[:])
           if random.randint(a,b) ==1:
                   line = article + ' ' + noun + ' '+ verb + ' ' + adverb
           else:
                   line = article +' ' + noun + ' ' + verb
           print(line)
           line = []
           n += 1
                                 
        
                
           
