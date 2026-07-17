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

    # Starter example profile
    user_prefs = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.8,
        "target_tempo": 120,
        "target_valence": 0.8
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "=" * 70)
    print("🎵 TOP 5 MUSIC RECOMMENDATIONS".center(70))
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
