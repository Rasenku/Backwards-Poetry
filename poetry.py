import random

def reverse(s):
    s.reverse()
    index = len(s)
    for line in s:
        print(f"{index} {line}")
        index -= 1

s = '''The wind whistles past my ears.
Closing my eyes, I lose all my fears.
The waves crash into the rocks.
Out here there is no time on my clock.
The serenity I feel here just soothes my mind.
A peaceful day so hard to find.
The breeze just calms my soul.
Helps me think about what is my life's goal.
I then look out over the ocean,
And it feels like my life has lost its commotion.
The sun sets down over the clouds.
But the orange glow around makes me proud.
As the night draws near.
I feel like where I need to be is here.
The soothing nature this afternoon brings
Just feels like such a beautiful thing.
I sit and wonder where life will go,
But right now all I want is for time to slow.
To enjoy this moment and feel free,
To clear my mind and find some glee.
It's days like these I truly treasure.
Amazing nights and beautiful weather.
It may not seem like much.
But it's moments like these I want to clutch.
For once I feel like life is bliss.
So many hard days in which my happiness was missed.
I could get lost listening to the waves.
Listening to the birds and watching how the clouds behave.
I could close my eyes and fade into the night.
The tranquility I feel helps me win the fight.
As the waves keep crashing into the rocks,
I feel the happiness in my heart become unlocked.
The day is drawing to a close.
The peacefulness I feel right now I'll only know.
Right now my mind is finally clear.
It's time to go as the night draws near.''' .split("\n")
reverse(s)

def lines_printed_random(s):

    lines = []

    for i in range(0, len(s)):
        index = random.randint(0, len(s) - 1)
        lines.append(s[index])

    print("\n".join(lines))


def unique_lines(s):
    s = '''The wind whistles past my ears.
Closing my eyes, I lose all my fears.
The waves crash into the rocks.
Out here there is no time on my clock.
The serenity I feel here just soothes my mind.
A peaceful day so hard to find.
The breeze just calms my soul.
Helps me think about what is my life's goal.
I then look out over the ocean,
And it feels like my life has lost its commotion.
The sun sets down over the clouds.
But the orange glow around makes me proud.
As the night draws near.
I feel like where I need to be is here.
The soothing nature this afternoon brings
Just feels like such a beautiful thing.
I sit and wonder where life will go,
But right now all I want is for time to slow.
To enjoy this moment and feel free,
To clear my mind and find some glee.
It's days like these I truly treasure.
Amazing nights and beautiful weather.
It may not seem like much.
But it's moments like these I want to clutch.
For once I feel like life is bliss.
So many hard days in which my happiness was missed.
I could get lost listening to the waves.
Listening to the birds and watching how the clouds behave.
I could close my eyes and fade into the night.
The tranquility I feel helps me win the fight.
As the waves keep crashing into the rocks,
I feel the happiness in my heart become unlocked.
The day is drawing to a close.
The peacefulness I feel right now I'll only know.
Right now my mind is finally clear.
It's time to go as the night draws near.'''
    print (s.upper())







# if __name__ == '__main__':
    #Uncomment one line at a time to test
    # lines_printed_random(s)
    # unique_lines(s)
