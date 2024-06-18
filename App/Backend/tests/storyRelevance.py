import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
# Load the pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Function to calculate relevance score
def calculate_relevance(news_article, generated_story):
    # Generate embeddings for the news article and the generated story
    article_embedding = model.encode([news_article])
    story_embedding = model.encode([generated_story])
    
    # Calculate cosine similarity
    similarity = cosine_similarity(article_embedding, story_embedding)
    
    # Return the similarity score
    return similarity[0][0]

# Load the first 7 articles from articles.json
#print current directory
with open('output.json', 'r') as file:
    articles = json.load(file)[:5]

# Example generated stories (replace with actual generation process)
generated_stories = [
    "Joe Biden is a very experienced politician who has been both the vice president and president of the United States. He became a senator a long time ago in 1972 and in 2021, at the age of 78, he became the oldest person ever to be sworn in as president. Joe Biden won the 2020 election and is facing Donald Trump again in 2024. There are two main political parties in the US: the Democratic Party and the Republican Party. Even though Joe Biden is the current president, he has to work hard to get re-elected because many people support the Republican Party and Donald Trump. Story for Children: Once upon a time, in a country called the United States, there was a kind and determined man named Joe Biden. Joe had always loved helping people and making his country a better place. When he was young, he studied law at university and became one of the youngest senators ever in 1972. Joe worked hard for the people of Delaware, where he lived, and they liked him very much. Years later, in 2009, Joe Biden became the vice president to President Barack Obama. Together, they worked on many important things for the country, like helping families and making sure everyone had good healthcare. Then, in 2020, Joe Biden decided to run for president himself. It was a big decision because he was already 78 years old, which made him the oldest person ever to become president! But Joe believed he could do a great job, so he worked really hard and won the election. People were excited because Joe promised to help the country recover from a big sickness called the coronavirus and to make sure everyone had a chance to be happy and safe. As president, Joe Biden did many things to keep his promises. He helped families who were struggling with money because of the coronavirus. He also joined an agreement with other countries to protect the environment and reversed some decisions made by the previous president that he didn't agree with. But being president wasn't always easy. Some people didn't agree with everything Joe did, and he had to work with other politicians to make sure everyone's ideas were heard. He also had to make big decisions about other countries, like when to bring American soldiers home from a place far away called Afghanistan. Now, Joe Biden is getting ready to run for president again in 2024. He knows it won't be easy, but he believes he can \"finish the job\" and keep doing good things for the country. Joe's friend Kamala Harris, who is the first female vice president and also the first Black and South Asian American vice president, is helping him too. Joe Biden loves his country very much and wants to make sure everyone has a chance to be happy and safe. He believes in working together and being kind to others, no matter what. And so, the story of Joe Biden continues, as he works hard every day to make the United States a better place for everyone.",
    "In the United States, there are two main political parties: the Democratic Party and the Republican Party. These parties have different ideas about important issues like climate change, money, and rights for people. In the upcoming election on November 5, 2024, Joe Biden from the Democratic Party will try to win again as president against Donald Trump from the Republican Party. This election is really important because the United States is very powerful and has a big impact on the world. The person who wins will be inaugurated as president at the US Capitol Building in Washington DC. Story for Children: In the land called the United States, there were two powerful groups of people who wanted to be in charge and make important decisions. These groups were called political parties. One was called the Democratic Party, and the other was called the Republican Party. The Democrats and Republicans had different ideas about how to take care of the country. They talked about things like how to protect the environment, how to make money fair for everyone, and how to make sure people were treated well. One day, it was time for the people to choose who they wanted to be their leader. The Democrats picked a kind man named Joe Biden. Joe had been the president before, and he wanted to keep helping the country. He promised to do good things for the people and make sure everyone was happy and safe. The Republicans chose a strong man named Donald Trump. Donald had been president too, and he wanted to be the leader again. He promised to do things differently than Joe and help the country in his own way. The election day was coming soon, and everyone in the United States was getting ready to vote. When people vote, they choose who they want to be the leader by marking their choice on a special paper. The election was really important because the United States was a big and powerful country. The person who won would become the leader and live in a special place called the US Capitol Building in Washington DC. Joe Biden and Donald Trump traveled all around the country to talk to people and ask for their votes. They visited places called swing states, where people were still deciding who to vote for. These states were very important because they could help decide who would win the election. People in the United States were excited and curious to see who would become their leader. They watched debates on TV where Joe and Donald talked about their ideas. They listened to speeches and talked with their friends and family about who they thought would be the best leader. And so, as the big day of the election got closer, everyone in the United States waited to see who would win. They knew that no matter what happened, their country would keep going, and they would keep working together to make things better for everyone.",
    "Donald Trump, a former president of the United States, is running again as a candidate for the Republican Party in the upcoming election against Joe Biden. He has many supporters who are happy about his return, but there is also controversy because he has faced serious legal problems. Despite being convicted of a crime in May 2024, Donald Trump plans to run for president again. Before becoming president, he was known for his business and TV shows. As president, he made many changes to US policies, but his time in office was also filled with controversies and impeachments. Story for Children: In the big country of the United States, there was a man named Donald Trump who wanted to be the leader. Before he was a president, Donald Trump was famous for being a businessman and for appearing on television. He even had a small part in a funny movie called Home Alone 2! When Donald Trump became president, he wanted to make the country strong and safe. He did things like changing tax rules to help people keep more money, and he tried to stop people from coming into the country illegally. He even met with a leader from a faraway place called North Korea to try and make peace. But being president was not easy for Donald Trump. Some people didn't agree with everything he did, and there were times when he got in trouble for his actions. Twice, he was impeached, which means people in charge thought he did something wrong and needed to be punished. Even after he finished being president, Donald Trump still wanted to lead the country. He traveled around to different places and talked to many people who liked him and wanted him to be president again. Some people were happy about this, but others were worried because Donald Trump had legal problems. In May 2024, Donald Trump was even convicted of a crime, but he said he still wanted to be president. His supporters liked his ideas about making the country strong and proud again, which was his slogan \"Make America Great Again.\" Now, Donald Trump was getting ready to run for president again against Joe Biden. They would have a big election to see who the people wanted to be their leader. It was an exciting time in the United States, as everyone waited to see what would happen next. No matter what, the people knew that their country would keep going, and they would keep working together to make it the best it could be.",
    "Once upon a time, in a school called Hamstel Junior School, a group of curious Year 6 students had a big question: why can our eyes see such long distances? They pondered over this mystery until one day, they decided to seek answers. Their teacher, Mrs. Green, encouraged them to reach out to an expert, so they turned to Dr. Maddy Dann, a TikTok star known for explaining scientific wonders in simple ways. Dr. Maddy Dann was excited to receive their question. She explained that the small spheres in our heads, our eyes, are amazing organs designed to capture light and turn it into images. Through a process called vision, our eyes can perceive objects even at great distances. She shared with the students that our eyes work like cameras, with lenses that focus light onto a special part called the retina. The retina then sends signals to our brain, which interprets them as images. This incredible ability allows us to see everything around us, from nearby objects to faraway mountains and stars in the night sky. The Year 6 students were fascinated by Dr. Dann's explanation. They learned that the science behind sight is both complex and magical. Armed with this newfound knowledge, they continued their studies with a deeper appreciation for the wonders of the human body and the world around them. And so, the mystery of why our eyes can see such long distances was solved, thanks to curious minds and the guidance of a knowledgeable scientist. The students at Hamstel Junior School realized that every question, no matter how big, can lead to amazing discoveries.",
    "In a busy city called London, there lived children who loved to learn about their country. One day, they heard exciting news: there would be a general election! The prime minister, Mr. Sunak, stood outside his home at 10 Downing Street and announced that on Thursday 30 May, parliament would be dissolved. This meant that current Members of Parliament would become ordinary citizens again and had to try to get elected once more. But what exactly is a general election? Let's find out! A general election is when grown-ups all across the United Kingdom decide who they want to represent them in the big building called Parliament. Each area in the UK, like towns and cities, has its own special person called a Member of Parliament, or MP. These MPs speak up for their local area and help make important decisions about our country. Before the election, people who want to become MPs, called candidates, tell everyone why they would be great at the job. They join groups of other people who believe in similar things, called political parties, such as the Conservative Party or the Labour Party. When it's election day, adults go to special places called polling stations to vote. They can vote in person, by post, or even have someone vote for them if they can't go themselves. Everyone needs to show a form of ID to make sure everything is fair. The UK is divided into 650 areas called constituencies, and each one gets to choose its own MP. The most straightforward way to win is to get something called a majority. If a party gets at least 326 MPs elected out of the 650, they have more than half and can form a government. Sometimes, if no party gets a majority, they might work together in a group called a coalition to make decisions together. After all the votes are counted, the results are announced. The newly elected MPs then go to Parliament to start working. There's even a special ceremony, called the State Opening of Parliament, where the King announces what the new government wants to do. So, the children of London learned that a general election is an exciting time when everyone's voice is heard, and they get to choose who represents them in Parliament. It's a big responsibility and a great way to make sure our country keeps running smoothly! And that's how a general election works in the United Kingdom. I hope you enjoyed this story! If you have any more questions or want to learn about something else, just ask!",
]

reference_story = '''Once upon a time, in a small village nestled deep within a lush green forest, there lived a peculiar little creature named Milo. Milo wasn't like the other forest animals; he had wings that shimmered like opals and could change color with his mood. One sunny morning, Milo woke up with a tickling feeling in his wings, a sensation he had never felt before. Curious and excited, he fluttered out of his cozy nest in an old oak tree and soared through the forest canopy. As he flew, he discovered a hidden clearing filled with colorful flowers that seemed to dance in the gentle breeze. Milo was entranced by the beauty of the place and decided to explore further. Deep in the heart of the clearing, Milo stumbled upon a group of tiny creatures he had never seen before. They were no bigger than his wingtip and had shiny scales that glistened in the sunlight. They introduced themselves as the Glowbugs, guardians of the forest's secret treasures. The Glowbugs were delighted to meet Milo, for they had heard tales of a winged creature with magical wings that could bring harmony to the forest. They explained that Milo's wings were a gift from the ancient Tree of Whispers, which stood tall and wise at the center of the clearing. Eager to learn more, Milo listened intently as the Glowbugs shared stories of their adventures protecting the forest's wonders from harm. They showed him how to make the flowers bloom brighter and how to sing melodies that made the trees sway with joy. Milo felt a deep connection to the Glowbugs and their mission. He knew in his heart that he had found his purpose—to protect and preserve the beauty of the forest and its inhabitants. From that day on, Milo became the Guardian of the Forest, working alongside the Glowbugs to ensure that every creature, big and small, could live in harmony. Together, they planted new flowers, whispered to the trees, and chased away the shadows that dared to disturb the peace. As seasons passed, Milo's wings shimmered even more brightly, reflecting the love and care he poured into his newfound home. The forest flourished under his watchful eye, becoming a sanctuary of wonder and magic for all who entered. And so, Milo the Winged Guardian and the Glowbugs continued their adventures, spreading joy and protecting the secrets of the forest for generations to come.'''

# Calculate relevance scores for each article and its generated story
for i, article in enumerate(articles):
    news_content = article['content']
    generated_story = generated_stories[i]
    
    relevance_score = calculate_relevance(news_content, generated_story)
    reference_score = calculate_relevance(news_content, reference_story)
    print(f"Relevance Score for Article {i+1}: {relevance_score}")

# If you want to store the results in a list or dictionary:
relevance_results = []

for i, article in enumerate(articles):
    news_content = article['content']
    generated_story = generated_stories[i]
    
    relevance_score = calculate_relevance(news_content, generated_story)
    reference_score = calculate_relevance(news_content, reference_story)
    relevance_results.append({
        "article_id": article['id'],
        "article_title": article['name'],
        "relevance_score": relevance_score,
        "reference_score": reference_score
    })

# Print the results
for result in relevance_results:
    print(f"Article ID: {result['article_id']}, Title: {result['article_title']}, Relevance Score: {result['relevance_score']}, Reference Score: {result['reference_score']}")


# Example usage
news_article = "Paris welcomed in 2024 - the Olympic year - by projecting the Olympic rings on the historic landmark, the Arc de Triomphe, during the new year celebrations This year, the world's greatest athletes will come together in France's capital city Paris to run, jump, swim, twist, twirl, kick, punch and climb their way to the top of the Olympic podium.  These Games are, for many athletes, the pinnacle of their sport - there is no greater achievement than earning an Olympic gold medal.  But with more than 10,000 athletes competing and only 300 gold medals up for grabs, only the best will be able to call themselves Olympic champions when the Games end.  So, here is everything you need to know about the 2024 Olympics.  What a spot for an Olympic selfie! The opening ceremony will take place on Friday 26 July 2024.  There will be a total of 19 days of competition but some preliminary events take place before the opening ceremony, such as archery qualifying and early rounds of rugby sevens, football and handball.  The first gold medal will be won on Saturday 27 July and will likely come from the shooting ranges, with rifle and pistol shooting competitions kicking things off.  This will be followed by 16 days of world class sport, and   will be in Paris to make sure you don't miss a moment.  The closing ceremony takes place on Sunday 11 August.  Some of the world's most famous landmarks will be the backdrop to the Games in Paris.  We could just let these mocked-up images of the venues speak for themselves, but let us take you through some of them.  Check out the beach volleyball arena, located in front of the world famous Eiffel Tower.  Just below the iconic structure will also be a huge fan park where members of the public can watch events on big screens and even meet some of the athletes after they have competed.  Check out the start line of the triathlon, which is located under the spectacular 19th century Alexandre III bridge and its golden statues across the River Seine.  Team GB are defending Olympic champions in the mixed team relay event, so will this be a spot of interest?  The bridge will also be the setting of the finish line for the cycling time trials and the marathon swims. The Alexandre III bridge will be the backdrop for the triathlon To the south west of the city, you will find the spectacularly majestic Palace of Versailles, where some of the most talented four-legged Olympians will compete.  Yes, the equestrian events will take place in the grounds of the stunning royal palace where more than 15 million people visit every year.  Dancing horses in the grounds of a royal palace? 'Yes please\", or 'oui s'il vous plait' as the French would say For the sailing competition, athletes will be heading south to the Mediterranean city of Marseille.  The port in the south of France has hosted plenty of sailing events in its time as it is known for its great weather and windy conditions.  France's second largest arena, the Stade V\u00e9lodrome, also in Marseille, will play host to some of the men's and women's Olympic football tournament.  Let's hope the weather is as good as it appears in this artist's impression of Marseille marina Despite France's multitude of beaches, the Olympic surfing competition will not be taking part within the country.  It won't even be taking place within the continent of Europe - or even in the northern hemisphere.  The Olympic surfers will be 9,500 miles from Paris, on the remote Pacific island of Tahiti, which is part of French Polynesia - a territory of France. Blue waters, sunny weather, and most importantly, big waves - this is the location for the Paris 2024 Olympic surfing event... but it's a long way from Paris Unlike the last Summer Olympics in Tokyo, most of the events will be taking place at a TV-friendly time for viewers in the UK.  Paris is just one hour ahead of the UK, so any event that takes place at 6pm in Paris will be on TV at 5pm here in the UK.  Plus, the Games will be taking place during the summer holidays for most schools, so you may even be able to negotiate a slightly later bedtime to watch the biggest moments, including the 100m finals in the athletics.  Don't worry though, the BBC will be broadcasting hundreds of hours of Olympics coverage on television and online. Team GB's Charlotte Worthington took gold in Tokyo - can she do it again in Paris? There will be plenty of the traditional Olympic sports such as athletics, swimming, rowing and cycling as well as gymnastics, badminton, tennis and boxing.  This year, surfing, skateboarding, BMX freestyle and sport climbing will also return after their success in Tokyo.  There will also be the brand new addition of breaking at this year's Games, which is a form of acrobatic dance where competitors combine power moves and freezes to impress judges and earn themselves the Olympic gold medal.  We can also expect to see combat sports such as taekwondo, judo and wrestling.  The Olympics is often a great opportunity to see sports you don't get the chance to watch very often, for example water polo, artistic swimming, fencing, handball and basketball.  New events in the sailing competitions will also include a form of windsurfing called iQFoil and kiteboarding. Ondine Achampong could be a breakout star for Team GB in Paris Well at the moment, there are only a handful of athletes who have been officially named in Team GB's Olympic squads, but let's look at who is aiming to be in the French capital this summer.   Experts are predicting big things from skateboarder  , who took bronze in Tokyo.  She won the world park championships in February last year, and is also hoping to become the first British athlete to compete in two sports at the same Olympic Games as she hopes to qualify for both the skateboarding AND surfing events.  Britain's artistic gymnasts are also ones to watch, with high hopes for medals from both the men's and women's teams.  , world floor champion in 2022, admits she has a tough journey ahead of her if she is to make it to Paris. The 19-year-old suffered an anterior cruciate ligament injury just days before the 2023 World Championships in Antwerp last October.  But will twin sister Jennifer join her? She has also been recovering from surgery after an ankle injury last year.  Veteran bars expert   is hoping to reach her third Olympics, while   and  , who were in the team that won gold at the 2023 European Championships, are hoping to all make their mark on the Olympic stage.   will also want to prove himself on an Olympic stage after he took an historic world gold on the vault last year.  In athletics,   will no doubt want to go one better than her breakout performance in Tokyo, where she took home the silver medal in the 800m.  Plus world champion   will want to complete her major medal collection in the heptathlon.  In the pool,   will hope to add to his medal tally, and  , who also took home two golds from the last Olympics, says he is aiming to pick up five more in Paris. Triathletes  and   are two of the athletes confirmed to be heading to Paris and will both have big goals for the year ahead.  Beth is a current world champion and Alex won a gold and a silver in Tokyo, so will he add to his haul?   Fourteen-year-old Fay DeFazio Ebert is hoping to beat off tough competition from athletes much older than her... One of the biggest stars you will not want to miss in Paris is of course US pocket powerhouse  .  The most decorated gymnast of all time is hoping to add to her already impressive medal tally of four golds, one silver and two bronzes.  But she will have to beat another breakout gymnastics star in Brazilian  , who took the all-around title in Tokyo after Biles withdrew from the event citing mental health struggles.  It won't just be about Sky Brown at the skatepark in 2024.  Canadian teenager   has burst onto the scene in recent months after her incredible win at the 2023 Pan Am Games (where athletes from the Americas - North, Central and South America, compete for intercontinental glory) in Chile. Not only that, but Fay, who is 14, is a talented singer, so watch out for her in the charts as well as the medal tables. \u00a9 2024 BBC. The BBC is not responsible for the content of external sites."
original = '''Once upon a time, in the bustling city of Paris, a magical event was about to unfold. It was the year 2024, and the city was adorned with excitement and anticipation as it prepared to host the Olympic Games. Let's embark on a journey to discover what this grand event was all about. In a cozy little neighborhood near the River Seine lived a curious girl named Sophie. Sophie loved sports of all kinds, from running in the park to swimming in the local pool. But what fascinated her the most were the stories her grandfather told her about the Olympics. "Sophie," her grandfather would say, "the Olympics are a celebration where athletes from all over the world come together to compete in their favorite sports. It's a chance for them to show their skills and make their countries proud." Sophie's eyes widened with wonder. "Grandpa, will there be athletes jumping, swimming, and running all around Paris?" "Absolutely, Sophie," her grandfather chuckled. "In fact, right here in Paris, they'll be setting up special places for different sports. Imagine beach volleyball right by the Eiffel Tower and triathlons starting under the beautiful Alexandre III bridge!" Sophie giggled with excitement. "That sounds amazing, Grandpa! But why are they doing it here?" "Well, Sophie, Paris is a city full of history and beauty," her grandfather explained. "The Olympics choose cities like Paris because they have iconic landmarks where athletes can compete in front of the whole world." Sophie nodded, imagining herself cheering on athletes as they dashed toward victory beneath the majestic bridges and alongside the sparkling River Seine. As the days passed, Sophie and her friends couldn't wait for the Olympics to begin. They watched on TV as athletes from countries far and wide arrived in Paris. They saw swimmers dive into pools, gymnasts flip and twist, and cyclists race through the streets. One day, Sophie's favorite athlete, a skateboarder named Sky Brown, won a gold medal for her incredible tricks. Sophie jumped up and down, cheering as if she were right there in the skatepark with Sky. But it wasn't just about winning medals. Sophie learned that the Olympics were also about friendship and sportsmanship. Athletes supported each other, even if they were competing against one another. It was about doing your best and celebrating everyone's achievements. On the last day of the Olympics, Sophie and her family gathered around the TV to watch the closing ceremony. They saw fireworks light up the Parisian sky and heard music from around the world. Sophie felt a warm glow in her heart, knowing she had witnessed something truly special. "Grandpa," Sophie whispered as the ceremony ended, "I want to be an athlete too, just like them." Her grandfather smiled proudly. "Remember, Sophie, you can achieve anything you set your mind to. Just like these athletes, with hard work and determination, you can reach for the stars." Sophie nodded, her eyes sparkling with newfound dreams. As the TV showed images of athletes waving and saying goodbye to Paris, Sophie whispered to herself, "One day, I'll be there too." And with that, as the 2024 Olympics came to a close, Sophie knew that the magic of the Games had inspired her to aim high and chase her own dreams, no matter how big they may seem.''',
''''''

reference_story = '''Once upon a time, in a small village nestled deep within a lush green forest, there lived a peculiar little creature named Milo. Milo wasn't like the other forest animals; he had wings that shimmered like opals and could change color with his mood. One sunny morning, Milo woke up with a tickling feeling in his wings, a sensation he had never felt before. Curious and excited, he fluttered out of his cozy nest in an old oak tree and soared through the forest canopy. As he flew, he discovered a hidden clearing filled with colorful flowers that seemed to dance in the gentle breeze. Milo was entranced by the beauty of the place and decided to explore further. Deep in the heart of the clearing, Milo stumbled upon a group of tiny creatures he had never seen before. They were no bigger than his wingtip and had shiny scales that glistened in the sunlight. They introduced themselves as the Glowbugs, guardians of the forest's secret treasures. The Glowbugs were delighted to meet Milo, for they had heard tales of a winged creature with magical wings that could bring harmony to the forest. They explained that Milo's wings were a gift from the ancient Tree of Whispers, which stood tall and wise at the center of the clearing. Eager to learn more, Milo listened intently as the Glowbugs shared stories of their adventures protecting the forest's wonders from harm. They showed him how to make the flowers bloom brighter and how to sing melodies that made the trees sway with joy. Milo felt a deep connection to the Glowbugs and their mission. He knew in his heart that he had found his purpose—to protect and preserve the beauty of the forest and its inhabitants. From that day on, Milo became the Guardian of the Forest, working alongside the Glowbugs to ensure that every creature, big and small, could live in harmony. Together, they planted new flowers, whispered to the trees, and chased away the shadows that dared to disturb the peace. As seasons passed, Milo's wings shimmered even more brightly, reflecting the love and care he poured into his newfound home. The forest flourished under his watchful eye, becoming a sanctuary of wonder and magic for all who entered. And so, Milo the Winged Guardian and the Glowbugs continued their adventures, spreading joy and protecting the secrets of the forest for generations to come.'''

# relevance_score = calculate_relevance(news_article, generated_story)
# print(f"Relevance Score: {relevance_score}")
