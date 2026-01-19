# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

TuneMatch 1.0



## 2. Intended Use  

This recommender generates music suggestions based on a user’s stated preferences for genre, mood, and audio features.
It assumes users can describe their tastes with simple numeric values.
The model is designed for classroom exploration and learning, not real-world deployment.



## 3. How the Model Works  

The model compares each song’s features, such as energy, tempo, mood, and danceability, to the user’s preferences.
Songs earn points for matching genre and mood and additional points for how close their numeric features are to the user’s targets.
The final score combines all these signals, and songs with the highest scores are recommended.
Compared to the starter logic, this version rewards similarity rather than just higher or lower values.



## 4. Data  

The dataset contains a small catalog of songs with metadata such as genre, mood, and audio features.
Multiple genres and moods are represented, but the dataset is limited in size.
No external data was added.
Some musical styles and cultural preferences are likely missing.

## 5. Strengths  

The system works well for users with clear, consistent preferences.
It captures intensity, mood, and tempo relationships accurately.
Recommendations often matched what I expected based on the user profile.

## 6. Limitations and Bias 

The model does not consider lyrics, cultural context, or user listening history.
Some genres and moods are underrepresented in the dataset.
The scoring can over-prioritize genre and reinforce narrow listening patterns.
Users with complex or conflicting preferences may get less accurate results.

## 7. Evaluation  

I tested multiple user profiles, including high-energy, chill, and conflicting preference cases.
I looked for whether the top recommendations aligned with the intended mood and intensity.
Some edge cases produced unexpected but explainable results.
Simple ranking comparisons helped confirm the logic worked as intended.

## 8. Future Work  

I would add support for multiple favorite genres and moods.
Explanations could be more detailed and user-friendly.
I would improve diversity so recommendations are not too similar.
Handling mixed or evolving user tastes would make the model more realistic.

## 9. Personal Reflection  

I learned how small design choices strongly affect recommendation outcomes.
It was interesting to see how numeric features can represent subjective taste.
This project made me more aware of how music apps shape what users discover.
