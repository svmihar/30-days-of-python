# blinkies, for cli
this demonstrates the infamous race conditions, and how to get around it <br>
![](img/img.gif)

## requirement
`pipenv install` <br>
`pipenv shell` <br>
and good to go <br>


## single thread
`python blink.py` <br>
produces single blinkies <br>

## threading
`python blink_thread.py` <br>
produces 4 blinkies, but has problems when added delay all processes doesn't wait for other processes to finish

## asyncio!
`python blink_async.py` <br>
produces 4 blinkies, has no problem when delay is addded, thus calling the `call_loop_later` function vigirously

### variations on the looping
you can use default asyncio methods, to use `await` functions on the `sleep` and `set_face` methods

## trio
`python blink_trio.py` <br>
uses the easier framework for asyncio, produces literally the result and method used by the asyncio