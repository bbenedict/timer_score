# Timer Score API

## TSTimer

Generalized timer class that generates a score from 0 to 1 using an inverted, adjusting, sigmoid function.

Properties:  
* target (float) - target duration of the timer
* start (float) - the time when the timer was started
* finish (float) - the time when the timer was stopped, or None if the timer is still going
* checkpoints (list[TSCheckpoint]) - list of all captured checkpoints including the final time

Paramaters:  
* target (float) - (optional) target duration of the timer, the score is not calculated if none provided

Returns:  
* N/A

### stop()

Stops the timer amd marks the finish time as the final checkpoint. No further checkpoints can be recorded.

Paramaters:  
* none

Returns:  
* N/A

### checkpoint(name, target)

Captures the time at a specific checkpoint.  

Paramaters:  
* name (str) - (optional) name of the checkpoint, a random one is generated if none provided
* target (float) - (optional) target duration for checkpoint, the timer target is used if none provided

Returns:  
* TSCheckpoint (see below)

### duration(name)

Returns the total duration of the timer or the duration at a specific checkpoint if a name is provided.
Returns the current duration if the timer is still running.

Paramaters:  
* name (str) - (optional) - name of the checkpoint to use for the duration

Returns:  
* duration (float) - elapsed time from start

### score(name)

Returns the score, target and duration of the timer or the same values for a specific checkpoint if a name is provided.
The score is based on the current duration if the timer is still running.

Paramaters:  
* name (str) - (optional) name of the checkpoint to use for the score calculation

Returns:  
* score (float) - score based on the duration against the target
* duration (float) - duration that was used to calculate the score
* target (float) - target that was used to calculate the score

### execute(func, *args, **kwargs)

Returns the score, target and duration of the function that is executed.

Paramaters:  
* func (function) - function to execute
* args (list) - (optional) positional arguments to pass to function
* kwargs (list) - (optional) named arguments to pass to function

Returns:  
* score (float) - score based on the duration against the target
* duration float) - duration that was used to calculate the score
* target (float) - target that was used to calculate the score

### reset()

Resets the timer by clearing all checkpoints and recording a new start time.

Paramaters:  
* none

Returns:  
* N/A

### sleep(seconds)

Sleeps the timer

Paramaters:  
* seconds (float) - the seconds to sleep

Returns:  
* N/A

## TSCheckpoint:

Checkpoint class to store data of a checkpoint. This class should be treated as READONLY data.

Properties:  
* name (str) - name of the checkpoint
* target (float) - target duration of the checkpoint
* time (float) - the time when the checkpoint was created
* duration (float) - elapsed time from when the timer was started to the checkpoint
