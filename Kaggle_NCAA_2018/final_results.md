# Final Results of Kaggle's NCAA 2018 Men's and Women's competitions.

## Men's Event

- My Score: 0.629549 (550 / 934 | Top 59%)
- Winner: 0.531942
- Random (guess 0.5 each): ~0.69

## Women's Event

- My Score: 0.581599 (332 / 505 | Top 66%)
- Winner: 0.406819
- Random:

Winner's model (raddar) was a single XGBoost with careful feature selection. A few notes:
- https://www.kaggle.com/c/womens-machine-learning-competition-2018/discussion/53597
- https://github.com/fakyras/ncaa_women_2018/blob/master/win_ncaa.R#L149
- measured win margin with MAE metric together with cauchy objective function
- Score difference predictions were used as inputs for smoothing splines GAM model to transform them into probabilities
- Used only the supplied, regular season data
  - Accidentally forgot to include the stage2 reg season upda
  - if they had incorporated it, they would have got 10th place
- Used extended data, which I didn't do
- Swapped team positions to double data
- Used GLMM on regular season data for march March Madness teams only
- Clipped the edges [0.025] and [0.975]
- Hand-coded a few of the anomoly upset events
