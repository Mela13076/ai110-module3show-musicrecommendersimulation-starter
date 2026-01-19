from __future__ import annotations
from typing import Dict, List, Tuple
import csv


def load_songs(csv_path: str) -> list[dict]:
    songs = []

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": int(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }
            songs.append(song)

    return songs


def _closeness(song_value: float, target_value: float, weight: float) -> float:
    """
    Returns weighted closeness score:
    weight * (1 - abs(song_value - target_value))
    Assumes song_value and target_value are in [0, 1].
    """
    return weight * (1.0 - abs(song_value - target_value))


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against a user's preferences.
    Returns:
      (total_score, reasons)

    Expected user_prefs keys:
      favorite_genre, favorite_mood,
      target_energy, target_tempo_bpm, target_valence, target_danceability, target_acousticness,
      tempo_min, tempo_max  (needed to normalize BPM)

    Expected song keys:
      genre, mood, energy, tempo_bpm, valence, danceability, acousticness
    """
    score = 0.0
    reasons: List[str] = []

    # --- Categorical bonuses ---
    if song["genre"] == user_prefs["favorite_genre"]:
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song["mood"] == user_prefs["favorite_mood"]:
        score += 1.0
        reasons.append("mood match (+1.0)")

    # --- Numeric similarity weights ---
    W_ENERGY = 1.2
    W_TEMPO = 1.0
    W_VALENCE = 1.0
    W_DANCE = 0.9
    W_ACOUSTIC = 0.9

    # Features already in [0, 1]
    energy_pts = _closeness(song["energy"], user_prefs["target_energy"], W_ENERGY)
    score += energy_pts
    reasons.append(f"energy closeness (+{energy_pts:.2f})")

    valence_pts = _closeness(song["valence"], user_prefs["target_valence"], W_VALENCE)
    score += valence_pts
    reasons.append(f"valence closeness (+{valence_pts:.2f})")

    dance_pts = _closeness(song["danceability"], user_prefs["target_danceability"], W_DANCE)
    score += dance_pts
    reasons.append(f"danceability closeness (+{dance_pts:.2f})")

    acoustic_pts = _closeness(song["acousticness"], user_prefs["target_acousticness"], W_ACOUSTIC)
    score += acoustic_pts
    reasons.append(f"acousticness closeness (+{acoustic_pts:.2f})")

    # Tempo: normalize BPM -> [0, 1], then closeness
    tempo_min = user_prefs["tempo_min"]
    tempo_max = user_prefs["tempo_max"]
    tempo_range = tempo_max - tempo_min if tempo_max != tempo_min else 1  # avoid divide by zero

    song_tempo_norm = (song["tempo_bpm"] - tempo_min) / tempo_range
    target_tempo_norm = (user_prefs["target_tempo"] - tempo_min) / tempo_range

    tempo_pts = _closeness(song_tempo_norm, target_tempo_norm, W_TEMPO)
    score += tempo_pts
    reasons.append(f"tempo closeness (+{tempo_pts:.2f})")

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int) -> List[Dict]:
    """
    Scores all songs and returns the top K as a list of dicts.
    Each returned item includes:
      - song metadata
      - score
      - reasons
    """
    scored: List[Dict] = []

    for song in songs:
        s, reasons = score_song(user_prefs, song)
        scored.append({
            **song,
            "score": s,
            "reasons": reasons
        })

    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored[:k]
