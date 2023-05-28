import os, requests, cssutils, argparse, tempfile

def getArgs():
    parser = argparse.ArgumentParser(description='FontHarvest helps you to comply with the various regulations on data management. This tool lets you download all fonts given in a css file, such as Google Fonts, and install them on your local server.')
    parser.add_argument('--css', '-c', type=str, required=True, help='CSS file or URL containing the fonts to download')
    parser.add_argument('--output', '-o', type=str, default='fonts', help='Folder to store the downloaded fonts')
    return parser.parse_args()


def main():
    args = getArgs()
    css_file = args.css
    if not os.path.isfile(css_file):
        css_file_content = requests.get(css_file)
        if css_file_content.status_code == 200:
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(css_file_content.content)
                temp_file_path = temp_file.name
            css_file = temp_file_path
            print(f"CSS file downloaded and saved to: {temp_file_path}")
        else:
            print(f"Failed to download css file: {css_file}")
            return
    output_directory = args.output
    def downloadFontsFromCSS(css_file, output_dir):
        with open(css_file, 'r') as f:
            css_content = f.read()
        sheet = cssutils.parseString(css_content)
        font_rules = [rule for rule in sheet if rule.type == rule.FONT_FACE_RULE]
        for rule in font_rules:
            font_src = rule.style.getPropertyValue('src')
            font_url = extractFontUrl(font_src)
            font_filename = font_url.split('/')[-1]
            font_path = os.path.join(output_dir, font_filename)
            downloadFont(font_url, font_path)

    def extractFontUrl(font_src):
        font_src = font_src.strip("url('')")
        font_src_parts = font_src.split(' ')
        url = font_src_parts[0]
        return url.strip('url(').strip(')').strip("'")

    def downloadFont(url, output_path):
        response = requests.get(url)
        if response.status_code == 200:
            with open(output_path, 'wb') as f:
                f.write(response.content)
                print(f"Font downloaded: {output_path}")
        else:
            print(f"Failed to download font: {url}")
            
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    downloadFontsFromCSS(css_file, output_directory)

if __name__ == '__main__':
    main()