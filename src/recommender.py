from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    target_tempo: float
    target_valence: float
    likes_acoustic: bool #Probably will delete.

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and convert numeric fields to floats."""
    songs = []
    numeric_fields = ['id', 'energy', 'tempo_bpm', 'valence', 'danceability', 'acousticness']

    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            for field in numeric_fields:
                if field in row:
                    row[field] = float(row[field])
            songs.append(row)

    print(f"Loaded {len(songs)} songs from {csv_path}")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song against user preferences, returning score and reasons."""
    score = 0.0
    reasons = []

    # Genre match: +40 points
    if song.get('genre') == user_prefs.get('favorite_genre'):
        score += 40
        reasons.append(f"✓ Genre match: {song['genre']}")

    # Mood match: +30 points
    if song.get('mood') == user_prefs.get('favorite_mood'):
        score += 30
        reasons.append(f"✓ Mood match: {song['mood']}")

    # Energy proximity: up to +15 points
    target_energy = user_prefs.get('target_energy', 0.5)
    song_energy = song.get('energy', 0.5)
    energy_distance = abs(song_energy - target_energy)
    energy_points = 15 * max(0, 1 - energy_distance)
    score += energy_points
    reasons.append(f"Energy: {energy_points:.1f}/15 (target {target_energy}, song {song_energy})")

    # Tempo proximity: up to +10 points
    target_tempo = user_prefs.get('target_tempo', 100)
    song_tempo = song.get('tempo_bpm', 100)
    tempo_distance = abs(song_tempo - target_tempo)
    max_tempo_distance = 50
    tempo_points = 10 * max(0, 1 - (tempo_distance / max_tempo_distance))
    score += tempo_points
    reasons.append(f"Tempo: {tempo_points:.1f}/10 (target {target_tempo}, song {song_tempo})")

    # Valence proximity: up to +5 points
    target_valence = user_prefs.get('target_valence', 0.5)
    song_valence = song.get('valence', 0.5)
    valence_distance = abs(song_valence - target_valence)
    valence_points = 5 * max(0, 1 - valence_distance)
    score += valence_points
    reasons.append(f"Valence: {valence_points:.1f}/5 (target {target_valence}, song {song_valence})")

    return (score, reasons)

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score all songs and return top k recommendations sorted by score."""
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored_songs.append((song, score, '\n'.join(reasons)))

    return sorted(scored_songs, key=lambda x: x[1], reverse=True)[:k]
