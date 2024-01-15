print('Hello, Welcome to Trivia!')

ans= input ('Are you ready to play (yes/no): ')
score = 0
total_q = 5
 
if ans.lower() == "yes":
    ans = input ('1. What is the oldest programming language?')
    if ans.lower() == 'python': 
        score += 1
        print('Correct!')
    else:
        print('Wrong!')


    ans = input ('2. What color does Yellow and red make?')
    if ans.lower() == 'orange': 
        score += 1
        print('Smarty pants!')
    else:
        print('Really?')

    ans = input ('3. What rapper whose name is also a sum of money?')
    if ans.lower() == '50 cents': 
        score += 1
        print('If I Was Your Bestfriend!')
    else:
        print('Wise Men Listen and Laugh, While Fools Talk.')

        ans = input ('4. Roses are red, violets are?')
    if ans.lower() == 'blue': 
        score += 1
        print('Picasso I See You!')
    else:
        print('You need to look at some violets.')

        ans = input ('5. Which is easiest Java or Python?')
    if ans.lower() == 'Python': 
        score += 1
        print('Yeah!')
    else:
        print('Really?')

print(' Thank You For Playing, You Got ', score, "questions correct.")
mark = (score/total_q) * 100

print("Mark:", str(mark) + '%')

print("Bye!")
        
