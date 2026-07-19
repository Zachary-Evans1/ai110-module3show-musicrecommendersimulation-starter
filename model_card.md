# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

One weakness I discoverd is that my recommender heavily prioritizes exact genre and mood matches. Genre and mood account for 70% of the total score, songs that match those categories rank above songs with very similar, energy, tempo, and valence values to a users preferences. The system also does not have a similarity ranking between genres, for a user who likes "pop" songs a song in the "indie pop" genre will get 0/40 points in the ranking. These factors lead to the system not supporting cross-genre exploration, and creating a filter bubble where a user will get songs that match their genre and mood preferences, without energy, tempo, and valence having much sway in scoring.
---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I tested the recommender using five different user profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, Genre Mismatch (K-Pop), and Conflicting Preferences. I looked at whether the recommended songs matched the genre, mood, and audio characteristics that each profile had as their preferences.

The results mostly matched my expectations. The High-Energy Pop profile was recommended upbeat and fast paced pop songs that had high energy scores, while the Chill Lofi profile was recommended slower, and more focused lofi songs. Deep Intense Rock profile was recommended heavy rock and metal songs with high energy and tempo values.

Comparing the High-Energy Pop and Chill Lofi profiles showed how much energy and genre influence the rankings. The High-Energy Pop profile recommended upbeat songs with faster tempos, while the Chill Lofi profile recommended slower and more focused tracks. This makes sense because the two profiles have very different target energy and tempo values.

Comparing the Chill Lofi and Deep Intense Rock profiles produced almost opposite results. The lofi profile favored calm songs with lower energy, while the rock profile favored aggressive songs with high energy and high tempo. This demonstrates that the recommender is responding to changes in user preferences as intended.

What surprised me was the Genre Mismatch (K-Pop) profile. I did not have any K-pop songs in the dataset so the recommender relied on mood, energy, tempo and valence instead. To my surprise it worked quite well, mostly ended up recommending pop and electronic songs which are as close as you can get to K-pop in my data set.

The Conflicting Preferences profile is the one that showed the limitations in my scoring system. Even though the user requested a pop song with a sad mood and high energy, songs like "Gym Hero" still ranked at the top because of the genre and energy matches outweighed the mood mismatch. This helped show the limitations in my current score weight system.
---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
