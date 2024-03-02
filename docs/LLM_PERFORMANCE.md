# LLM performance tracking

This example demonstrates how to measure the timing of the streaming API from OpenAI.  We are capturing time to first token from streaming along with total time to completion.  You use timer.checkpoint() to store a specific point during your time measurement.

The target for first token is less than 1/2 a second.  
The target for total completion is 5 seconds.

First install the timer_score library.

```
pip install timer_score
```

Import the libraries and initialize the OpenAI client. Define the targets mentioned above as well.

```
import os
from openai import OpenAI
from timer_score import TSTimer

# Instantiate the client first so this is not included in the test
prompt = "Why is the sun so hot and how does the sunlight reach the earth?"
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

# Define the targets in seconds
first_token_target = 0.5
target = 5
```

Bookend the code we want to evaluate by starting and stopping the timer.  Make sure to also checkpoint the time of the first token from the OpenAI streaming API using the name "first token".  The name is used later to retrieve the score at the checkpoint.

```
# Start the clock
timer = TSTimer(target)

# Send the prompt to the API
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}],
    stream=True
)

# Capture the stream making sure to checkpoint the first token
content = ""
for chunk in response:
    if len(timer.checkpoints) == 0:
        timer.checkpoint(name="first token", target=first_token_target)
    if chunk.choices[0].delta.content:
        content += chunk.choices[0].delta.content

# Stop the timer
timer.stop()
```

And finally, use score() to calculate the score for the first token checkpoint and the total completion. 

```
# Calculate the scores

score, duration, target = timer.score(name="first token")
# 0.409... 0.68... 0.5

score, duration, target = timer.score()
# 0.147... 6.76... 5
```

See the [API documentation](TIMER_SCORE_API.md) for a full explanation of the Timer Score library.