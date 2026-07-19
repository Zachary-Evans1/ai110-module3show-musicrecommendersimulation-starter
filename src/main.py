"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    profiles = {
        "High-Energy Pop": {
            "favorite_genre": "pop",
            "favorite_mood": "happy",
            "target_energy": 0.9,
            "target_tempo": 130,
            "target_valence": 0.8
        },
        "Chill Lofi": {
            "favorite_genre": "lofi",
            "favorite_mood": "focused",
            "target_energy": 0.4,
            "target_tempo": 80,
            "target_valence": 0.6
        },
        "Deep Intense Rock": {
            "favorite_genre": "metal",
            "favorite_mood": "aggressive",
            "target_energy": 0.95,
            "target_tempo": 160,
            "target_valence": 0.3
        },
        "Genre Mismatch (K-Pop)": {
            "favorite_genre": "k-pop",
            "favorite_mood": "happy",
            "target_energy": 0.8,
            "target_tempo": 120,
            "target_valence": 0.8
        },
        "Conflicting Preferences": {
            "favorite_genre": "pop",
            "favorite_mood": "sad",
            "target_energy": 0.95,
            "target_tempo": 160,
            "target_valence": 0.2
        }
    }

    for profile_name, user_prefs in profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print("\n" + "=" * 70)
        print(f"🎵 {profile_name.upper()}".center(70))
        print("=" * 70 + "\n")

        for idx, rec in enumerate(recommendations, 1):
            song, score, explanation = rec
            artist = song.get('artist', 'Unknown')

            print(f"{idx}. {song['title']} - {artist}")
            print(f"   Score: {score:.1f}/100")
            print("   " + "─" * 66)

            for reason in explanation.split('\n'):
                print(f"   {reason}")

            print()


if __name__ == "__main__":
    main()
