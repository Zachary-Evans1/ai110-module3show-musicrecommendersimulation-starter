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
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



