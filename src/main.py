"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import STRATEGIES, load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded songs: {len(songs)}")

    mode = "mood_first" # Change to "genre_first", "mood_first", or "balanced" to test other strategies
    strategy = STRATEGIES.get(mode, STRATEGIES["balanced"])

    test_profiles = []

    # Example user profile
    user_profile = {
        "favorite_genre": "lofi", 
        "favorite_mood": "chill",
        "target_energy": 0.4,
        "target_tempo": 80,
        "target_valence": 0.6,
        "target_danceability": 0.3,
        "target_acousticness": 0.5,
    }
    user_profile2 = {
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "target_energy": 0.8,
        "target_tempo": 120,
        "target_valence": 0.6,
        "target_danceability": 0.7,
        "target_acousticness": 0.2,
    }
    high_energy_pop = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.85,
        "target_tempo": 120,
        "target_valence": 0.80,
        "target_danceability": 0.75,
        "target_acousticness": 0.15,
    }
    chill_lofi = {
        "favorite_genre": "lofi",
        "favorite_mood": "calm",
        "target_energy": 0.30,
        "target_tempo": 70,
        "target_valence": 0.40,
        "target_danceability": 0.35,
        "target_acousticness": 0.70,
    }
    deep_intense_rock = {
        "favorite_genre": "rock",
        "favorite_mood": "angry",
        "target_energy": 0.90,
        "target_tempo": 140,
        "target_valence": 0.25,
        "target_danceability": 0.45,
        "target_acousticness": 0.10,
    }
    conflicting_emotions = {
        "favorite_genre": "pop",
        "favorite_mood": "sad",
        "target_energy": 0.90,
        "target_tempo": 125,
        "target_valence": 0.15,
        "target_danceability": 0.70,
        "target_acousticness": 0.20,
    }
    genre_only_bias = {
        "favorite_genre": "jazz",
        "favorite_mood": "happy",
        "target_energy": 0.50,
        "target_tempo": 100,
        "target_valence": 0.50,
        "target_danceability": 0.50,
        "target_acousticness": 0.50,
    }

    #test_profiles.extend([user_profile, user_profile2, high_energy_pop, chill_lofi, deep_intense_rock, conflicting_emotions, genre_only_bias])
    test_profiles.extend([high_energy_pop, chill_lofi, deep_intense_rock, conflicting_emotions, genre_only_bias])


    tempo_min = min(s["tempo_bpm"] for s in songs)
    tempo_max = max(s["tempo_bpm"] for s in songs)

    
    for profile in test_profiles:
        profile["tempo_min"] = tempo_min
        profile["tempo_max"] = tempo_max
        recommendations = recommend_songs(profile, songs, k=5, strategy=strategy)
        

        print("\nTop recommendations:\n")
        for rec in recommendations:
            print(f"{rec['title']} - Score: {rec['score']:.2f}")
            print("Because:", ", ".join(rec["reasons"]))
            print()
        print("====" * 10)


if __name__ == "__main__":
    main()
