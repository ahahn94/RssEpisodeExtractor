# RssEpisodeExtractor

## Dependencies
RssEpisodeExtractor needs the following dependencies:
- Python 3
- GTK3
- setuptools
- feedparser (python module)

## Installation
Just run `./install.sh` to install and `./remove.sh` to uninstall the program.
#### Only linux is supported!

## Usage:
### Console
Just run `rssepisodeextractor link_to_feed` and the links will be printed to the cli.  

If you run `rssepisodeextractor` you will be asked for your url.  

To follow links in case of redirection, use `rssepisodeextractor -redirect link_to_feed`.  

If you want to download the files directly from the cli, run `rssepisodeextractor yourfeedurl | xargs wget`. Be aware that this can take some time, depending on the number of episodes and the connection speed.

#### Tip:
Run the code from the first example and paste the result into a download manager like JDownloader.
#### Please be patient with the program.
It will first load all pages and then start processing them. As loading the pages depends on your internet connection, it may take a while.
#### The program has no additional output apart from the links. If you get no output, it is probably still loading the pages.

### GUI
Just run `rssepisodeextractor-gtk`.  
## In Action
### Console
#### Not following links
![RssEpisodeExtractor-CLI.gif](RssEpisodeExtractor-CLI.gif)
#### Following links
![RssEpisodeExtractor-CLI-Redirect](RssEpisodeExtractor-CLI-Redirect.gif)
### GUI
#### Not following links
![RssEpisodeExtractor-GTK.gif](RssEpisodeExtractor-GTK.gif)
#### Following links
![RssEpisodeExtractor-GTK-Redirect](RssEpisodeExtractor-GTK-Redirect.gif)
