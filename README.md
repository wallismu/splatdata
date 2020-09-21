# Splatdata
I used [mitmproxy](https://mitmproxy.org/) to make automated calls to Nintendo's API from my server. I wanted to be able to analyze my play history to see where I could improve my strategy. It was important to me that I regularly poll for new data for two reasons:
1. Nintendo only saves the previous 50 battles. As old battles get deleted, they are gone forever. As someone who has 500+ hours of Splatoon 2 logged, I need (and desire) far more than 50 battles to make any kind of worthwhile statistical analysis. 
2. I play Splatoon at weird times. If I say, only played for two hours on Sunday, I could just poll every Monday morning. But as a true addict, games can be at 6:30 in the morning or at night, any day of the week. 

Inspired by [NintendoSwitchRESTAPI](https://github.com/ZekeSnider/NintendoSwitchRESTAPI)
