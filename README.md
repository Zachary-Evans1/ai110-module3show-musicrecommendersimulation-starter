# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Real world recommendations work by combining many different types of signals to predict what a user might enjoy next. The two major approaches to this are Content-Based Filtering, which checks how similar a song is to the songs you have enjoyed before, and Collaborative Filtering, which recommends items based on other users that have similar taste profiles to you. In this project I'm going to be using Content-Based Filtering, as I don't have access to a large amount of user data needed which is needed to make Collaborative Filtering work.

My UserProfile will store a user's favorite music genres, favorite song moods, and the average/preferred energy, tempo, and valence of the songs a user listens to. Each song will have these attributes along with the songs id, artist, and title. The Recommender will compute a score by checking if a song's genre or mood matches a user's favorites, and adding points if it does. It will then calculate a songs closeness in its energy, tempo, and valence scores, giving more points if the scores are closer to a users average/preferred scores. The scores for each feature will be weighted like this:

Genre = 40
Mood = 30
Energy = 15
Tempo = 10
Valence = 5

Adding up to 100.

After all songs have been scored, they are sorted from highest score to lowest score. The recommender then returns the highest-ranked songs as recommendations.



For biases This recommender weighs genre and mood very heavily, which may lead to them being over-prioritized. This may cause songs with similar energy, tempo, or valence to be ranked lower than they maybe should be. Also, as it is a purely Content-Based Filtering system, it also runs into the downside of CBF which is creating a filter bubble of repeatedly recommending songs that are very similar to a users existing music tastes.

Explain your design in plain language.

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
Loaded 20 songs from data/songs.csv

======================================================================
                    🎵 TOP 5 MUSIC RECOMMENDATIONS                     
======================================================================

1. Sunrise City - Neon Echo
   Score: 99.1/100
   ──────────────────────────────────────────────────────────────────
   ✓ Genre match: pop
   ✓ Mood match: happy
   Energy: 14.7/15 (target 0.8, song 0.82)
   Tempo: 9.6/10 (target 120, song 118.0)
   Valence: 4.8/5 (target 0.8, song 0.84)

2. Gym Hero - Max Pulse
   Score: 65.5/100
   ──────────────────────────────────────────────────────────────────
   ✓ Genre match: pop
   Energy: 13.1/15 (target 0.8, song 0.93)
   Tempo: 7.6/10 (target 120, song 132.0)
   Valence: 4.8/5 (target 0.8, song 0.77)

3. Rooftop Lights - Indigo Parade
   Score: 58.6/100
   ──────────────────────────────────────────────────────────────────
   ✓ Mood match: happy
   Energy: 14.4/15 (target 0.8, song 0.76)
   Tempo: 9.2/10 (target 120, song 124.0)
   Valence: 5.0/5 (target 0.8, song 0.81)

4. Pulsing Lights - ElectroWave
   Score: 26.6/100
   ──────────────────────────────────────────────────────────────────
   Energy: 14.7/15 (target 0.8, song 0.82)
   Tempo: 7.0/10 (target 120, song 135.0)
   Valence: 4.9/5 (target 0.8, song 0.78)

5. Neon Dreams - SynthMaster
   Score: 26.5/100
   ──────────────────────────────────────────────────────────────────
   Energy: 13.8/15 (target 0.8, song 0.88)
   Tempo: 8.4/10 (target 120, song 128.0)
   Valence: 4.2/5 (target 0.8, song 0.65)

```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

### Multiple Profile Outputs

I tested my recommended with five distinct user profiles to see how the scoring logic handles diverse or conflicting preferences: 

======================================================================
                          🎵 HIGH-ENERGY POP                           
======================================================================

1. Sunrise City - Neon Echo
   Score: 96.2/100
   ──────────────────────────────────────────────────────────────────
   ✓ Genre match: pop
   ✓ Mood match: happy
   Energy: 13.8/15 (target 0.9, song 0.82)
   Tempo: 7.6/10 (target 130, song 118.0)
   Valence: 4.8/5 (target 0.8, song 0.84)

2. Gym Hero - Max Pulse
   Score: 69.0/100
   ──────────────────────────────────────────────────────────────────
   ✓ Genre match: pop
   Energy: 14.5/15 (target 0.9, song 0.93)
   Tempo: 9.6/10 (target 130, song 132.0)
   Valence: 4.8/5 (target 0.8, song 0.77)

3. Rooftop Lights - Indigo Parade
   Score: 56.7/100
   ──────────────────────────────────────────────────────────────────
   ✓ Mood match: happy
   Energy: 12.9/15 (target 0.9, song 0.76)
   Tempo: 8.8/10 (target 130, song 124.0)
   Valence: 5.0/5 (target 0.8, song 0.81)

4. Neon Dreams - SynthMaster
   Score: 28.5/100
   ──────────────────────────────────────────────────────────────────
   Energy: 14.7/15 (target 0.9, song 0.88)
   Tempo: 9.6/10 (target 130, song 128.0)
   Valence: 4.2/5 (target 0.8, song 0.65)

5. Pulsing Lights - ElectroWave
   Score: 27.7/100
   ──────────────────────────────────────────────────────────────────
   Energy: 13.8/15 (target 0.9, song 0.82)
   Tempo: 9.0/10 (target 130, song 135.0)
   Valence: 4.9/5 (target 0.8, song 0.78)


======================================================================
                             🎵 CHILL LOFI                             
======================================================================

1. Focus Flow - LoRoom
   Score: 100.0/100
   ──────────────────────────────────────────────────────────────────
   ✓ Genre match: lofi
   ✓ Mood match: focused
   Energy: 15.0/15 (target 0.4, song 0.4)
   Tempo: 10.0/10 (target 80, song 80.0)
   Valence: 5.0/5 (target 0.6, song 0.59)

2. Midnight Coding - LoRoom
   Score: 69.1/100
   ──────────────────────────────────────────────────────────────────
   ✓ Genre match: lofi
   Energy: 14.7/15 (target 0.4, song 0.42)
   Tempo: 9.6/10 (target 80, song 78.0)
   Valence: 4.8/5 (target 0.6, song 0.56)

3. Library Rain - Paper Lanterns
   Score: 67.7/100
   ──────────────────────────────────────────────────────────────────
   ✓ Genre match: lofi
   Energy: 14.2/15 (target 0.4, song 0.35)
   Tempo: 8.4/10 (target 80, song 72.0)
   Valence: 5.0/5 (target 0.6, song 0.6)

4. Autumn Leaves - FolkTales
   Score: 27.9/100
   ──────────────────────────────────────────────────────────────────
   Energy: 14.7/15 (target 0.4, song 0.42)
   Tempo: 8.4/10 (target 80, song 88.0)
   Valence: 4.8/5 (target 0.6, song 0.65)

5. Coffee Shop Stories - Slow Stereo
   Score: 27.0/100
   ──────────────────────────────────────────────────────────────────
   Energy: 14.5/15 (target 0.4, song 0.37)
   Tempo: 8.0/10 (target 80, song 90.0)
   Valence: 4.5/5 (target 0.6, song 0.71)


======================================================================
                         🎵 DEEP INTENSE ROCK                          
======================================================================

1. Metal Assault - HeavyThunder
   Score: 99.8/100
   ──────────────────────────────────────────────────────────────────
   ✓ Genre match: metal
   ✓ Mood match: aggressive
   Energy: 15.0/15 (target 0.95, song 0.95)
   Tempo: 10.0/10 (target 160, song 160.0)
   Valence: 4.8/5 (target 0.3, song 0.25)

2. Storm Runner - Voltline
   Score: 26.9/100
   ──────────────────────────────────────────────────────────────────
   Energy: 14.4/15 (target 0.95, song 0.91)
   Tempo: 8.4/10 (target 160, song 152.0)
   Valence: 4.1/5 (target 0.3, song 0.48)

3. Electric Rebellion - PunkRiot
   Score: 22.1/100
   ──────────────────────────────────────────────────────────────────
   Energy: 12.8/15 (target 0.95, song 0.8)
   Tempo: 6.0/10 (target 160, song 140.0)
   Valence: 3.4/5 (target 0.3, song 0.62)

4. Gym Hero - Max Pulse
   Score: 21.8/100
   ──────────────────────────────────────────────────────────────────
   Energy: 14.7/15 (target 0.95, song 0.93)
   Tempo: 4.4/10 (target 160, song 132.0)
   Valence: 2.7/5 (target 0.3, song 0.77)

5. Neon Dreams - SynthMaster
   Score: 20.8/100
   ──────────────────────────────────────────────────────────────────
   Energy: 14.0/15 (target 0.95, song 0.88)
   Tempo: 3.6/10 (target 160, song 128.0)
   Valence: 3.2/5 (target 0.3, song 0.65)


======================================================================
                       🎵 GENRE MISMATCH (K-POP)                       
======================================================================

1. Sunrise City - Neon Echo
   Score: 59.1/100
   ──────────────────────────────────────────────────────────────────
   ✓ Mood match: happy
   Energy: 14.7/15 (target 0.8, song 0.82)
   Tempo: 9.6/10 (target 120, song 118.0)
   Valence: 4.8/5 (target 0.8, song 0.84)

2. Rooftop Lights - Indigo Parade
   Score: 58.6/100
   ──────────────────────────────────────────────────────────────────
   ✓ Mood match: happy
   Energy: 14.4/15 (target 0.8, song 0.76)
   Tempo: 9.2/10 (target 120, song 124.0)
   Valence: 5.0/5 (target 0.8, song 0.81)

3. Pulsing Lights - ElectroWave
   Score: 26.6/100
   ──────────────────────────────────────────────────────────────────
   Energy: 14.7/15 (target 0.8, song 0.82)
   Tempo: 7.0/10 (target 120, song 135.0)
   Valence: 4.9/5 (target 0.8, song 0.78)

4. Neon Dreams - SynthMaster
   Score: 26.5/100
   ──────────────────────────────────────────────────────────────────
   Energy: 13.8/15 (target 0.8, song 0.88)
   Tempo: 8.4/10 (target 120, song 128.0)
   Valence: 4.2/5 (target 0.8, song 0.65)

5. Night Drive Loop - Neon Echo
   Score: 25.7/100
   ──────────────────────────────────────────────────────────────────
   Energy: 14.2/15 (target 0.8, song 0.75)
   Tempo: 8.0/10 (target 120, song 110.0)
   Valence: 3.4/5 (target 0.8, song 0.49)


======================================================================
                      🎵 CONFLICTING PREFERENCES                       
======================================================================

1. Gym Hero - Max Pulse
   Score: 61.2/100
   ──────────────────────────────────────────────────────────────────
   ✓ Genre match: pop
   Energy: 14.7/15 (target 0.95, song 0.93)
   Tempo: 4.4/10 (target 160, song 132.0)
   Valence: 2.1/5 (target 0.2, song 0.77)

2. Sunrise City - Neon Echo
   Score: 56.4/100
   ──────────────────────────────────────────────────────────────────
   ✓ Genre match: pop
   Energy: 13.1/15 (target 0.95, song 0.82)
   Tempo: 1.6/10 (target 160, song 118.0)
   Valence: 1.8/5 (target 0.2, song 0.84)

3. Metal Assault - HeavyThunder
   Score: 29.8/100
   ──────────────────────────────────────────────────────────────────
   Energy: 15.0/15 (target 0.95, song 0.95)
   Tempo: 10.0/10 (target 160, song 160.0)
   Valence: 4.8/5 (target 0.2, song 0.25)

4. Storm Runner - Voltline
   Score: 26.4/100
   ──────────────────────────────────────────────────────────────────
   Energy: 14.4/15 (target 0.95, song 0.91)
   Tempo: 8.4/10 (target 160, song 152.0)
   Valence: 3.6/5 (target 0.2, song 0.48)

5. Electric Rebellion - PunkRiot
   Score: 21.6/100
   ──────────────────────────────────────────────────────────────────
   Energy: 12.8/15 (target 0.95, song 0.8)
   Tempo: 6.0/10 (target 160, song 140.0)
   Valence: 2.9/5 (target 0.2, song 0.62)


## Experiments You Tried

The experiment I ran was doubling the importance of energy (score of 15 to 30) and halving the importance of genre (score from 40 to 20). This changed the ranking behavior of my recommender by making the audio characteristics of a song more important that the genre matches.

The biggest change was that songs with energy levels closer to the user's target moved higher in the rankings, even without a genre match. In the profile HIGH-ENERGY POP the song Rooftop Lights moved ahead of Gym Hero because its mood and energy aligned more with the user's preferences.

The GENRE MISMATCH (K-POP) profile also produced higher scores after the experiment. There are no K-Pop songs in the dataset, so when genre was weighed more heavily the maximum score for the profile could only hit 60/100. After the experiment, the maximum score could now hit 75/95, showing that the changes let the system generate reasonable recommendations even without a genre match.

Overall, I'd say the recommendations became different, but not necessarily more accurate. It did show that my recommendation system is very sensitive to different weighting choices, and even small changes can significancy affect the ranking of results.
---

## Limitations and Risks

Some of the biases and limitations my recommender has are:

* It only checks for direct matches with genre or mood, there is no closeness score, meaning if you like "pop" a song with "indie pop" will get zero points.
* The system very heavily weighs Genre and Mood with 70 of the 100 points coming from those two scoring categories.
* The system doesn't really serve people who want cross-genre exploration.
* Lofi has 3 songs compared to most other genres 1 or 2, meaning the dataset has more trouble recommending non Lofi songs.
* The system will always recommend the same five songs for a user profile no matter what.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



