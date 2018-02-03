# RssEpisodeExtractor

## Dependencies
RssEpisodeExtractor needs the following dependencies:
- Python 3
- feedparser (python module)

## Usage:
Just run `python3 main.py link_to_feed` and the links will be printed to the cli.  

If you run `python3 main.py` you will be asked for your url.  

If you want to download the files directly from the cli, run `python3 main.py yourfeedurl | xargs wget`. Be aware that this can take some time, depending on the number of episodes and the connection speed.

## Tip:
Run the code from the first example and paste the result into a download manager like JDownloader.
### Please be patient with the program.
It will first load all pages and then start processing them. As loading the pages depends on your internet connection, it may take a while.
#### The program has no additional output apart from the links. If you get no output, it is probably still loading the pages.