#!/usr/bin/env python
# coding: utf-8

# In[3]:


def score_board(name1='Player',name2 = 'Player'):
    print(f'Game of 501 Darts {name1} vs {name2}')
    players = [name1,name2]
    start_score_p1 = 501
    start_score_p2 = 501
    average_array_p1=[]
    average_array_p2=[]
    turn = 0
    while True:
        current_player = players[turn%2]
        turn +=1
        if current_player == name1:
            score_p1 = int(input(f'Enter Score {name1} :'))
            overall_score_p1 = start_score_p1 - score_p1
            start_score_p1 = overall_score_p1
            average_array_p1.append(score_p1)
            average_p1 = sum(average_array_p1)/len(average_array_p1)
            print(f'{name1} Score = ',overall_score_p1)
            print(f'{name1} Average =' ,average_p1)
        
            if start_score_p1-score_p1 < 0:
                print(f'{name1} Score : ',start_score_p1)
                average_array_p1.append(0)
        
            if overall_score_p1 == 0:
              print(f'Game Over! Winner is {name1}')
              return 

        else:
            score_p2 = int(input(f'Enter Score {name2} :'))
            overall_score_p2 = start_score_p2 - score_p2
            start_score_p2 = overall_score_p2
            average_array_p2.append(score_p2)
            average_p2 = sum(average_array_p2)/len(average_array_p2)
            print(f'{name2} Score = ',overall_score_p2)
            print(f'{name2} Average =' ,average_p2)
        
            if start_score_p2-score_p2 < 0:
                print(f'{name2} Score : ',start_score_p2)
                average_array_p2.append(0)
        
            if overall_score_p2 == 0:
              print(f'Game Over! Winner is {name2}')
              return 

        

                
            
        
            
    
        
        

player_1 = input('Enter Your Name:')
player_2 = input('Enter Your Name:')
start_scorep1 = 501
start_scorep2 = 501
print(player_1,':',start_scorep1)
print(player_2,':',start_scorep2)
score_board(player_1,player_2)


# In[ ]:




