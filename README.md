# FontHarvest

FontHarvest is a tool that helps you comply with various regulations on data management. This tool allows you to download all fonts specified in a CSS file, such as Google Fonts, and install them on your local server.

## Installation

FontHarvest requires the following dependencies:

- Python 3.x
- `os`
- `requests`
- `cssutils`
- `argparse`
- `tempfile`

To install the dependencies, run the following command:

```bash
pip install -r requirements.txt
```
## Usage

FontHarvest can be used from the command line with the following options:

```bash
python main.py --css <css_file> [--output <output_directory>]
```

- --css or -c: Specifies the CSS file or URL containing the fonts to download.
- --output or -o (optional): Specifies the folder to store the downloaded fonts. Default is the "fonts" folder.

You can now copy the CSS file provided by your font supplier (e.g. Google Fonts) and replace the beginning of the URL with your local path.

**Here's how to perform the replacement in the main IDEs.**
- Visual Studio Code (VS Code):   
    1. Select the text you wish to modify. 
    2. Press Ctrl+H to open the search and replace dialog box. 
    3. Enter the search string in the "Search" field and the replacement string in the "Replace with" field.   
    4. Use the available options (such as case-sensitive search, search within selection, etc.) as required.   
    5. Click the "Replace" button to replace one occurrence at a time, or "Replace All" to replace all occurrences at once.     

-   IntelliJ :
    1. Select the text you wish to modify. 
    2. Press Ctrl+R to open the search and replace dialog box. 
    3. Enter the search string in the "Search" field and the replacement string in the "Replace with" field.   
    4. Use the available options (such as case-sensitive search, search within selection, etc.) as required.   
    5. Click the "Replace" button to replace one occurrence at a time, or "Replace All" to replace all occurrences at once.        

-   Xcode : 
    1. Select the text you wish to modify. 
    2. Press Cmd+Shift+F to open the search and replace dialog box.    
    3. Enter the search string in the "Search" field and the replacement string in the "Replace with" field.   
    4. Use the available options (such as case-sensitive search, search within selection, etc.) as required.   
    5. Click on the "Replace" button to replace one occurrence at a time, or on "Replace All" to replace all occurrences at once.  

## Example

Here's an example of how to use FontHarvest to download fonts from a CSS file:

```bash
python main.py --css fonts.css --output fonts
```

This will download the fonts specified in "fonts.css" and store them in the "fonts" folder.

> Notes: you don't need to specify the output folder if you want it to be "fonts".

## Why use FontHarvest with Google Fonts?

Google Fonts provides a wide variety of fonts that can be easily added to web projects. However, relying on external resources like Google Fonts can introduce performance and privacy concerns. FontHarvest allows you to download the fonts and host them on your local server, giving you more control over the fonts used on your website.  

Please note that you should respect the licensing and usage terms for the fonts you download, especially when using them for commercial purposes.   

## License

This project is licensed under the MIT License.