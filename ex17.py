lyrics = "Ground control to major Tom Ground control to major Tom Take your protein pills and put your helmet on (Ten) Ground control (Nine) to major Tom (Eight) (Seven, six) Commencing countdown (Five), engines on (Four) (Three, two) Check ignition (One) and may gods (Blastoff) love be with you This is ground control to major Tom, you've really made the grade And the papers want to know whose shirts you wear Now it's time to leave the capsule if you dare This is major Tom to ground control, I'm stepping through the door And I'm floating in a most peculiar way And the stars look very different today Here am I sitting in a tin can far above the world Planet Earth is blue and there's nothing I can do Though I'm past one hundred thousand miles, I'm feeling very still And I think my spaceship knows which way to go Tell my wife I love her very much, she knows Ground control to major Tom, your circuits dead, there's something wrong Can you hear me, major Tom? Can you hear me, major Tom? Can you hear me, major Tom? Can you...  Here am I sitting in my tin can far above the Moon Planet Earth is blue and there's nothing I can do"

lookup = input("Enter a number to see all the words that appear that many times or greater: ")

words = lyrics.split()
unwanted_char = ".,-_?!()"
wordfreq = {}
for raw_word in words:
    word = raw_word.strip(unwanted_char)
    if word not in wordfreq:
        wordfreq[word] = 0
    wordfreq[word] += 1

largest = -1
theword = None
for Up_word, Up_num in wordfreq.items():
    if Up_num >= largest:
        largest = Up_num

for Up_word,Up_num in wordfreq.items():
    if Up_num > int(lookup):
        print(Up_word, Up_num)