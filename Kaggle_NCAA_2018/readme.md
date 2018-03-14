## Kaggle Competitions

### Google Cloud & NCAA® ML Competition 2018-Men's
**Apply Machine Learning to NCAA® March Madness®**

https://www.kaggle.com/c/mens-machine-learning-competition-2018/



### Google Cloud & NCAA® ML Competition 2018-Women's
**Apply machine learning to NCAA® March Madness®**

https://www.kaggle.com/c/womens-machine-learning-competition-2018/


Predict Probabilities of Victory for NCAA (Men and Women) Tournament
- Predict probabilities of a Team A winning for all possible pairings of teams
  - Ignore duplicates. once A vs B is calculated, B vs A is dropped. Results in n * (n - 1) / 2 pairings
- Scoring will use LogLoss, comparing calculated probabilities and the 1 or 0 for the real win/loss
- Ranking will unfold as the tournament progresses


Strategy
- I came to the competition late, and based my strategy around what I read in the Kernels and what I was thinking about elsewhere.

Data
- Simple dataset using the "Compact" results data from Kaggle, and a few calculated features
- Kaggle offered large amounts of data and external data was allowed, so mine really was simple in compare
- Used ELO feature similar to how chess players are ranked (and 538 ranks sports teams), based on one Kaggle Kernel's implementation

Model
- Single Catboost GBM. I had been playing with it for Titanic and talking about it with some peers, so I used it.

Reuse my model
 - The data for the Men's and Women's were formatted the same
 - Use the Men's notebooks to perform the women's workup/modelling/prediction (refitting the models)
 
 Submissions
 - Select 2 of my submissions per competition to be scored
 - I chose to provide only 2 each: 
  - Default Catboost params (its good)
  - "Optimized" parameters
  - Notebooks have graphs comparing training vs cv logloss


