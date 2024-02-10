# Hirst Spot Painting Generator

This Python script generates abstract artworks in the style of Damien Hirst's iconic spot paintings, using color extraction and random placement of colorful circles.

### Features:

- Creates spot paintings inspired by Hirst's signature style.
- Leverages the colorgram library for accurate color extraction from an image.

### Requirements:

1. Python
2. colorgram library (can be installed using `pip install colorgram`)
3. turtle library (included in standard Python installation)

### Instructions:
1. Clone or fork this repository.

2. Download a hirst-painting.jpg image:
- This image will be used to extract the color palette for your paintings.
- You can use the one from the repo, find similar images online or create your own.
- In case you an image other than the one in the repo, make sure to name it `hirst-painting.jpg`

3. Run the script:
``` bash
    python3 main.py
```
### Customization:

- Change the values of `num_rows`, `num_cols`, `dot_size`, `spacing`, and `background_color` to adjust the appearance of your paintings.
- Use a different image for hirst-painting.jpg to create a new color palette.
- Feel free to experiment with the code and modify it further to add more features or personalize your Hirst-inspired art!