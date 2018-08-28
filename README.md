# Rock-Paper-Scissor

This project focuses on creating a bot that can play the common game of Rock Paper Scissors (RPS) better than its human opponent.
The key idea is that humans tend to play in patterns rather than completely at random. Using machine learning techniques, we will 
train a bot to learn how we play RPS, thus giving it an advantage over us. For example, if every time we play the sequence of "Rock",
"Rock", "Paper" and "Rock" our next throw is consistently "Scissors", then our bot learns that and plays "Rock" in the next game to 
beat us.So, for this problem our input is a sequence of n human plays, which we represent as an n length vector, where each element in
the vector is an integer in [1,3]. "Rock" is represented by 1, "Paper" is represented by 2, and "Scissors" is represented by 3. 
Given this sequence of human plays, our bot uses various classifiers to predict our n+1 th play, which is also represented by an 
integer as described above.Given this play, the bot chooses its winning counterpart (i.e. predicting "Rock" entails playing "Paper‟,
predicting "Paper" entails playing "Scissors", and predicting "Scissors" entails playing "Rock").

We will also create different difficulty level:
1. Easy – just a random guess out of the three possibilities.
2. Medium – based on previous inputs by the user and the maximum probabilities of the user to choose their next move.
3. Hard – In addition to the checking the previous inputs it will also keep a track of the current player playing style
          and pattern and make its next move.
