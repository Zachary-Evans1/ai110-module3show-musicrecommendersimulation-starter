# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**TuneMatch 1.0**  

## 2. Intended Use  

This recommender is designed to suggest songs based on a users preferred genre, mood, energy, tempo, and valence. It assumes the user is able to describe the type of music they enjoy using those preferences. The system is designed for classroom exploration of recommendation systems and is not currently designed for real use in a music service.

## 3. How the Model Works  

The recommender uses each song's genre, energy, mood, tempo, and valence to determine a score for each song. Songs receive points when their genre or mood matches the user's favorites. Additional points are also added when a song's energy, tempo, and valence are close to the user's target values. The weights of these scores are 40 points for genre, 30 points for mood, 15 points for energy, 10 points for tempo, and 5 points for valence, adding up to a score of 100 for each song.

After all songs are scored, they are sorted from highest to lowest score. The recommender then returns the highest scoring songs along with explanations describing why they were selected.

Compared to the starting logic, I implemented the song CSV loading function, the scoring functions, the recommendation ranking logic, and recommendation explanations.

## 4. Data  

The dataset contains 20 songs. Each song has an ID, title, artist, genre, mood, energy score, tempo, and valence score.

The dataset contains a variety of genres including pop, lofi, rock, jazz, ambient, synthwave, indie pop, classical, electronic, blues, country, metal, hip-hop, reggae, folk, and punk. It also contains moods such as happy, chill, intense, relaxed, focused, peaceful, moody, energetic, melancholic, nostalgic, aggressive, confident, wistful, and euphoric.

I removed the danceability and acousticness scores from the data. One limitation of my dataset is that some genres only have one song represented while others have multiple. The dataset is also very small compared to real-world music catalogs, which makes it difficult for my program to represent the full range of musical tastes.

## 5. Strengths  

The recommender performs well when a user's preferences closely match songs in the dataset. The profiles I created: High-Energy Pop, Chill Lofi, and Deep Intense Rock all produced recommendations that matched my expectations.

The scoring system successfully captured the relationship between user preferences and song attributes. The high-energy profiles were consistently recommended faster and more energetic songs, while the low-energy profiles were recommended calmer and slower songs.

The explanations for the recommendations also make it easy to understand why a song was selected and how it matched the user's preferences.

## 6. Limitations and Bias 

One weakness I discovered is that my recommender heavily prioritizes exact genre and mood matches. Genre and mood account for 70% of the total score, songs that match those categories rank above songs with very similar, energy, tempo, and valence values to a user's preferences. The system also does not have a similarity ranking between genres or moods, for a user who likes "pop" songs a song in the "indie pop" genre will get 0/40 points in the ranking. These factors lead to the system not supporting cross-genre exploration, and creating a filter bubble where a user will get songs that match their genre and mood preferences, without energy, tempo, and valence having much sway in scoring.

## 7. Evaluation  

No need for numeric metrics unless you created some.

I tested the recommender using five different user profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, Genre Mismatch (K-Pop), and Conflicting Preferences. I looked at whether the recommended songs matched the genre, mood, and audio characteristics that each profile had as their preferences.

The results mostly matched my expectations. The High-Energy Pop profile was recommended upbeat and fast paced pop songs that had high energy scores, while the Chill Lofi profile was recommended slower, and more focused lofi songs. Deep Intense Rock profile was recommended heavy rock and metal songs with high energy and tempo values.

Comparing the High-Energy Pop and Chill Lofi profiles showed how much energy and genre influence the rankings. The High-Energy Pop profile recommended upbeat songs with faster tempos, while the Chill Lofi profile recommended slower and more focused tracks. This makes sense because the two profiles have very different target energy and tempo values.

Comparing the Chill Lofi and Deep Intense Rock profiles produced almost opposite results. The lofi profile favored calm songs with lower energy, while the rock profile favored aggressive songs with high energy and high tempo. This demonstrates that the recommender is responding to changes in user preferences as intended.

What surprised me was the Genre Mismatch (K-Pop) profile. I did not have any K-pop songs in the dataset so the recommender relied on mood, energy, tempo and valence instead. To my surprise it worked quite well, mostly ended up recommending pop and electronic songs which are as close as you can get to K-pop in my data set.

The Conflicting Preferences profile is the one that showed the limitations in my scoring system. Even though the user requested a pop song with a sad mood and high energy, songs like "Gym Hero" still ranked at the top because of the genre and energy matches outweighed the mood mismatch. This helped show the limitations in my current score weight system.

## 8. Future Work  

If I continued developing this project, I would add more songs and genres to create a larger and more diverse dataset. I would also add similarity scoring for genres and moods, so that genres like pop and indie pop, or moods like relaxed and peaceful could receive partial credit instead of zero points as it is now. Another improvement would be some sort of system that could occasionally recommend songs outside of a user's normal preferences. This could reduce the effects of the filter bubbles and help users discover new music. If I had a lot more time I would even possibly think about experimenting with collaborative filtering and/or user listening history to create recommendations that are more realistic.

## 9. Personal Reflection  

My biggest learning moment from this project was that planning your system out before ever touching the code can make the coding process a lot easier. When it came time to implement my scoring logic, I just gave claude my ideas and it did a pretty good job implementing the code. I had to make very minor changes later, but overall the implementation was very easy after I had everything planned out.

AI tools were helpful throughout this project for brainstorming and implementation. It helped suggest edge-case user profiles and identify biases in my recommender. I did need to undo some suggestions as it changed more than I wanted to, and I always made sure to verify the suggestion before accepting it.

I was surprised by just how simple recommenders can be and still work. Systems like Spotify and YouTube's recommendation algorithm are very complex and in a lot of ways very hard to understand and rely on AI models. Through this project I've learned that at a base level, a working recommender can just be a few lines of code that compare strings and floats and assign scores based on how close a user's preferences are.

If I extended this project I would like to do two things, add a much larger dataset and implement similarity scores between related genres and moods.